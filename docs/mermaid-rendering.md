# Mermaid Rendering In VS Code

## Problema osservato

I diagrammi Mermaid appaiono per una frazione di secondo nella Markdown Preview e poi scompaiono, soprattutto dopo un cambio tema.

## Causa rilevata

Questa installazione di VS Code contiene gia' un renderer Mermaid integrato:

- `mermaid-markdown-features`

In piu' e' installata l'estensione:

- `bierner.markdown-mermaid`

L'estensione di Bierner risulta `deprecated` nel suo `package.json`. Quando entrambi i renderer sono attivi, possono processare lo stesso blocco Markdown ` ```mermaid ` e produrre conflitti post-render.

## Decisione per questo workspace

Per Graph usare il renderer Mermaid integrato di VS Code e disabilitare `bierner.markdown-mermaid` almeno per questo workspace.

## Procedura

1. Aprire il pannello Extensions.
2. Cercare `Markdown Preview Mermaid Support`.
3. Selezionare l'estensione di Matt Bierner.
4. Usare `Disable (Workspace)` o `Disable`.
5. Eseguire `Developer: Reload Window`.
6. Aprire `docs/mermaid-preview-smoke-test.md`.
7. Eseguire `Markdown: Open Preview to the Side`.

## Diagnosi del flash seguito da occultamento

Se il diagramma appare per una frazione di secondo e poi scompare:

- se resta un riquadro tratteggiato vuoto, il renderer ha svuotato il container Mermaid durante il re-render;
- se resta spazio occupato ma non si legge nulla, il problema e' contrasto tra tema VS Code, tema Mermaid e CSS;
- se non resta neanche spazio, e' probabile un conflitto tra due renderer Mermaid attivi.

Il primo controllo resta disabilitare `bierner.markdown-mermaid` nel workspace, perche' VS Code include gia' `mermaid-markdown-features`.

## Impostazioni workspace

Il file `.vscode/settings.json` imposta:

- tema Mermaid adattivo VS Code per tema chiaro e scuro;
- resize e controlli disabilitati;
- CSS workspace per preservare visibilita' e contrasto.

## Regola

Non installare o attivare due renderer Mermaid Markdown nello stesso workspace.
