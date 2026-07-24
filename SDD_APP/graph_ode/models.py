from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from typing import Any


CONFIDENCE_LABELS = ("bassa", "media", "alta")


@dataclass(frozen=True)
class CellRef:
    sheet: str
    address: str
    row: int
    column: int
    raw_value: Any
    display_value: str
    formula: str | None = None
    data_type: str | None = None
    is_merged: bool = False
    is_hidden: bool = False


@dataclass
class WorkbookScan:
    input_path: str
    sheets_scanned: list[str]
    cells_seen: int
    limits: dict[str, Any]
    cells: list[CellRef] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stop_reason: str | None = None


@dataclass
class Evidence:
    feature: str
    weight: int
    note: str


@dataclass
class CandidateBlock:
    id: str
    kind: str
    raw_value: str
    normalized_value: str
    confidence_score: float
    confidence_label: str
    source_cells: list[CellRef]
    evidence: list[Evidence] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class OdeInterpretation:
    id: str
    status: str
    confidence_score: float
    equation_block: str | None
    parameter_blocks: list[str]
    initial_condition_blocks: list[str]
    plot_blocks: list[str]
    normalized_equation: str | None
    parameters: dict[str, str]
    initial_conditions: list[str]
    source_cells: list[dict[str, str]]
    decision_required: bool = False
    rejection_reason: str = ""
    warnings: list[str] = field(default_factory=list)


@dataclass
class SolveResult:
    status: str
    normalized_equation: str | None = None
    solution: str | None = None
    verification: str | None = None
    hints: list[str] = field(default_factory=list)
    plot: str | None = None
    llm_explanation: str | None = None
    warnings: list[str] = field(default_factory=list)
    stop_reason: str | None = None
    error: str | None = None


@dataclass
class RunReport:
    run_id: str
    input: dict[str, Any]
    configuration: dict[str, Any]
    candidate_blocks: list[CandidateBlock]
    interpretations: list[OdeInterpretation]
    selected_interpretation: str | None
    solve_result: SolveResult
    diagnostics: dict[str, Any]


def confidence_label(score: float) -> str:
    if score >= 80:
        return "alta"
    if score >= 50:
        return "media"
    return "bassa"


def to_jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return to_jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(key): to_jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [to_jsonable(item) for item in value]
    return value
