from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class AppConfig:
    scan_max_sheets: int = 20
    scan_max_cells: int = 20000
    cell_neighborhood_radius: int = 2
    candidate_min_confidence: int = 50
    auto_solve_confidence: int = 80
    allow_hidden_sheets: bool = False
    allow_formula_cells: bool = True
    model_name: str = "phi4-mini"
    ollama_host: str = "http://localhost:11434"
    ollama_timeout: int = 180
    plot_enabled: bool = True
    plot_x_min: float = 0.0
    plot_x_max: float = 10.0
    plot_points: int = 100
    show_plot: bool = False
    pause_at_end: bool = True

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def default_output_dir(input_path: Path, run_id: str) -> Path:
    stem = input_path.stem if input_path.name else "run"
    return Path("outputs") / f"{stem}_{run_id}"
