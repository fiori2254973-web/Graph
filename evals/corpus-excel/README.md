# Corpus Excel

Conservare qui file Excel campione non sensibili.

Regole:

- non inserire dati personali o aziendali reali non anonimizzati;
- ogni file deve avere una descrizione in `evals/casi-di-riferimento/`;
- ogni file ambiguo deve dichiarare quale ambiguita' e' attesa;
- file grandi devono essere esplicitamente marcati come test performance.

## File registrati

### `data/PP5-CONTATORE.xlsx`

- Mappatura: `evals/corpus-excel/PP5-CONTATORE.mapping.md`
- Tipo: workbook Excel reale con piu' fogli di misura e sintesi.
- Dominio inferito: fisica sperimentale con analisi statistica di conteggi nel tempo.
- Uso consigliato: testare rilevamento multi-tabella, normalizzazione numerica, inferenza tempo/conteggi e gestione di metriche derivate.
- Ambiguita': contiene fogli con piu' blocchi, layout variante e formule cross-sheet.
