@echo off
setlocal

set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet
set TRUNK_ROOT=%PROJECT_ROOT%\data_api\Data_API_Official_Trunk_v1
set PACK_DIR=%PROJECT_ROOT%\migration_workspace\app_core_orchestrator\sbo9

echo ==========================================
echo   SIGNALBET - ORCHESTRATOR REAL PROOF
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
echo [2/7] A verificar project_root...
if not exist "%PROJECT_ROOT%" (
    echo ERRO: PROJECT_ROOT nao encontrado:
    echo %PROJECT_ROOT%
    pause
    exit /b 1
)

echo.
echo [3/7] A verificar trunk root...
if not exist "%TRUNK_ROOT%\data_api" (
    echo ERRO: TRUNK_ROOT invalido:
    echo %TRUNK_ROOT%\data_api
    pause
    exit /b 1
)

echo.
echo [4/7] A verificar pack do Orchestrator...
if exist "%PACK_DIR%\run_real_proof.py" (
    set RUN_PROOF=run_real_proof.py
) else if exist "%PACK_DIR%\run_real_proof" (
    set RUN_PROOF=run_real_proof
) else (
    echo ERRO: Nao encontrei run_real_proof nem run_real_proof.py em:
    echo %PACK_DIR%
    pause
    exit /b 1
)

echo.
echo [5/7] A definir PYTHONPATH...
set PYTHONPATH=%TRUNK_ROOT%;%PACK_DIR%

echo PROJECT_ROOT=%PROJECT_ROOT%
echo TRUNK_ROOT=%TRUNK_ROOT%
echo PACK_DIR=%PACK_DIR%
echo PYTHONPATH=%PYTHONPATH%
echo RUN_PROOF=%RUN_PROOF%

echo.
echo [6/7] A correr prova real do Orchestrator...
cd /d "%PACK_DIR%"
python "%RUN_PROOF%" "%PROJECT_ROOT%"
if errorlevel 1 (
    echo.
    echo ERRO: A prova real do Orchestrator falhou.
    pause
    exit /b 1
)

echo.
echo [7/7] Prova concluida.
echo Verifica agora no output:
echo - project_mode
echo - preflight_status
echo - readiness_level
echo - cta_state
echo - modules_run
echo - module_feed_stats
echo.

if exist out start "" "out"

pause
exit /b 0