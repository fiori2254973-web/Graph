# Registro dei rischi

## Scopo

Registrare rischi, probabilita', impatto, mitigazioni e segnali di intervento umano.

## Template

```markdown
### RISK-000 - Titolo

- Data:
- Area:
- Descrizione:
- Severita':
- Probabilita':
- Rilevabilita':
- Mitigazione:
- Segnale HITL:
- Stato:
- Collegamenti:
```

## Rischi iniziali

### RISK-001 - Grafico semanticamente sbagliato ma plausibile

- Data: 2026-07-13
- Area: inferenza dati, proposta grafico
- Descrizione: Graph potrebbe proporre un grafico visivamente valido basato su interpretazione errata del foglio.
- Severita': alta
- Probabilita': media
- Rilevabilita': media
- Mitigazione: preview obbligatoria, motivazione della proposta, warning su confidenza bassa.
- Segnale HITL: interpretazioni multiple incompatibili.
- Stato: aperto
- Collegamenti: `AI-LEDGER.md`, `specs/005-proposta-grafico.md`

### RISK-002 - Browser bloccato da file grande

- Data: 2026-07-13
- Area: performance
- Descrizione: parsing client-side di file grandi puo' rendere la pagina non responsiva.
- Severita': alta
- Probabilita': media
- Rilevabilita': alta
- Mitigazione: budget iniziale, messaggio di stop, valutazione Web Worker dopo misure.
- Segnale HITL: impossibilita' di definire limiti misurabili.
- Stato: aperto
- Collegamenti: `AI-LEDGER.md`, `specs/002-import-excel.md`

### RISK-003 - Supporto `.xls` insufficiente

- Data: 2026-07-13
- Area: import Excel
- Descrizione: il supporto al formato legacy `.xls` potrebbe essere incompleto nel browser.
- Severita': media
- Probabilita': media
- Rilevabilita': alta
- Mitigazione: scelta libreria con MCDA/Kepner-Tregoe e messaggi chiari sui limiti.
- Segnale HITL: libreria candidata non supporta `.xls` in modo affidabile.
- Stato: aperto
- Collegamenti: `TASK-002-scelta-librerie-excel-charting.md`

### RISK-004 - Mapping Excel elastico matematicamente plausibile ma falso

- Data: 2026-07-24
- Area: parsing Excel, equazioni differenziali, inferenza
- Descrizione: Graph potrebbe associare una equazione, un parametro o una condizione iniziale a celle semanticamente non collegate e produrre una soluzione verificata per il problema sbagliato.
- Severita': alta
- Probabilita': alta
- Rilevabilita': media
- Mitigazione: celle sorgente obbligatorie, confidenza, alternative candidate, preview, stop su interpretazioni incompatibili.
- Segnale HITL: parametri duplicati, celle lontane, etichette ambigue, piu' interpretazioni sopra soglia media.
- Stato: aperto
- Collegamenti: `specs/007-excel-equazioni-differenziali-python.md`, `AI-LEDGER.md`

### RISK-005 - Spiegazione LLM contraddittoria rispetto a SymPy

- Data: 2026-07-24
- Area: Ollama, phi4-mini, spiegazione matematica
- Descrizione: `phi4-mini` puo' dichiarare errata una soluzione verificata o sostenere che una condizione iniziale non e' soddisfatta anche quando `checkodesol` e' positivo.
- Severita': alta
- Probabilita': media
- Rilevabilita': alta
- Mitigazione: ruolo LLM `explain_only`, prompt vincolante, soppressione di risposte contraddittorie, fallback deterministico.
- Segnale HITL: marker testuali come `non corretta`, `non soddisfa`, `errore nella soluzione` in presenza di verifica `(True, 0)`.
- Stato: contenuto
- Collegamenti: `AI-LEDGER.md`, `scripts/ode_phi4_solver.py`, `scripts/ode_phi4_mini_solver.py`

### RISK-006 - Elasticita' percepita come assenza di perimetro

- Data: 2026-07-24
- Area: prodotto, SDD, UX
- Descrizione: l'obiettivo di accettare Excel liberi puo' essere interpretato come obbligo di calcolare sempre, anche quando mancano prove sufficienti.
- Severita': alta
- Probabilita': media
- Rilevabilita': media
- Mitigazione: perimetri espliciti, configurazioni documentate, stop condition, black hat obbligatorio per ogni euristica.
- Segnale HITL: richiesta di calcolo automatico su foglio con piu' interpretazioni plausibili.
- Stato: aperto
- Collegamenti: `specs/000-costituzione-del-progetto.md`, `specs/007-excel-equazioni-differenziali-python.md`
