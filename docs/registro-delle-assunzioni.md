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

