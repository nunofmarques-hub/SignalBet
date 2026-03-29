@echo off
setlocal EnableExtensions EnableDelayedExpansion

REM ============================================================
REM SignalBet / ABC PRO
REM SHADOW RUN PONTA A PONTA - VERSAO ADAPTADA AO REPO
REM ============================================================
REM OBJETIVO
REM   Executar um shadow run curto e controlado do corredor:
REM   Data/API -> Orchestrator -> Modulos -> GPS -> Banca -> Execution -> UI
REM
REM COMO USAR
REM   1) Colocar este .cmd na raiz do projeto SignalBet
REM   2) Rever a secção "MAPEAMENTO DOS SCRIPTS"
REM   3) Ajustar apenas os scripts que faltarem
REM   4) Correr o .cmd e rever o log/resultados
REM
REM RESULTADO FINAL
REM   GREEN  = corredor correu sem falha estrutural
REM   YELLOW = corredor correu com warnings/reservas
REM   RED    = falha estrutural num step critico
REM ============================================================

cd /d "%~dp0"

REM ------------------------------------------------------------
REM DETECAO DE RAIZ / PASTAS PRINCIPAIS
REM ------------------------------------------------------------
set ROOT_DIR=%CD%
set LOG_DIR=%ROOT_DIR%\logs\shadow_run
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

set RUN_ID=%DATE:~-4%%DATE:~3,2%%DATE:~0,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set RUN_ID=%RUN_ID: =0%

set LOG_FILE=%LOG_DIR%\shadow_run_%RUN_ID%.log
set RESULT_FILE=%LOG_DIR%\shadow_run_result_%RUN_ID%.txt

set DATA_API_ROOT=%ROOT_DIR%\data_api\Data_API_Official_Trunk_v1
set APP_CORE_ROOT=%ROOT_DIR%\app_core
set MODULES_ROOT=%ROOT_DIR%\modules
set MIGRATION_ROOT=%ROOT_DIR%\migration_workspace

set HAS_WARNING=0
set HAS_ERROR=0

call :log ============================================================
call :log SHADOW RUN START
call :log ROOT_DIR=%ROOT_DIR%
call :log RUN_ID=%RUN_ID%
call :log DATA_API_ROOT=%DATA_API_ROOT%
call :log APP_CORE_ROOT=%APP_CORE_ROOT%
call :log MODULES_ROOT=%MODULES_ROOT%
call :log MIGRATION_ROOT=%MIGRATION_ROOT%
call :log ============================================================

if not exist "%DATA_API_ROOT%" (
    call :log ERRO: nao encontrei data_api\Data_API_Official_Trunk_v1
    goto :hard_fail
)

REM ------------------------------------------------------------
REM PRE-CHECKS DE ESTRUTURA
REM ------------------------------------------------------------
if not exist "%APP_CORE_ROOT%" call :warn "app_core nao encontrado na raiz. Rever estrutura real."
if not exist "%MODULES_ROOT%" call :warn "modules nao encontrado na raiz. Rever estrutura real."
if not exist "%MIGRATION_ROOT%" call :warn "migration_workspace nao encontrado na raiz. Rever estrutura real."

REM ============================================================
REM MAPEAMENTO DOS SCRIPTS
REM ============================================================
REM REGRAS
REM  - Ajustar apenas os caminhos do lado direito
REM  - Usar comandos completos (python <script>.py ...)
REM  - Se um step nao tiver script proprio ainda, apontar para um smoke/check existente
REM
REM DATA/API
REM  A estrutura real observada confirma:
REM    data_api\Data_API_Official_Trunk_v1\data_api\...
REM
REM  SUGESTAO:
REM    criar/usar um script curto de shadow run na raiz do trunk
REM    ou usar um script de smoke/readiness existente
REM ============================================================

REM -------- Data/API Layer --------
set DATA_API_CMD=python "%DATA_API_ROOT%\run_shadow_data_api.py"

REM -------- Orchestrator / App Core --------
set ORCHESTRATOR_CMD=python "%APP_CORE_ROOT%\orchestrator\run_shadow_orchestrator.py"

REM -------- Modulos integrados --------
set V12_CMD=python "%MODULES_ROOT%\v12\run_shadow_v12.py"
set CARDS_CMD=python "%MODULES_ROOT%\cards\run_smoke.py"
set BTTS_CMD=python "%MODULES_ROOT%\btts\src\btts\run_minimal_flow.py"
set CORNERS_CMD=python "%MODULES_ROOT%\corners\run_smoke.py"

REM -------- Camadas centrais --------
set GPS_CMD=python "%MODULES_ROOT%\gps\run_shadow_gps.py"
set BANK_CMD=python "%MODULES_ROOT%\bankroll\run_shadow_bankroll.py"
set EXEC_CMD=python "%MODULES_ROOT%\execution\run_shadow_execution.py"

