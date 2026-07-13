# SPEC-003 - Rilevamento tabella

## Contesto

Graph deve individuare una struttura tabellare plausibile in fogli Excel generici. Questa e' una fase ad alto rischio perche' un errore puo' produrre grafici convincenti ma sbagliati.

## Fatti noti

- I fogli possono contenere righe introduttive, celle vuote e intestazioni spezzate.
- Possono esistere piu' tabelle nello stesso foglio.
- Nessun formato Excel e' obbligatorio.

## Assunzioni

- La prima versione puo' proporre una tabella principale e segnalare candidate alternative.
- Ogni euristica deve essere documentata.
- Una bassa confidenza deve richiedere conferma o correzione.

## Domande aperte

- Quale metrica di confidenza usare?
- Quando considerare due blocchi come tabelle separate?
- Come trattare celle unite e intestazioni multi-riga?

## Comportamento atteso

- Identificare blocchi rettangolari o quasi rettangolari.
- Stimare riga di intestazione.
- Separare categorie e valori candidati solo come proposta, non come verita'.
- Restituire motivazione, warning e candidate alternative.

## Criteri di accettazione

- Tabella semplice con intestazioni in prima riga viene riconosciuta.
- Righe introduttive prima della tabella non impediscono il riconoscimento se il blocco e' chiaro.
- Se piu' tabelle sono plausibili, il sistema segnala ambiguita'.
- Se mancano intestazioni riconoscibili, il sistema chiede intervento o usa nomi generati con warning.
- Ogni tabella candidata contiene coordinate origine/fine e motivazione.

## Segnali di stop

- Euristica nuova non documentata.
- Scelta tra candidate incompatibili senza warning.
- Confidenza non esposta alla UI o al log decisionale.

