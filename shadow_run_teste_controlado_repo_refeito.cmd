@echo off
setlocal EnableExtensions EnableDelayedExpansion

REM ============================================================
REM SignalBet / ABC PRO
REM SHADOW RUN PONTA A PONTA - VERSAO REFEITA
REM ============================================================
REM Colocar este ficheiro na raiz do projeto SignalBet
REM
REM Fluxo:
REM   Data/API -> Orchestrator -> v12 -> Cards -> BTTS -> Corners
REM   -> GPS -> Banca -> Execution -> UI
REM
REM Resultado:
REM   GREEN / YELLOW / RED
REM ============================================================

cd /d "%~dp0"

set PYTHONPATH=U:\Users\genuser\Desktop\SignalBet\data_api\Data_API_Official_Trunk_v1;U:\Users\genuser\Desktop\SignalBet\data_api\Data_API_Official_Trunk_v1\data_api && python "U:\Users\genuser\Desktop\SignalBet\modules\v12\motor\smoke_test.py"

set ROOT_DIR=%CD%
set LOG_DIR=%ROOT_DIR%\logs\shadow_run
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

set RUN_ID=%DATE:~-4%%DATE:~3,2%%DATE:~0,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set RUN_ID=%RUN_ID: =0%

set LOG_FILE=%LOG_DIR%\shadow_run_%RUN_ID%.log
set RESULT_FILE=%LOG_DIR%\shadow_run_result_%RUN_ID%.txt

set DATA_API_ROOT=%ROOT_DIR%\data_api\Data_API_Official_Trunk_v1
set MODULES_ROOT=%ROOT_DIR%\modules
set MIGRATION_ROOT=%ROOT_DIR%\migration_workspace

set HAS_WARNING=0
set HAS_ERROR=0

call :log ============================================================
call :log SHADOW RUN START
call :log ROOT_DIR=%ROOT_DIR%
call :log RUN_ID=%RUN_ID%
call :log DATA_API_ROOT=%DATA_API_ROOT%
call :log MODULES_ROOT=%MODULES_ROOT%
call :log MIGRATION_ROOT=%MIGRATION_ROOT%
call :log LOG_FILE=%LOG_FILE%
call :log RESULT_FILE=%RESULT_FILE%
call :log ============================================================

if not exist "%DATA_API_ROOT%" (
    call :log ERRO: DATA_API_ROOT nao encontrado: %DATA_API_ROOT%
    goto :hard_fail
)

if not exist "%MODULES_ROOT%" (
    call :log ERRO: MODULES_ROOT nao encontrado: %MODULES_ROOT%
    goto :hard_fail
)

if not exist "%MIGRATION_ROOT%" (
    call :warn "MIGRATION_ROOT nao encontrado: %MIGRATION_ROOT%"
)

REM ============================================================
REM MAPEAMENTO DOS SCRIPTS
REM ============================================================

REM Data/API
set DATA_API_CMD=python "%DATA_API_ROOT%\run_shadow_data_api.py"

REM Orchestrator
set ORCHESTRATOR_CMD=python "%MIGRATION_ROOT%\app_core_orchestrator\2026-03-27_sbo_or16_protected_output_increment\run_smoke.py"

REM Modulos integrados
set V12_CMD=python "%MODULES_ROOT%\v12\motor\smoke_test.py"
set CARDS_CMD=python "%MODULES_ROOT%\cards\run_smoke.py"
set BTTS_CMD=python "%MODULES_ROOT%\btts\src\btts\run_minimal_flow.py"
set CORNERS_CMD=python "%MODULES_ROOT%\corners\run_smoke.py"

REM Camadas centrais
set GPS_CMD=python "%MODULES_ROOT%\gps\run_smoke.py"
set BANK_CMD=python "%MODULES_ROOT%\bankroll\run_smoke.py"
set EXEC_CMD=python "%MODULES_ROOT%\execution\run_smoke.py"

REM UI
set UI_CMD=call "%MIGRATION_ROOT%\ui_frontend\2026-03-27_signalbet_ui_pack_v26_or16_min_panel\2026-03-27_signalbet_ui_pack_v26_or12\run_smoke.bat"

call :log ---------------- SCRIPT MAP ----------------
call :log DATA_API_CMD=%DATA_API_CMD%
call :log ORCHESTRATOR_CMD=%ORCHESTRATOR_CMD%
call :log V12_CMD=%V12_CMD%
call :log CARDS_CMD=%CARDS_CMD%
call :log BTTS_CMD=%BTTS_CMD%
call :log CORNERS_CMD=%CORNERS_CMD%
call :log GPS_CMD=%GPS_CMD%
call :log BANK_CMD=%BANK_CMD%
call :log EXEC_CMD=%EXEC_CMD%
call :log UI_CMD=%UI_CMD%
call :log ------------------------------------------------

REM ============================================================
REM EXECUCAO
REM ============================================================

call :run_step "Data/API Layer" "%DATA_API_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Orchestrator / App Core" "%ORCHESTRATOR_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Modulo v12" "%V12_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Modulo Cards" "%CARDS_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Modulo BTTS" "%BTTS_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Modulo Corners" "%CORNERS_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "GPS / Global Pick Selector" "%GPS_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Bankroll / Banca" "%BANK_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Execution / Tracking" "%EXEC_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "UI / Frontend check" "%UI_CMD%"
if errorlevel 1 (
    call :warn "UI falhou. Corredor tecnico pode estar OK, mas a camada visivel precisa de revisao."
)

if "%HAS_ERROR%"=="1" goto :hard_fail
if "%HAS_WARNING%"=="1" goto :yellow
goto :green

:green
call :log ============================================================
call :log SHADOW RUN RESULT = GREEN
call :log Corredor ponta a ponta correu sem falha estrutural.
call :log ============================================================
> "%RESULT_FILE%" echo SHADOW RUN RESULT = GREEN
pause
exit /b 0

:yellow
call :log ============================================================
call :log SHADOW RUN RESULT = YELLOW
call :log Corredor correu, mas houve warnings/reservas a rever.
call :log ============================================================
> "%RESULT_FILE%" echo SHADOW RUN RESULT = YELLOW
pause
exit /b 0

:hard_fail
set HAS_ERROR=1
call :log ============================================================
call :log SHADOW RUN RESULT = RED
call :log Corredor interrompido por falha estrutural ou step critico.
call :log ============================================================
> "%RESULT_FILE%" echo SHADOW RUN RESULT = RED
pause
exit /b 1

REM ============================================================
REM FUNCOES
REM ============================================================

:run_step
set "STEP_NAME=%~1"
set "STEP_CMD=%~2"

call :log "------------------------------------------------------------"
call :log "STEP START: !STEP_NAME!"
call :log "STEP CMD  : !STEP_CMD!"

cmd /c !STEP_CMD! >> "%LOG_FILE%" 2>&1
set "STEP_EXIT=!ERRORLEVEL!"

if not "!STEP_EXIT!"=="0" (
    call :log "STEP FAIL : !STEP_NAME! (exit=!STEP_EXIT!)"
    exit /b 1
)

call :log "STEP OK   : !STEP_NAME!"
exit /b 0

:warn
set HAS_WARNING=1
call :log "WARNING   : %*"
exit /b 0

:log
echo %~1
>> "%LOG_FILE%" echo %~1
exit /b 0