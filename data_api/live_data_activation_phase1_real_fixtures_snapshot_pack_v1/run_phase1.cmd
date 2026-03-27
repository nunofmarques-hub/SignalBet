@echo off
setlocal
cd /d "%~dp0"

python src\phase1_real_fixtures_snapshot.py
if errorlevel 1 (
  echo.
  echo [ERRO] Live Data Activation fase 1 terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Live Data Activation fase 1 concluida.
pause
