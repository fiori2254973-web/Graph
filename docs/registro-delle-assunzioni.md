# Registro delle assunzioni

## Scopo

Rendere visibili le ipotesi non ancora verificate.

## Template

```markdown
### ASM-000 - Titolo

- Data:
- Assunzione:
- Fiducia:
- Prova mancante:
- Metodo di verifica:
- Stato:
- Collegamenti:
```

## Assunzioni iniziali

### ASM-001 - Prototipo senza backend

- Data: 2026-07-13
- Assunzione: il prototipo iniziale puo' funzionare interamente nel browser.
- Fiducia: media
- Prova mancante: scelta librerie e misure su file campione.
- Metodo di verifica: completare `TASK-002` e testare corpus iniziale.
- Stato: aperta
- Collegamenti: `adr/ADR-002-elaborazione-client-side-iniziale.md`

### ASM-002 - Una tabella principale e' sufficiente per il primo prototipo

- Data: 2026-07-13
- Assunzione: il prototipo puo' proporre una tabella principale per foglio e segnalare alternative.
- Fiducia: media
- Prova mancante: corpus con piu' tabelle nello stesso foglio.
- Metodo di verifica: creare caso in `evals/corpus-excel/` e criterio in `evals/casi-di-riferimento/`.
- Stato: aperta
- Collegamenti: `specs/003-rilevamento-tabella.md`

### ASM-003 - La correzione manuale minima basta per il primo valore utente

- Data: 2026-07-13
- Assunzione: modificare tipo grafico, asse categorie e serie e' sufficiente per validare il prototipo.
- Fiducia: media
- Prova mancante: prova manuale con utente o scenario realistico.
- Metodo di verifica: test di usabilita' leggero su file semplice e ambiguo.
- Stato: aperta
- Collegamenti: `specs/006-correzione-manuale-preview.md`

### ASM-004 - Il primo Graph ODE puo' essere Python CLI-first

- Data: 2026-07-24
- Assunzione: un primo prototipo locale da console e' sufficiente per validare parsing Excel, mapping, soluzione, verifica, grafico e spiegazione.
- Fiducia: media
- Prova mancante: test con corpus Excel realistico e feedback utente.
- Metodo di verifica: implementare `TASK-004` e provare almeno sei casi `CASE-ODE-*`.
- Stato: aperta
- Collegamenti: `specs/007-excel-equazioni-differenziali-python.md`, `tasks/TASK-004-rifondazione-graph-ode-excel.md`

### ASM-005 - Excel elastici sono gestibili con blocchi candidati e confidenza

- Data: 2026-07-24
- Assunzione: celle libere possono essere ricondotte a blocchi logici come equazione, parametri, condizioni iniziali, range grafico e note senza imporre celle fisse.
- Fiducia: media-bassa
- Prova mancante: corpus con layout diversi, celle sparse, duplicati e ambiguita'.
- Metodo di verifica: costruire mapping JSON con celle sorgente e misurare quanti casi richiedono conferma utente.
- Stato: aperta
- Collegamenti: `specs/007-excel-equazioni-differenziali-python.md`

### ASM-006 - phi4-mini e' utile come spiegatore se vincolato

- Data: 2026-07-24
- Assunzione: `phi4-mini` puo' produrre spiegazioni utili se il prompt limita il ruolo del modello e l'output viene filtrato contro contraddizioni SymPy.
- Fiducia: media
- Prova mancante: batteria di esempi con risposte corrette, lente, vuote e contraddittorie.
- Metodo di verifica: testare le risposte LLM su casi `CASE-ODE-*` e aggiornare `AI-LEDGER.md` a ogni recidiva.
- Stato: aperta
- Collegamenti: `AI-LEDGER.md`, `scripts/ode_phi4_mini_solver.py`, `scripts/ode_phi4_solver.py`
