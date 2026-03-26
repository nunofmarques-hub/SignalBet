@echo off
setlocal
cd /d "%~dp0"

python src\cards_trunk_smoke.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do Cards terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do Cards concluido.
pause
