# ADR-001 - Alberatura SDD del progetto

## Stato

Accettata

## Data

2026-07-13

## Contesto

Graph sara' sviluppato con Spec Driven Development. Il README richiede specifiche verificabili per caricamento Excel, interpretazione dati, decisioni automatiche, correzione utente e casi non gestibili.

## Decisione

Il repository adotta una struttura SDD esplicita:

- `specs/` per specifiche verificabili;
- `adr/` per decisioni tecniche;
- `tasks/` per lavoro delimitato;
- `prompts/` per istruzioni riusabili agli agenti;
- `evals/` per checklist, casi di riferimento e corpus Excel;
- `docs/` per registri di decisioni, assunzioni e rischi;
- `AI-LEDGER.md` per anti-recidiva;
- `src/` e `tests/` come sede futura di implementazione e verifiche.

## Alternative considerate

- Tenere tutto nel README: scartato perche' non scala e confonde descrizione, specifica e decisioni.
- Creare solo cartelle vuote: scartato perche' Git non traccia cartelle vuote e gli agenti avrebbero meno guida.
- Introdurre subito strumenti avanzati: scartato perche' AGENTS.md richiede file semplici prima di orchestrazione complessa.

## Conseguenze

- Ogni lavoro rilevante deve puntare a una specifica.
- Le decisioni importanti devono avere ADR o voce nel diario.
- I rischi ricorrenti devono passare da `AI-LEDGER.md`.

## Verifica

- Alberatura presente nel repository.
- File seme creati con contenuti Graph-specifici.

