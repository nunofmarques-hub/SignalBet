@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Trunk Collect Fixture Statistics Sample
echo ============================================
echo.

python -c "from data_api.collectors.collect_fixture_statistics import collect_fixture_statistics; r=collect_fixture_statistics(140, 2024, 10); print(r)"
if errorlevel 1 (
  echo.
  echo [ERRO] O collect_fixture_statistics do tronco terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Trunk collect fixture statistics concluido.
pause
