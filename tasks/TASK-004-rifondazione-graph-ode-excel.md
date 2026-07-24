# TASK-004 - Rifondazione Graph per Excel elastici e ODE

- Data: 2026-07-24
- Stato: aperto
- Specifica collegata: `specs/007-excel-equazioni-differenziali-python.md`
- ADR collegata: `adr/ADR-003-python-sympy-ollama-phi4-mini.md`
- Ledger collegato: `AI-LEDGER.md`
- Owner: progetto Graph

## Obiettivo

Riallineare il progetto Graph al nuovo scopo: software Python che legge Excel elastici, individua dati per equazioni differenziali, risolve con SymPy, verifica, grafica e spiega con `phi4-mini`.

## Compiti

1. Aggiornare la costituzione del progetto.
2. Aggiornare il README.
3. Scrivere la specifica operativa dei perimetri e delle configurazioni.
4. Eseguire second pass con schema dati, invarianti, confidenza, lifecycle e output contract.
5. Eseguire third pass con black hat spietato, FMEA, criteri di rifiuto e test matrix.
6. Registrare ADR architetturale.
7. Aggiornare registri decisioni, assunzioni e rischi.
8. Collegare o aggiornare `AI-LEDGER.md`.
9. Preparare un corpus Excel iniziale con almeno dodici casi.
10. Progettare modello dati per `CellRef`, `Evidence`, `CandidateBlock`, `OdeInterpretation`, `SolveResult`.
11. Implementare parser Excel iniziale.
12. Implementare mapping candidati con confidenza.
13. Integrare il solver esistente con input da mapping Excel.
14. Generare report tracciabile.

## Criteri di accettazione

- AC-001: la SDD aggiornata dichiara che il vecchio obiettivo HTML5 e' storico.
- AC-002: i perimetri accettati sono documentati in tabella.
- AC-003: ogni configurazione prevista ha default, tipo, descrizione e stop condition o criterio di verifica.
- AC-004: esiste almeno un diagramma Mermaid per pipeline e uno per modello dati.
- AC-005: il ruolo di `phi4-mini` e' limitato a spiegazione/supporto e subordinato a SymPy.
- AC-006: i rischi principali sono registrati in `docs/registro-dei-rischi.md`.
- AC-007: le assunzioni principali sono registrate in `docs/registro-delle-assunzioni.md`.
- AC-008: il ledger e' consultato e aggiornato se emerge una recidiva.
- AC-009: SPEC-007 contiene second pass e third pass espliciti.
- AC-010: SPEC-007 contiene FMEA, matrice conflitti, regole HITL e criteri di rifiuto immediato.
- AC-011: il corpus iniziale previsto copre almeno dodici casi `CASE-ODE-*`.
- AC-012: nessun task di parsing puo' partire se non produce `workbook_scan.json`, `candidate_blocks.json`, `interpretations.json`, `solve_result.json` e `report.md`.

## Black hat

- Un task di implementazione non puo' partire se non produce celle sorgente.
- Un parser elastico senza confidenza e' un generatore di falsi positivi.
- Un report senza interpretazioni scartate nasconde l'ambiguita'.
- Una spiegazione LLM non verificata puo' convincere l'utente piu' del solver.

## Verifiche previste

```text
python -m py_compile scripts/ode_phi4_solver.py scripts/ode_phi4_mini_solver.py
```

Verifiche documentali:

- lettura manuale di `specs/000-costituzione-del-progetto.md`;
- lettura manuale di `specs/007-excel-equazioni-differenziali-python.md`;
- controllo `git diff --check`.

## Dipendenze future

- scelta libreria Excel;
- definizione corpus;
- scelta formato report;
- definizione UX di conferma utente.
