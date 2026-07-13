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
- Verifica anti-ricorrenza: `PP5-CONTATORE.mapping.md` mantiene tre blocchi `mindmap`; `.vscode/extensions.json` marca `bierner.markdown-mermaid` come indesiderata; `.vscode/settings.json` usa tema Mermaid `vscode`; `.vscode/markdown-preview.css` forza visibilita' e contrasto; `docs/mermaid-preview-smoke-test.md` isola il problema di rendering.
- File collegati: `evals/corpus-excel/PP5-CONTATORE.mapping.md`, `.vscode/settings.json`, `.vscode/extensions.json`, `.vscode/markdown-preview.css`, `docs/mermaid-preview-smoke-test.md`, `docs/mermaid-rendering.md`
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