REM -------- UI --------
set UI_CMD=python "%MODULES_ROOT%\ui\run_shadow_ui_check.py"

REM ============================================================
REM NOTAS IMPORTANTES
REM ============================================================
REM 1) Se alguns destes scripts ainda nao existirem:
REM    - criar wrappers muito curtos com esse nome
REM    - cada wrapper deve:
REM         a) consumir o artefacto esperado da camada anterior
REM         b) validar input minimo
REM         c) gerar output/snapshot minimo
REM         d) devolver exit 0 quando OK
REM         e) devolver exit 1 quando houver falha estrutural
REM
REM 2) Para o shadow run inicial, basta 1 script por camada.
REM    Nao precisas de grande engenharia aqui.
REM
REM 3) Se a tua estrutura real estiver em migration_workspace e nao em modules,
REM    troca "%MODULES_ROOT%\..." por "%MIGRATION_ROOT%\...".
REM ============================================================

REM ------------------------------------------------------------
REM 1. Data/API
REM ------------------------------------------------------------
call :run_step "Data/API Layer" "%DATA_API_CMD%"
if errorlevel 1 goto :hard_fail

REM ------------------------------------------------------------
REM 2. Orchestrator
REM ------------------------------------------------------------
call :run_step "Orchestrator / App Core" "%ORCHESTRATOR_CMD%"
if errorlevel 1 goto :hard_fail

REM ------------------------------------------------------------
REM 3. Modulos integrados
REM ------------------------------------------------------------
call :run_step "Modulo v12" "%V12_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Modulo Cards" "%CARDS_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Modulo BTTS" "%BTTS_CMD%"
if errorlevel 1 goto :hard_fail

call :run_step "Modulo Corners" "%CORNERS_CMD%"
if errorlevel 1 goto :hard_fail

REM ------------------------------------------------------------
REM 4. GPS
REM ------------------------------------------------------------
call :run_step "GPS / Global Pick Selector" "%GPS_CMD%"
if errorlevel 1 goto :hard_fail

REM ------------------------------------------------------------
REM 5. Banca
REM ------------------------------------------------------------
call :run_step "Bankroll / Banca" "%BANK_CMD%"
if errorlevel 1 goto :hard_fail

REM ------------------------------------------------------------
REM 6. Execution
REM ------------------------------------------------------------
call :run_step "Execution / Tracking" "%EXEC_CMD%"
if errorlevel 1 goto :hard_fail

REM ------------------------------------------------------------
REM 7. UI
REM ------------------------------------------------------------
call :run_step "UI / Frontend check" "%UI_CMD%"
if errorlevel 1 (
    call :warn "UI check falhou. Corredor tecnico pode estar OK, mas a camada visivel precisa de revisao."
)

REM ------------------------------------------------------------
REM RESULTADO FINAL
REM ------------------------------------------------------------
if "%HAS_ERROR%"=="1" goto :hard_fail
if "%HAS_WARNING%"=="1" goto :yellow
goto :green

:green
call :log ============================================================
call :log SHADOW RUN RESULT = GREEN
call :log Corredor ponta a ponta correu sem falha estrutural.
call :log ============================================================
> "%RESULT_FILE%" echo SHADOW RUN RESULT = GREEN
exit /b 0

:yellow
call :log ============================================================
call :log SHADOW RUN RESULT = YELLOW
call :log Corredor correu, mas houve warnings/reservas a rever.
call :log ============================================================
> "%RESULT_FILE%" echo SHADOW RUN RESULT = YELLOW
exit /b 0

:hard_fail
set HAS_ERROR=1
call :log ============================================================
call :log SHADOW RUN RESULT = RED
call :log Corredor interrompido por falha estrutural ou step critico.
call :log ============================================================
> "%RESULT_FILE%" echo SHADOW RUN RESULT = RED
exit /b 1

REM ============================================================
REM FUNCOES AUXILIARES
REM ============================================================

:run_step
set STEP_NAME=%~1
set STEP_CMD=%~2

call :log ------------------------------------------------------------
call :log STEP START: %STEP_NAME%
call :log CMD: %STEP_CMD%

cmd /c %STEP_CMD% >> "%LOG_FILE%" 2>&1
set STEP_EXIT=%ERRORLEVEL%

if not "%STEP_EXIT%"=="0" (
    call :log STEP FAIL: %STEP_NAME% (exit=%STEP_EXIT%)
    exit /b 1
)

call :log STEP OK: %STEP_NAME%
exit /b 0

:warn
set HAS_WARNING=1
call :log WARNING: %~1
exit /b 0

:log
echo %~1
>> "%LOG_FILE%" echo %~1
exit /b 0
