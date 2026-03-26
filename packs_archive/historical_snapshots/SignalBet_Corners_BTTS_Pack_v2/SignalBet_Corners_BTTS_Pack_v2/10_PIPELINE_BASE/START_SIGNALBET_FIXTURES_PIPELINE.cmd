@echo off
setlocal
cd /d "%~dp0"

if not exist api.env.txt (
  echo [ERRO] Nao encontrei api.env.txt ao lado deste ficheiro.
  echo Cria um ficheiro com: API_KEY=...
  exit /b 2
)

python signalbet_fixtures_pipeline.py full-bootstrap
if errorlevel 1 (
  echo [ERRO] O pipeline terminou com erro.
  exit /b %errorlevel%
)

echo.
echo [OK] Pipeline concluido.
pause
