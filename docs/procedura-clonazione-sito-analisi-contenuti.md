# Procedura SDD leggera per clonare un sito e analizzarne i contenuti HTML

## Scopo

Definire un approccio prudente per creare una copia locale di un sito web autorizzato e analizzarne i contenuti HTML con strumenti Python.

Questa procedura non serve a copiare aree private, aggirare protezioni, ignorare limiti del sito o replicare codice server. Serve a raccogliere pagine pubbliche o autorizzate per analisi testuale, inventario dei contenuti, controllo link, studio della struttura informativa o migrazione documentale.

## Fatti noti

- WinHTTrack e' la versione Windows di HTTrack Website Copier.
- HTTrack crea una copia locale navigabile di pagine e asset pubblicamente raggiungibili.
- HTTrack non scarica database, backend, codice server, contenuti dietro login o contenuti caricati solo tramite API non catturate.
- I file HTML clonati possono essere analizzati con BeautifulSoup.
- Scrapy e' piu' adatto quando l'obiettivo e' crawling strutturato e ripetibile.
- Playwright e' piu' adatto quando il contenuto appare solo dopo esecuzione JavaScript nel browser.

## Assunzioni

- Il sito e' dell'utente oppure l'utente ha autorizzazione esplicita ad analizzarlo.
- L'analisi riguarda contenuti pubblici o comunque permessi.
- Il clone locale viene usato per studio, inventario o migrazione, non per ripubblicazione non autorizzata.
- La copia deve essere limitata al dominio e al perimetro deciso prima dell'esecuzione.

## Domande aperte

- Qual e' il dominio o sottodominio esatto da analizzare?
- Quante pagine ci si aspetta di scaricare?
- Il sito e' statico, CMS classico, SPA JavaScript o area autenticata?
- L'obiettivo e' estrarre testo, link, immagini, metadati, tabelle o struttura di navigazione?
- Esistono termini d'uso, `robots.txt`, sitemap o policy interne da rispettare?

## Segnali di stop

Fermarsi prima di clonare quando:

- il sito non e' proprio e manca autorizzazione;
- il sito richiede login, paywall o aggiramento di restrizioni;
- `robots.txt` o termini d'uso vietano il crawling richiesto;
- il numero di pagine o asset e' ignoto e potenzialmente molto alto;
- il sito contiene dati personali o sensibili non necessari all'obiettivo;
- il clone richiederebbe carichi aggressivi sul server;
- l'obiettivo reale e' replicare il sito, non analizzarne contenuti autorizzati.

## Sei cappelli per pensare

### Fatti

- HTTrack e WinHTTrack sono strumenti pensati per creare mirror locali di siti.
- HTTrack documenta l'uso di meta tag e `robots.txt` come segnali per indicare cosa i programmi automatici dovrebbero visitare o evitare.
- BeautifulSoup serve a estrarre dati da HTML e XML gia' disponibili.
- Scrapy e' un framework di crawling e scraping per estrarre dati strutturati.
- Playwright automatizza browser reali ed e' utile quando il contenuto dipende da JavaScript.

### Rischi e criticita'

- Scaricare troppo puo' caricare inutilmente il server.
- Un clone puo' includere dati non necessari o sensibili.
- Alcuni siti generano URL infiniti tramite filtri, calendari, ricerca o parametri.
- HTTrack puo' non catturare contenuti generati via JavaScript.
- BeautifulSoup vede solo cio' che e' presente nei file HTML salvati.
- Una copia locale puo' essere scambiata erroneamente per autorizzazione alla ripubblicazione.

### Opportunita'

- Il clone locale rende l'analisi ripetibile e non dipendente dalla rete.
- Separare download e parsing riduce richieste ripetute al sito.
- BeautifulSoup permette estrazioni semplici e leggibili.
- Una procedura SDD rende chiari perimetro, limiti, output e verifica.
- Il risultato puo' diventare un inventario: titoli, URL, heading, link, immagini, file mancanti, parole chiave.

### Percezione ed emozioni

- L'utente vuole controllo e ispezionabilita', non una scatola nera.
- Il rischio percepito e' fare "troppo" senza accorgersene: troppe pagine, troppi file, troppi dati.
- Una procedura a fasi riduce ansia operativa: prima perimetro, poi clone piccolo, poi analisi.

### Alternative e lenti multiprospettiche

| Scenario | Strumento consigliato | Motivo |
| --- | --- | --- |
| Sito statico o CMS semplice | WinHTTrack / HTTrack | Crea mirror locale navigabile. |
| File HTML gia' disponibili | BeautifulSoup | Analisi semplice dei contenuti salvati. |
| Estrazione strutturata su molte pagine | Scrapy | Pipeline, spider, esportazione dati. |
| Sito con contenuti renderizzati da JavaScript | Playwright | Esegue il browser prima di leggere la pagina. |
| Solo elenco URL ufficiale | Sitemap XML + script Python | Meno invasivo del crawling completo. |

### Decisioni e regia

Approccio raccomandato:

1. Definire autorizzazione, dominio, obiettivo e limiti.
2. Fare un clone pilota piccolo con WinHTTrack.
3. Analizzare i file HTML clonati con BeautifulSoup.
4. Passare a Scrapy solo se serve crawling ripetibile e strutturato.
5. Passare a Playwright solo se il contenuto non compare nell'HTML statico.
6. Conservare log, comandi e risultati in una cartella dedicata.

