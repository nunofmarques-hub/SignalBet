@echo off
setlocal
cd /d "%~dp0"

set "PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet"

if not exist "%PROJECT_ROOT%" (
    echo [ERRO] PROJECT_ROOT nao existe:
    echo %PROJECT_ROOT%
    pause
    exit /b 1
)

if not exist "src\app_orch\run_baseline_control.py" (
    echo [ERRO] Coloca este .cmd na raiz do pack OR12 extraido.
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
    echo [ERRO] Nao encontrei Python.
    pause
    exit /b 1
)

%PYTHON_CMD% -c "import sys; from pathlib import Path; root = Path('.').resolve(); sys.path.insert(0, str((root / 'src').resolve())); from app_orch.run_baseline_control import run; result = run(project_root=r'%PROJECT_ROOT%', out_dir='runtime_outputs'); print('run_ok=1'); print('readiness_level=' + str(result['summary']['readiness_level'])); print('cta_state=' + str(result['summary']['cta_state'])); print('source_mode=' + str(result['summary']['source_mode'])); print('observed_mode=' + str(result['button_payload']['observed_mode'])); print('bridge_status=' + str(result['button_payload']['bridge_status'])); print('snapshot_name=' + str(result['summary']['snapshot_name'])); print('final_status=' + str(result['summary']['final_status']))"

echo.
echo Ficheiros gerados em:
echo %CD%\runtime_outputs
echo.
pause
endlocal
