# AGENTS.md

## Scopo

Questo file guida gli agenti AI che lavorano sul progetto Graph. Il progetto usa SDD, Spec Driven Development, per costruire una pagina HTML5 capace di trasformare fogli Excel generici in grafici interattivi.

Un agente deve usare questo documento per:

- scegliere il framework decisionale adatto al problema;
- evitare decisioni implicite o non verificabili;
- applicare pattern software e agentici noti;
- produrre specifiche, implementazioni e verifiche coerenti.

## Regola generale

Preferire sempre il framework piu' semplice che rende espliciti:

1. il problema;
2. i vincoli;
3. le alternative;
4. la decisione;
5. il criterio di verifica.

Se il contesto e' ambiguo, non fingere certezza: registrare l'ambiguita' nella specifica e progettare un punto di intervento per l'utente.

## Fondamenti SDD integrati da `SDD_FROM_SCRATCH.pdf`

### Definizione operativa

Lo Spec Driven Development, SDD, e' il modo di lavorare in cui la specifica scritta, controllabile e aggiornata e' la fonte di verita' del progetto. La specifica descrive che cosa il programma deve fare, con quali regole, quali limiti, quali esempi, quali criteri di verifica e quali decisioni gia' prese.

La sequenza di base da applicare e':

`specifica -> piano -> compiti -> realizzazione -> verifica -> decisione`

Per Graph questo significa che il codice deve essere trattato come conseguenza di specifiche verificabili, non come sostituto della specifica. Se la specifica non chiarisce obiettivo, input, output, vincoli, casi limite e criteri di accettazione, il lavoro resta in analisi invece di passare direttamente alla realizzazione.

### Origine del metodo

Lo SDD riordina pratiche gia' consolidate:

- 1996 / 2002, TDD, Test Driven Development: Kent Beck rese popolare l'idea di scrivere prima controlli automatici e poi il codice che li soddisfa.
- 2002 / 2011, Specification by Example: Martin Fowler uso' l'espressione per indicare specifiche rese chiare da esempi concreti; Gojko Adzic diffuse poi il metodo in un libro dedicato.
- 2003-2006, BDD, Behavior Driven Development: Dan North propose di descrivere il comportamento atteso con frasi leggibili anche da chi non scrive codice.
- 2025, GitHub Spec Kit: secondo il PDF, GitHub ha reso pubblico uno strumento che organizza il lavoro in specifica, piano, compiti e realizzazione.

La regola centrale e': la specifica e' il punto di controllo tra cio' che si vuole ottenere e cio' che viene realizzato davvero.

### Quattro abitudini di base

1. Scrivere prima che cosa si vuole ottenere, non come lo si otterra'.
2. Scomporre problemi grandi in pezzi piccoli e verificabili.
3. Scrivere le domande aperte invece di indovinarne la risposta.
4. Verificare con criteri oggettivi, non con impressioni.

### Glossario minimo

| Termine | Significato operativo |
| --- | --- |
| Specifica | Documento che descrive un obiettivo in modo preciso e verificabile. |
| Agente artificiale | Programma di IA che legge specifiche, scrive codice, analizza codice o segnala problemi. |
| Verifica | Controllo oggettivo che stabilisce se il lavoro rispetta la specifica. |
| Decisione tracciata | Scelta importante scritta con motivazione, alternative scartate e impatto atteso. |
| Ruolo | Parte assegnata a una persona o agente: progettare, realizzare, rivedere, collaudare, mettere alla prova. |

Chi verifica un lavoro non deve essere lo stesso ruolo che lo ha realizzato. Se una sola persona o un solo agente copre piu' ruoli, il cambio di ruolo deve essere esplicito e deve includere una revisione critica reale.

### Sigle da conoscere

| Sigla | Esteso | Uso nel progetto |
| --- | --- | --- |
| SDD | Spec Driven Development | Sviluppo guidato da specifica scritta e verificabile. |
| SPEC | Specification | File di specifica. |
| ADR | Architectural Decision Record | Registro di una scelta tecnica importante. |
| TASK | Task | Pezzo di lavoro piccolo, delimitato e verificabile. |
| AC | Acceptance Criteria | Condizioni vere per considerare accettato un lavoro. |
| DoD | Definition of Done | Definizione condivisa di "davvero finito". |
| BDD | Behavior Driven Development | Descrizione del comportamento atteso in linguaggio leggibile. |
| TDD | Test Driven Development | Scrittura dei test prima o insieme al codice. |
| FMEA | Failure Mode and Effects Analysis | Analisi preventiva dei modi di guasto. |
| OODA | Observe, Orient, Decide, Act | Ciclo rapido di osservazione, orientamento, decisione e azione. |
| RAG | Retrieval-Augmented Generation | Recupero di informazioni pertinenti prima della risposta. |
| SELF-RAG | SELF Retrieval-Augmented Generation | RAG sul corpus documentale interno. |
| CAG | Context Augmented Generation | Preparazione ordinata del contesto prima della generazione. |
| MCP | Model Context Protocol | Protocollo per collegare agenti a strumenti esterni. |
| LLM | Large Language Model | Modello linguistico capace di generare testo e codice. |
| HITL | Human In The Loop | Punto in cui deve intervenire una persona. |
| API | Application Programming Interface | Regole con cui un programma comunica con un altro. |
| SDK | Software Development Kit | Pacchetto di strumenti per usare un servizio o piattaforma. |
| UI | User Interface | Parte visibile e usabile del programma. |
| ERP | Enterprise Resource Planning | Gestionale aziendale integrato. |
| JWT | JSON Web Token | Token usato per autenticazione. |
| SQL | Structured Query Language | Linguaggio per interrogare database. |
| ROI | Return on Investment | Rendimento rispetto al costo sostenuto. |
| .NET | Piattaforma Microsoft | Esempio di piattaforma applicativa citata dal PDF. |

### Quando conviene usare SDD

Usare SDD con disciplina quando:

- il dominio e' complesso o regolato da norme;
- collaborano piu' persone, gruppi o fornitori;
- un errore costa denaro, tempo, reputazione o fiducia;
- il software deve vivere a lungo ed essere modificato;
- il codice e' scritto o modificato anche da agenti artificiali;
- bisogna ricostruire mesi dopo perche' una decisione e' stata presa.

### Vantaggi attesi

- riduzione delle incomprensioni tra profili tecnici e non tecnici;
- maggiore controllo del lavoro delegato agli agenti;
- verifiche piu' semplici e oggettive;
- tracciabilita' delle decisioni;
- possibilita' di cambiare strumento o fornitore senza perdere la logica del progetto;
- riuso di soluzioni, controlli e pezzi di lavoro gia' collaudati.

