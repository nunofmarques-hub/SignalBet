@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Week1 Bootstrap Check
echo ============================================
echo.

python bootstrap_check.py
if errorlevel 1 (
  echo.
  echo [ERRO] O bootstrap_check terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Bootstrap check concluido.
pause
