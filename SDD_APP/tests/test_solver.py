from __future__ import annotations

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from graph_ode.models import OdeInterpretation
from graph_ode.solver import normalize_ode_text, solve_interpretation


class SolverTests(unittest.TestCase):
    def test_normalize_prime_notation(self) -> None:
        self.assertEqual(normalize_ode_text("y' = a*y"), "Derivative(y(x), x) = a*y(x)")

    def test_solve_linear_ode_with_parameter_and_ic(self) -> None:
        interpretation = OdeInterpretation(
            id="I001",
            status="selected",
            confidence_score=100,
            equation_block="B001",
            parameter_blocks=["B002"],
            initial_condition_blocks=["B003"],
            plot_blocks=[],
            normalized_equation="y' = a*y",
            parameters={"a": "2"},
            initial_conditions=["y(0)=1"],
            source_cells=[{"sheet": "S", "address": "A1"}],
        )
        result, _context = solve_interpretation(interpretation)
        self.assertEqual(result.status, "solved")
        self.assertIn("exp(2*x)", result.solution or "")
        self.assertTrue((result.verification or "").startswith("(True"))

    def test_missing_parameter_blocks_run(self) -> None:
        interpretation = OdeInterpretation(
            id="I001",
            status="selected",
            confidence_score=90,
            equation_block="B001",
            parameter_blocks=[],
            initial_condition_blocks=[],
            plot_blocks=[],
            normalized_equation="y' = a*y",
            parameters={},
            initial_conditions=[],
            source_cells=[{"sheet": "S", "address": "A1"}],
        )
        result, _context = solve_interpretation(interpretation)
        self.assertEqual(result.status, "blocked")
        self.assertIn("Parametro richiesto mancante", result.stop_reason or "")


if __name__ == "__main__":
    unittest.main()