### Rischi se usato male

- credere che una specifica basti da sola a garantire qualita';
- produrre documenti lunghi, vaghi o non verificabili;
- confondere specifica, piano tecnico e codice;
- lasciare che specifica e codice divergano;
- trattare la specifica come decorazione invece che come fonte di verita';
- irrigidire il processo mentre il problema e' ancora esplorativo;
- affidare a un agente compiti troppo grandi rispetto alla chiarezza della specifica.

Il rischio maggiore e' una specifica che sembra autorevole senza esserlo davvero.

## Governo SDD del repository

### Livelli di lavoro

Distinguere sempre:

- livello di governo dell'archivio: specifiche, compiti, revisioni, decisioni, codice, test, smistamento del lavoro;
- livello specialistico: contenuti di settore, regole verticali, eccezioni, casi limite, conoscenza normativa o di dominio.

Regola di confine:

- chi governa l'archivio non decide da solo contenuti specialistici;
- chi lavora sui contenuti specialistici non decide il governo dell'archivio;
- se un agente attraversa entrambi i livelli, deve esistere un accordo scritto su che cosa puo' decidere, che cosa puo' proporre e dove deve fermarsi.

### Struttura consigliata

Quando il progetto cresce, usare o introdurre progressivamente questa struttura:

```text
cartella-principale-del-progetto/
  specs/
    000-costituzione-del-progetto.md
    001-*.md
  adr/
    ADR-001-*.md
  tasks/
    TASK-001-*.md
  prompts/
    architetto.md
    realizzatore.md
    revisore.md
    collaudatore.md
    lavagna-condivisa-agenti.md
  evals/
    liste-di-controllo-accettazione/
    casi-di-riferimento/
  src/
  tests/
  AI-LEDGER.md
  docs/
    diario-delle-decisioni.md
    registro-delle-assunzioni.md
    registro-dei-rischi.md
```

Non introdurre orchestrazione complessa, knowledge graph, MCP avanzati, sistemi RAG articolati o automazioni multi-agente finche' la coordinazione manuale tramite file semplici non e' diventata un ostacolo concreto.

### Ciclo di lavoro

1. Nasce un problema o bisogno.
2. Si scrive una prima versione della specifica.
3. Si chiariscono dubbi, assunzioni e vincoli.
4. Si registrano le decisioni tecniche importanti.
5. Si divide il lavoro in compiti piccoli.
6. Si realizza con l'aiuto di un agente artificiale o di una persona.
7. Si collauda e si revisiona.
8. Si consulta `AI-LEDGER.md` per verificare regole anti-recidiva applicabili.
9. Si aggiorna `AI-LEDGER.md` se e' emerso un errore, rischio o pattern che puo' ripetersi.
10. Si verifica se il lavoro rispetta i criteri di accettazione.
11. Se non li rispetta, si corregge specifica, codice o ledger.
12. Se li rispetta, si unisce il lavoro, si rilascia e si aggiorna la memoria del progetto.

### Documenti minimi iniziali

- `docs/diario-delle-decisioni.md`: per ogni decisione, riportare cosa e' stato deciso, perche', alternative scartate, effetto atteso, data e decisore.
- `docs/registro-delle-assunzioni.md`: per ogni assunzione, riportare cosa si presume vero, livello di fiducia, prova mancante e metodo di verifica.
- `docs/registro-dei-rischi.md`: per ogni rischio, riportare gravita', probabilita', mitigazione e segnale che richiede intervento umano.
- `AI-LEDGER.md`: registro anti-recidiva obbligatorio per errori, rischi, scorciatoie, pattern fragili o decisioni implicite che possono ripetersi.
- `prompts/lavagna-condivisa-agenti.md`: modello standard per far lavorare piu' ruoli sullo stesso problema senza reinventare il coordinamento.

### Prima settimana

Nella prima settimana scegliere un modulo pilota piccolo e reale, scrivere in una pagina la costituzione del progetto, preparare una specifica con criteri di accettazione chiari e far lavorare due ruoli distinti sullo stesso compito. Il dato da osservare e' se il metodo migliora chiarezza, qualita' e tempo impiegato.

### Percorso 30 / 60 / 90 giorni

Primi 30 giorni:

- scegliere un progetto pilota piccolo ma reale;
- creare `specs/`, `adr/`, `tasks/`, `prompts/`, `docs/`;
- scrivere la costituzione del progetto;
- scegliere assistenti in base al ruolo, non alla moda;
- lavorare con uno o due agenti governati da specifiche;
- misurare tempo, errori, lavoro rifatto e qualita' percepita.

Dai 31 ai 60 giorni:

- introdurre un piccolo gruppo di agenti delimitato su compiti non banali;
- stabilizzare ruoli di progettazione, realizzazione, revisione e collaudo;
- creare liste di controllo per la revisione;
- introdurre valutazioni manuali o semi-automatiche su casi di riferimento;
- confrontare costo e qualita' tra strumenti diversi.

Dai 61 ai 90 giorni:

- individuare i compiti delegabili con piu' autonomia;
- definire regole chiare su dati delicati e codice proprietario;
- spostare contenuti specialistici su un livello dedicato, se serve;
- usare fornitori economici solo per lavoro a basso rischio;
- introdurre agenti dedicati solo su lavori ricorrenti;
- decidere se servono davvero MCP, orchestrazione, RAG avanzato, modelli locali o fornitori dedicati.

### Scala di maturita'

1. Editor, controllo versioni e collaudo.
2. Un solo agente disciplinato.
3. Due agenti con contraddittorio reciproco.
4. Piccolo gruppo delimitato su compiti non banali.
5. Istruzioni pronte e ruoli standard.
6. Agenti dedicati solo dove serve davvero.
7. Collegamenti a strumenti esterni, se giustificati.
8. Orchestrazione avanzata, solo se necessaria.

### Regola di chiusura prudente

Quando manca una prova solida, il gruppo di lavoro deve convergere su una chiusura prudente, non su un'invenzione plausibile. I buchi di conoscenza vanno resi visibili, non riempiti per supposizione.

## Uso canonico e obbligatorio di `AI-LEDGER.md`

### Regola primaria

`AI-LEDGER.md` e' parte canonica del processo SDD di Graph. Non e' un documento opzionale, non e' un archivio storico decorativo e non puo' essere sostituito da memoria di conversazione.

Ogni agente deve consultarlo prima di iniziare un lavoro operativo e prima di dichiararlo concluso. Ogni recidiva possibile deve essere registrata o collegata a una voce esistente.

### Quando consultarlo

Consultare `AI-LEDGER.md` obbligatoriamente:

- prima di implementare codice;
- prima di modificare specifiche, ADR, task o prompt;
- prima di fare review o collaudo;
- quando un test fallisce;
- quando emerge un'ambiguita' gia' vista o strutturalmente ripetibile;
- quando una soluzione richiede una nuova euristica;
- prima di chiudere un task o dichiarare una verifica completata.

### Quando aggiornarlo

Aggiornare `AI-LEDGER.md` obbligatoriamente quando:

- un errore puo' ripetersi in futuro;
- una decisione implicita e' stata scoperta nel codice, nella specifica o nella UI;
- una euristica e' stata introdotta, modificata o resa piu' restrittiva;
- un warning, errore o stop condition non era previsto;
- una verifica ha trovato un buco nei criteri di accettazione;
- una regressione e' stata corretta;
- un rischio noto e' stato mitigato o cambia stato.

Se una nuova osservazione e' coperta da una voce esistente, aggiornare quella voce con collegamenti, stato o verifica. Se non e' coperta, creare una nuova voce.

### Stati ammessi

Usare gli stati definiti nel ledger:

- `aperto`: rischio noto ma non mitigato;
- `contenuto`: mitigazione temporanea;
- `prevenuto`: regola o test anti-ricorrenza presente;
- `chiuso`: mitigazione verificata e documentata.

Non inventare stati alternativi senza aggiornare prima la convenzione nel ledger.

### Gate di chiusura

Un task, una specifica, una ADR o una modifica di codice non puo' essere considerata conclusa se:

- `AI-LEDGER.md` non e' stato consultato;
- una recidiva possibile non e' stata registrata;
- una voce ledger collegata resta incoerente con il nuovo comportamento;
- la verifica anti-ricorrenza dichiarata non esiste o non e' stata pianificata;
- una nuova euristica non ha voce ledger, specifica o criterio di accettazione collegato.

### Relazione con gli altri registri

Usare i registri in modo distinto:

- `AI-LEDGER.md`: anti-recidiva, cioe' impedire che problemi noti ritornino;
- `docs/registro-dei-rischi.md`: rischi di progetto, anche se non ancora osservati;
- `docs/registro-delle-assunzioni.md`: ipotesi non verificate;
- `docs/diario-delle-decisioni.md`: decisioni prese e alternative scartate;
- `adr/`: decisioni architetturali con conseguenze tecniche stabili.

Quando una voce riguarda piu' registri, usare collegamenti espliciti invece di duplicare testo divergente.

### Output obbligatorio degli agenti

Ogni risposta operativa che chiude lavoro sul repository deve indicare:

- se `AI-LEDGER.md` e' stato consultato;
- se e' stato aggiornato;
- quali voci ledger sono collegate;
- quali rischi di recidiva restano aperti.

Se il lavoro e' solo esplorativo e non chiude alcun artefatto, dichiarare comunque se il ledger non e' stato toccato.

## Consapevolezza del ragionamento

### Protocollo minimo

Ogni specifica importante deve contenere, o rimandare esplicitamente a, questi blocchi:

1. Fatti noti: cio' che e' verificato.
2. Assunzioni: cio' che si presume vero ma non e' ancora verificato.
3. Domande aperte: cio' che manca e blocca una decisione definitiva.
4. Rischi: cio' che potrebbe andare storto e quanto sarebbe grave.
5. Segnali di stop: condizioni che fermano il lavoro finche' una persona non decide.

Formato consigliato:

```markdown
## Fatti noti
- ...

## Assunzioni
- ...

## Domande aperte
- ...

## Rischi
- ...

## Segnali di stop
- ...
```

Separare sempre fatti e assunzioni. Confondere un dato verificato con un'ipotesi non verificata degrada la qualita' del lavoro come in un esperimento scientifico mal impostato.

### Segnali di stop tipici per Graph

Fermarsi e chiedere decisione umana quando:

- manca il criterio di accettazione per un comportamento visibile;
- un file Excel produce interpretazioni plausibili ma incompatibili;
- la scelta automatica del grafico non e' spiegabile;
- il parsing richiede un'euristica nuova non documentata;
- una modifica cambia il perimetro del prodotto;
- una dipendenza esterna introduce costi, licenze o vincoli di privacy non valutati;
- i test o la verifica manuale contraddicono la specifica.

## Istruzioni efficaci per agenti

### Struttura di una buona istruzione

Una richiesta operativa riusabile deve indicare:

1. ruolo dell'agente;
2. obiettivo;
3. contesto disponibile;
4. vincoli;
5. forma esatta del risultato;
6. condizioni di stop.

Modello:

```markdown
Ruolo:
Sei il revisore della specifica o del modulo X.

Obiettivo:
Preparare un piano, una revisione o una modifica per la funzionalita' Y.

Contesto disponibile:
- Specifica: specs/...
- Decisione tecnica: adr/...
- Compito: tasks/...

Vincoli:
- Non inventare requisiti mancanti.
- Non introdurre dipendenze senza motivazione.
- Se mancano informazioni, elencale e fermati.

Forma del risultato atteso:
1. Sintesi del problema
2. Assunzioni
3. Rischi
4. Piano o modifica
5. File coinvolti
6. Verifiche

Condizioni di stop:
- ...
```

### Regole pratiche sui prompt

- Usare istruzioni brevi per compiti semplici.
- Usare istruzioni strutturate per compiti ambigui o rischiosi.
- Salvare modelli ricorrenti in `prompts/`.
- Non usare la conversazione passata come unica memoria del lavoro.
- Per i modelli OpenAI recenti preferire istruzioni orientate al risultato finale.
- Per Claude esplicitare criteri di successo, struttura e controlli intermedi.
- In ogni caso contano prove disponibili, vincoli e forma del risultato atteso.

## Ruoli degli agenti

### Regola generale sui ruoli

Gli agenti propongono, esplorano, realizzano compiti delimitati, criticano soluzioni e velocizzano riscrittura o collaudo. Le persone decidono scelte di business, requisiti mancanti, decisioni difficili da invertire e introduzione di strutture tecniche complesse.

Un nuovo ruolo o agente si introduce solo se:

- il tipo di lavoro si ripete spesso;
- input e output del ruolo sono stabili;
- il valore supera il costo di coordinamento.

### Coordinatore del gruppo di agenti

Ruolo:

- coordina piu' agenti con ruoli diversi;
- assegna il compito al ruolo giusto;
- impone un ordine chiaro di intervento;
- raccoglie pareri contrari;
- chiude con decisione, punto di controllo e prossimo passo.

Ordine obbligatorio:

1. fatti;
2. assunzioni;
3. rischi;
4. alternative;
5. decisione.

Restituisce:

- decisione presa;
- agenti o ruoli coinvolti;
- documenti letti;
- rischi rimasti aperti;
- segnale che richiede intervento umano.

