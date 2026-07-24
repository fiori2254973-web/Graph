# AI-LEDGER.md

## Scopo

Questo file e' il registro anti-recidiva del progetto Graph.

Serve a impedire che un errore, una decisione implicita o una scorciatoia gia' riconosciuta come rischiosa ritorni nel progetto senza essere vista. Ogni voce deve trasformare una lezione appresa in una regola verificabile.

## Regola generale

Quando un agente, una persona, un test o una revisione scopre un problema che potrebbe ripetersi, deve registrarlo qui prima di considerare il lavoro chiuso.

Una voce e' utile solo se contiene:

- sintomo osservabile;
- causa probabile;
- punto in cui il problema e' sfuggito;
- regola aggiornata;
- verifica che impedira' la ricorrenza;
- stato.

## Stati ammessi

- `aperto`: il rischio e' noto ma non ancora mitigato.
- `contenuto`: esiste una mitigazione temporanea.
- `prevenuto`: esiste una regola o un test anti-ricorrenza.
- `chiuso`: la mitigazione e' verificata e documentata.

## Template voce

```markdown
### LEDGER-000 - Titolo breve

- Data:
- Stato:
- Area:
- Sintomo osservabile:
- Causa probabile:
- Escape point:
- Regola aggiornata:
- Verifica anti-ricorrenza:
- File collegati:
- Owner:
- Note:
```

## Regole anti-recidiva iniziali per Graph

### LEDGER-001 - Nessuna inferenza Excel non spiegabile

- Data: 2026-07-13
- Stato: aperto
- Area: parsing Excel, inferenza dati, UX
- Sintomo osservabile: il sistema propone tabella, assi, serie o tipo di grafico senza mostrare perche' quella scelta e' stata fatta.
- Causa probabile: euristica implementata direttamente nel codice senza specifica e senza traccia delle assunzioni.
- Escape point: assenza di controllo obbligatorio su `warnings`, `assumptions` e motivazione della proposta.
- Regola aggiornata: ogni step della pipeline deve produrre dati, warning, errori e assunzioni leggibili.
- Verifica anti-ricorrenza: ogni specifica di parsing o inferenza deve includere almeno un criterio di accettazione sulla spiegabilita'.
- File collegati: `AGENTS.md`, `README.md`, `specs/000-costituzione-del-progetto.md`
- Owner: progetto Graph
- Note: Graph deve dare controllo, non magia opaca.

### LEDGER-002 - Ambiguita' Excel non trasformata in risultato silenzioso

- Data: 2026-07-13
- Stato: aperto
- Area: rilevamento tabelle, normalizzazione, preview
- Sintomo osservabile: un foglio ambiguo produce un grafico apparentemente valido ma semanticamente incerto.
- Causa probabile: il sistema privilegia sempre una proposta automatica invece di chiedere correzione manuale.
- Escape point: mancanza di soglie e condizioni di stop nella specifica.
- Regola aggiornata: quando esistono interpretazioni plausibili incompatibili, il sistema deve esporre l'ambiguita' e chiedere intervento utente.
- Verifica anti-ricorrenza: il corpus di riferimento deve includere almeno un file o scenario ambiguo e un criterio di accettazione che vieti il rendering silenzioso.
- File collegati: `specs/001-prototipo-end-to-end.md`, `evals/casi-di-riferimento/README.md`
- Owner: progetto Graph
- Note: un risultato non spiegabile e' peggiore di una richiesta di conferma.

### LEDGER-003 - File grandi non devono bloccare il browser

- Data: 2026-07-13
- Stato: aperto
- Area: performance, sicurezza operativa client-side
- Sintomo osservabile: caricamento o parsing di un file Excel grande rende la pagina non responsiva.
- Causa probabile: assenza di budget espliciti su dimensione file, numero celle, tempo di parsing o memoria.
- Escape point: specifiche prive di limiti misurabili.
- Regola aggiornata: ogni feature di import deve dichiarare limiti, budget e comportamento di stop.
- Verifica anti-ricorrenza: aggiungere scenario di file grande in `evals/casi-di-riferimento/` e criterio di accettazione sul messaggio non bloccante.
- File collegati: `specs/002-import-excel.md`, `docs/registro-dei-rischi.md`
- Owner: progetto Graph
- Note: i limiti potranno cambiare dopo misure reali, ma devono esistere da subito.

