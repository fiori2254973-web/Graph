# SPEC-005 - Proposta grafico

## Contesto

Graph propone una configurazione grafica iniziale a partire da tabella normalizzata e ruoli dati inferiti.

## Fatti noti

- L'utente deve poter correggere la proposta.
- Il suggerimento deve dipendere da cardinalita', tipi di dato e numero di serie.
- La proposta deve essere spiegabile.

## Assunzioni

- La prima versione puo' supportare pochi tipi di grafico.
- La proposta puo' essere conservativa: meglio chiedere conferma che generare un grafico sbagliato.
- Le serie numeriche sono candidate principali per valori.

## Domande aperte

- Tipi iniziali: barre, linee, torta, scatter? TUTTI QUANTI 
- Quali regole scegliere per date su asse X? FORMATO: GG/MM/AAAA
- Quando una torta va esclusa? MAI

## Comportamento atteso

- Inferire ruoli dati: categoria, valore, serie, data, etichetta.
- Proporre tipo di grafico.
- Produrre motivazione sintetica.
- Restituire warning se i ruoli sono incerti.

## Criteri di accettazione

- Una categoria testuale piu' una colonna numerica propone grafico a barre o equivalente.
- Una data piu' una o piu' serie numeriche propone grafico temporale.
- Nessun grafico viene renderizzato se non esiste almeno una serie numerica valida.
- La proposta contiene motivazione e confidenza.
- L'utente puo' modificare tipo grafico, asse categorie e serie.

