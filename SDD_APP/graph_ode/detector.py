from __future__ import annotations

import re
from collections import defaultdict
from typing import Iterable

from .config import AppConfig
from .models import CandidateBlock, CellRef, Evidence, OdeInterpretation, WorkbookScan, confidence_label
from .solver import normalize_ode_text


MATH_WORDS = ("equazione", "equation", "ode", "differenziale", "parametro", "parameter", "condizione", "initial")


def _nearby_text(cell: CellRef, cells: Iterable[CellRef], radius: int) -> str:
    pieces: list[str] = []
    for other in cells:
        if other.sheet != cell.sheet or other.address == cell.address:
            continue
        if abs(other.row - cell.row) <= radius and abs(other.column - cell.column) <= radius:
            pieces.append(other.display_value.lower())
    return " ".join(pieces)


def _add(evidence: list[Evidence], feature: str, weight: int, note: str) -> None:
    evidence.append(Evidence(feature=feature, weight=weight, note=note))


def _score(evidence: list[Evidence]) -> int:
    return max(0, min(100, sum(item.weight for item in evidence)))


def _looks_like_note(text: str) -> bool:
    lowered = text.lower()
    return any(word in lowered for word in ("esempio", "example", "nota", "note", "descrizione", "legend", "legenda"))


def classify_cells(scan: WorkbookScan, config: AppConfig) -> list[CandidateBlock]:
    blocks: list[CandidateBlock] = []
    for index, cell in enumerate(scan.cells, start=1):
        raw = cell.display_value.strip()
        if not raw:
            continue
        lowered = raw.lower()
        near = _nearby_text(cell, scan.cells, config.cell_neighborhood_radius)
        evidence: list[Evidence] = []
        warnings: list[str] = []
        kind = "unknown"
        normalized = raw

        if _looks_like_note(raw):
            warnings.append("Cella trattata con prudenza perche' sembra una nota o un esempio.")
            _add(evidence, "nota testuale", -25, "testo descrittivo/non operativo")

        ic_match = re.match(r"^y\s*'{0,6}\s*\(\s*[^)]*\s*\)\s*=", raw.replace("^", "**"))
        param_match = re.match(r"^(?!y\s*\()[A-Za-z_]\w*\s*=\s*[-+]?[\w./*^() ]+$", raw)
        has_derivative = bool(re.search(r"\by\s*'{1,6}|Derivative\s*\(", raw))
        has_equation_symbols = "=" in raw and bool(re.search(r"\by\b|Derivative|sin|cos|exp|log", raw))
        has_math_operator = bool(re.search(r"[+\-*/^=()]", raw))

        if ic_match:
            kind = "initial_condition"
            normalized = raw.replace("^", "**")
            _add(evidence, "pattern y(x0)=value", 45, "condizione iniziale esplicita")
        elif has_derivative or (has_equation_symbols and not param_match):
            kind = "equation"
            normalized = normalize_ode_text(raw)
            if has_derivative:
                _add(evidence, "derivata esplicita", 40, "contiene y' o Derivative")
            if has_equation_symbols:
                _add(evidence, "uguaglianza matematica", 15, "contiene = e simboli di funzione")
        elif param_match:
            kind = "parameter"
            normalized = raw.replace("^", "**")
            _add(evidence, "pattern nome=valore", 35, "parametro scalare candidato")
        elif re.match(r"^(x_min|x_max|plot_points|points)\s*=", lowered):
            kind = "plot_range"
            normalized = raw.replace("^", "**")
            _add(evidence, "parametro grafico", 35, "configurazione del grafico candidata")
        elif has_math_operator:
            kind = "unknown"
            _add(evidence, "testo matematico debole", 20, "contiene operatori ma manca struttura ODE")

        if any(word in near for word in ("equazione", "equation", "ode", "differenziale")) and kind == "equation":
            _add(evidence, "etichetta vicina equazione", 25, "label vicina coerente")
        if any(word in near for word in ("parametro", "parameter")) and kind == "parameter":
            _add(evidence, "etichetta vicina parametro", 20, "label vicina coerente")
        if any(word in near for word in ("condizione", "initial")) and kind == "initial_condition":
            _add(evidence, "etichetta vicina condizione", 20, "label vicina coerente")
        if any(word in cell.sheet.lower() for word in ("ode", "equazione", "equation", "caso", "case")):
            _add(evidence, "nome foglio coerente", 10, "foglio orientato al problema")
        if cell.formula:
            warnings.append("La cella contiene una formula: il report conserva la formula, non il valore cached.")
        if cell.is_hidden:
            warnings.append("La cella e' nascosta: usare il risultato con prudenza.")

        score = _score(evidence)
        if kind != "unknown" or score >= 20:
            blocks.append(
                CandidateBlock(
                    id=f"B{index:03d}",
                    kind=kind,
                    raw_value=raw,
                    normalized_value=normalized,
                    confidence_score=score,
                    confidence_label=confidence_label(score),
                    source_cells=[cell],
                    evidence=evidence,
                    warnings=warnings,
                )
            )
    return blocks


