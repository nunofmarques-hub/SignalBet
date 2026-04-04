@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Trunk Collect Fixtures
echo ============================================
echo.

python -c "from data_api.collectors.collect_fixtures import collect_fixtures; r=collect_fixtures(140, 2024, 'FT-AET-PEN'); print(r)"
if errorlevel 1 (
  echo.
  echo [ERRO] O collect_fixtures do tronco terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Trunk collect fixtures concluido.
pause
