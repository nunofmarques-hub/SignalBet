@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Collect Fixtures
echo ============================================
echo.

python -c "from data_api.collectors.collect_fixtures import collect_fixtures; r=collect_fixtures(140, 2024, 'FT-AET-PEN'); print(r)"
if errorlevel 1 (
  echo.
  echo [ERRO] O collect_fixtures terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Collect fixtures concluido.
pause
