# SPEC-001 - Prototipo end-to-end

## Contesto

Il primo obiettivo di Graph e' un prototipo end-to-end che carica un file Excel, mostra una preview dei dati interpretati, propone una configurazione grafica, consente una correzione manuale minima e renderizza il grafico.

## Fatti noti

- L'input e' un file Excel scelto dall'utente.
- Il rendering avviene in una pagina web.
- La proposta automatica deve essere spiegabile.
- L'utente deve poter correggere almeno assi, serie, etichette o tipo di grafico.

## Assunzioni

- Il prototipo puo' supportare inizialmente un solo foglio selezionato.
- Il prototipo puo' partire da una tabella principale per foglio.
- La correzione manuale minima puo' essere limitata a campi fondamentali.
- I casi complessi possono mostrare warning invece di completare tutto automaticamente.

## Domande aperte

- Se il workbook contiene piu' fogli, si seleziona automaticamente il primo foglio con dati o si chiede scelta?
- Quali tipi di grafico sono inclusi nel primo prototipo?
- Quale soglia definisce una tabella "abbastanza plausibile"?
- Come mostrare all'utente la motivazione della proposta senza appesantire la UI?

## Input

- File `.xlsx` o `.xls` locale.
- Azioni utente di correzione manuale.

## Comportamento atteso

1. L'utente seleziona un file Excel.
2. Il sistema prova a caricare il workbook.
3. Il sistema individua fogli e una struttura tabellare plausibile.
4. Il sistema mostra una preview normalizzata.
5. Il sistema propone una configurazione grafica iniziale.
6. Il sistema mostra warning o ambiguita' rilevate.
7. L'utente puo' correggere la configurazione minima.
8. Il sistema renderizza il grafico.

## Casi limite

- File non Excel.
- File Excel vuoto.
- Foglio con righe introduttive.
- Piu' tabelle nello stesso foglio.
- Colonne con valori misti.
- Date o numeri localizzati.
- File troppo grande per il budget iniziale.

## Criteri di accettazione

- Dato un file Excel semplice con intestazioni e numeri, Graph mostra preview e grafico.
- Dato un file non Excel, Graph mostra errore bloccante leggibile e non prova a renderizzare.
- Dato un foglio ambiguo, Graph mostra almeno un warning e non nasconde l'ambiguita'.
- Ogni proposta di grafico espone almeno: asse categorie, serie numeriche, tipo grafico e motivazione sintetica.
- L'utente puo' modificare la configurazione minima prima del rendering finale.
- Il rendering non parte se mancano dati essenziali.

## Verifica

- Verifica manuale con scenari in `evals/casi-di-riferimento/README.md`.
- Test automatici da definire dopo scelta stack.