### LEDGER-004 - Specifica e codice non devono divergere

- Data: 2026-07-13
- Stato: aperto
- Area: SDD, manutenzione
- Sintomo osservabile: comportamento implementato senza criterio di accettazione o criterio non piu' vero.
- Causa probabile: modifica rapida fatta direttamente nel codice.
- Escape point: chiusura del task senza aggiornare specifica, ADR o registro decisioni.
- Regola aggiornata: nessuna modifica funzionale rilevante e' chiusa se non punta a una specifica o a una decisione registrata.
- Verifica anti-ricorrenza: ogni TASK deve indicare specifica collegata, criteri di accettazione e verifica eseguita.
- File collegati: `tasks/TASK-001-avvio-alberatura-sdd.md`, `docs/diario-delle-decisioni.md`
- Owner: progetto Graph
- Note: il README stabilisce che ogni funzionalita' rilevante nasce da specifica verificabile.

### LEDGER-005 - Le mappature dati devono dichiarare dominio e confidenza

- Data: 2026-07-13
- Stato: prevenuto
- Area: corpus Excel, mapping dati, inferenza semantica, SDD
- Sintomo osservabile: una mappatura descrive fogli, righe, colonne e formule, ma non dichiara in modo esplicito il dominio dei dati e il livello di confidenza delle inferenze.
- Causa probabile: attenzione concentrata sulla struttura tecnica del workbook invece che sul significato semantico necessario a proporre grafici corretti.
- Escape point: assenza di una sezione obbligatoria `Dominio inferito` nei mapping del corpus.
- Regola aggiornata: ogni mapping di un file dati deve includere dominio inferito, indizi osservati, interpretazioni probabili, diagrammi o mappa concettuale quando utile, confidenza e punti da confermare.
- Verifica anti-ricorrenza: `evals/corpus-excel/PP5-CONTATORE.mapping.md` contiene una sezione introduttiva dettagliata `Dominio inferito` con diagrammi Mermaid compatibili con la preview VS Code e tabella di confidenza.
- File collegati: `evals/corpus-excel/PP5-CONTATORE.mapping.md`
- Owner: progetto Graph
- Note: Graph puo' proporre grafici utili solo se distingue struttura tabellare e dominio semantico.

### LEDGER-006 - I diagrammi Mermaid devono essere compatibili con la preview VS Code

- Data: 2026-07-13
- Stato: prevenuto
- Area: documentazione, Mermaid, VS Code, SDD
- Sintomo osservabile: diagrammi Mermaid presenti nei documenti Markdown appaiono per una frazione di secondo nella preview VS Code e poi scompaiono.
- Causa probabile: doppio renderer Mermaid attivo nella Markdown Preview: renderer integrato VS Code `mermaid-markdown-features` piu' estensione installata `bierner.markdown-mermaid`, con possibile collasso post-render aggravato da resize, controlli o tema.
- Escape point: verifica limitata alla sintassi Mermaid, senza controllare comportamento dopo render della preview target.
- Regola aggiornata: non cambiare il tipo semantico dei diagrammi richiesti per aggirare un problema di rendering; usare un solo renderer Mermaid per workspace, preferendo quello integrato di VS Code, e verificare con smoke test dedicato.
- Verifica anti-ricorrenza: `PP5-CONTATORE.mapping.md` mantiene tre blocchi `mindmap` e include SVG locali come fallback visibile; `.vscode/extensions.json` marca `bierner.markdown-mermaid` come indesiderata; `.vscode/settings.json` usa tema Mermaid `vscode`; `.vscode/markdown-preview.css` forza visibilita' e contrasto; `docs/mermaid-preview-smoke-test.md` isola il problema di rendering; `docs/riepilogo-2026-07-17-sixhats.md` incorpora PNG inline in base64, cosi' la preview non dipende da renderer Mermaid, percorsi asset o cache immagini.
- File collegati: `evals/corpus-excel/PP5-CONTATORE.mapping.md`, `evals/corpus-excel/assets/PP5-CONTATORE-dominio.svg`, `evals/corpus-excel/assets/PP5-CONTATORE-relazioni-dominio.svg`, `evals/corpus-excel/assets/PP5-CONTATORE-grafici-candidati.svg`, `.vscode/settings.json`, `.vscode/extensions.json`, `.vscode/markdown-preview.css`, `docs/mermaid-preview-smoke-test.md`, `docs/mermaid-rendering.md`, `docs/riepilogo-2026-07-17-sixhats.md`
- Owner: progetto Graph
- Note: la resa visuale deve essere verificabile nello strumento realmente usato dal progetto.

