# Symposium LLM adapters

These adapters read a prompt from stdin and write only the model text to stdout.
They are intentionally small and use only the Python standard library.

They automatically load local secrets from:

```powershell
.symposium\secrets.env
```

Generate that file interactively:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\write-symposium-secrets.ps1
```

## Claude

Required environment variable:

```powershell
$env:ANTHROPIC_API_KEY = "..."
```

Optional:

```powershell
$env:CLAUDE_MODEL = "claude-sonnet-5"
```

Commands:

```powershell
python adapters/claude_adapter.py --self-test
"hello" | python adapters/claude_adapter.py
```

## Gemini

Required environment variable:

```powershell
$env:GEMINI_API_KEY = "..."
```

Optional:

```powershell
$env:GEMINI_MODEL = "gemini-3.5-flash"
```

Commands:

```powershell
python adapters/gemini_adapter.py --self-test
"hello" | python adapters/gemini_adapter.py
```

## Symposium integration

`symposium.py` auto-detects these built-in adapters for agents named `claude` and `gemini`.

```powershell
python symposium.py agent-adapters --agents codex,claude,gemini
python symposium.py agent-launch --agents claude,gemini
```

Use `--mock` only for local smoke tests. Mock output is not a real agent contribution.
