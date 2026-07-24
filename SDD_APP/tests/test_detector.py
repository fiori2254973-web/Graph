from __future__ import annotations

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from graph_ode.config import AppConfig
from graph_ode.detector import build_interpretations, classify_cells
from graph_ode.models import CellRef, WorkbookScan


def cell(address: str, value: str, row: int, column: int) -> CellRef:
    return CellRef(sheet="Caso ODE", address=address, row=row, column=column, raw_value=value, display_value=value)


class DetectorTests(unittest.TestCase):
    def test_baseline_interpretation_selected(self) -> None:
        scan = WorkbookScan(
            input_path="sample.xlsx",
            sheets_scanned=["Caso ODE"],
            cells_seen=6,
            limits={},
            cells=[
                cell("A1", "Equazione", 1, 1),
                cell("B1", "y' = a*y", 1, 2),
                cell("A2", "Parametro", 2, 1),
                cell("B2", "a=2", 2, 2),
                cell("A3", "Condizione iniziale", 3, 1),
                cell("B3", "y(0)=1", 3, 2),
            ],
        )
        blocks = classify_cells(scan, AppConfig())
        interpretations = build_interpretations(blocks, AppConfig())
        self.assertEqual(interpretations[0].status, "selected")
        self.assertEqual(interpretations[0].parameters["a"], "2")

    def test_conflicting_parameters_block(self) -> None:
        scan = WorkbookScan(
            input_path="sample.xlsx",
            sheets_scanned=["Caso ODE"],
            cells_seen=5,
            limits={},
            cells=[
                cell("A1", "Equazione", 1, 1),
                cell("B1", "y' = a*y", 1, 2),
                cell("A2", "Parametro", 2, 1),
                cell("B2", "a=2", 2, 2),
                cell("B3", "a=3", 3, 2),
            ],
        )
        blocks = classify_cells(scan, AppConfig())
        interpretations = build_interpretations(blocks, AppConfig())
        self.assertEqual(interpretations[0].status, "blocked")
        self.assertIn("Parametri duplicati", interpretations[0].rejection_reason)


if __name__ == "__main__":
    unittest.main()
