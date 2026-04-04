@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Smoke Test BTTS
echo ============================================
echo.

python smoke_test_btts_from_trunk.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do BTTS terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do BTTS concluido.
pause
