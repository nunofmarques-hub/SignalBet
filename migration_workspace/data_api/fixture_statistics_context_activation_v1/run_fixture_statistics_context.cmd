@echo off
setlocal
set SCRIPT_DIR=%~dp0
set TRUNK_ROOT=%SCRIPT_DIR%_trunk\Data_API_Official_Trunk_v1

if not exist "%TRUNK_ROOT%" (
  echo [ERRO] Trunk nao encontrado em "%TRUNK_ROOT%"
  echo Coloca uma copia de Data_API_Official_Trunk_v1 dentro de _trunk\
  exit /b 1
)

python "%SCRIPT_DIR%src\fixture_statistics_context_runner.py" "%TRUNK_ROOT%"
if errorlevel 1 (
  echo [ERRO] fixture_statistics_context_activation_v1 terminou com erro.
  pause
  exit /b 1
)

echo [OK] fixture_statistics_context_activation_v1 terminada com sucesso.
pause