### LEDGER-007 - I diagrammi Mermaid devono restare leggibili cambiando tema VS Code

- Data: 2026-07-13
- Stato: prevenuto
- Area: documentazione, Mermaid, VS Code, temi, accessibilita'
- Sintomo osservabile: i diagrammi Mermaid sono leggibili con tema scuro, ma diventano invisibili o illeggibili dopo passaggio a tema chiaro o diverso.
- Causa probabile: colori generati dal tema Mermaid o dal tema VS Code non compatibili con sfondo, testo, nodi o bordi del diagramma; possibile conflitto se due renderer Mermaid sono attivi.
- Escape point: verifica del rendering su un solo tema.
- Regola aggiornata: la preview Markdown deve usare un solo renderer Mermaid, temi Mermaid `vscode` per light/dark mode e CSS basato su variabili VS Code per testo, sfondo, nodi e linee.
- Verifica anti-ricorrenza: `.vscode/settings.json` imposta `markdown-mermaid.lightModeTheme` e `markdown-mermaid.darkModeTheme` a `vscode`; `.vscode/extensions.json` segnala `bierner.markdown-mermaid` come indesiderata; `.vscode/markdown-preview.css` forza colori leggibili tramite variabili `--vscode-*`.
- File collegati: `.vscode/settings.json`, `.vscode/extensions.json`, `.vscode/markdown-preview.css`, `docs/mermaid-preview-smoke-test.md`, `docs/mermaid-rendering.md`
- Owner: progetto Graph
- Note: dopo ogni cambio tema usare lo smoke test Mermaid prima di diagnosticare errori nei documenti.

### LEDGER-008 - Clonazione siti solo con perimetro autorizzato e limiti espliciti

- Data: 2026-07-17
- Stato: prevenuto
- Area: documentazione, crawling, scraping, analisi HTML, sicurezza operativa
- Sintomo osservabile: una procedura per clonare o analizzare un sito viene applicata senza autorizzazione, senza perimetro scritto o senza limiti su dominio, profondita', percorsi e tipi file.
- Causa probabile: confusione tra copia tecnica di pagine pubbliche e diritto di scaricare, analizzare o riusare ogni contenuto raggiungibile.
- Escape point: mancanza di segnali di stop e checklist prima del clone.
- Regola aggiornata: ogni procedura di clonazione o analisi HTML deve dichiarare autorizzazione, dominio, percorsi inclusi/esclusi, rispetto di `robots.txt`, limiti di carico e dati da estrarre prima di avviare strumenti automatici.
- Verifica anti-ricorrenza: `docs/procedura-clonazione-sito-analisi-contenuti.md` contiene segnali di stop, hardening, checklist prima/dopo clone e divieto di aggirare restrizioni o ignorare `robots.txt`.
- File collegati: `docs/procedura-clonazione-sito-analisi-contenuti.md`
- Owner: progetto Graph
- Note: separare sempre analisi autorizzata dei contenuti da copia, ripubblicazione o accesso ad aree non permesse.

