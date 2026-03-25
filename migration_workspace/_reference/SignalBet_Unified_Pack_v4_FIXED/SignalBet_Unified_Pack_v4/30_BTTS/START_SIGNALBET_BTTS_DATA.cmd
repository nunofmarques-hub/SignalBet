@echo off
setlocal
cd /d "%~dp0"

if not exist "..\api.env.txt" (
  echo [ERRO] Nao encontrei ..\api.env.txt
  echo Coloca a tua chave no ficheiro api.env.txt na raiz do pack.
  pause
  exit /b 2
)

python signalbet_btts_data_collector.py full-bootstrap --root .. --league 140 --season 2024 --status FT-AET-PEN
if errorlevel 1 (
  echo [ERRO] O coletor BTTS terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Coletor BTTS concluido.
pause
