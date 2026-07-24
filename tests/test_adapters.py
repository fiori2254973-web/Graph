from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
ADAPTERS = ROOT / "adapters"
sys.path.insert(0, str(ADAPTERS))

import claude_adapter  # noqa: E402
import gemini_adapter  # noqa: E402


class AdapterTests(unittest.TestCase):
    def run_adapter(self, script: str, args: list[str], prompt: str, env: dict[str, str] | None = None):
        merged_env = os.environ.copy()
        if env:
            merged_env.update(env)
        return subprocess.run(
            [sys.executable, str(ADAPTERS / script), *args],
            input=prompt,
            text=True,
            capture_output=True,
            cwd=str(ROOT),
            env=merged_env,
            timeout=20,
        )

    def test_claude_mock_outputs_text(self):
        result = self.run_adapter("claude_adapter.py", ["--mock"], "hello claude")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[claude-mock:", result.stdout)
        self.assertIn("hello claude", result.stdout)

    def test_gemini_mock_outputs_text(self):
        result = self.run_adapter("gemini_adapter.py", ["--mock"], "hello gemini")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[gemini-mock:", result.stdout)
        self.assertIn("hello gemini", result.stdout)

    def test_claude_self_test_requires_key(self):
        env = {"ANTHROPIC_API_KEY": "", "CLAUDE_API_KEY": ""}
        result = self.run_adapter("claude_adapter.py", ["--self-test"], "", env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required environment variable", result.stderr)

    def test_gemini_self_test_requires_key(self):
        env = {"GEMINI_API_KEY": "", "GOOGLE_API_KEY": "", "GOOGLE_GENERATIVE_AI_API_KEY": ""}
        result = self.run_adapter("gemini_adapter.py", ["--self-test"], "", env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required environment variable", result.stderr)

    def test_claude_extract_text(self):
        response = {"content": [{"type": "text", "text": "first"}, {"type": "text", "text": "second"}]}
        self.assertEqual(claude_adapter.extract_text(response), "first\nsecond")

    def test_gemini_extract_text(self):
        response = {"candidates": [{"content": {"parts": [{"text": "first"}, {"text": "second"}]}}]}
        self.assertEqual(gemini_adapter.extract_text(response), "first\nsecond")


if __name__ == "__main__":
    unittest.main()
