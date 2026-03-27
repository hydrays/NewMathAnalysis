@echo off
setlocal
set PORT=8123
if not "%~1"=="" set PORT=%~1

cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    echo Serving skill_tree at http://localhost:%PORT%/
    py -m http.server %PORT%
    exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
    echo Serving skill_tree at http://localhost:%PORT%/
    python -m http.server %PORT%
    exit /b %errorlevel%
)

echo Python was not found. Install Python, or use VS Code Live Server.
exit /b 1
