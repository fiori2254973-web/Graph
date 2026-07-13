# Golden files

I golden file descrivono l'output atteso per un input noto.

Nel progetto Graph servono a verificare che parsing, normalizzazione, inferenza ruoli e proposta grafico restino stabili quando il codice cambia.

## Regole

- Ogni golden file deve collegarsi a un caso di riferimento.
- Il contenuto deve essere deterministico e verificabile.
- Le inferenze devono includere motivazione, confidenza, warning e assunzioni.
- Se il comportamento atteso cambia, aggiornare prima la specifica o la decisione collegata.
- Un golden file non deve nascondere ambiguita': se il caso e' ambiguo, l'output atteso deve contenere warning o richiesta di intervento utente.

## Convenzione nome

`CASE-<numero>-<nome>.<step>.golden.json`

Esempi:

- `CASE-001-tabella-semplice.chart-proposal.golden.json`
- `CASE-004-piu-tabelle.table-detection.golden.json`

