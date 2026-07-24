#!/usr/bin/env python3
"""Google Gemini adapter for Symposium.

Reads a prompt from stdin and writes only the model text to stdout.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Any

from common import AdapterError, fail, parse_float_env, parse_int_env, post_json, read_prompt, require_env

API_BASE = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = "gemini-3.5-flash"


def extract_text(response: dict[str, Any]) -> str:
    if isinstance(response.get("error"), dict):
        error = response["error"]
        message = error.get("message", "unknown error")
        status = error.get("status", "unknown status")
        raise AdapterError(f"Gemini API error: {status}: {message}")
    candidates = response.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        feedback = response.get("promptFeedback", {})
        raise AdapterError(f"Gemini response missing candidates; promptFeedback={feedback}")
    first = candidates[0]
    parts = first.get("content", {}).get("parts", [])
    if not isinstance(parts, list):
        raise AdapterError(f"Gemini response missing content parts; finishReason={first.get('finishReason', '')}")
    texts = [part.get("text", "") for part in parts if isinstance(part, dict)]
    text = "\n".join(part.strip() for part in texts if isinstance(part, str) and part.strip()).strip()
    if not text:
        raise AdapterError(
            f"Gemini response contains no text; finishReason={first.get('finishReason', '')}; "
            f"safetyRatings={first.get('safetyRatings', '')}"
        )
    return text


def build_payload(prompt: str, args: argparse.Namespace) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": args.temperature,
            "maxOutputTokens": args.max_tokens,
        },
    }
    system = args.system or os.environ.get("GEMINI_SYSTEM_PROMPT", "")
    if system:
        payload["systemInstruction"] = {"parts": [{"text": system}]}
    return payload


def call_gemini(prompt: str, args: argparse.Namespace) -> str:
    api_key = require_env(["GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENERATIVE_AI_API_KEY"])
    model = args.model or os.environ.get("GEMINI_MODEL", DEFAULT_MODEL)
    endpoint = os.environ.get("GEMINI_API_BASE", API_BASE).rstrip("/")
    url = f"{endpoint}/models/{model}:generateContent"
    response = post_json(
        url,
        {
            "content-type": "application/json",
            "x-goog-api-key": api_key,
        },
        build_payload(prompt, args),
        timeout=args.timeout,
    )
    return extract_text(response)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Symposium Gemini adapter")
    parser.add_argument("--self-test", action="store_true", help="check configuration without calling the API")
    parser.add_argument("--live-test", action="store_true", help="make a minimal API call to verify credentials")
    parser.add_argument("--mock", action="store_true", help="return deterministic output without calling the API")
    parser.add_argument("--model", default=os.environ.get("GEMINI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--max-tokens", type=int, default=parse_int_env("GEMINI_MAX_TOKENS", 1200), dest="max_tokens")
    parser.add_argument("--temperature", type=float, default=parse_float_env("GEMINI_TEMPERATURE", 0.2))
    parser.add_argument("--timeout", type=float, default=parse_float_env("GEMINI_TIMEOUT", 180))
    parser.add_argument("--system", default=os.environ.get("GEMINI_SYSTEM_PROMPT", ""))
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.self_test:
            require_env(["GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENERATIVE_AI_API_KEY"])
            if not args.model:
                raise AdapterError("Gemini model is empty")
            print(f"ready gemini model={args.model}")
            return 0
        if args.live_test:
            call_gemini("Rispondi esattamente con OK_GEMINI.", args)
            print(f"live-ok gemini model={args.model}")
            return 0
        prompt = read_prompt()
        if args.mock:
            print(f"[gemini-mock:{args.model}] {prompt[:500]}")
            return 0
        print(call_gemini(prompt, args))
        return 0
    except AdapterError as exc:
        return fail(exc)


if __name__ == "__main__":
    sys.exit(main())