Non deve:

- confondere governo dell'archivio e specialisti di settore;
- chiudere in positivo senza confronto critico;
- nascondere punti di disaccordo.

### Codex

Ruolo:

- realizzatore principale nell'archivio di progetto.

Obiettivi:

- tradurre compiti delimitati in modifiche concrete;
- aggiungere test e controlli minimi;
- restare coerente con specifiche e ADR.

Deve ricevere:

- specifica;
- compito assegnato;
- file da modificare;
- vincoli tecnici;
- criteri di accettazione.

Deve restituire:

- file toccati;
- modifica realizzata;
- test aggiunti o mancanti;
- rischi residui;
- assunzioni dichiarate.

Non deve:

- inventare requisiti di business;
- introdurre dipendenze senza motivarle;
- dichiarare chiuso un compito senza verifica.

### Claude

Ruolo:

- progettista, revisore e chiarificatore dei rischi.

Obiettivi:

- chiarire ambiguita';
- preparare piani;
- fare revisione critica del lavoro altrui;
- far emergere rischi, errori e problemi sospesi.

Deve ricevere:

- specifica;
- decisioni tecniche registrate;
- compito;
- risultato prodotto;
- contesto tecnico generale.

Deve restituire:

- sintesi del problema;
- assunzioni;
- rischi;
- compromessi considerati;
- giudizio esplicito sul procedere o fermarsi.

Non deve:

- sostituire una prova reale con un discorso convincente;
- approvare lavoro non tracciabile;
- trascurare rischi per eleganza della soluzione.

### Perplexity

Ruolo:

- verifica esterna, ricerca fonti e contraddittorio.

Obiettivi:

- cercare fonti affidabili;
- proporre alternative;
- contestare assunzioni deboli;
- confrontare standard, schemi e prassi.

Deve ricevere:

- affermazione da verificare;
- domande di confronto;
- limiti di tempo o area geografica;
- criteri di qualita' delle fonti.

Deve restituire:

- fonti con link;
- confronto sintetico;
- punti di disaccordo;
- limiti delle prove trovate.

Non deve:

- produrre codice proprietario come compito principale;
- trasformare un confronto generico in regola assoluta;
- dichiarare certezza dove esistono solo indizi.

### DeepSeek Coder

Ruolo:

- agente tecnico attento ai costi.

Obiettivi:

- assorbire compiti ripetitivi;
- produrre riscritture meccaniche;
- estendere impalcature di test;
- gestire modifiche ripetute a costo contenuto.

Deve ricevere:

- file da modificare;
- schema da applicare;
- vincoli di stile;
- limiti del perimetro.

Deve restituire:

- modifica proposta;
- punti dubbi;
- parti da far rivedere.

Non deve:

- decidere architettura;
- agire su parti delicate senza doppia revisione;
- assumere corrette assunzioni di settore non verificate.

### Agente specialista di settore

Ruolo:

- specialista di un settore su piattaforma dedicata, come Regolo.ai o equivalente.

Obiettivi:

- verificare regole del proprio settore;
- segnalare eccezioni;
- proporre casi limite;
- distinguere fatto normativo, prassi diffusa e ipotesi.

Deve ricevere:

- specifica di settore;
- glossario del settore;
- caso concreto;
- domanda delimitata.

Deve restituire:

- risposta specialistica;
- regole applicate;
- casi dubbi;
- parti da affidare a revisione umana.

Non deve:

- riscrivere il governo generale del progetto;
- prendere decisioni fuori dal proprio settore;
- nascondere incertezze normative o interpretative.

## Scelta degli strumenti

### Criteri

Scegliere strumenti chiedendosi quale sia il piu' adatto al lavoro, al costo e al rischio, non quale sia il piu' nuovo.

| Criterio | Domanda |
| --- | --- |
| Scrittura del codice | Scrive bene nel linguaggio e tecnologia scelti? |
| Riscrittura | Mantiene struttura e vincoli esistenti? |
| Collaudo | Genera test utili o superficiali? |
| Revisione | Trova problemi reali o commenti generici? |
| Gestione contesto | Regge specifiche lunghe e repository grandi? |
| Costo | Il valore supera il costo effettivo? |
| Riservatezza | Dove passano codice e dati? |
| Guidabilita' | Segue bene specifiche e istruzioni chiare? |

### Smistamento del lavoro

| Tipo di lavoro | Destinazione principale | Alternativa |
| --- | --- | --- |
| Pianificazione archivio e divisione compiti | Claude o Codex | DeepSeek Coder |
| Scrittura e riscrittura del codice | Codex | DeepSeek Coder |
| Revisione critica e dubbi | Claude | Codex |
| Ricerca web e prova esterna | Perplexity | Claude |
| Contenuti specialistici | Regolo.ai o equivalente | fornitore specialistico |
| Compiti veloci, economici, poco delicati | Groq o simili | DeepSeek Coder |
| Carichi portabili o semi-dedicati | Runpod o simili | fornitore gestito |

### Costo e riservatezza

- Per codice proprietario delicato, ridurre il contesto al minimo necessario e usare strumenti con regole prudenti.
- Per compiti tecnici ripetitivi e poco delicati, usare opzioni economiche.
- Per compiti di settore delicati, preferire il livello specialistico principale anche se costa di piu'.
- Per crescita futura, valutare fornitori piu' controllabili solo quando il volume giustifica la complessita'.

## Framework decisionali

### Sei cappelli per pensare

Usare i Sei cappelli per pensare quando serve una revisione multiprospettica ordinata, soprattutto prima di fissare una specifica SDD, scegliere una direzione progettuale o fare hardening di un documento.

Nel progetto Graph usare questa traduzione operativa:

- Cappello bianco: fatti.
- Cappello nero: rischi e criticita'.
- Cappello giallo: opportunita'.
- Cappello rosso: percezione ed emozioni.
- Cappello verde: alternative e lenti multiprospettiche.
- Cappello blu: decisioni e regia.

Output atteso:

- fatti verificabili separati dalle opinioni;
- rischi espliciti e mitigazioni candidate;
- opportunita' di valore;
- impatto percepito dall'utente;
- alternative non ancora scelte;
- decisione finale, owner e prossimo passo.

Regola di scrittura:

- nei documenti finali evitare di parlare necessariamente di "cappelli";
- preferire titoli professionali come `Fatti`, `Rischi e criticita'`, `Opportunita'`, `Percezione ed emozioni`, `Alternative e lenti multiprospettiche`, `Decisioni e regia`.

### TRIZ

Usare TRIZ quando il problema contiene una contraddizione: migliorare una qualita' peggiora un'altra.