### LEDGER-009 - I Sei cappelli non devono diventare personalita' o regole community non dichiarate

- Data: 2026-07-17
- Stato: prevenuto
- Area: documentazione, framework decisionali, facilitazione, SDD
- Sintomo osservabile: una guida o una sessione sui Sei cappelli tratta i cappelli come tipi di persona, oppure presenta adattamenti community come se fossero regole canoniche del metodo.
- Causa probabile: uso del framework tramite template, retrospettive o strumenti AI senza distinguere fonte ufficiale, pratica community e adattamento locale.
- Escape point: mancanza di hardening sulle fonti e assenza di una nota che ricordi il principio del pensiero parallelo.
- Regola aggiornata: ogni documento sui Sei cappelli deve distinguere definizioni canoniche, adattamenti community e uso locale; deve inoltre dichiarare che tutti i partecipanti usano lo stesso cappello nello stesso momento e che i cappelli non sono etichette personali.
- Verifica anti-ricorrenza: `sixhats.md` contiene una sezione `Second pass - hardening prima della scrittura`, fonti distinte, limiti del metodo, nota sulle fonti community e avvertenza contro l'uso dei cappelli come personalita'.
- File collegati: `sixhats.md`
- Owner: progetto Graph
- Note: l'AI puo' facilitare la sequenza, ma la chiusura decisionale e la verifica restano responsabilita' umana.

### LEDGER-010 - I framework decisionali non devono essere presentati come prove universali

- Data: 2026-07-17
- Stato: prevenuto
- Area: documentazione, framework decisionali, evidenza, SDD
- Sintomo osservabile: una guida presenta un framework decisionale come garanzia di decisioni migliori, senza distinguere definizione del metodo, pratica community, prove empiriche limitate e verifica locale.
- Causa probabile: uso di fonti promozionali, template o casi applicativi senza dichiarare livello di confidenza e perimetro delle prove.
- Escape point: assenza di una sezione su limiti, evidenza, confidenza e criteri di verifica.
- Regola aggiornata: ogni documento su framework decisionali deve dichiarare limiti, tipo di fonte, livello di confidenza e modo in cui il progetto verifichera' l'utilita' del metodo nel proprio contesto.
- Verifica anti-ricorrenza: `sixhats.md` contiene `Third pass - hardening approfondito dal web`, classificazione delle fonti, nota sulle prove di efficacia e regola SDD che collega cappelli a output verificabili.
- File collegati: `sixhats.md`
- Owner: progetto Graph
- Note: un framework puo' migliorare il processo di pensiero, ma il risultato resta da verificare con dati, test, criteri e decisioni tracciate.

### LEDGER-011 - I documenti italiani devono usare sentence case coerente

- Data: 2026-07-17
- Stato: prevenuto
- Area: documentazione, stile editoriale, Markdown, Mermaid
- Sintomo osservabile: titoli, etichette, frasi dopo i due punti e label Mermaid usano title case inglese in un documento italiano, per esempio `Diagramma di Flusso Applicativo` invece di `Diagramma di flusso applicativo`.
- Causa probabile: generazione automatica influenzata da convenzioni inglesi o da titoli accademici in stile title case.
- Escape point: assenza di un controllo editoriale specifico su sentence case prima della chiusura del documento.
- Regola aggiornata: nei documenti italiani usare sentence case per titoli, sottotitoli, label Mermaid e frasi dopo i due punti, mantenendo maiuscole solo per inizio frase, acronimi, nomi propri e denominazioni ufficiali.
- Verifica anti-ricorrenza: `docs/riepilogo-2026-07-17-sixhats.md` e' stato corretto su titoli, cappelli, esempi, label Mermaid e sezioni operative.
- File collegati: `docs/riepilogo-2026-07-17-sixhats.md`
- Owner: progetto Graph
- Note: esempi corretti: `Cappello verde (le alternative e la creativita'): e' il cappello`; `Diagramma di flusso applicativo`.

