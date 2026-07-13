# ADR-002 - Elaborazione client-side iniziale

## Stato

Proposta

## Data

2026-07-13

## Contesto

Il README indica come ambiente iniziale browser moderno, HTML5 ed elaborazione client-side. I file Excel sono caricati localmente dall'utente.

## Decisione candidata

La prima architettura di Graph elabora i file Excel nel browser senza inviarli a un server.

## Motivazione

- Riduce rischi privacy sui file Excel.
- Permette prototipo HTML5 rapido.
- Mantiene l'esperienza locale e immediata.

## Rischi

- File grandi possono bloccare il browser.
- Supporto `.xls` potrebbe dipendere dalla libreria scelta.
- Parsing e charting aumentano peso della pagina.

## Alternative

- Backend per parsing: piu' controllo e performance, ma piu' rischio privacy e infrastruttura.
- Worker client-side: possibile mitigazione per file grandi, da valutare dopo misure.

## Criteri di conferma

- Esiste una libreria compatibile con i formati richiesti.
- Sono dichiarati budget di dimensione e tempo.
- La UI resta responsiva su casi di riferimento.

