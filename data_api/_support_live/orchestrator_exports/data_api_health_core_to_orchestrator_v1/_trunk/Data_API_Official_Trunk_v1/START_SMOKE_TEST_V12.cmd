@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Smoke Test V12
echo ============================================
echo.

python smoke_test_v12_from_trunk.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do v12 terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do v12 concluido.
pause
