# Graph ODE Report `20260724_121137`

## Input
- File: `SDD_APP\examples\sample_ode.xlsx`
- Fogli scansionati: Secondo ordine
- Celle non vuote viste: 5

## Configurazione
- `scan_max_sheets`: `20`
- `scan_max_cells`: `20000`
- `cell_neighborhood_radius`: `2`
- `candidate_min_confidence`: `50`
- `auto_solve_confidence`: `80`
- `allow_hidden_sheets`: `False`
- `allow_formula_cells`: `True`
- `model_name`: `phi4-mini`
- `ollama_host`: `http://localhost:11434`
- `ollama_timeout`: `180`
- `plot_enabled`: `True`
- `plot_x_min`: `0.0`
- `plot_x_max`: `10.0`
- `plot_points`: `100`
- `show_plot`: `False`
- `pause_at_end`: `False`

## Blocchi candidati
- `B002` `equation` score `80` (alta) da Secondo ordine!B1: `Derivative(y(x), (x, 2)) + y(x) = 0`
- `B004` `initial_condition` score `65` (media) da Secondo ordine!B2: `y(0)=0`
- `B005` `initial_condition` score `65` (media) da Secondo ordine!B3: `y'(0)=1`

## Interpretazioni
- `I001` status `selected` score `90` decision_required `False` reason ``

## Interpretazione selezionata
- ID: `I001`
- Equazione: `Derivative(y(x), (x, 2)) + y(x) = 0`
- Parametri: `{}`
- Condizioni iniziali: `['y(0)=0', "y'(0)=1"]`

### Celle sorgente
- Secondo ordine!B1
- Secondo ordine!B2
- Secondo ordine!B3

## Risultato SymPy
- Status: `solved`
- Equazione normalizzata: `Derivative(y(x), (x, 2)) + y(x) = 0`
- Soluzione: `Eq(y(x), sin(x))`
- Verifica: `(True, 0)`
- Stop reason: `None`
- Errore: `None`
- Grafico: `SDD_APP\outputs\second_order\plot.png`

## Spiegazione phi4-mini
_Non generata._

## Warning
- Spiegazione Ollama disabilitata con --no-ollama.
