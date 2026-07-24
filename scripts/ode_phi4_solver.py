#!/usr/bin/env python3
"""Solver interattivo per equazioni differenziali con SymPy, Ollama e symposium.

Uso rapido:
  python scripts/ode_phi4_solver.py --equation "y' = y" --ics "y(0)=1"
  python scripts/ode_phi4_solver.py --equation "y'' + y = 0" --ics "y(0)=0, y'(0)=1"
  python scripts/ode_phi4_solver.py --equation "y' = a*y" --params "a=2" --ics "y(0)=1"
  python scripts/ode_phi4_solver.py --equation "y' = a*y" --params "a=2" --ics "y(0)=1" --plot

Note:
  - SymPy produce la soluzione simbolica verificabile quando possibile.
  - Ollama/phi4-mini spiega il risultato o il limite incontrato.
  - Il symposium locale viene usato come log opzionale se Redis e' attivo.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import textwrap
import time
import urllib.error
import urllib.request
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

REDIS_CONTAINER_NAME = os.environ.get("SYMPOSIUM_REDIS_CONTAINER", "redis-stack-symposium")
REDIS_IMAGE = os.environ.get("SYMPOSIUM_REDIS_IMAGE", "redis/redis-stack-server:latest")
REDIS_VOLUME = os.environ.get("SYMPOSIUM_REDIS_VOLUME", "redis-stack-symposium-data")


def require_sympy() -> Any:
    try:
        import sympy as sp
        from sympy.parsing.sympy_parser import (
            implicit_multiplication_application,
            standard_transformations,
        )
    except ModuleNotFoundError:
        print(
            "Manca SymPy. Installalo con:\n\n"
            "  python -m pip install sympy\n",
            file=sys.stderr,
        )
        sys.exit(1)
    return sp, standard_transformations + (implicit_multiplication_application,)


def require_plot_deps() -> tuple[Any, Any]:
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ModuleNotFoundError:
        print(
            "Per generare grafici servono numpy e matplotlib. Installali con:\n\n"
            "  python -m pip install numpy matplotlib\n",
            file=sys.stderr,
        )
        sys.exit(1)
    return np, plt


def build_local_dict(sp: Any, x: Any, y: Any, params: dict[str, Any] | None = None) -> dict[str, Any]:
    local_dict = {
        "x": x,
        "y": y,
        "Derivative": sp.Derivative,
        "Eq": sp.Eq,
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "asin": sp.asin,
        "acos": sp.acos,
        "atan": sp.atan,
        "sinh": sp.sinh,
        "cosh": sp.cosh,
        "tanh": sp.tanh,
        "exp": sp.exp,
        "log": sp.log,
        "sqrt": sp.sqrt,
        "pi": sp.pi,
        "E": sp.E,
        "I": sp.I,
    }
    if params:
        local_dict.update(params)
    return local_dict


def normalize_ode_text(raw: str) -> str:
    text = raw.strip().replace("^", "**")

    def prime_repl(match: re.Match[str]) -> str:
        order = len(match.group("primes"))
        if order == 1:
            return "Derivative(y(x), x)"
        return f"Derivative(y(x), (x, {order}))"

    text = re.sub(r"\by\s*(?P<primes>'{1,6})", prime_repl, text)
    text = re.sub(r"\by\b(?!\s*\()", "y(x)", text)
    return text


def parse_expression(expr: str, sp: Any, transformations: Any, local_dict: dict[str, Any]) -> Any:
    from sympy.parsing.sympy_parser import parse_expr

    return parse_expr(
        expr,
        local_dict=local_dict,
        transformations=transformations,
        evaluate=False,
    )


def parse_parameters(raw: str, sp: Any, x: Any, y: Any, transformations: Any) -> dict[str, Any]:
    if not raw.strip():
        return {}

    params: dict[str, Any] = {}
    reserved_names = set(build_local_dict(sp, x, y))
    parts = [item.strip() for item in re.split(r"[;,]", raw) if item.strip()]
    for item in parts:
        if "=" not in item:
            raise ValueError("Parametro non riconosciuto. Usa forme tipo a=2 oppure k=1/3.")
        name, value_text = [piece.strip() for piece in item.split("=", 1)]
        if not re.match(r"^[A-Za-z_]\w*$", name):
            raise ValueError(f"Nome parametro non valido: {name!r}.")
        if name in reserved_names:
            raise ValueError(f"Nome parametro riservato: {name!r}.")
        local_dict = build_local_dict(sp, x, y, params)
        params[name] = parse_expression(value_text.replace("^", "**"), sp, transformations, local_dict)
    return params


def parse_equation(
    raw: str,
    sp: Any,
    x: Any,
    y: Any,
    transformations: Any,
    params: dict[str, Any],
) -> tuple[Any, str]:
    local_dict = build_local_dict(sp, x, y, params)
    normalized = normalize_ode_text(raw)
    if normalized.startswith("Eq("):
        parsed = parse_expression(normalized, sp, transformations, local_dict)
        return parsed, normalized
    if "=" in normalized:
        left, right = normalized.split("=", 1)
        return (
            sp.Eq(
                parse_expression(left, sp, transformations, local_dict),
                parse_expression(right, sp, transformations, local_dict),
            ),
            normalized,
        )
    return (
        sp.Eq(parse_expression(normalized, sp, transformations, local_dict), 0),
        normalized,
    )


def parse_initial_conditions(
    raw: str,
    sp: Any,
    x: Any,
    y: Any,
    yx: Any,
    transformations: Any,
    params: dict[str, Any],
) -> dict[Any, Any]:
    if not raw.strip():
        return {}

    from sympy.parsing.sympy_parser import parse_expr

    ics: dict[Any, Any] = {}
    parts = [item.strip() for item in re.split(r"[;,]", raw) if item.strip()]
    for item in parts:
        match = re.match(
            r"^y(?P<primes>'*)\s*\(\s*(?P<x0>[^)]*)\s*\)\s*=\s*(?P<value>.+)$",
            item.replace("^", "**"),
        )
        if not match:
            raise ValueError(
                "Condizione iniziale non riconosciuta. Usa forme tipo "
                "y(0)=1 oppure y'(0)=0."
            )
        local_dict = build_local_dict(sp, x, y, params)
        x0 = parse_expr(match.group("x0"), local_dict=local_dict, transformations=transformations)
        value = parse_expr(
            match.group("value"),
            local_dict=local_dict,
            transformations=transformations,
        )
        order = len(match.group("primes"))
        lhs = yx.subs(x, x0) if order == 0 else sp.Derivative(yx, (x, order)).subs(x, x0)
        ics[lhs] = value
    return ics


def solve_with_sympy(equation: Any, sp: Any, yx: Any, ics: dict[Any, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "solution": None,
        "hints": [],
        "verification": None,
        "error": None,
    }
    try:
        result["hints"] = list(sp.classify_ode(equation, yx))
    except Exception as exc:  # SymPy puo' fallire anche solo nella classificazione.
        result["hints"] = [f"classify_ode non riuscito: {exc}"]

    try:
        kwargs = {"ics": ics} if ics else {}
        solution = sp.dsolve(equation, yx, **kwargs)
        result["solution"] = solution
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        return result

    try:
        result["verification"] = sp.checkodesol(equation, result["solution"], func=yx)
    except Exception as exc:
        result["verification"] = f"Verifica automatica non riuscita: {type(exc).__name__}: {exc}"
    return result


def extract_solution_expression(solution: Any, yx: Any) -> Any | None:
    if solution is None:
        return None
    candidates = solution if isinstance(solution, list | tuple) else [solution]
    for item in candidates:
        if getattr(item, "lhs", None) == yx:
            return item.rhs
    return None


def parse_numeric_bound(raw: str, default: float, sp: Any, transformations: Any) -> float:
    if not raw.strip():
        return default
    value = parse_expression(raw.replace("^", "**"), sp, transformations, build_local_dict(sp, sp.Symbol("x"), sp.Function("y")))
    return float(sp.N(value))


def plot_solution(
    solution: Any,
    sp: Any,
    x: Any,
    yx: Any,
    *,
    x_min: float,
    x_max: float,
    points: int,
    output: str,
    show: bool,
) -> bool:
    expr = extract_solution_expression(solution, yx)
    if expr is None:
        print("\n=== Grafico ===")
        print("Grafico non generato: la soluzione non ha forma y(x) = espressione.")
        return False

    unresolved = sorted(str(symbol) for symbol in (expr.free_symbols - {x}))
    if unresolved:
        print("\n=== Grafico ===")
        print(
            "Grafico non generato: la soluzione contiene simboli senza valore: "
            + ", ".join(unresolved)
        )
        print("Aggiungi condizioni iniziali o parametri numerici prima di plottare.")
        return False

    if points < 2:
        print("\n=== Grafico ===")
        print("Grafico non generato: --plot-points deve essere almeno 2.")
        return False
    if x_min == x_max:
        print("\n=== Grafico ===")
        print("Grafico non generato: x minimo e x massimo coincidono.")
        return False

    np, plt = require_plot_deps()
    x_values = np.linspace(x_min, x_max, points)
    numeric_func = sp.lambdify(x, expr, "numpy")
    y_values = numeric_func(x_values)
    if np.isscalar(y_values):
        y_values = np.full_like(x_values, y_values, dtype=float)
    y_values = np.asarray(y_values)
    if np.iscomplexobj(y_values):
        if np.allclose(np.imag(y_values), 0):
            y_values = np.real(y_values)
        else:
            print("\n=== Grafico ===")
            print("Grafico non generato: la soluzione produce valori complessi nel range richiesto.")
            return False

    plt.figure(figsize=(10, 4))
    plt.plot(x_values, y_values, label="y(x)")
    plt.title("Soluzione dell'equazione differenziale")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=150)
        print("\n=== Grafico ===")
        print(f"Grafico salvato in: {output}")
    if show:
        plt.show()
    else:
        plt.close()
    return True


def ollama_generate(host: str, model: str, prompt: str, timeout: int) -> str:
    url = host.rstrip("/") + "/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama ha risposto HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Ollama non raggiungibile su {host}: {exc.reason}") from exc
    response_text = str(body.get("response", "")).strip()
    if not response_text:
        raise RuntimeError(
            "Ollama ha risposto senza testo. Prova a verificare il modello con: "
            f"ollama run {model}"
        )
    return response_text


def sympy_verified(sympy_result: dict[str, Any]) -> bool:
    verification = sympy_result.get("verification")
    return isinstance(verification, tuple) and len(verification) >= 1 and verification[0] is True


def llm_contradicts_verified_solution(text: str) -> bool:
    lowered = text.lower().replace("\u00e8", "e'").replace("\u00e9", "e'")
    contradiction_markers = [
        "c'e' un errore nella soluzione",
        "errore nella soluzione fornita",
        "mancava della condizione iniziale",
        "non soddisfa la condizione iniziale",
        "non soddisfa le condizioni iniziali",
        "sympy ha fornito la risposta errata",
        "sympy ha fornito una risposta errata",
        "sympy ha sbagliato",
        "sympy non e' corretta",
        "sympy fornita non era corretta",
        "soluzione fornita da sympy, non e' corretta",
        "la soluzione fornita da sympy non",
        "la soluzione sympy fornita non era corretta",
        "non e' corretta per l'equazione",
        "non era corretta",
    ]
    return any(marker in lowered for marker in contradiction_markers)


def fallback_verified_explanation(sympy_result: dict[str, Any]) -> str:
    return textwrap.dedent(
        f"""
        Spiegazione deterministica:
        1. La soluzione riportata da SymPy e' stata verificata automaticamente.
        2. Soluzione verificata: {sympy_result["solution"]}
        3. Verifica SymPy: {sympy_result["verification"]}
        4. Se vuoi una spiegazione discorsiva, puoi riprovare: il risultato matematico da mantenere e' quello verificato sopra.
        """
    ).strip()


def print_llm_response(response: str, sympy_result: dict[str, Any]) -> None:
    if sympy_verified(sympy_result) and llm_contradicts_verified_solution(response):
        print(
            "[avviso] La risposta LLM contraddice una soluzione verificata da SymPy "
            "ed e' stata soppressa."
        )
        print(fallback_verified_explanation(sympy_result))
        return
    print(response)


def build_phi4_prompt(
    raw_equation: str,
    normalized: str,
    params: dict[str, Any],
    ics: dict[Any, Any],
    sympy_result: dict[str, Any],
) -> str:
    return textwrap.dedent(
        f"""
        Sei un tutor di matematica. Il programma usa SymPy come fonte della soluzione
        e tu devi solo spiegare. Non descrivere te stesso come un modello progettato
        per usare SymPy.

        Regole obbligatorie:
        - Se `Verifica SymPy` e' `(True, 0)`, dichiara che la soluzione SymPy e' corretta.
        - Non dire che SymPy ha sbagliato quando la verifica e' positiva.
        - Non dire che la soluzione non soddisfa le condizioni iniziali quando la verifica e' positiva.
        - Non usare parole come `errore`, `errata`, `non corretta` riferite alla soluzione SymPy se la verifica e' positiva.
        - Non proporre una soluzione alternativa se coincide con quella gia' verificata.
        - Se SymPy fallisce o la verifica non e' positiva, spiega il limite e proponi una riscrittura.

        Equazione utente:
        {raw_equation}

        Equazione normalizzata per SymPy:
        {normalized}

        Parametri:
        {params or "nessuno"}

        Condizioni iniziali:
        {ics or "nessuna"}

        Hint/classificazione SymPy:
        {sympy_result["hints"]}

        Soluzione SymPy:
        {sympy_result["solution"]}

        Verifica SymPy:
        {sympy_result["verification"]}

        Errore SymPy:
        {sympy_result["error"]}

        Rispondi con:
        1. interpretazione dell'equazione;
        2. soluzione verificata o motivo del fallimento;
        3. come verificare il risultato;
        4. eventuale input alternativo consigliato.
        """
    ).strip()


def redis_reachable(host: str, port: int) -> bool:
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except OSError:
        return False


def run_docker_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    creationflags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.run(
        ["docker", *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=120,
        cwd=str(ROOT_DIR),
        creationflags=creationflags,
    )


def ensure_redis_container(host: str, port: int, wait_seconds: float = 25.0) -> str:
    if redis_reachable(host, port):
        return f"Redis gia' raggiungibile su {host}:{port}."
    if host not in {"127.0.0.1", "localhost", "::1"}:
        raise RuntimeError(f"Redis non raggiungibile su host non locale {host}:{port}; autostart Docker saltato.")
    if shutil.which("docker") is None:
        raise RuntimeError("Redis non raggiungibile e Docker non trovato nel PATH.")

    inspect = run_docker_command(["container", "inspect", "-f", "{{.State.Running}}", REDIS_CONTAINER_NAME])
    if inspect.returncode == 0:
        if inspect.stdout.strip().lower() != "true":
            started = run_docker_command(["start", REDIS_CONTAINER_NAME])
            if started.returncode != 0:
                detail = started.stderr.strip() or started.stdout.strip()
                raise RuntimeError(f"docker start {REDIS_CONTAINER_NAME} non riuscito: {detail}")
            action = f"Container Redis avviato: {REDIS_CONTAINER_NAME}."
        else:
            action = f"Container Redis gia' in esecuzione: {REDIS_CONTAINER_NAME}."
    else:
        created = run_docker_command(
            [
                "run",
                "-d",
                "--name",
                REDIS_CONTAINER_NAME,
                "-p",
                f"{port}:6379",
                "-v",
                f"{REDIS_VOLUME}:/data",
                REDIS_IMAGE,
            ]
        )
        if created.returncode != 0:
            detail = created.stderr.strip() or created.stdout.strip()
            raise RuntimeError(f"docker run {REDIS_CONTAINER_NAME} non riuscito: {detail}")
        action = f"Container Redis creato e avviato: {REDIS_CONTAINER_NAME}."

    deadline = time.time() + wait_seconds
    while time.time() < deadline:
        if redis_reachable(host, port):
            return f"{action} Redis raggiungibile su {host}:{port}."
        time.sleep(0.5)
    raise RuntimeError(f"{action} Redis non raggiungibile su {host}:{port} dopo {wait_seconds:.0f}s.")


def log_to_symposium(
    raw_equation: str,
    normalized: str,
    params: dict[str, Any],
    result: dict[str, Any],
    *,
    auto_start_redis: bool,
) -> str:
    try:
        import symposium

        if auto_start_redis:
            redis_status = ensure_redis_container(symposium.REDIS_HOST, symposium.REDIS_PORT)
        else:
            redis_status = "Avvio automatico Redis disattivato."
        r = symposium.store()
        r.execute("PING")
        thread_id = symposium.create_thread(
            r,
            topic="Risoluzione equazione differenziale con Ollama phi4-mini",
            by="custom",
            max_turns=8,
        )
        body = textwrap.dedent(
            f"""
            Input utente:
            {raw_equation}

            Equazione normalizzata:
            {normalized}

            Parametri:
            {params or "nessuno"}

            Soluzione:
            {result["solution"]}

            Verifica:
            {result["verification"]}

            Errore:
            {result["error"]}
            """
        ).strip()
        msg_id = symposium.post_message(
            r,
            thread_id=thread_id,
            from_agent="custom",
            to_agent="all",
            hat="bianco",
            claim="fatto" if result["solution"] is not None else "inferenza",
            body=body,
        )
        return f"{redis_status}\nthread #{thread_id}, messaggio #{msg_id}"
    except SystemExit as exc:
        return f"symposium non disponibile o Redis spento (exit {exc.code})"
    except Exception as exc:
        return f"symposium non disponibile: {type(exc).__name__}: {exc}"


def print_result(result: dict[str, Any]) -> None:
    print("\n=== Risultato SymPy ===")
    if result["solution"] is not None:
        print(result["solution"])
    else:
        print("Nessuna soluzione simbolica trovata.")
    print("\n=== Verifica ===")
    print(result["verification"])
    if result["error"]:
        print("\n=== Errore ===")
        print(result["error"])
    print("\n=== Hint/classificazione ===")
    for hint in result["hints"][:12]:
        print(f"- {hint}")
    if len(result["hints"]) > 12:
        print(f"- ... altri {len(result['hints']) - 12} hint")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Risolvi equazioni differenziali con SymPy, spiega con Ollama phi4-mini e logga su symposium."
    )
    parser.add_argument("--equation", "-e", help="Equazione, es. \"y' = y\" oppure \"y'' + y = 0\".")
    parser.add_argument("--params", default=None, help="Parametri, es. \"a=2, b=1/3\".")
    parser.add_argument("--ics", default=None, help="Condizioni iniziali, es. \"y(0)=1, y'(0)=0\".")
    parser.add_argument("--model", default=os.environ.get("OLLAMA_MODEL", "phi4-mini"))
    parser.add_argument("--ollama-host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    parser.add_argument("--ollama-timeout", type=int, default=180)
    parser.add_argument("--plot", action="store_true", help="Disegna il grafico della soluzione y(x), se possibile.")
    parser.add_argument("--plot-x-min", type=float, default=0.0, help="Valore minimo di x per il grafico.")
    parser.add_argument("--plot-x-max", type=float, default=10.0, help="Valore massimo di x per il grafico.")
    parser.add_argument("--plot-points", type=int, default=100, help="Numero di punti del grafico.")
    parser.add_argument("--plot-output", default="", help="Percorso PNG in cui salvare il grafico.")
    parser.add_argument("--no-show", action="store_true", help="Non aprire la finestra del grafico.")
    parser.add_argument("--no-ollama", action="store_true", help="Non chiamare Ollama.")
    parser.add_argument("--no-symposium", action="store_true", help="Non scrivere sul bus symposium.")
    parser.add_argument("--no-redis-auto-start", action="store_true", help="Non avviare Docker/Redis per symposium.")
    parser.add_argument("--no-pause", action="store_true", help="Non attendere Invio prima di chiudere.")
    return parser.parse_args()


def pause_before_exit(enabled: bool) -> None:
    if not enabled:
        return
    try:
        input("\nPremi Invio per chiudere...")
    except EOFError:
        pass


def main() -> int:
    args = parse_args()
    pause_on_exit = sys.stdin.isatty() and not args.no_pause
    sp, transformations = require_sympy()
    x = sp.symbols("x")
    y = sp.Function("y")
    yx = y(x)

    interactive = args.equation is None
    raw_equation = args.equation or input("Equazione differenziale: ").strip()
    raw_params = args.params if args.params is not None else ""
    raw_ics = args.ics if args.ics is not None else ""
    if interactive:
        raw_params = input("Parametri opzionali, es. a=2, b=1/3 (Invio per saltare): ").strip()
        raw_ics = input("Condizioni iniziali opzionali (Invio per saltare): ").strip()
    plot_requested = args.plot
    plot_x_min = args.plot_x_min
    plot_x_max = args.plot_x_max
    plot_points = args.plot_points
    plot_output = args.plot_output
    plot_show = not args.no_show

    if interactive and not args.plot:
        answer = input("Vuoi generare il grafico della soluzione? [s/N]: ").strip().lower()
        plot_requested = answer in {"s", "si", "y", "yes"}
        if plot_requested:
            try:
                plot_x_min = parse_numeric_bound(input("x minimo [0]: "), 0.0, sp, transformations)
                plot_x_max = parse_numeric_bound(input("x massimo [10]: "), 10.0, sp, transformations)
                raw_points = input("Numero punti [100]: ").strip()
                plot_points = int(raw_points) if raw_points else 100
                plot_output = input("File PNG opzionale (Invio per non salvare): ").strip()
            except Exception as exc:
                print(f"Parametri grafico non interpretabili: {type(exc).__name__}: {exc}", file=sys.stderr)
                pause_before_exit(pause_on_exit)
                return 2

    try:
        params = parse_parameters(raw_params, sp, x, y, transformations)
        equation, normalized = parse_equation(raw_equation, sp, x, y, transformations, params)
        ics = parse_initial_conditions(raw_ics, sp, x, y, yx, transformations, params)
    except Exception as exc:
        print(f"Input non interpretabile: {type(exc).__name__}: {exc}", file=sys.stderr)
        pause_before_exit(pause_on_exit)
        return 2

    print("\n=== Equazione normalizzata ===")
    print(equation)
    if params:
        print("\n=== Parametri ===")
        print(params)
    if ics:
        print("\n=== Condizioni iniziali ===")
        print(ics)

    result = solve_with_sympy(equation, sp, yx, ics)
    print_result(result)

    if plot_requested:
        plot_solution(
            result["solution"],
            sp,
            x,
            yx,
            x_min=plot_x_min,
            x_max=plot_x_max,
            points=plot_points,
            output=plot_output,
            show=plot_show,
        )

    if not args.no_symposium:
        print("\n=== Symposium ===")
        print(
            log_to_symposium(
                raw_equation,
                normalized,
                params,
                result,
                auto_start_redis=not args.no_redis_auto_start,
            )
        )

    if not args.no_ollama:
        print("\n=== Spiegazione Ollama / phi4-mini ===")
        print("Generazione in corso, puo' richiedere tempo su CPU...")
        sys.stdout.flush()
        prompt = build_phi4_prompt(raw_equation, normalized, params, ics, result)
        try:
            response = ollama_generate(args.ollama_host, args.model, prompt, args.ollama_timeout)
            print_llm_response(response, result)
        except RuntimeError as exc:
            print(exc)
            print(f"Se il modello manca, prova: ollama pull {args.model}")

    pause_before_exit(pause_on_exit)
    return 0 if result["solution"] is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
