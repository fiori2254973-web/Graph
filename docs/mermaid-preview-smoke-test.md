# Mermaid Preview Smoke Test

Questo file serve a verificare se la preview Markdown di VS Code renderizza Mermaid nel workspace.

```mermaid
flowchart TD
  A[Markdown file] --> B[VS Code Markdown Preview]
  B --> C[Markdown Preview Mermaid Support]
  C --> D[SVG visibile]
```

Se questo diagramma appare e poi scompare, il problema e' nella preview/CSS/estensione, non nel documento `PP5-CONTATORE.mapping.md`.
