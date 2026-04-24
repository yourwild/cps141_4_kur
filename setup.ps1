$ErrorActionPreference = "Stop"

if (Get-Command py -ErrorAction SilentlyContinue) {
    py setup.py
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    python setup.py
}
else {
    Write-Host "❌ Python 3.11+ not found. Install Python and rerun setup."
    exit 1
}
