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

