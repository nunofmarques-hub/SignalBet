@echo off
setlocal
cd /d "%~dp0"

python bootstrap_integration_check.py
if errorlevel 1 (
  echo.
  echo [ERRO] O integration check terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Integration check concluido.
pause
