param(
    [int]$Port = 8123
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path

try {
    Push-Location $root

    if (Get-Command py -ErrorAction SilentlyContinue) {
        Write-Host "Serving skill_tree at http://localhost:$Port/"
        py -m http.server $Port
    } elseif (Get-Command python -ErrorAction SilentlyContinue) {
        Write-Host "Serving skill_tree at http://localhost:$Port/"
        python -m http.server $Port
    } else {
        Write-Error "Python was not found. Install Python, or use VS Code Live Server."
        exit 1
    }
} finally {
    Pop-Location
}