Esempi per Graph:

- aumentare l'automatismo senza ridurre il controllo dell'utente;
- supportare Excel generici senza introdurre troppe eccezioni;
- rendere il parsing tollerante senza accettare dati semanticamente sbagliati.

Output atteso:

- contraddizione formulata;
- parametro da migliorare;
- parametro da non peggiorare;
- possibili principi inventivi applicabili;
- scelta progettuale candidata.

### OODA

Usare OODA per decisioni rapide in contesti dinamici.

Sequenza:

1. Observe: raccogliere dati, errori, esempi Excel, feedback utente.
2. Orient: interpretare il contesto, distinguere ipotesi da fatti.
3. Decide: scegliere la prossima azione minima.
4. Act: implementare, testare o chiedere conferma.

Applicazione:

- debugging;
- triage di bug;
- iterazioni UI;
- scelta della prossima specifica.

### 8D

Usare 8D per problemi gravi, ricorrenti o di qualita'.

Sequenza operativa:

1. D0: preparare il lavoro.
2. D1: formare il gruppo o il ruolo responsabile.
3. D2: descrivere il problema con dati osservabili.
4. D3: contenere temporaneamente l'impatto.
5. D4: trovare root cause ed escape point.
6. D5: scegliere azione correttiva permanente.
7. D6: implementare e validare.
8. D7: prevenire ricorrenza.
9. D8: chiudere e documentare lezioni apprese.

Applicazione:

- bug che causano grafici sbagliati;
- parsing Excel instabile;
- regressioni su file campione;
- errori silenziosi.

### Cynefin

Usare Cynefin per capire che tipo di problema si sta affrontando.

- Clear: causa-effetto evidente; applicare best practice.
- Complicated: serve analisi esperta; confrontare alternative.
- Complex: causa-effetto visibile solo dopo esperimenti; fare probe piccoli.
- Chaotic: serve stabilizzare prima di analizzare.
- Confused: scomporre il problema in parti classificabili.

Applicazione:

- Excel semplice: Clear.
- Excel con formati misti: Complicated.
- Excel generici non prevedibili: Complex.
- crash o blocco browser: Chaotic.

### PDCA / PDSA

Usare PDCA o PDSA per miglioramento continuo.

Sequenza:

1. Plan: ipotesi e criterio di successo.
2. Do: esperimento piccolo.
3. Check/Study: confronto con dati e specifica.
4. Act: standardizzare, correggere o ripianificare.

Applicazione:

- miglioramento parsing;
- raffinamento UX;
- ottimizzazione performance;
- riduzione falsi positivi nei suggerimenti grafici.

### DMAIC

Usare DMAIC quando serve migliorare un processo misurabile.

Sequenza:

1. Define: definire problema, obiettivo e perimetro.
2. Measure: raccogliere misure.
3. Analyze: trovare cause.
4. Improve: introdurre cambiamenti.
5. Control: prevenire regressioni.

Metriche utili:

- tempo di caricamento file;
- percentuale di file interpretati correttamente;
- numero di interventi manuali richiesti;
- errori di normalizzazione;
- copertura dei file campione.

### A3

Usare A3 quando serve condensare un problema in una pagina.

Struttura:

- contesto;
- stato attuale;
- obiettivo;
- analisi root cause;
- contromisure;
- piano;
- follow-up.

Applicazione:

- decisioni architetturali;
- bug complessi;
- scelta libreria;
- evoluzioni importanti della UX.

### Five Whys e Ishikawa

Usare Five Whys per risalire da sintomo a causa probabile. Usare Ishikawa quando le cause possono appartenere a famiglie diverse.

Famiglie consigliate per Graph:

- dati;
- parsing;
- UI;
- librerie;
- performance;
- specifiche;
- test.

### FMEA

Usare FMEA quando una funzione puo' fallire in piu' modi e serve prevenzione.

Campi minimi:

- failure mode;
- effetto;
- causa;
- severita';
- probabilita';
- rilevabilita';
- mitigazione.

Applicazione:

- upload file;
- parsing celle;
- scelta automatica grafico;
- esportazione;
- salvataggio configurazione.

### SWOT / TOWS

Usare SWOT per strategia e posizionamento.

- Strengths: punti forti interni.
- Weaknesses: limiti interni.
- Opportunities: possibilita' esterne.
- Threats: rischi esterni.

Usare TOWS dopo SWOT per trasformare la matrice in azioni: SO, ST, WO, WT.

### PESTEL

Usare PESTEL per rischi esterni:

- Political;
- Economic;
- Social;
- Technological;
- Environmental;
- Legal.

Applicazione:

- privacy dei file Excel;
- dipendenze browser;
- licenze librerie;
- uso locale vs cloud;
- accessibilita'.

### MCDA / matrice decisionale pesata

Usare MCDA quando ci sono alternative con criteri in conflitto.

Esempio: scelta libreria grafici.

Criteri possibili:

- licenza;
- peso bundle;
- accessibilita';
- tipi di grafico;
- performance;
- manutenzione;
- integrazione HTML5;
- esportazione.

Output:

- alternative;
- criteri;
- pesi;
- punteggi;
- decisione;
- sensibilita' del risultato ai pesi.

### Kepner-Tregoe

Usare Kepner-Tregoe quando bisogna confrontare alternative tecniche diverse e distinguere requisiti obbligatori da preferenze.

Esempi:

- modello IA potente contro modello leggero e aperto;
- cloud contro esecuzione locale;
- piu' agenti separati contro un agente unico;
- applicazione monolitica contro moduli collegati;
- libreria di charting completa contro libreria piu' piccola.

Output atteso:

- decisione da prendere;
- requisiti obbligatori;
- criteri desiderabili;
- alternative;
- rischi negativi di ciascuna alternativa;
- scelta raccomandata;
- verifica o esperimento minimo prima dell'adozione.

### Eisenhower

Usare la matrice urgenza/importanza per triage operativo.

- Urgente e importante: fare subito.
- Importante non urgente: pianificare.
- Urgente non importante: delegare o automatizzare.
- Non urgente non importante: eliminare.

### RICE

Usare RICE per prioritizzare feature.

Formula:

`score = (Reach * Impact * Confidence) / Effort`

Applicazione:

- backlog prodotto;
- miglioramenti UX;
- nuove tipologie di grafico;
- supporto a casi Excel aggiuntivi.

### MoSCoW

Usare MoSCoW per definire una release.

- Must: necessario per il successo della release.
- Should: importante ma non bloccante.
- Could: utile se resta capacita'.
- Won't: esplicitamente fuori scope per ora.

### Kano

Usare Kano per distinguere:

