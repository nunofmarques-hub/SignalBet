@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Trunk Collect Events Sample
echo ============================================
echo.

python -c "from data_api.collectors.collect_events import collect_events; r=collect_events(140, 2024, 10); print(r)"
if errorlevel 1 (
  echo.
  echo [ERRO] O collect_events do tronco terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Trunk collect events concluido.
pause
