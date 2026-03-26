@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Collect Team Statistics Sample
echo ============================================
echo.

python -c "from data_api.collectors.collect_team_statistics import collect_team_statistics; r=collect_team_statistics(140, 2024, 10); print(r)"
if errorlevel 1 (
  echo.
  echo [ERRO] O collect_team_statistics terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Collect team statistics concluido.
pause