## Second pass - hardening

### Rischi aggiunti dopo revisione critica

- Parametri URL come `?page=`, `?sort=`, `?search=` possono creare esplosione del crawling.
- Pagine calendario, tag, ricerca interna e filtri possono produrre molte varianti quasi duplicate.
- Asset pesanti come video, archivi e PDF possono rendere il clone enorme.
- Alcuni link esterni possono portare HTTrack fuori perimetro se i filtri non sono stretti.
- Salvare una copia locale puo' introdurre obblighi di protezione se contiene dati personali.

### Contromisure obbligatorie

- Usare una allowlist di dominio e sottopercorsi.
- Impostare profondita' ridotta nel clone pilota.
- Escludere file pesanti se non necessari.
- Non disattivare il rispetto di `robots.txt`.
- Evitare pagine di login, ricerca interna, checkout, account, admin e parametri non necessari.
- Salvare il clone in una cartella nominata con dominio e data.
- Annotare comando, data, perimetro, esclusioni e motivo dell'analisi.
- Verificare un campione prima di lanciare un clone piu' ampio.

### Criteri di accettazione hardening

- Il perimetro e' scritto prima del download.
- Il primo clone riguarda un campione piccolo.
- Il clone non esce dal dominio previsto.
- L'analisi non richiede credenziali.
- I dati estratti sono solo quelli necessari.
- I log permettono di ricostruire cosa e' stato scaricato e perche'.

## Procedura operativa

### 1. Definire la mini-specifica

Scrivere in un file o ticket:

```markdown
## Obiettivo
Estrarre da `https://example.com/` titoli, heading, link interni e testo principale.

## Perimetro
- Dominio: `example.com`
- Percorsi inclusi: `/docs/`, `/blog/`
- Percorsi esclusi: `/login`, `/account`, `/search`, `/cart`

## Output atteso
- `pages.csv` con URL locale, titolo, H1, conteggio link.
- `links.csv` con link sorgente, link destinazione, testo ancora.

## Limiti
- Nessun login.
- Nessun bypass di restrizioni.
- Nessun download di video o archivi.
```

### 2. Installare WinHTTrack su Windows

Con `winget`:

```powershell
winget install --id XavierRoche.HTTrack
```

Oppure scaricare l'installer ufficiale dalla pagina download di HTTrack.

### 3. Eseguire un clone pilota

Con interfaccia grafica:

1. Aprire WinHTTrack.
2. Creare un nuovo progetto.
3. Scegliere una cartella locale dedicata, per esempio `data/cloni/example-2026-07-17`.
4. Inserire l'URL iniziale.
5. Limitare dominio, profondita' e tipi file.
6. Avviare un primo clone piccolo.
7. Aprire `index.html` locale e controllare che le pagine attese siano presenti.

Da riga di comando, esempio prudente:

```powershell
httrack "https://example.com/" -O "data\cloni\example-2026-07-17" -s2 -r3
```

Nota: adattare URL, profondita' e filtri al perimetro autorizzato. Non usare opzioni pensate per ignorare `robots.txt` o restrizioni del sito.

### 4. Analizzare i file HTML con BeautifulSoup

Installazione:

```powershell
python -m pip install beautifulsoup4 lxml
```

Esempio di analisi locale:

```python
from pathlib import Path
from bs4 import BeautifulSoup

root = Path("data/cloni/example-2026-07-17")

for html_file in root.rglob("*.html"):
    html = html_file.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "lxml")

    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    h1 = soup.find("h1")
    h1_text = h1.get_text(" ", strip=True) if h1 else ""

    print(html_file, title, h1_text)
```

### 5. Scegliere quando cambiare strumento

Usare Scrapy quando:

- servono spider ripetibili;
- l'output deve essere CSV/JSON strutturato;
- servono pipeline di pulizia;
- i selettori HTML diventano molti.

Usare Playwright quando:

- l'HTML salvato non contiene i dati visibili nel browser;
- il contenuto appare solo dopo JavaScript;
- serve attendere caricamenti dinamici prima dell'estrazione.

## Schema sintetico

```text
autorizzazione
  -> mini-specifica
  -> clone pilota limitato
  -> controllo manuale campione
  -> parsing BeautifulSoup
  -> esportazione dati
  -> verifica output
  -> estensione controllata del perimetro
```

## Checklist prima del clone

- Ho autorizzazione sul sito.
- Ho letto termini d'uso o vincoli noti.
- Ho controllato `robots.txt` quando applicabile.
- Ho definito dominio e percorsi ammessi.
- Ho escluso login, account, ricerca interna e aree non necessarie.
- Ho deciso quali dati estrarre.
- Ho scelto una cartella locale dedicata.
- Ho previsto un clone pilota prima del clone completo.

## Checklist dopo il clone

- Il clone resta nel perimetro.
- La dimensione locale e' ragionevole.
- Le pagine campione sono navigabili offline.
- Non sono presenti dati sensibili non necessari.
- BeautifulSoup trova gli elementi attesi.
- Gli output sono riproducibili.
- I comandi e le impostazioni usate sono documentati.

## Fonti

- HTTrack Website Copier: https://www.httrack.com/
- HTTrack User Guide: https://www.httrack.com/html/fcguide.html
- Beautiful Soup documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
- Scrapy documentation: https://docs.scrapy.org/
- Playwright documentation: https://playwright.dev/
