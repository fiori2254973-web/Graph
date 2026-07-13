# SPEC-004 - Normalizzazione dati

## Contesto

La normalizzazione converte celle Excel in valori utilizzabili per preview, inferenza ruoli e grafici, preservando warning e assunzioni.

## Fatti noti

- I dati possono includere numeri, testo, date, valute e valori misti.
- Separatore decimale e formato data possono dipendere dalla localizzazione.
- Valori numerici possono essere salvati come testo.

## Assunzioni

- La prima versione puo' distinguere almeno testo, numero, data e vuoto.
- Le conversioni incerte devono generare warning.
- Il valore originale deve restare disponibile per debug e preview.

## Domande aperte

- Quali locali supportare esplicitamente nella prima versione?
- Come distinguere data seriale Excel e numero ordinario?
- Come gestire percentuali e valute?

## Comportamento atteso

- Produrre righe normalizzate.
- Mantenere valore originale e valore normalizzato.
- Identificare tipo dominante per colonna.
- Segnalare valori incompatibili con il tipo dominante.

## Criteri di accettazione

- Numeri Excel restano numeri.
- Numeri testuali chiaramente riconoscibili possono essere convertiti con assunzione registrata.
- Date riconosciute vengono marcate come date.
- Colonne miste generano warning.
- La preview mostra dati coerenti con la normalizzazione.