- bisogni base;
- prestazioni attese;
- elementi di soddisfazione;
- elementi irrilevanti;
- elementi potenzialmente negativi.

Applicazione:

- upload affidabile: base;
- preview dati: prestazione attesa;
- suggerimento grafico intelligente: soddisfazione;
- animazioni eccessive: potenzialmente negative.

### WSJF / Cost of Delay

Usare WSJF per decidere cosa sviluppare prima quando il ritardo ha costo.

Formula tipica:

`WSJF = Cost of Delay / Job Size`

Applicazione:

- bug bloccanti;
- lavoro abilitante per molte specifiche;
- riduzione rischio tecnico.

### RAPID

Usare RAPID quando la decisione coinvolge piu' ruoli.

- Recommend: formula raccomandazione.
- Agree: approva o pone vincoli.
- Perform: esegue.
- Input: fornisce informazioni.
- Decide: decide.

### DACI

Usare DACI per decisioni di progetto leggere.

- Driver: guida il processo.
- Approver: prende la decisione.
- Contributors: contribuiscono dati e alternative.
- Informed: vengono aggiornati.

### RACI

Usare RACI per responsabilita' operative.

- Responsible: esegue.
- Accountable: risponde del risultato.
- Consulted: viene consultato.
- Informed: viene informato.

### Premortem

Usare il premortem prima di una scelta rischiosa.

Domanda guida:

> Immagina che questa scelta sia fallita tra tre mesi. Perche'?

Output:

- lista fallimenti plausibili;
- segnali precoci;
- mitigazioni;
- decisione di procedere, cambiare o fermare.

### Double Diamond / Design Thinking

Usare Double Diamond o Design Thinking per problemi utente non ancora chiari.

Fasi:

1. divergere sul problema;
2. convergere sulla definizione;
3. divergere sulle soluzioni;
4. convergere su prototipo e test.

Applicazione:

- UX di correzione manuale;
- linguaggio dei messaggi di errore;
- modalita' di preview.

## Selettore rapido

| Situazione | Framework consigliato | Output |
| --- | --- | --- |
| Revisione multiprospettica | Sei cappelli per pensare | fatti + rischi + opportunita' + percezione + alternative + regia |
| Contraddizione tecnica | TRIZ | contraddizione + principi candidati |
| Bug grave o ricorrente | 8D | root cause + azione permanente |
| Iterazione veloce | OODA | prossima azione verificabile |
| Ambiguita' del dominio | Cynefin | classificazione + strategia |
| Miglioramento continuo | PDCA/PDSA | esperimento + risultato |
| Processo misurabile | DMAIC | metriche + controllo |
| Decisione tra alternative | MCDA, Kepner-Tregoe | matrice pesata o must/want + rischi |
| Priorita' backlog | RICE, MoSCoW, Kano | ordine di lavoro |
| Decisione multi-ruolo | RAPID, DACI, RACI | ruoli espliciti |
| Scelta rischiosa | Premortem, FMEA | rischi + mitigazioni |
| Problema UX aperto | Double Diamond | prototipo testabile |

## Best design patterns software

### Principi base

- Programmare verso interfacce, non implementazioni concrete.
- Favorire composizione rispetto a ereditarieta' profonda.
- Rendere esplicite dipendenze, effetti collaterali e confini.
- Usare pattern per ridurre complessita', non per esibire architettura.
- Preferire testabilita', osservabilita' e sostituibilita'.

### Pattern GoF piu' rilevanti

#### Creazionali

- Factory Method: creare parser, renderer o normalizzatori senza legare il chiamante alla classe concreta.
- Abstract Factory: creare famiglie coerenti di componenti, per esempio set di grafici o adapter.
- Builder: costruire configurazioni di grafico passo-passo.
- Prototype: clonare configurazioni di grafico modificabili.
- Singleton: usare con cautela solo per risorse realmente uniche; evitare stato globale nascosto.

#### Strutturali

- Adapter: uniformare API di librerie Excel o charting.
- Facade: offrire un'interfaccia semplice a parsing, normalizzazione e rendering.
- Decorator: aggiungere validazioni, logging o metriche senza cambiare il componente base.
- Proxy: ritardare caricamenti pesanti o proteggere accessi.
- Composite: rappresentare workbook, fogli, tabelle, serie e celle come albero.
- Bridge: separare astrazione del grafico dal renderer concreto.

#### Comportamentali

- Strategy: cambiare algoritmo di rilevamento tabella o scelta grafico.
- Chain of Responsibility: pipeline di validazione e interpretazione.
- Command: azioni annullabili dell'utente sulla configurazione.
- Observer / Pub-Sub: aggiornare UI quando cambia stato dati o grafico.
- State: gestire stati upload, parsing, preview, configurazione, rendering, errore.
- Template Method: definire scheletro comune per importatori o validatori.
- Iterator: attraversare righe, colonne, celle e serie.
- Visitor: calcolare statistiche o validazioni su una struttura dati composita.

### Pattern web e .NET storicamente associabili a 4GuysFromRolla

4GuysFromRolla e' una fonte storica ASP/ASP.NET. Per un progetto moderno non va copiata letteralmente, ma alcune idee web restano utili:

- Base Page / classe base di pagina: centralizzare comportamento comune di pagina; in Graph puo' diventare un layout o shell applicativa.
- Page Controller: ogni pagina coordina input, stato e output; utile solo per pagine semplici.
- Front Controller / Router: un punto unico riceve l'azione e smista verso handler.
- MVC / MVP: separare vista, stato e logica di presentazione.
- Repository: isolare accesso a file campione, specifiche o configurazioni.
- Unit of Work: utile solo se in futuro ci sara' persistenza complessa.
- Dependency Injection: rendere sostituibili parser, renderer, logger, store.
- Service Layer: concentrare casi d'uso come `importWorkbook`, `inferChart`, `renderChart`.

### Pattern architetturali utili a Graph

- Pipeline: upload -> parse -> detect tables -> normalize -> infer chart -> preview -> render.
- Ports and Adapters: tenere il dominio indipendente da librerie Excel e charting.
- Hexagonal Architecture: UI, filesystem e librerie esterne come adapter.
- Bounded Context: separare aree di competenza diverse, per esempio import Excel, normalizzazione dati, inferenza ruoli, rendering grafico, esportazione.
- Anti-Corruption Layer: tradurre dati tra librerie esterne e dominio Graph senza far entrare nel dominio formati sporchi o convenzioni della libreria.
- CQRS leggero: separare comandi utente da query di preview.
- Event Log: registrare decisioni automatiche e correzioni manuali.
- Specification Pattern: rappresentare requisiti SDD come regole verificabili.
- Result / Either: restituire successi, warning ed errori senza eccezioni silenziose.
- Null Object: gestire assenza controllata di serie, titolo o foglio selezionato.
- Circuit Breaker / Budget: fermare elaborazioni costose su file troppo grandi.
- Contract Tests: verificare che parser, normalizzatore e renderer continuino a capirsi dopo le modifiche.
- Feature Flags: attivare o disattivare funzioni sperimentali senza riscrivere codice o rompere il flusso stabile.

