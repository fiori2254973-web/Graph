# Graph

## Descrizione del progetto

Graph e' un'applicazione web HTML5 per trasformare fogli Excel generici in grafici interattivi. L'utente carica un file `.xlsx` o `.xls`, il sistema individua una struttura tabellare plausibile, propone una configurazione visuale e permette di correggerla prima del rendering.

Il progetto sara' sviluppato con SDD, Spec Driven Development. Ogni funzionalita' rilevante dovra' nascere da una specifica verificabile: cosa accetta il sistema, come interpreta i dati, quali decisioni automatiche prende, quando chiede conferma all'utente e come segnala un caso non gestibile.

## Analisi del progetto

### Fatti

- Input: file Excel caricati localmente dall'utente.
- Output: grafici renderizzati in una pagina web.
- Ambiente iniziale: browser moderno, HTML5, elaborazione client-side.
- Dati attesi: intestazioni, categorie, numeri, date, serie singole o multiple.
- Primo vincolo: nessun formato Excel obbligatorio, ma ogni inferenza deve essere spiegabile.

### Rischi e criticita'

- Tabelle non rettangolari, righe introduttive, celle vuote e intestazioni spezzate.
- Piu' tabelle nello stesso foglio.
- Valori misti nella stessa colonna, inclusi numeri formattati come testo.
- Date, valute e separatori dipendenti dalla localizzazione.
- File grandi o complessi che possono bloccare il browser.
- Suggerimenti automatici apparentemente validi ma semanticamente errati.

Questi casi dovranno diventare scenari di specifica, non eccezioni scoperte a posteriori.

### Opportunita'

Graph riduce il passaggio manuale da dato tabellare a visualizzazione. Il valore principale e' dare a utenti non tecnici uno strumento rapido per esplorare file Excel senza preparazione preventiva, mantenendo comunque trasparenza sulle assunzioni fatte dal sistema.

La SDD aggiunge valore tecnico: rende il progetto incrementale, testabile e meno dipendente da decisioni implicite nel codice.

### Percezione ed emozioni

L'utente deve percepire controllo, non magia opaca. Il sistema puo' proporre una lettura del foglio, ma deve rendere facile capire cosa ha riconosciuto e modificare assi, serie, etichette o tipo di grafico.

La qualita' dell'esperienza dipendera' soprattutto dalla gestione dell'incertezza: un foglio ambiguo non dovra' produrre un risultato silenziosamente sbagliato, ma una scelta guidata.

### Alternative e lenti multiprospettiche

Possibili capacita' evolutive:

- riconoscimento di una tabella principale e, in seguito, di piu' tabelle;
- anteprima normalizzata dei dati estratti;
- suggerimento del grafico in base a cardinalita', tipi di dato e numero di serie;
- configurazione manuale di assi, serie, filtri e titolo;
- esportazione del grafico come immagine o della configurazione come JSON;
- raccolta di file Excel di esempio come corpus di specifica.

### Decisioni e regia

Il lavoro sara' organizzato in specifiche piccole, versionate e verificabili.

Sequenza iniziale:

1. Definire gli scenari utente minimi.
2. Specificare il caricamento dei file Excel e i messaggi di errore.
3. Specificare le regole di individuazione della tabella.
4. Specificare la normalizzazione dei valori.
5. Specificare la selezione o proposta del grafico.
6. Specificare l'interazione di correzione manuale.
7. Implementare solo il comportamento coperto da criteri di accettazione.
8. Validare con file campione: semplice, incompleto, ambiguo, grande.

## Primo obiettivo

Realizzare un prototipo end-to-end che:

1. carica un file Excel nel browser;
2. mostra una preview dei dati interpretati;
3. propone una configurazione grafica iniziale;
4. permette una correzione manuale minima;
5. renderizza il grafico;
6. documenta il comportamento in specifiche controllabili.

## Principio guida

Graph non deve indovinare a ogni costo. Deve trasformare dati tabellari in grafici quando ha elementi sufficienti e, quando non li ha, deve rendere esplicita l'ambiguita' all'utente.