### LEDGER-012 - Le conversioni PDF tecniche devono dichiarare i limiti delle tabelle estratte

- Data: 2026-07-21
- Stato: contenuto
- Area: documentazione, conversione PDF, Markdown, manuali tecnici
- Sintomo osservabile: un manuale PDF tecnico viene convertito in Markdown conservando il testo, ma le tabelle di allarmi risultano linearizzate e non sempre ricostruibili automaticamente in tabelle Markdown affidabili.
- Causa probabile: il layer testuale del PDF espone righe e colonne come sequenze di testo, senza una struttura tabellare stabile.
- Escape point: dichiarare la conversione come completa senza indicare che la struttura visuale delle tabelle non e' stata ricostruita.
- Regola aggiornata: ogni conversione PDF tecnica deve indicare metodo di estrazione, numero di pagine, pagine senza testo estraibile, valori o sezioni campione verificati e limiti sulla ricostruzione di tabelle/impaginazione.
- Verifica anti-ricorrenza: `PVX-(107-241) Series Alarm Manual REV_A 2026.05.14.md` contiene note di conversione, separatori pagina e verifica di presenza su sezioni e ID allarme campione.
- File collegati: `PVX-(107-241) Series Alarm Manual REV_A 2026.05.14.pdf`, `PVX-(107-241) Series Alarm Manual REV_A 2026.05.14.md`
- Owner: progetto Graph
- Note: se serve fedelta' tabellare completa, pianificare una seconda passata dedicata a layout/table extraction o revisione manuale.

### LEDGER-013 - Gli agenti del symposium non devono essere confusi con versioni modello non verificate

- Data: 2026-07-21
- Stato: prevenuto
- Area: symposium, agenti IA, documentazione, SDD
- Sintomo osservabile: una documentazione del symposium cita `codex`, `claude` e `gemini` come se il nome agente locale implicasse automaticamente provider, modello e versione LLM precisa.
- Causa probabile: sovrapposizione tra identita' nel bus, prodotto usato dall'utente, provider del modello e modello effettivamente attivo nella sessione.
- Escape point: descrivere i "modelli coinvolti" senza distinguere fatti verificati nel repository, informazioni dichiarate dalla sessione e assunzioni non verificabili localmente.
- Regola aggiornata: ogni documento sul symposium deve distinguere agente nel bus, provider/famiglia, modello concreto, ruolo SDD e livello di verifica; le versioni modello non lette da configurazione o sessione devono essere dichiarate come non verificate.
- Verifica anti-ricorrenza: `Lezione del 21 luglio.md` contiene una sezione `Second pass` e una sezione `Third pass: hardening del protocollo` che separano agenti locali, provider, modello concreto, fatti, assunzioni e limiti tecnici del bus.
- File collegati: `Lezione del 21 luglio.md`, `SYMPOSIUM.md`, `symposium.py`
- Owner: progetto Graph
- Note: il symposium e' un bus locale di coordinamento, non una prova automatica della versione o dell'identita' runtime dei modelli remoti.

### LEDGER-014 - Gli LLM non devono sostituire la verifica simbolica nelle equazioni

- Data: 2026-07-24
- Stato: prevenuto
- Area: strumenti Python, equazioni differenziali, Ollama, SymPy, symposium
- Sintomo osservabile: un modello LLM propone o conferma una soluzione matematica senza verifica simbolica o numerica indipendente.
- Causa probabile: confusione tra spiegazione linguistica del modello e dimostrazione computazionale verificabile.
- Escape point: uno script usa l'LLM come fonte primaria della soluzione invece di usarlo come supporto esplicativo.
- Regola aggiornata: gli strumenti per equazioni devono usare SymPy o un solver deterministico come fonte della soluzione; Ollama puo' spiegare, suggerire una riscrittura o descrivere il fallimento, ma non deve trasformare un errore del solver in soluzione dichiarata.
- Verifica anti-ricorrenza: `scripts/ode_phi4_solver.py` e `scripts/ode_phi4_mini_solver.py` chiamano `sympy.dsolve` e `sympy.checkodesol`; il prompt al modello Ollama vieta di inventare una soluzione diversa da quella di SymPy e marca i fallimenti come limiti. Il default locale e' `phi4-mini`, coerente con il modello installato dall'utente.
- File collegati: `scripts/ode_phi4_solver.py`, `scripts/ode_phi4_mini_solver.py`
- Owner: progetto Graph
- Note: "qualunque equazione differenziale" resta un obiettivo non garantibile in forma chiusa; i casi non risolti devono restare visibili.

