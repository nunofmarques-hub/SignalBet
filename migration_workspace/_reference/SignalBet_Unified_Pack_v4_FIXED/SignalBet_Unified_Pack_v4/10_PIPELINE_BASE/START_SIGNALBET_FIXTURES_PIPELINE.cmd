@echo off
setlocal
cd /d "%~dp0"

if not exist "..\api.env.txt" (
  echo [ERRO] Nao encontrei ..\api.env.txt
  echo Coloca a tua chave no ficheiro api.env.txt na raiz do pack.
  pause
  exit /b 2
)

python signalbet_fixtures_pipeline.py --root .. full-bootstrap
if errorlevel 1 (
  echo [ERRO] O pipeline terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Pipeline concluido.
pause