def _cell_key(block: CandidateBlock) -> list[dict[str, str]]:
    return [{"sheet": cell.sheet, "address": cell.address} for cell in block.source_cells]


def build_interpretations(blocks: list[CandidateBlock], config: AppConfig) -> list[OdeInterpretation]:
    eligible = [block for block in blocks if block.confidence_score >= config.candidate_min_confidence]
    equations = [block for block in eligible if block.kind == "equation"]
    params = [block for block in eligible if block.kind == "parameter"]
    ics = [block for block in eligible if block.kind == "initial_condition"]
    plots = [block for block in eligible if block.kind == "plot_range"]
    interpretations: list[OdeInterpretation] = []

    if not equations:
        return [
            OdeInterpretation(
                id="I001",
                status="blocked",
                confidence_score=0,
                equation_block=None,
                parameter_blocks=[],
                initial_condition_blocks=[],
                plot_blocks=[],
                normalized_equation=None,
                parameters={},
                initial_conditions=[],
                source_cells=[],
                decision_required=True,
                rejection_reason="Nessuna equazione differenziale con confidenza sufficiente.",
            )
        ]

    for idx, equation in enumerate(equations, start=1):
        selected_params = _dedupe_parameter_values(params)
        selected_ics = _dedupe_initial_conditions(ics)
        source_cells = _cell_key(equation)
        for block in params + ics + plots:
            source_cells.extend(_cell_key(block))
        confidence = min(
            100,
            equation.confidence_score
            + (10 if params else 0)
            + (10 if ics else 0)
            - (20 if len(equations) > 1 else 0),
        )
        warnings: list[str] = []
        status = "candidate"
        rejection = ""
        decision_required = confidence < config.auto_solve_confidence or len(equations) > 1
        if selected_params["conflicts"]:
            status = "blocked"
            rejection = "Parametri duplicati con valori incompatibili: " + "; ".join(selected_params["conflicts"])
            decision_required = True
        elif selected_ics["conflicts"]:
            status = "blocked"
            rejection = "Condizioni iniziali duplicate incompatibili: " + "; ".join(selected_ics["conflicts"])
            decision_required = True
        elif confidence >= config.auto_solve_confidence and len(equations) == 1:
            status = "selected"
        else:
            warnings.append("Interpretazione proposta ma non selezionata automaticamente per confidenza/ambiguita'.")

        interpretations.append(
            OdeInterpretation(
                id=f"I{idx:03d}",
                status=status,
                confidence_score=confidence,
                equation_block=equation.id,
                parameter_blocks=[block.id for block in params],
                initial_condition_blocks=[block.id for block in ics],
                plot_blocks=[block.id for block in plots],
                normalized_equation=equation.normalized_value,
                parameters=selected_params["values"],
                initial_conditions=list(selected_ics["values"].values()),
                source_cells=source_cells,
                decision_required=decision_required,
                rejection_reason=rejection,
                warnings=warnings,
            )
        )
    return interpretations


def _dedupe_parameter_values(blocks: list[CandidateBlock]) -> dict[str, object]:
    seen: dict[str, str] = {}
    source: dict[str, str] = {}
    conflicts: list[str] = []
    for block in blocks:
        if "=" not in block.normalized_value:
            continue
        name, value = [piece.strip() for piece in block.normalized_value.split("=", 1)]
        if name in seen and seen[name] != value:
            conflicts.append(f"{name}: {seen[name]} ({source[name]}) vs {value} ({block.id})")
        else:
            seen[name] = value
            source[name] = block.id
    return {"values": seen, "conflicts": conflicts}


def _dedupe_initial_conditions(blocks: list[CandidateBlock]) -> dict[str, object]:
    seen: dict[str, str] = {}
    conflicts: list[str] = []
    grouped: defaultdict[str, list[str]] = defaultdict(list)
    for block in blocks:
        if "=" not in block.normalized_value:
            continue
        lhs, value = [piece.strip() for piece in block.normalized_value.split("=", 1)]
        grouped[lhs].append(value)
        if lhs in seen and seen[lhs] != value:
            conflicts.append(f"{lhs}: {seen[lhs]} vs {value}")
        else:
            seen[lhs] = value
    return {"values": {lhs: f"{lhs}={value}" for lhs, value in seen.items()}, "conflicts": conflicts}
