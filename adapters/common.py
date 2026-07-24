#!/usr/bin/env python3
"""Shared helpers for Symposium LLM adapters."""

from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


class AdapterError(Exception):
    """Expected adapter failure without leaking credentials."""


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip()
        if not name or name in os.environ:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ[name] = value


load_env_file(Path(__file__).resolve().parents[1] / ".symposium" / "secrets.env")


def env_first(names: list[str]) -> str:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return ""


def require_env(names: list[str]) -> str:
    value = env_first(names)
    if value:
        return value
    raise AdapterError("missing required environment variable: " + " or ".join(names))


def read_prompt() -> str:
    prompt = sys.stdin.read().strip()
    if not prompt:
        raise AdapterError("empty prompt on stdin")
    return prompt


def parse_int_env(name: str, default: int) -> int:
    raw = os.environ.get(name, "")
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise AdapterError(f"{name} must be an integer") from exc


def parse_float_env(name: str, default: float) -> float:
    raw = os.environ.get(name, "")
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError as exc:
        raise AdapterError(f"{name} must be a float") from exc


def sanitize_text(value: str) -> str:
    return "".join("\ufffd" if 0xD800 <= ord(ch) <= 0xDFFF else ch for ch in value)


def sanitize_json(value: Any) -> Any:
    if isinstance(value, str):
        return sanitize_text(value)
    if isinstance(value, list):
        return [sanitize_json(item) for item in value]
    if isinstance(value, dict):
        return {sanitize_text(str(key)): sanitize_json(item) for key, item in value.items()}
    return value


def post_json(url: str, headers: dict[str, str], payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    data = json.dumps(sanitize_json(payload), ensure_ascii=False).encode("utf-8", errors="replace")
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise AdapterError(f"HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise AdapterError(f"network error: {exc.reason}") from exc
    try:
        decoded = json.loads(body)
    except json.JSONDecodeError as exc:
        raise AdapterError("response is not valid JSON") from exc
    if not isinstance(decoded, dict):
        raise AdapterError("response JSON is not an object")
    return decoded


def fail(exc: Exception) -> int:
    print(f"[adapter-error] {exc}", file=sys.stderr)
    return 2
