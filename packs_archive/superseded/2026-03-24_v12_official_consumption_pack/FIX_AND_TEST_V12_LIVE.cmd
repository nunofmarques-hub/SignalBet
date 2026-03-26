@echo off
setlocal

REM =========================
REM CONFIG
REM =========================
set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet
set TRUNK_ROOT=%PROJECT_ROOT%\data_api\Data_API_Official_Trunk_v1
set PACK_DIR=%PROJECT_ROOT%\migration_workspace\v12\2026-03-24_v12_official_consumption_pack

REM Escolhe um team_id real do trunk
set REAL_TEAM_ID=529

echo ==========================================
echo   SIGNALBET - V12 FIX AND LIVE TEST
echo ==========================================
echo.

echo [1/7] A verificar Python...
python --version
if errorlevel 1 (
    echo ERRO: Python nao encontrado no PATH.
    pause
    exit /b 1
)

echo.
echo [2/7] A verificar trunk root...
if not exist "%TRUNK_ROOT%\data_api" (
    echo ERRO: Nao encontrei a pasta data_api em:
    echo %TRUNK_ROOT%\data_api
    pause
    exit /b 1
)

echo.
echo [3/7] A definir PYTHONPATH...
set PYTHONPATH=%TRUNK_ROOT%;%PACK_DIR%

echo PROJECT_ROOT=%PROJECT_ROOT%
echo TRUNK_ROOT=%TRUNK_ROOT%
echo PACK_DIR=%PACK_DIR%
echo PYTHONPATH=%PYTHONPATH%
echo REAL_TEAM_ID=%REAL_TEAM_ID%

echo.
echo [4/7] A testar imports do trunk...
python -c "from data_api.services.fixtures_service import get_fixtures_by_league_season; from data_api.services.standings_service import get_standings_snapshot; from data_api.services.statistics_service import get_team_statistics, get_fixture_statistics; print('TRUNK_IMPORT_OK')"
if errorlevel 1 (
    echo ERRO: O import dos services do trunk falhou.
    pause
    exit /b 1
)

echo.
echo [5/7] A confirmar cobertura real do team_id...
python -c "from data_api.services.statistics_service import get_team_statistics; import json; data=get_team_statistics(%REAL_TEAM_ID%,140,2024); print('TEAM_STATS_OK' if data else 'TEAM_STATS_EMPTY')"
if errorlevel 1 (
    echo ERRO: Falha ao validar team statistics.
    pause
    exit /b 1
)

echo.
echo [6/7] A localizar referencias antigas ao team_id 33...
powershell -NoProfile -Command "Get-ChildItem -Path '%PACK_DIR%' -Recurse -File | Select-String -Pattern '\b33\b' | ForEach-Object { $_.Path + ':' + $_.LineNumber + ' -> ' + $_.Line }"

echo.
echo [7/7] INSTRUCAO:
echo Se vires o team_id 33 em smoke_test.py ou noutro ficheiro de cenario live,
echo troca-o por %REAL_TEAM_ID% e depois corre:
echo.
echo   python motor\smoke_test.py --mode live --league 140 --season 2024
echo.
echo Para facilitar, vou abrir a pasta do pack e o smoke_test.py se existir.
if exist "%PACK_DIR%\motor\smoke_test.py" (
    start "" notepad "%PACK_DIR%\motor\smoke_test.py"
)
start "" "%PACK_DIR%"

pause
exit /b 0