from __future__ import annotations

import re
from typing import Any

from .models import OdeInterpretation, SolveResult


def require_sympy() -> tuple[Any, Any]:
    try:
        import sympy as sp
        from sympy.parsing.sympy_parser import (
            implicit_multiplication_application,
            standard_transformations,
        )
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Dipendenza mancante: sympy. Installa con `python -m pip install -r SDD_APP\\requirements.txt`."
        ) from exc
    return sp, standard_transformations + (implicit_multiplication_application,)


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
    if text.startswith("="):
        text = text[1:].strip()

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


def parse_parameters(values: dict[str, str], sp: Any, x: Any, y: Any, transformations: Any) -> dict[str, Any]:
    params: dict[str, Any] = {}
    reserved = set(build_local_dict(sp, x, y))
    for name, raw_value in values.items():
        if not re.match(r"^[A-Za-z_]\w*$", name):
            raise ValueError(f"Nome parametro non valido: {name!r}.")
        if name in reserved:
            raise ValueError(f"Nome parametro riservato: {name!r}.")
        local_dict = build_local_dict(sp, x, y, params)
        params[name] = parse_expression(str(raw_value).replace("^", "**"), sp, transformations, local_dict)
    return params


def parse_equation(raw: str, sp: Any, x: Any, y: Any, transformations: Any, params: dict[str, Any]) -> tuple[Any, str]:
    local_dict = build_local_dict(sp, x, y, params)
    normalized = normalize_ode_text(raw)
    if normalized.startswith("Eq("):
        return parse_expression(normalized, sp, transformations, local_dict), normalized
    if "=" in normalized:
        left, right = normalized.split("=", 1)
        return (
            sp.Eq(
                parse_expression(left, sp, transformations, local_dict),
                parse_expression(right, sp, transformations, local_dict),
            ),
            normalized,
        )
    return sp.Eq(parse_expression(normalized, sp, transformations, local_dict), 0), normalized


def parse_initial_conditions(items: list[str], sp: Any, x: Any, y: Any, yx: Any, transformations: Any, params: dict[str, Any]) -> dict[Any, Any]:
    from sympy.parsing.sympy_parser import parse_expr

    ics: dict[Any, Any] = {}
    for item in items:
        match = re.match(
            r"^y(?P<primes>'*)\s*\(\s*(?P<x0>[^)]*)\s*\)\s*=\s*(?P<value>.+)$",
            item.replace("^", "**"),
        )
        if not match:
            raise ValueError(f"Condizione iniziale non riconosciuta: {item!r}.")
        local_dict = build_local_dict(sp, x, y, params)
        x0 = parse_expr(match.group("x0"), local_dict=local_dict, transformations=transformations)
        value = parse_expr(match.group("value"), local_dict=local_dict, transformations=transformations)
        order = len(match.group("primes"))
        lhs = yx.subs(x, x0) if order == 0 else sp.Derivative(yx, (x, order)).subs(x, x0)
        ics[lhs] = value
    return ics


def _verification_ok(verification: Any) -> bool:
    return isinstance(verification, tuple) and len(verification) >= 1 and verification[0] is True


def solve_interpretation(interpretation: OdeInterpretation) -> tuple[SolveResult, dict[str, Any]]:
    if interpretation.status not in {"selected", "candidate"}:
        return (
            SolveResult(
                status="blocked",
                stop_reason=interpretation.rejection_reason or "Interpretazione non selezionabile.",
            ),
            {},
        )
    if not interpretation.normalized_equation:
        return SolveResult(status="blocked", stop_reason="Equazione normalizzata assente."), {}

    sp, transformations = require_sympy()
    x = sp.symbols("x")
    y = sp.Function("y")
    yx = y(x)
    warnings: list[str] = []
    context: dict[str, Any] = {"sp": sp, "x": x, "y": y, "yx": yx}

    try:
        params = parse_parameters(interpretation.parameters, sp, x, y, transformations)
        equation, normalized = parse_equation(interpretation.normalized_equation, sp, x, y, transformations, params)
        ics = parse_initial_conditions(interpretation.initial_conditions, sp, x, y, yx, transformations, params)
    except Exception as exc:
        return (
            SolveResult(status="blocked", error=f"{type(exc).__name__}: {exc}", stop_reason="Parsing simbolico fallito."),
            context,
        )

    missing = sorted(str(symbol) for symbol in equation.free_symbols - {x})
    if missing:
        return (
            SolveResult(
                status="blocked",
                normalized_equation=normalized,
                stop_reason="Parametro richiesto mancante: " + ", ".join(missing),
            ),
            context,
        )

    hints: list[str] = []
    try:
        hints = [str(item) for item in sp.classify_ode(equation, yx)]
    except Exception as exc:
        warnings.append(f"classify_ode non riuscito: {type(exc).__name__}: {exc}")

    try:
        kwargs = {"ics": ics} if ics else {}
        solution = sp.dsolve(equation, yx, **kwargs)
    except Exception as exc:
        return (
            SolveResult(
                status="failed",
                normalized_equation=normalized,
                hints=hints,
                error=f"{type(exc).__name__}: {exc}",
                stop_reason="SymPy non ha trovato una soluzione simbolica.",
                warnings=warnings,
            ),
            context,
        )

    try:
        verification = sp.checkodesol(equation, solution, func=yx)
    except Exception as exc:
        verification = f"Verifica automatica non riuscita: {type(exc).__name__}: {exc}"
        warnings.append(str(verification))

    status = "solved" if _verification_ok(verification) else "failed"
    stop_reason = None if status == "solved" else "Verifica SymPy non positiva."
    context.update({"equation": equation, "solution": solution, "verification": verification, "hints": hints, "params": params, "ics": ics})
    return (
        SolveResult(
            status=status,
            normalized_equation=normalized,
            solution=str(solution),
            verification=str(verification),
            hints=hints,
            warnings=warnings,
            stop_reason=stop_reason,
        ),
        context,
    )


def extract_solution_expression(solution: Any, yx: Any) -> Any | None:
    if solution is None:
        return None
    candidates = solution if isinstance(solution, (list, tuple)) else [solution]
    for item in candidates:
        if getattr(item, "lhs", None) == yx:
            return item.rhs
    return None