### LEDGER-015 - I grafici matematici non devono nascondere parametri liberi

- Data: 2026-07-24
- Stato: prevenuto
- Area: strumenti Python, equazioni differenziali, plotting, SymPy, matplotlib
- Sintomo osservabile: un grafico viene generato assegnando valori impliciti a costanti di integrazione o parametri non specificati.
- Causa probabile: trasformare automaticamente una soluzione simbolica parametrica in curva numerica senza chiedere valori all'utente.
- Escape point: la funzione di plotting valuta `y(x)` anche quando l'espressione contiene simboli liberi diversi da `x`.
- Regola aggiornata: prima di generare un grafico, lo script deve verificare che la soluzione sia in forma `y(x) = espressione` e che non restino simboli liberi oltre a `x`; in caso contrario deve fermare solo il grafico e spiegare quali valori mancano.
- Verifica anti-ricorrenza: `scripts/ode_phi4_solver.py` e `scripts/ode_phi4_mini_solver.py` usano `extract_solution_expression` e controllano `expr.free_symbols - {x}` prima di chiamare `lambdify`; i parametri grafici sono espliciti via console o CLI.
- File collegati: `scripts/ode_phi4_solver.py`, `scripts/ode_phi4_mini_solver.py`
- Owner: progetto Graph
- Note: il grafico e' una rappresentazione numerica della soluzione verificata, non una nuova inferenza matematica.

### LEDGER-016 - Gli script console interattivi devono lasciare leggere l'output

- Data: 2026-07-24
- Stato: prevenuto
- Area: strumenti Python, Windows, UX console
- Sintomo osservabile: una finestra console aperta per eseguire uno script si chiude al termine, impedendo all'utente di leggere risultato, errori o percorso del grafico salvato.
- Causa probabile: lo script termina subito dopo l'ultima operazione senza una pausa finale in modalita' console interattiva.
- Escape point: verifica eseguita solo da terminale gia' aperto, dove la chiusura del processo non chiude la finestra.
- Regola aggiornata: gli script pensati per uso interattivo su Windows devono attendere Invio prima della chiusura quando stdin e' una console reale, offrendo un flag per disattivare la pausa nelle automazioni.
- Verifica anti-ricorrenza: `scripts/ode_phi4_solver.py` e `scripts/ode_phi4_mini_solver.py` espongono `--no-pause` e chiamano `pause_before_exit` nei percorsi normali e negli errori di input gestiti.
- File collegati: `scripts/ode_phi4_solver.py`, `scripts/ode_phi4_mini_solver.py`
- Owner: progetto Graph
- Note: nei test automatici usare `--no-pause` o input non interattivo per evitare blocchi.

### LEDGER-018 - Le chiamate Ollama lente o vuote devono essere diagnosticate

