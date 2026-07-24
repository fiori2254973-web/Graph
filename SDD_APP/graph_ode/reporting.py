from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import CandidateBlock, OdeInterpretation, RunReport, SolveResult, WorkbookScan, to_jsonable


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(to_jsonable(value), ensure_ascii=False, indent=2), encoding="utf-8")


def _sources_md(sources: list[dict[str, str]]) -> str:
    if not sources:
        return "- nessuna cella sorgente"
    return "\n".join(f"- {item['sheet']}!{item['address']}" for item in sources)


def build_markdown_report(
    run_id: str,
    scan: WorkbookScan,
    blocks: list[CandidateBlock],
    interpretations: list[OdeInterpretation],
    selected: OdeInterpretation | None,
    result: SolveResult,
    config: dict[str, Any],
) -> str:
    warnings = list(scan.warnings) + result.warnings
    lines = [
        f"# Graph ODE Report `{run_id}`",
        "",
        "## Input",
        f"- File: `{scan.input_path}`",
        f"- Fogli scansionati: {', '.join(scan.sheets_scanned) or 'nessuno'}",
        f"- Celle non vuote viste: {scan.cells_seen}",
        "",
        "## Configurazione",
    ]
    for key, value in config.items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Blocchi candidati"])
    for block in blocks:
        cell_list = ", ".join(f"{cell.sheet}!{cell.address}" for cell in block.source_cells)
        lines.append(
            f"- `{block.id}` `{block.kind}` score `{block.confidence_score}` "
            f"({block.confidence_label}) da {cell_list}: `{block.normalized_value}`"
        )
    lines.extend(["", "## Interpretazioni"])
    for item in interpretations:
        lines.append(
            f"- `{item.id}` status `{item.status}` score `{item.confidence_score}` "
            f"decision_required `{item.decision_required}` reason `{item.rejection_reason}`"
        )
    lines.extend(["", "## Interpretazione selezionata"])
    if selected:
        lines.append(f"- ID: `{selected.id}`")
        lines.append(f"- Equazione: `{selected.normalized_equation}`")
        lines.append(f"- Parametri: `{selected.parameters}`")
        lines.append(f"- Condizioni iniziali: `{selected.initial_conditions}`")
        lines.append("")
        lines.append("### Celle sorgente")
        lines.append(_sources_md(selected.source_cells))
    else:
        lines.append("- nessuna")
    lines.extend(
        [
            "",
            "## Risultato SymPy",
            f"- Status: `{result.status}`",
            f"- Equazione normalizzata: `{result.normalized_equation}`",
            f"- Soluzione: `{result.solution}`",
            f"- Verifica: `{result.verification}`",
            f"- Stop reason: `{result.stop_reason}`",
            f"- Errore: `{result.error}`",
            f"- Grafico: `{result.plot}`",
            "",
            "## Spiegazione phi4-mini",
            result.llm_explanation or "_Non generata._",
            "",
            "## Warning",
        ]
    )
    if scan.stop_reason:
        lines.append(f"- Stop scansione: {scan.stop_reason}")
    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    if not warnings and not scan.stop_reason and not result.stop_reason:
        lines.append("- nessuno")
    return "\n".join(lines) + "\n"


def write_run_artifacts(
    output_dir: Path,
    report: RunReport,
    scan: WorkbookScan,
    blocks: list[CandidateBlock],
    interpretations: list[OdeInterpretation],
    selected: OdeInterpretation | None,
    result: SolveResult,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "workbook_scan.json", scan)
    write_json(output_dir / "candidate_blocks.json", blocks)
    write_json(output_dir / "interpretations.json", interpretations)
    write_json(output_dir / "selected_interpretation.json", selected)
    write_json(output_dir / "solve_result.json", result)
    write_json(output_dir / "run_report.json", report)
    markdown = build_markdown_report(
        report.run_id,
        scan,
        blocks,
        interpretations,
        selected,
        result,
        report.configuration,
    )
    (output_dir / "report.md").write_text(markdown, encoding="utf-8")
