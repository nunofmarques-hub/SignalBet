@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Smoke Test Cards
echo ============================================
echo.

python smoke_test_cards_from_trunk.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do Cards terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do Cards concluido.
pause
