@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Collect Standings
echo ============================================
echo.

python -c "from data_api.collectors.collect_standings import collect_standings; r=collect_standings(140, 2024); print(r)"
if errorlevel 1 (
  echo.
  echo [ERRO] O collect_standings terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Collect standings concluido.
pause