- Data: 2026-07-24
- Stato: prevenuto
- Area: strumenti Python, Ollama, phi4-mini, UX console
- Sintomo osservabile: dopo l'intestazione della spiegazione LLM non compare testo, lasciando l'utente senza capire se il modello stia ancora generando, sia bloccato o abbia restituito una risposta vuota.
- Causa probabile: la chiamata HTTP a Ollama e' sincrona e senza messaggio di avanzamento; una risposta JSON senza campo `response` utile viene stampata come stringa vuota.
- Escape point: stampare solo il titolo `Spiegazione Ollama` prima della chiamata e non validare il testo ricevuto.
- Regola aggiornata: prima di chiamare Ollama gli script devono stampare un messaggio di generazione in corso e fare flush della console; se la risposta e' vuota devono mostrare un errore diagnostico con comando di verifica del modello.
- Verifica anti-ricorrenza: `scripts/ode_phi4_solver.py` e `scripts/ode_phi4_mini_solver.py` stampano `Generazione in corso...`, chiamano `sys.stdout.flush()` e trasformano risposta Ollama vuota in `RuntimeError` con suggerimento `ollama run ...`.
- File collegati: `scripts/ode_phi4_solver.py`, `scripts/ode_phi4_mini_solver.py`
- Owner: progetto Graph
- Note: su macchine senza GPU dedicata la generazione puo' richiedere tempo; il messaggio evita di confondere attesa e assenza di output.

### LEDGER-019 - Le spiegazioni LLM non devono contraddire una verifica SymPy positiva

- Data: 2026-07-24
- Stato: prevenuto
- Area: strumenti Python, Ollama, SymPy, spiegazione matematica
- Sintomo osservabile: il modello LLM afferma che la soluzione SymPy non e' corretta anche quando `checkodesol` ha restituito `(True, 0)`, poi magari conferma la stessa soluzione poche righe dopo.
- Causa probabile: prompt troppo permissivo e modello che interpreta il proprio ruolo come revisore della soluzione invece che come spiegatore di una verifica gia' eseguita.
- Escape point: l'output LLM viene stampato senza controllare frasi di contraddizione rispetto a una verifica simbolica positiva.
- Regola aggiornata: quando `Verifica SymPy` e' positiva, il prompt deve imporre che la soluzione sia trattata come verificata; se la risposta LLM contiene marker di contraddizione, lo script deve sopprimere la risposta LLM e mostrare un fallback deterministico basato sul risultato SymPy.
- Verifica anti-ricorrenza: `scripts/ode_phi4_solver.py` e `scripts/ode_phi4_mini_solver.py` usano `sympy_verified`, `llm_contradicts_verified_solution`, `fallback_verified_explanation` e `print_llm_response`; il prompt vieta di dire che SymPy ha sbagliato o che le condizioni iniziali non sono soddisfatte quando la verifica e' positiva.
- File collegati: `scripts/ode_phi4_solver.py`, `scripts/ode_phi4_mini_solver.py`
- Owner: progetto Graph
- Note: la risposta LLM contraddittoria viene censurata intenzionalmente perche' peggiora l'affidabilita' dell'output matematico.

### LEDGER-017 - L'avvio automatico di Redis deve restare esplicito e disattivabile

- Data: 2026-07-24
- Stato: prevenuto
- Area: strumenti Python, symposium, Redis, Docker, automazione locale
- Sintomo osservabile: uno script fallisce il log symposium se Redis non e' gia' in esecuzione, oppure avvia servizi Docker senza indicare quale container, immagine, volume e porta usa.
- Causa probabile: dipendenza implicita dal backend Redis del symposium e assenza di bootstrap locale controllato.
- Escape point: chiamare `symposium.store().execute("PING")` senza controllare prima lo stato della porta Redis o del container Docker previsto.
- Regola aggiornata: gli script che usano il symposium possono avviare il container Redis locale solo con nome, immagine, volume e porta dichiarati; devono attendere la raggiungibilita' della porta, riportare l'esito all'utente e offrire un flag per disattivare l'autostart.
- Verifica anti-ricorrenza: `scripts/ode_phi4_solver.py` usa `ensure_redis_container` con `redis-stack-symposium`, `redis/redis-stack-server:latest`, `redis-stack-symposium-data:/data`, porta `SYMPOSIUM_REDIS_PORT`; espone `--no-redis-auto-start`.
- File collegati: `scripts/ode_phi4_solver.py`, `SYMPOSIUM.md`
- Owner: progetto Graph
- Note: se Docker non e' installato o non e' avviato, il solver continua a riportare il limite del log symposium senza bloccare il calcolo gia' fatto.

