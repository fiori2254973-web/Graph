#!/usr/bin/env python3
"""Anthropic Claude adapter for Symposium.

Reads a prompt from stdin and writes only the model text to stdout.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Any

from common import AdapterError, fail, parse_float_env, parse_int_env, post_json, read_prompt, require_env

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"
DEFAULT_MODEL = "claude-sonnet-5"


def extract_text(response: dict[str, Any]) -> str:
    blocks = response.get("content")
    if not isinstance(blocks, list):
        raise AdapterError("Claude response missing content list")
    parts: list[str] = []
    for block in blocks:
        if isinstance(block, dict) and block.get("type") == "text" and isinstance(block.get("text"), str):
            parts.append(block["text"])
    text = "\n".join(part.strip() for part in parts if part.strip()).strip()
    if not text:
        block_types = [block.get("type", "unknown") for block in blocks if isinstance(block, dict)]
        raise AdapterError(
            f"Claude response contains no text; stop_reason={response.get('stop_reason', '')}; "
            f"content_types={block_types}"
        )
    return text


def build_payload(prompt: str, args: argparse.Namespace) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": args.model or os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL),
        "max_tokens": args.max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if os.environ.get("CLAUDE_SEND_TEMPERATURE", "").lower() in {"1", "true", "yes"}:
        payload["temperature"] = args.temperature
    system = args.system or os.environ.get("CLAUDE_SYSTEM_PROMPT", "")
    if system:
        payload["system"] = system
    return payload


def call_claude(prompt: str, args: argparse.Namespace) -> str:
    api_key = require_env(["ANTHROPIC_API_KEY", "CLAUDE_API_KEY"])
    payload = build_payload(prompt, args)
    response = post_json(
        API_URL,
        {
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": os.environ.get("ANTHROPIC_VERSION", API_VERSION),
        },
        payload,
        timeout=args.timeout,
    )
    return extract_text(response)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Symposium Claude adapter")
    parser.add_argument("--self-test", action="store_true", help="check configuration without calling the API")
    parser.add_argument("--live-test", action="store_true", help="make a minimal API call to verify credentials")
    parser.add_argument("--mock", action="store_true", help="return deterministic output without calling the API")
    parser.add_argument("--model", default=os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--max-tokens", type=int, default=parse_int_env("CLAUDE_MAX_TOKENS", 1200), dest="max_tokens")
    parser.add_argument("--temperature", type=float, default=parse_float_env("CLAUDE_TEMPERATURE", 0.2))
    parser.add_argument("--timeout", type=float, default=parse_float_env("CLAUDE_TIMEOUT", 180))
    parser.add_argument("--system", default=os.environ.get("CLAUDE_SYSTEM_PROMPT", ""))
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.self_test:
            require_env(["ANTHROPIC_API_KEY", "CLAUDE_API_KEY"])
            if not args.model:
                raise AdapterError("Claude model is empty")
            print(f"ready claude model={args.model}")
            return 0
        if args.live_test:
            call_claude("Rispondi esattamente con OK_CLAUDE.", args)
            print(f"live-ok claude model={args.model}")
            return 0
        prompt = read_prompt()
        if args.mock:
            print(f"[claude-mock:{args.model}] {prompt[:500]}")
            return 0
        print(call_claude(prompt, args))
        return 0
    except AdapterError as exc:
        return fail(exc)


if __name__ == "__main__":
    sys.exit(main())
