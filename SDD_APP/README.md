# Graph ODE SDD_APP

Rilascio locale `v0.1.0` generato dalla SDD di Graph.

L'app legge file Excel elastici, identifica celle candidate per equazioni differenziali, parametri e condizioni iniziali, produce interpretazioni tracciabili, risolve con SymPy, salva un grafico quando sicuro e usa Ollama `phi4-mini` solo per spiegare il risultato.

## Installazione

```powershell
cd C:\Users\dell\Desktop\Projects\Graph
python -m pip install -r .\SDD_APP\requirements.txt
```

## Esempio rapido

```powershell
python .\SDD_APP\examples\create_sample_workbook.py
python .\SDD_APP\run_graph_ode.py --input .\SDD_APP\examples\sample_ode.xlsx --sheet "Caso ODE" --output .\SDD_APP\outputs\sample --no-ollama --no-pause
```

Corpus iniziale SDD `CASE-ODE-001..012`:

```powershell
python .\SDD_APP\examples\create_reference_workbooks.py
```

Con Ollama attivo e `phi4-mini` installato:

```powershell
python .\SDD_APP\run_graph_ode.py --input .\SDD_APP\examples\sample_ode.xlsx --sheet "Caso ODE" --output .\SDD_APP\outputs\sample_phi4 --no-pause
```

## Artefatti obbligatori del run

Ogni esecuzione scrive nella cartella di output:

- `workbook_scan.json`
- `candidate_blocks.json`
- `interpretations.json`
- `selected_interpretation.json`
- `solve_result.json`
- `run_report.json`
- `report.md`
- `plot.png`, se il grafico e' matematicamente sicuro

## Regole di sicurezza matematica

- SymPy e' la fonte della soluzione.
- `phi4-mini` non decide la soluzione, la spiega soltanto.
- Se un parametro richiesto manca, il run si ferma.
- Se due parametri hanno valori incompatibili, il run si ferma.
- Se piu' interpretazioni sono plausibili, serve `--select-interpretation` o `--confirm-low-confidence`.
- Il grafico non viene generato quando la soluzione contiene simboli liberi.

## Test

```powershell
cd C:\Users\dell\Desktop\Projects\Graph\SDD_APP
python -m unittest discover -s tests
```
