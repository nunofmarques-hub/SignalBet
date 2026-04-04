@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Trunk Collect Standings
echo ============================================
echo.

python -c "from data_api.collectors.collect_standings import collect_standings; r=collect_standings(140, 2024); print(r)"
if errorlevel 1 (
  echo.
  echo [ERRO] O collect_standings do tronco terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Trunk collect standings concluido.
pause
