# SPEC-000 - Costituzione del progetto Graph

## Contesto

Graph e' un'applicazione web HTML5 per trasformare fogli Excel generici in grafici interattivi. L'elaborazione iniziale avviene nel browser, su file caricati localmente dall'utente.

Il progetto usa SDD: ogni funzionalita' rilevante deve nascere da una specifica verificabile, con criteri di accettazione e gestione esplicita delle ambiguita'.

## Fatti noti

- Input iniziale: file `.xlsx` o `.xls`.
- Output iniziale: grafico interattivo renderizzato in pagina web.
- Ambiente iniziale: browser moderno, HTML5, elaborazione client-side.
- Dati attesi: intestazioni, categorie, numeri, date, serie singole o multiple.
- Vincolo primario: nessun formato Excel obbligatorio.
- Vincolo di qualita': ogni inferenza deve essere spiegabile.

## Assunzioni

- Il prototipo iniziale puo' lavorare senza backend.
- L'utente accetta una correzione manuale minima prima del rendering.
- Il primo corpus di verifica puo' essere descritto con scenari testuali prima di avere file Excel reali.
- Le librerie Excel e charting saranno scelte con ADR dedicata.

## Domande aperte

- Quale libreria verra' usata per leggere `.xlsx` e `.xls` nel browser?
- Quale libreria verra' usata per i grafici interattivi?
- Quali limiti iniziali applicare a dimensione file, numero celle e tempo di parsing?
- Quali browser minimi supportare?
- Serve esportare immagine, JSON di configurazione o entrambi nella prima release?

## Rischi

- Tabelle non rettangolari, righe introduttive, celle vuote e intestazioni spezzate.
- Piu' tabelle nello stesso foglio.
- Valori misti nella stessa colonna.
- Date, valute e separatori dipendenti dalla localizzazione.
- File grandi che bloccano il browser.
- Suggerimenti automatici semanticamente errati ma visivamente plausibili.

## Segnali di stop

- Una scelta automatica non puo' essere spiegata all'utente.
- Due interpretazioni del foglio sono plausibili ma incompatibili.
- Una nuova euristica non e' documentata in specifica.
- Una dipendenza esterna introduce licenza, peso o rischio privacy non valutato.
- Il comportamento implementato non ha criterio di accettazione.

## Principi di prodotto

- Graph non deve indovinare a ogni costo.
- L'utente deve percepire controllo, non magia opaca.
- Un foglio ambiguo deve produrre una scelta guidata, non un grafico silenziosamente sbagliato.
- La preview dei dati interpretati e' parte della fiducia, non un dettaglio accessorio.
- Le assunzioni del sistema devono essere visibili o ispezionabili.

## Pipeline di riferimento

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
- assunzioni.

## Definition of Done SDD

Un lavoro funzionale e' chiuso solo se:

- punta a una specifica;
- dichiara criteri di accettazione;
- registra assunzioni e rischi nuovi;
- aggiorna ADR o registri se prende decisioni importanti;
- aggiunge test o verifica manuale proporzionata;
- aggiorna `AI-LEDGER.md` se scopre una recidiva possibile.

## Criteri di accettazione

- La costituzione descrive contesto, fatti, assunzioni, rischi e segnali di stop.
- La pipeline di riferimento e' esplicita.
- La Definition of Done vieta lavoro funzionale non collegato a specifica.
- I principi del README sono preservati.

