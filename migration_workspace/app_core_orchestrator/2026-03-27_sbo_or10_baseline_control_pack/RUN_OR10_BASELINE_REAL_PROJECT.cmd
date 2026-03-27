@echo off
setlocal

REM OR10 baseline control runner against a real project root
REM Uso:
REM 1) Extrair o pack OR10
REM 2) Colocar este ficheiro .cmd na raiz do pack extraido
REM 3) Editar a linha PROJECT_ROOT abaixo
REM 4) Fazer duplo clique

cd /d "%~dp0"

set "PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet"
set "BASELINE_PATH="

if not exist "src\app_orch\run_baseline_control.py" (
    echo [ERRO] Nao encontrei src\app_orch\run_baseline_control.py na pasta atual.
    echo Coloca este ficheiro .cmd na raiz do pack OR10 extraido.
    pause
    exit /b 1
)

if not exist "%PROJECT_ROOT%" (
    echo [ERRO] PROJECT_ROOT nao existe:
    echo %PROJECT_ROOT%
    echo.
    echo Edita o ficheiro .cmd e corrige a linha:
    echo set "PROJECT_ROOT=..."
    pause
    exit /b 1
)

set "PYTHON_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PYTHON_CMD=py"
if not defined PYTHON_CMD (
    where python >nul 2>nul
    if %errorlevel%==0 set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    echo [ERRO] Nao encontrei Python no sistema.
    pause
    exit /b 1
)

if defined BASELINE_PATH (
    %PYTHON_CMD% -c "import sys; from pathlib import Path; sys.path.insert(0, str(Path('src').resolve())); from app_orch.run_baseline_control import run; result = run(project_root=r'%PROJECT_ROOT%', baseline_path=r'%BASELINE_PATH%', out_dir='runtime_outputs'); print('run_ok=1'); print('readiness_level=' + str(result['summary']['readiness_level'])); print('cta_state=' + str(result['summary']['cta_state'])); print('source_mode=' + str(result['summary']['source_mode']))"
) else (
    %PYTHON_CMD% -c "import sys; from pathlib import Path; sys.path.insert(0, str(Path('src').resolve())); from app_orch.run_baseline_control import run; result = run(project_root=r'%PROJECT_ROOT%', out_dir='runtime_outputs'); print('run_ok=1'); print('readiness_level=' + str(result['summary']['readiness_level'])); print('cta_state=' + str(result['summary']['cta_state'])); print('source_mode=' + str(result['summary']['source_mode']))"
)

echo.
echo Ficheiros gerados em:
echo %CD%\runtime_outputs
echo.
echo Teste concluido.
pause
endlocal
