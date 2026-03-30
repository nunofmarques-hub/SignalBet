@echo off
setlocal
cd /d "%~dp0"

python trunk_check.py
if errorlevel 1 (
  echo.
  echo [ERRO] O trunk_check terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Trunk check concluido.
pause