### Pattern di lavoro da preferire

- Specifica -> Piano -> Compiti -> Realizzazione -> Verifica.
- ADR per ogni scelta importante.
- Definition of Done esplicita.
- Revisione secondo accordo scritto, non a sensazione.
- Planner, executor, reviewer e tester come ruoli distinti.
- Ciclo di valutazione e miglioramento continuo del risultato.
- Critica finale prima della consegna.
- Routing del compito verso l'agente o strumento piu' adatto.
- Lavagna condivisa fatta di file di testo leggibili da tutti gli agenti coinvolti.

## Pattern applicabili ad agenti AI

### Augmented LLM

LLM con strumenti, memoria, retrieval e contesto esterno. Usarlo come blocco base, non come architettura completa.

Regole:

- tool piccoli e ben documentati;
- input strutturati;
- output verificabili;
- limiti di tempo, costo e iterazioni.

### Prompt Chaining

Dividere un compito in passi sequenziali.

Applicazione:

1. estrai requisiti;
2. genera specifica;
3. valida casi limite;
4. implementa;
5. verifica.

### Routing

Classificare il problema e inviarlo al flusso corretto.

Esempi:

- domanda sul progetto -> lettura documenti;
- bug -> 8D leggero;
- scelta architetturale -> MCDA;
- UX incerta -> Double Diamond.

### Parallelization

Usare prospettive parallele quando il problema e' divisibile.

Esempi:

- un controllo per sicurezza;
- uno per performance;
- uno per UX;
- uno per coerenza SDD.

### Orchestrator-Workers

Un agente centrale scompone il lavoro e sintetizza risultati.

Applicazione:

- modifiche multi-file;
- ricerca web ampia;
- valutazione di piu' librerie;
- generazione di test e specifiche.

### Evaluator-Optimizer

Un agente produce, un altro valuta secondo criteri espliciti, poi si itera.

Applicazione:

- hardening README;
- revisione specifiche;
- controlli anti-duplicazione;
- qualita' messaggi UI.

### ReAct

Alternare ragionamento, azione e osservazione.

Applicazione:

- esplorare repository;
- usare strumenti;
- correggere dopo feedback reale;
- evitare conclusioni non supportate dai dati.

### Reflexion

Dopo un errore o un test fallito, produrre una riflessione breve e riusabile.

Formato:

- cosa e' fallito;
- perche' e' fallito;
- quale regola aggiorno;
- quale test impedira' la ricorrenza.

### RAG

Usare retrieval quando la risposta dipende da documenti, specifiche o fonti esterne.

Regole:

- citare fonti;
- distinguere dati recuperati da inferenze;
- non usare memoria generica per norme, API o versioni aggiornabili.

### Planner-Executor

Separare pianificazione ed esecuzione quando il lavoro e' lungo.

Output del planner:

- obiettivo;
- passi;
- dipendenze;
- rischi;
- verifiche.

Output dell'executor:

- modifiche;
- test;
- scostamenti;
- blocchi.

### Critic / Reviewer

Usare un ruolo critico prima di considerare completo un artefatto.

Checklist:

- duplicazioni semantiche;
- ipotesi non dichiarate;
- casi limite;
- criteri di accettazione;
- test mancanti;
- rischi di regressione.

### Human-in-the-loop

Chiedere intervento umano quando:

- una decisione cambia il perimetro prodotto;
- l'ambiguita' e' intenzionale o di business;
- il costo di un errore e' alto;
- ci sono opzioni equivalenti con trade-off soggettivi.

### Guardrails

Ogni agente operativo deve avere:

- perimetro;
- strumenti consentiti;
- stop condition;
- criteri di successo;
- log delle decisioni;
- fallback in caso di incertezza.

### Memory controllata

Usare memoria solo se:

- e' rilevante per il compito;
- ha data o origine;
- puo' essere corretta;
- non sostituisce una fonte autorevole.

### Tool-use hardening

Le interfacce verso tool devono essere progettate come API per un junior developer:

- nomi chiari;
- parametri espliciti;
- esempi;
- errori leggibili;
- vincoli validati;
- idempotenza dove possibile.

## Applicazione al progetto Graph

### Decisioni da registrare sempre

- quale formato Excel e' supportato;
- come viene scelta la tabella principale;
- come vengono interpretate intestazioni e valori;
- quando il sistema propone un grafico;
- quando chiede correzione manuale;
- quali errori sono bloccanti;
- quali warning sono accettabili.

### Pattern consigliato per il flusso dati

Usare una pipeline esplicita:

1. `loadWorkbook`
2. `extractSheets`
3. `detectTables`
4. `normalizeTable`
5. `inferDataRoles`
6. `proposeChart`
7. `previewDecision`
8. `renderChart`

Ogni step deve produrre:

- input dichiarato;
- output tipizzato;
- errori;
- warning;
- traccia delle assunzioni.

### Pattern consigliato per SDD

Ogni specifica deve contenere:

- contesto;
- precondizioni;
- input;
- comportamento atteso;
- casi limite;
- criteri di accettazione;
- esempi;
- test o verifica manuale.

### Anti-pattern da evitare

- parsing basato su euristiche non documentate;
- errori silenziosi;
- scelta automatica non spiegabile;
- stato globale condiviso;
- dipendenze hardcoded;
- UI che nasconde ambiguita';
- agenti autonomi senza stop condition;
- test solo sul caso ideale;
- refactor non richiesti durante una correzione puntuale;
- istruzione unica enorme per governare tutto il progetto;
- agenti senza ruoli chiari;
- codice scritto senza specifica alle spalle;
- revisione fatta dallo stesso ruolo che ha realizzato il lavoro senza contraddittorio;
- dipendenza dalla memoria delle conversazioni invece che da documenti versionati;
- strumenti di coordinamento complessi introdotti prima che servano davvero;
- esempi presentati come racconti generici senza compiti verificabili;
- tabelle troppo astratte, senza limiti o vincoli concreti;
- `AGENTS.md` che descrive modelli invece di regolare comportamenti;
- tecnologie o infrastrutture date per disponibili senza verifica;
- risparmio ottenuto usando uno strumento fuori dal proprio perimetro di rischio;
- documento approvato senza confronto critico tra chi propone e chi mette alla prova.

## Esempi pratici come schemi riusabili

