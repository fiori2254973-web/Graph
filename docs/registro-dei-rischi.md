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

