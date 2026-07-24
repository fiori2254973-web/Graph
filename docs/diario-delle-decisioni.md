# Diario delle decisioni

## Scopo

Registrare decisioni importanti, motivazione, alternative scartate e impatto atteso.

## Template

```markdown
### DEC-000 - Titolo

- Data:
- Decisione:
- Motivazione:
- Alternative scartate:
- Impatto atteso:
- Collegamenti:
- Owner:
```

## Decisioni iniziali

### DEC-001 - Graph adotta SDD come metodo di governo

- Data: 2026-07-13
- Decisione: ogni funzionalita' rilevante nasce da una specifica verificabile.
- Motivazione: il README richiede interpretazioni Excel spiegabili, gestione dell'ambiguita' e criteri di accettazione.
- Alternative scartate: sviluppo diretto da README senza specifiche separate.
- Impatto atteso: meno decisioni implicite e maggiore tracciabilita'.
- Collegamenti: `README.md`, `AGENTS.md`, `specs/000-costituzione-del-progetto.md`
- Owner: progetto Graph

### DEC-002 - Elaborazione iniziale nel browser

- Data: 2026-07-13
- Decisione: il primo disegno architetturale assume elaborazione client-side.
- Motivazione: il README indica browser moderno, HTML5 e file caricati localmente.
- Alternative scartate: backend obbligatorio nella prima fase.
- Impatto atteso: piu' privacy e prototipo piu' semplice, con rischio performance da mitigare.
- Collegamenti: `adr/ADR-002-elaborazione-client-side-iniziale.md`
- Owner: progetto Graph

### DEC-003 - Graph viene rifondato come software Python per Excel elastici e ODE

- Data: 2026-07-24
- Decisione: il progetto Graph assume come nuovo scopo la lettura di file Excel elastici contenenti dati per equazioni differenziali, con soluzione/verifica in Python tramite SymPy e spiegazione con Ollama `phi4-mini`.
- Motivazione: l'obiettivo dichiarato dall'utente richiede elasticita' nel mapping celle, solver simbolico, verifica matematica e guardrail LLM; il vecchio perimetro HTML5/charting generico non e' piu' sufficiente.
- Alternative scartate: mantenere il progetto come pagina HTML5; richiedere Excel a celle fisse; usare `phi4-mini` come solver primario; accettare parsing libero senza confidenza e stop condition.
- Impatto atteso: nuova SDD, nuova ADR, nuovi task, riallineamento delle specifiche precedenti e implementazione Python-first.
- Collegamenti: `specs/000-costituzione-del-progetto.md`, `specs/007-excel-equazioni-differenziali-python.md`, `adr/ADR-003-python-sympy-ollama-phi4-mini.md`, `tasks/TASK-004-rifondazione-graph-ode-excel.md`
- Owner: progetto Graph
