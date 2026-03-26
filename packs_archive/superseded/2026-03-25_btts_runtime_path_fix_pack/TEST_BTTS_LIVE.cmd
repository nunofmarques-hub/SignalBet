@echo off
setlocal

REM Raiz do projeto
set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet

REM Raiz do trunk que contém o pacote Python "data_api"
set TRUNK_ROOT=%PROJECT_ROOT%\data_api\Data_API_Official_Trunk_v1

REM Pasta do pack BTTS
set PACK_DIR=U:\Users\genuser\Desktop\SignalBet\migration_workspace\btts\2026-03-25_btts_runtime_path_fix_pack

echo ==========================================
echo   SIGNALBET - BTTS LIVE TEST
echo ==========================================
echo.

echo [1/6] A verificar Python...
python --version
if errorlevel 1 (
    echo ERRO: Python nao encontrado no PATH.
    pause
    exit /b 1
)

echo.
echo [2/6] A verificar trunk root...
if not exist "%TRUNK_ROOT%\data_api" (
    echo ERRO: Nao encontrei a pasta data_api em:
    echo %TRUNK_ROOT%\data_api
    pause
    exit /b 1
)

echo.
echo [3/6] A verificar pack BTTS...
if not exist "%PACK_DIR%\src\btts\run_minimal_flow.py" (
    echo ERRO: Nao encontrei o run_minimal_flow.py em:
    echo %PACK_DIR%\src\btts\run_minimal_flow.py
    pause
    exit /b 1
)

echo.
echo [4/6] A definir PYTHONPATH...
set PYTHONPATH=%TRUNK_ROOT%;%PACK_DIR%

echo PROJECT_ROOT=%PROJECT_ROOT%
echo TRUNK_ROOT=%TRUNK_ROOT%
echo PACK_DIR=%PACK_DIR%
echo PYTHONPATH=%PYTHONPATH%

echo.
echo [5/6] A testar imports do trunk...
python -c "from data_api.services.fixtures_service import get_fixtures_by_league_season; from data_api.services.events_service import get_fixture_events; from data_api.services.statistics_service import get_fixture_statistics, get_team_statistics; from data_api.services.standings_service import get_standings_snapshot; print('TRUNK_IMPORT_OK')"
if errorlevel 1 (
    echo ERRO: O import dos services do trunk falhou.
    pause
    exit /b 1
)

echo.
echo [6/6] A correr fluxo minimo BTTS...
cd /d "%PACK_DIR%"
python -m src.btts.run_minimal_flow
if errorlevel 1 (
    echo ERRO: O run_minimal_flow falhou.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo TESTE LIVE BTTS CONCLUIDO
echo ==========================================
echo Verifica agora o output final.
if exist sample_output start "" "sample_output"

pause
exit /b 0