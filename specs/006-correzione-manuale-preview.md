# SPEC-006 - Correzione manuale e preview

## Contesto

La UI deve mostrare all'utente che cosa Graph ha interpretato e permettere una correzione minima prima del rendering.

## Fatti noti

- L'utente deve percepire controllo.
- La preview e' il punto in cui ambiguita' e assunzioni diventano visibili.
- La correzione minima riguarda assi, serie, etichette o tipo di grafico.

## Assunzioni

- La prima UI puo' offrire controlli semplici e non tutte le opzioni avanzate.
- I warning possono essere mostrati in forma compatta ma ispezionabile.

## Domande aperte

- Quale layout usare per preview dati e configurazione grafico?
- Quali controlli manuali sono Must per la prima versione?
- Serve undo/redo nella prima release?

## Comportamento atteso

- Mostrare preview tabellare normalizzata.
- Mostrare configurazione proposta.
- Mostrare warning e assunzioni.
- Consentire modifica dei campi principali.
- Renderizzare solo configurazioni valide.

## Criteri di accettazione

- L'utente vede almeno prime righe/colonne della tabella interpretata.
- L'utente vede quale colonna e' usata come asse categorie.
- L'utente vede quali colonne sono usate come serie.
- L'utente puo' correggere tipo di grafico e mapping base.
- Errori bloccanti impediscono rendering e spiegano perche'.

