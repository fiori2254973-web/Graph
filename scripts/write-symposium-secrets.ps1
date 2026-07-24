param(
  [string]$Path = ".symposium\secrets.env"
)

$ErrorActionPreference = "Stop"

function Read-SecretPlainText([string]$Prompt) {
  $secure = Read-Host $Prompt -AsSecureString
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
  try {
    return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
  } finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
  }
}

function Escape-EnvValue([string]$Value) {
  return '"' + $Value.Replace('\', '\\').Replace('"', '\"') + '"'
}

$target = Join-Path (Get-Location) $Path
$dir = Split-Path -Parent $target
New-Item -ItemType Directory -Force $dir | Out-Null

$anthropic = Read-SecretPlainText "Anthropic API key"
$gemini = Read-SecretPlainText "Gemini API key"
$openai = Read-SecretPlainText "OpenAI API key"

$lines = @(
  "# Local secrets for Symposium adapters.",
  "# Generated locally by scripts/write-symposium-secrets.ps1.",
  "",
  "ANTHROPIC_API_KEY=$(Escape-EnvValue $anthropic)",
  "GEMINI_API_KEY=$(Escape-EnvValue $gemini)",
  "OPENAI_API_KEY=$(Escape-EnvValue $openai)",
  "",
  "CLAUDE_MODEL=claude-sonnet-5",
  "GEMINI_MODEL=gemini-3.5-flash",
  "CLAUDE_MAX_TOKENS=1200",
  "GEMINI_MAX_TOKENS=1200",
  "CLAUDE_TEMPERATURE=0.2",
  "GEMINI_TEMPERATURE=0.2"
)

Set-Content -LiteralPath $target -Value $lines -Encoding UTF8
Write-Host "[ok] secrets env scritto in $target"
