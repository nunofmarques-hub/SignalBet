@echo off
setlocal
cd /d "%~dp0"

python src\bankroll_smoke.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test da banca terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test da banca concluido.
pause