Gli esempi del PDF non sono soluzioni da copiare: sono modelli di scomposizione. Ogni nuovo esempio o caso studio deve mostrare:

- contesto e tipo di prodotto;
- obiettivo;
- specifica minima;
- primo gruppo di compiti;
- criteri di accettazione;
- ruoli o agenti consigliati;
- rischi principali.

### Catalogo di esempi dal PDF

1. Riconciliazione bancaria: import CSV/XLSX ed estratti contabili, abbinamento automatico, coda dei dubbi, registro esportabile; rischi principali: riconciliazioni errate, piano dei conti sbagliato, movimenti ambigui.
2. Fatture da pagare: anagrafiche fornitori, caricamento fatture, approvazione, export verso gestionale; rischi: duplicazioni contabili, workflow non verificabile, dipendenza da un ERP.
3. Chiusure contabili mensili: calendario, checklist, dipendenze, prove di completamento; rischi: sequenze errate, completamenti senza prova, workflow troppo rigido.
4. Clausole contrattuali: archivio modelli, etichette, confronto versioni, avvisi su clausole delicate; rischi: affermazioni legali non verificate, false equivalenze, tracciabilita' insufficiente.
5. Accoglienza nuove pratiche legali: raccolta richieste, classificazione, allegati, assegnazione; rischi: informazioni incomplete, dati delicati gestiti male, classificazione imprecisa.
6. Scadenze e adempimenti: calendario, preavvisi, responsabili, prove e storico; rischi: promemoria ignorati, scadenze duplicate, falsa sensazione di conformita'.
7. Previsione flussi di cassa: dati su saldi, incassi, pagamenti, scenari 30/60/90 giorni e assunzioni; rischi: confondere previsione e consuntivo, scenari non spiegabili, dati sporchi.
8. Valutazione rischio cliente: anagrafica, indicatori, regole, spiegazione del punteggio, storico decisioni; rischi: punteggio opaco, bias nei dati, uso improprio del risultato.
9. Prezzi e margini: costi diretti e indiretti, ripartizioni, scenari di prezzo, sensibilita'; rischi: formule opache, ripartizioni arbitrarie, simulazioni scambiate per certezze.
10. Due diligence documentale: archivio, checklist per categoria, stato documenti, registro mancanze; rischi: classificazione generica, documenti segnati completi senza esserlo, responsabilita' sovrapposte.

Per Graph, usare questa stessa struttura quando si aggiungono esempi su file Excel reali: contesto del foglio, obiettivo del grafico, specifica minima, compiti, criteri di accettazione, ruoli e rischi.

## Qualita' della documentazione

### Aggiornare questo documento

Ogni futura aggiunta a `AGENTS.md` deve essere valutata da quattro funzioni, anche se svolte dalla stessa persona o agente in momenti separati:

- chi progetta: controlla struttura, confini e coerenza degli schemi;
- chi realizza: trasforma richieste in sezioni concrete e tabelle verificabili;
- chi rivede: segnala dimenticanze, ripetizioni, ambiguita' e fuori tema;
- chi mette alla prova: contesta assunzioni, favoritismi verso fornitori e affermazioni non dimostrate.

Una nuova sezione e' accettabile quando:

- e' riusabile anche fuori dal caso specifico;
- distingue fatto, schema generale e consiglio;
- definisce un risultato verificabile;
- segnala almeno un rischio o limite;
- non richiede tecnologie non disponibili o non verificate.

### Stile documentale

Preferire un linguaggio impersonale nelle regole di governo, nei ruoli, nei criteri di qualita' e nelle condizioni di stop. Questo riduce la dipendenza da singole persone, facilita il riuso e rende il documento piu' stabile.

## Fonti consultate

- `SDD_FROM_SCRATCH.pdf`, "Sviluppo guidato dalla specifica (SDD, Spec Driven Development). Dispensa per chi parte da zero", Fabrizio Ricciarelli, giugno 2026.
- GitHub Spec Kit: https://github.com/github/spec-kit
- Documentazione GitHub Spec Kit: https://github.github.com/spec-kit/
- GitHub Blog, "Spec-driven development with AI": https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Martin Fowler, "Specification by Example": https://martinfowler.com/bliki/SpecificationByExample.html
- Martin Fowler, "Given When Then": https://martinfowler.com/bliki/GivenWhenThen.html
- Cucumber, "Behavior-Driven Development": https://cucumber.io/docs/bdd/
- Wikipedia, "Test-driven development": https://en.wikipedia.org/wiki/Test-driven_development
- Anthropic, "Building effective agents": https://www.anthropic.com/research/building-effective-agents
- Anthropic, prompt engineering per Claude: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- OpenAI, prompt engineering: https://developers.openai.com/api/docs/guides/prompt-engineering
- VS Code, AI chat overview: https://code.visualstudio.com/docs/chat/chat-overview
- Model Context Protocol: https://modelcontextprotocol.io/introduction
- de Bono Group, "Six Thinking Hats": https://www.debonogroup.com/services/core-programs/six-thinking-hats/
- TRIZ40, "Solve a Technical Problem": https://www.triz40.com/TRIZ_GB.php
- The Decision Lab, "The OODA Loop": https://thedecisionlab.com/reference-guide/computer-science/the-ooda-loop
- Quality-One, "Eight Disciplines of Problem Solving (8D)": https://quality-one.com/8d/
- The Cynefin Company, "The Cynefin Framework": https://thecynefin.co/about-us/about-cynefin-framework/
- ASQ, "PDCA Cycle": https://asq.org/quality-resources/pdca-cycle
- Lean Enterprise Institute, "A3 Report": https://www.lean.org/lexicon-terms/a3-report/
- UK Government Analysis Function, "Multi-Criteria Decision Analysis": https://analysisfunction.civilservice.gov.uk/policy-store/an-introductory-guide-to-mcda/
- Bain & Company, "RAPID Decision Making": https://www.bain.com/insights/rapid-decision-making/
- Atlassian, "DACI": https://www.atlassian.com/team-playbook/plays/daci
- Intercom, "RICE prioritization": https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
- Dofactory, "C# Design Patterns": https://www.dofactory.com/net/design-patterns
- Microsoft Learn, "Discovering the Design Patterns You're Already Using in .NET": https://learn.microsoft.com/en-us/archive/msdn-magazine/2005/july/discovering-the-design-patterns-you-re-already-using-in-net
- Google Research, "ReAct: Synergizing Reasoning and Acting in Language Models": https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/
- arXiv, "Reflexion: Language Agents with Verbal Reinforcement Learning": https://arxiv.org/abs/2303.11366
- Anthropic, "Building effective agents": https://www.anthropic.com/engineering/building-effective-agents
