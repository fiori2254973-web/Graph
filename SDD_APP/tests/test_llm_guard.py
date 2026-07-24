from __future__ import annotations

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from graph_ode.llm import llm_contradicts_verified_solution, repair_common_mojibake


class LlmGuardTests(unittest.TestCase):
    def test_detects_sympy_contradiction(self) -> None:
        self.assertTrue(llm_contradicts_verified_solution("SymPy ha fornito una risposta errata."))

    def test_allows_plain_explanation(self) -> None:
        self.assertFalse(llm_contradicts_verified_solution("La soluzione SymPy e' corretta e verificata."))

    def test_repairs_common_mojibake(self) -> None:
        self.assertEqual(repair_common_mojibake("La soluzione Ã¨ corretta"), "La soluzione è corretta")


if __name__ == "__main__":
    unittest.main()
