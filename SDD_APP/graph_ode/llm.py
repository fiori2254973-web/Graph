from __future__ import annotations

import json
import textwrap
import urllib.error
import urllib.request

from .config import AppConfig
from .models import OdeInterpretation, SolveResult


CONTRADICTION_MARKERS = [
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


def _verification_positive(result: SolveResult) -> bool:
    return result.verification is not None and result.verification.startswith("(True")


def _normalise_text(text: str) -> str:
    return text.lower().replace("è", "e'").replace("é", "e'").replace("’", "'")


def repair_common_mojibake(text: str) -> str:
    replacements = {
        "Ã ": "à",
        "Ã¨": "è",
        "Ã©": "é",
        "Ã¬": "ì",
        "Ã²": "ò",
        "Ã¹": "ù",
        "Ã€": "À",
        "Ãˆ": "È",
        "Ã‰": "É",
        "ÃŒ": "Ì",
        "Ã’": "Ò",
        "Ã™": "Ù",
        "Â°": "°",
        "Â": "",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    if "Ã" not in text and "Â" not in text:
        return text
    try:
        repaired = text.encode("latin-1", errors="ignore").decode("utf-8", errors="replace")
    except UnicodeError:
        return text
    return repaired if repaired.count("Ã") <= text.count("Ã") else text


def llm_contradicts_verified_solution(text: str) -> bool:
    lowered = _normalise_text(text)
    return any(marker in lowered for marker in CONTRADICTION_MARKERS)


def fallback_verified_explanation(result: SolveResult) -> str:
    return textwrap.dedent(
        f"""
        Spiegazione deterministica:
        1. SymPy ha prodotto una soluzione e la verifica automatica risulta positiva.
        2. Soluzione verificata: {result.solution}
        3. Verifica SymPy: {result.verification}
        4. Il testo LLM e' stato omesso per evitare una contraddizione con la verifica simbolica.
        """
    ).strip()


def build_prompt(interpretation: OdeInterpretation, result: SolveResult) -> str:
    return textwrap.dedent(
        f"""
        Sei un tutor di matematica. Il modello disponibile e' phi4-mini.
        Il programma usa SymPy come fonte della soluzione e tu devi solo spiegare.

        Regole obbligatorie:
        - Se `Verifica SymPy` inizia con `(True`, dichiara che la soluzione SymPy e' corretta.
        - Non dire che SymPy ha sbagliato quando la verifica e' positiva.
        - Non dire che la soluzione non soddisfa le condizioni iniziali quando la verifica e' positiva.
        - Non usare parole come `errore`, `errata`, `non corretta` riferite alla soluzione SymPy se la verifica e' positiva.
        - Se SymPy fallisce o la verifica non e' positiva, spiega il limite e proponi una riscrittura dell'input.

        Equazione normalizzata:
        {interpretation.normalized_equation}

        Parametri:
        {interpretation.parameters or "nessuno"}

        Condizioni iniziali:
        {interpretation.initial_conditions or "nessuna"}

        Celle sorgente:
        {interpretation.source_cells}

        Hint/classificazione SymPy:
        {result.hints}

        Soluzione SymPy:
        {result.solution}

        Verifica SymPy:
        {result.verification}

        Errore o stop:
        {result.error or result.stop_reason or "nessuno"}

        Rispondi in italiano con:
        1. interpretazione dell'equazione;
        2. soluzione verificata o motivo del fallimento;
        3. come verificare il risultato;
        4. eventuale input Excel alternativo consigliato.
        """
    ).strip()


def ollama_generate(prompt: str, config: AppConfig) -> str:
    url = config.ollama_host.rstrip("/") + "/api/generate"
    payload = {
        "model": config.model_name,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=config.ollama_timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama ha risposto HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Ollama non raggiungibile su {config.ollama_host}: {exc.reason}") from exc
    text = str(body.get("response", "")).strip()
    if not text:
        raise RuntimeError(
            "Ollama ha risposto senza testo. Verifica il modello con: "
            f"ollama run {config.model_name}"
        )
    return text


def explain_with_phi4_mini(interpretation: OdeInterpretation, result: SolveResult, config: AppConfig) -> str:
    response = repair_common_mojibake(ollama_generate(build_prompt(interpretation, result), config))
    if "�" in response:
        result.warnings.append("La risposta LLM contiene caratteri non riparabili di codifica.")
    if _verification_positive(result) and llm_contradicts_verified_solution(response):
        result.warnings.append("Risposta LLM soppressa per contraddizione con verifica SymPy positiva.")
        return fallback_verified_explanation(result)
    return response
