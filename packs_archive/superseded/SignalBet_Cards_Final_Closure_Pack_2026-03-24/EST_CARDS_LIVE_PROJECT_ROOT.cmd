@echo off
setlocal

REM Raiz do projeto
set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet

REM Raiz do trunk que contém a pasta Python "data_api"
set TRUNK_ROOT=%PROJECT_ROOT%\data_api\Data_API_Official_Trunk_v1

REM Pasta do pack Cards
set PACK_DIR=%PROJECT_ROOT%\migration_workspace\cards\SignalBet_Cards_Final_Closure_Pack_2026-03-24

echo ==========================================
echo   SIGNALBET - CARDS LIVE TEST
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
echo [3/6] A definir PYTHONPATH...
set PYTHONPATH=%TRUNK_ROOT%

echo PROJECT_ROOT=%PROJECT_ROOT%
echo TRUNK_ROOT=%TRUNK_ROOT%
echo PACK_DIR=%PACK_DIR%
echo PYTHONPATH=%PYTHONPATH%

echo.
echo [4/6] A testar import do trunk...
python -c "from data_api.services.fixtures_service import get_fixtures_by_league_season; from data_api.services.events_service import get_fixture_events; print('TRUNK_IMPORT_OK')"
if errorlevel 1 (
    echo ERRO: O import dos services do trunk falhou.
    pause
    exit /b 1
)

echo.
echo [5/6] A correr smoke basico...
cd /d "%PACK_DIR%"
python run_smoke.py
if errorlevel 1 (
    echo ERRO: O smoke basico falhou.
    pause
    exit /b 1
)

echo.
echo [6/6] A correr smoke live...
python run_smoke.py --mode live --league 140 --season 2024
if errorlevel 1 (
    echo ERRO: O smoke live falhou.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo TESTE LIVE CONCLUIDO COM SUCESSO
echo ==========================================
echo Verifica agora a pasta out\
if exist out start "" "out"

pause
exit /b 0