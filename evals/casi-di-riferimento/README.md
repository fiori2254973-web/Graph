# Casi di riferimento

Questa cartella descrive i casi Excel da usare per verificare Graph.

## Casi minimi

### CASE-001 - Tabella semplice

- Input: una riga intestazione, una colonna categoria, una colonna numerica.
- Atteso: preview corretta, proposta grafico spiegabile, rendering possibile.

### CASE-002 - File vuoto

- Input: workbook senza dati utili.
- Atteso: errore bloccante leggibile, nessun rendering.

### CASE-003 - Righe introduttive

- Input: testo descrittivo sopra la tabella.
- Atteso: tabella riconosciuta se il blocco dati e' chiaro, warning se incerto.

### CASE-004 - Piu' tabelle nello stesso foglio

- Input: due blocchi tabellari separati.
- Atteso: ambiguita' visibile o scelta guidata, nessun rendering silenzioso se incompatibili.

### CASE-005 - Valori misti

- Input: colonna numerica con testo o celle anomale.
- Atteso: warning di normalizzazione e preview del valore originale.

### CASE-006 - Date e valute localizzate

- Input: date, decimali e valute con formati locali.
- Atteso: conversione solo se spiegabile; warning in caso di incertezza.

### CASE-007 - File grande

- Input: workbook oltre budget iniziale.
- Atteso: stop controllato o messaggio non bloccante, browser responsivo.

