@echo off
setlocal
cd /d "%~dp0"

python src\execution_smoke.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test da Execution terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test da Execution concluido.
pause
