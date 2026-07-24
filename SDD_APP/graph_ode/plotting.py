from __future__ import annotations

from pathlib import Path
from typing import Any

from .config import AppConfig
from .models import SolveResult
from .solver import extract_solution_expression


def save_plot(context: dict[str, Any], config: AppConfig, output_path: Path) -> tuple[str | None, list[str]]:
    warnings: list[str] = []
    if not config.plot_enabled:
        return None, warnings
    if config.plot_points < 2:
        return None, ["Grafico bloccato: plot_points deve essere almeno 2."]
    if config.plot_x_min >= config.plot_x_max:
        return None, ["Grafico bloccato: plot_x_min deve essere minore di plot_x_max."]
    solution = context.get("solution")
    sp = context.get("sp")
    x = context.get("x")
    yx = context.get("yx")
    if solution is None or sp is None or x is None or yx is None:
        return None, ["Grafico bloccato: soluzione simbolica non disponibile."]

    expr = extract_solution_expression(solution, yx)
    if expr is None:
        return None, ["Grafico bloccato: la soluzione non ha forma y(x) = espressione."]
    free = sorted(str(symbol) for symbol in (expr.free_symbols - {x}))
    if free:
        return None, ["Grafico bloccato: simboli liberi senza valore: " + ", ".join(free)]

    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ModuleNotFoundError as exc:
        return None, [f"Grafico bloccato: dipendenza mancante {exc.name}."]

    x_values = np.linspace(config.plot_x_min, config.plot_x_max, config.plot_points)
    numeric_func = sp.lambdify(x, expr, "numpy")
    y_values = numeric_func(x_values)
    if np.isscalar(y_values):
        y_values = np.full_like(x_values, y_values, dtype=float)
    y_values = np.asarray(y_values)
    if np.iscomplexobj(y_values):
        if np.allclose(np.imag(y_values), 0):
            y_values = np.real(y_values)
        else:
            return None, ["Grafico bloccato: la soluzione produce valori complessi nel range richiesto."]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 4))
    plt.plot(x_values, y_values, label="y(x)")
    plt.title("Soluzione dell'equazione differenziale")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    if config.show_plot:
        plt.show()
    else:
        plt.close()
    return str(output_path), warnings


def attach_plot(result: SolveResult, context: dict[str, Any], config: AppConfig, output_path: Path) -> None:
    plot_path, warnings = save_plot(context, config, output_path)
    result.plot = plot_path
    result.warnings.extend(warnings)