### LEDGER-020 - Elasticita' Excel non deve diventare inferenza implicita

- Data: 2026-07-24
- Stato: prevenuto
- Area: SDD, parsing Excel, equazioni differenziali, mapping celle
- Sintomo osservabile: una specifica o implementazione promette di leggere Excel liberi senza dichiarare perimetri, configurazioni, confidenza, celle sorgente e stop condition.
- Causa probabile: confusione tra elasticita' del prodotto e assenza di vincoli verificabili.
- Escape point: aggiornare il dominio del progetto senza riscrivere costituzione, specifica operativa, ADR, task e registri.
- Regola aggiornata: ogni feature del nuovo Graph ODE deve documentare perimetri, parametri/configurazioni, celle sorgente, confidenza e criteri di stop; l'output finale deve essere rigido anche se l'input e' elastico.
- Verifica anti-ricorrenza: `specs/000-costituzione-del-progetto.md` e `specs/007-excel-equazioni-differenziali-python.md` descrivono perimetri, configurazioni, pipeline, diagrammi Mermaid, stop condition e ruolo subordinato di `phi4-mini`.
- File collegati: `specs/000-costituzione-del-progetto.md`, `specs/007-excel-equazioni-differenziali-python.md`, `README.md`, `adr/ADR-003-python-sympy-ollama-phi4-mini.md`, `tasks/TASK-004-rifondazione-graph-ode-excel.md`
- Owner: progetto Graph
- Note: formula guida: massima elasticita' in ingresso, massima rigidita' in uscita.

### LEDGER-021 - Le specifiche elastiche devono superare second e third pass

- Data: 2026-07-24
- Stato: prevenuto
- Area: SDD, specifiche, parsing elastico, black hat
- Sintomo osservabile: una SDD appare ricca ma resta insufficiente per implementare, testare o rifiutare comportamenti concreti; mancano schema dati, invarianti, confidenza, conflitti, FMEA o criteri di rifiuto.
- Causa probabile: prima stesura orientata a descrivere l'intenzione invece che a rendere falsificabile ogni passaggio operativo.
- Escape point: considerare accettata una specifica dopo aver elencato perimetri e configurazioni, senza hardening implementativo e black hat spietato.
- Regola aggiornata: ogni specifica su Excel elastici, mapping o inferenza matematica deve contenere second pass con schema dati/invarianti/confidenza/output contract e third pass con premortem/FMEA/gate/criteri di rifiuto/test matrix.
- Verifica anti-ricorrenza: `specs/007-excel-equazioni-differenziali-python.md` contiene sezioni `Second pass - hardening della specifica` e `Third pass - black hat spietato e FMEA`; `specs/000-costituzione-del-progetto.md` rende i passaggi obbligatori; `tasks/TASK-004-rifondazione-graph-ode-excel.md` li trasforma in acceptance criteria.
- File collegati: `specs/007-excel-equazioni-differenziali-python.md`, `specs/000-costituzione-del-progetto.md`, `tasks/TASK-004-rifondazione-graph-ode-excel.md`
- Owner: progetto Graph
- Note: una specifica elastica senza criteri di rifiuto e' una promessa, non una specifica.

## Checklist di chiusura anti-recidiva

Prima di chiudere un task, verificare:

- il comportamento nuovo o modificato ha una specifica collegata;
- le assunzioni sono registrate o eliminate;
- i rischi nuovi sono registrati;
- gli errori scoperti hanno una voce ledger se possono ripetersi;
- i mapping dati dichiarano dominio, confidenza e punti da confermare;
- i diagrammi Markdown usano sintassi Mermaid compatibile con la preview VS Code o dichiarano una eccezione motivata;
- i diagrammi Mermaid sono verificati almeno su tema chiaro e scuro quando diventano parte della documentazione SDD;
- il workspace non ha due renderer Mermaid Markdown attivi contemporaneamente;
- almeno una verifica manuale o automatica dimostra il criterio principale;
- eventuali stop condition sono state rispettate.
