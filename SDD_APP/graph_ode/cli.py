from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from . import __version__
from .config import AppConfig, default_output_dir
from .detector import build_interpretations, classify_cells
from .excel_reader import scan_workbook
from .llm import explain_with_phi4_mini
from .models import OdeInterpretation, RunReport, SolveResult
from .plotting import attach_plot
from .reporting import write_run_artifacts
from .solver import solve_interpretation


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Graph ODE SDD: legge Excel elastici, risolve ODE con SymPy e spiega con phi4-mini."
    )
    parser.add_argument("--input", "-i", required=True, help="File Excel .xlsx/.xlsm da analizzare.")
    parser.add_argument("--output", "-o", default="", help="Cartella di output degli artefatti.")
    parser.add_argument("--sheet", action="append", help="Foglio da analizzare. Ripetibile. Default: tutti.")
    parser.add_argument("--scan-max-sheets", type=int, default=20)
    parser.add_argument("--scan-max-cells", type=int, default=20000)
    parser.add_argument("--candidate-min-confidence", type=int, default=50)
    parser.add_argument("--auto-solve-confidence", type=int, default=80)
    parser.add_argument("--confirm-low-confidence", action="store_true", help="Permette di risolvere una candidate interpretation sotto soglia.")
    parser.add_argument("--select-interpretation", default="", help="ID interpretazione da selezionare, es. I002.")
    parser.add_argument("--allow-hidden-sheets", action="store_true")
    parser.add_argument("--disallow-formula-cells", action="store_true")
    parser.add_argument("--no-plot", action="store_true")
    parser.add_argument("--show-plot", action="store_true")
    parser.add_argument("--plot-x-min", type=float, default=0.0)
    parser.add_argument("--plot-x-max", type=float, default=10.0)
    parser.add_argument("--plot-points", type=int, default=100)
    parser.add_argument("--no-ollama", action="store_true", help="Non chiamare Ollama/phi4-mini.")
    parser.add_argument("--ollama-host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    parser.add_argument("--ollama-timeout", type=int, default=180)
    parser.add_argument("--model", default="phi4-mini", help="Modello Ollama. Default: phi4-mini.")
    parser.add_argument("--no-pause", action="store_true", help="Non attendere Invio prima di chiudere.")
    parser.add_argument("--version", action="version", version=f"Graph ODE SDD_APP {__version__}")
    return parser.parse_args(argv)


def _build_config(args: argparse.Namespace) -> AppConfig:
    return AppConfig(
        scan_max_sheets=args.scan_max_sheets,
        scan_max_cells=args.scan_max_cells,
        candidate_min_confidence=args.candidate_min_confidence,
        auto_solve_confidence=args.auto_solve_confidence,
        allow_hidden_sheets=args.allow_hidden_sheets,
        allow_formula_cells=not args.disallow_formula_cells,
        model_name=args.model,
        ollama_host=args.ollama_host,
        ollama_timeout=args.ollama_timeout,
        plot_enabled=not args.no_plot,
        plot_x_min=args.plot_x_min,
        plot_x_max=args.plot_x_max,
        plot_points=args.plot_points,
        show_plot=args.show_plot,
        pause_at_end=not args.no_pause,
    )


def _choose_interpretation(
    interpretations: list[OdeInterpretation],
    args: argparse.Namespace,
    config: AppConfig,
) -> tuple[OdeInterpretation | None, SolveResult | None]:
    if args.select_interpretation:
        selected = next((item for item in interpretations if item.id == args.select_interpretation), None)
        if selected is None:
            return None, SolveResult(status="blocked", stop_reason=f"Interpretazione non trovata: {args.select_interpretation}")
        selected.status = "selected"
        selected.decision_required = False
        return selected, None

    selected = next((item for item in interpretations if item.status == "selected"), None)
    if selected:
        return selected, None

    candidate = next((item for item in interpretations if item.status == "candidate"), None)
    if candidate and args.confirm_low_confidence:
        candidate.status = "selected"
        candidate.decision_required = False
        candidate.warnings.append("Selezionata con --confirm-low-confidence.")
        return candidate, None

    blocked = next((item for item in interpretations if item.status == "blocked"), None)
    reason = blocked.rejection_reason if blocked else "Nessuna interpretazione selezionata automaticamente."
    return None, SolveResult(
        status="blocked",
        stop_reason=(
            reason
            or f"Serve conferma: usare --select-interpretation ID oppure --confirm-low-confidence sotto soglia {config.auto_solve_confidence}."
        ),
    )


def _pause(enabled: bool) -> None:
    if not enabled or not sys.stdin.isatty():
        return
    try:
        input("\nPremi Invio per chiudere...")
    except EOFError:
        pass


def run(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    config = _build_config(args)
    input_path = Path(args.input)
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output) if args.output else default_output_dir(input_path, run_id)

    print("== Graph ODE SDD_APP ==")
    print(f"Input: {input_path}")
    print(f"Output: {output_dir}")

    scan = scan_workbook(input_path, config, selected_sheets=args.sheet)
    blocks = classify_cells(scan, config) if not scan.stop_reason else []
    interpretations = build_interpretations(blocks, config) if not scan.stop_reason else []
    selected, pre_result = _choose_interpretation(interpretations, args, config) if interpretations else (
        None,
        SolveResult(status="blocked", stop_reason=scan.stop_reason or "Nessuna interpretazione disponibile."),
    )
    result = pre_result or SolveResult(status="blocked", stop_reason="Nessuna interpretazione selezionata.")
    context: dict[str, object] = {}

    if selected and pre_result is None:
        result, context = solve_interpretation(selected)
        if result.status == "solved":
            attach_plot(result, context, config, output_dir / "plot.png")
        if not args.no_ollama:
            print("Chiamo Ollama/phi4-mini per la spiegazione...")
            try:
                result.llm_explanation = explain_with_phi4_mini(selected, result, config)
            except Exception as exc:
                result.warnings.append(f"Spiegazione Ollama non generata: {type(exc).__name__}: {exc}")
        else:
            result.warnings.append("Spiegazione Ollama disabilitata con --no-ollama.")

    diagnostics = {
        "warnings": list(scan.warnings) + result.warnings,
        "stop_reason": scan.stop_reason or result.stop_reason,
    }
    report = RunReport(
        run_id=run_id,
        input={
            "path": str(input_path),
            "sheets_scanned": scan.sheets_scanned,
            "limits": config.as_dict(),
        },
        configuration=config.as_dict(),
        candidate_blocks=blocks,
        interpretations=interpretations,
        selected_interpretation=selected.id if selected else None,
        solve_result=result,
        diagnostics=diagnostics,
    )
    write_run_artifacts(output_dir, report, scan, blocks, interpretations, selected, result)

    print("\n=== Esito ===")
    print(f"Status: {result.status}")
    if selected:
        print(f"Interpretazione: {selected.id}")
        print(f"Equazione: {selected.normalized_equation}")
    if result.solution:
        print(f"Soluzione: {result.solution}")
    if result.verification:
        print(f"Verifica: {result.verification}")
    if result.plot:
        print(f"Grafico: {result.plot}")
    if diagnostics["stop_reason"]:
        print(f"Stop: {diagnostics['stop_reason']}")
    print(f"Report: {output_dir / 'report.md'}")
    _pause(config.pause_at_end)
    return 0 if result.status == "solved" else 1


def main() -> None:
    raise SystemExit(run())
