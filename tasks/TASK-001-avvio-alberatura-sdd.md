# TASK-001 - Avvio alberatura SDD

## Stato

Completato

## Specifiche collegate

- `specs/000-costituzione-del-progetto.md`
- `specs/001-prototipo-end-to-end.md`

## Obiettivo

Creare l'alberatura SDD iniziale del progetto Graph e il registro anti-recidiva `AI-LEDGER.md`.

## Ambito

Incluso:

- cartelle SDD;
- specifiche iniziali;
- ADR iniziali;
- registri documentali;
- prompt riusabili;
- checklist e casi di riferimento.

Escluso:

- implementazione HTML/CSS/JavaScript;
- scelta librerie Excel e charting;
- test automatici reali.

## Criteri di accettazione

- `AI-LEDGER.md` esiste e contiene regole anti-recidiva iniziali.
- `specs/`, `adr/`, `tasks/`, `prompts/`, `evals/`, `docs/`, `src/`, `tests/` esistono.
- Le cartelle principali contengono file seme tracciabili.
- La struttura riflette il README.

## Verifica

- Controllo finale con `Get-ChildItem -Recurse`.

