# SPEC-002 - Import Excel

## Contesto

La funzione di import legge file Excel locali e produce una rappresentazione interna del workbook, senza ancora decidere in modo definitivo quale grafico mostrare.

## Fatti noti

- Formati richiesti dal README: `.xlsx` e `.xls`.
- L'elaborazione iniziale e' client-side.
- L'import deve restituire errori leggibili, non eccezioni silenziose.

## Assunzioni

- La libreria Excel sara' scelta con ADR dedicata.
- Il parsing puo' scartare formule complesse nel prototipo, pur mostrando warning.
- La prima versione puo' limitarsi ai valori visibili o calcolati disponibili dalla libreria scelta.

## Domande aperte

- Supporto `.xls`: nativo nella libreria scelta o conversione non supportata nella prima release?
- Quali limiti iniziali applicare a dimensione file e celle?
- Come trattare formule, celle unite e formattazioni?

## Comportamento atteso

- Validare estensione e tipo file quando possibile.
- Caricare workbook in memoria entro budget dichiarato.
- Estrarre elenco fogli.
- Estrarre celle con valore, tipo e posizione.
- Restituire `errors`, `warnings` e `assumptions`.

## Criteri di accettazione

- File non supportato produce errore bloccante.
- Workbook vuoto produce errore bloccante.
- Workbook con almeno un foglio non vuoto produce elenco fogli.
- Celle vuote non causano crash.
- File oltre budget produce messaggio non bloccante per il browser.

## Segnali di stop

- La libreria scelta non supporta in modo accettabile `.xls`.
- Il parsing richiede invio file a un server o servizio esterno.
- I limiti di performance non sono misurabili.

