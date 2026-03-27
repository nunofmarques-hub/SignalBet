@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

python "%SCRIPT_DIR%src\real_data_calibration_runner.py"
if errorlevel 1 (
  echo [ERRO] Real Data Calibration and Reliability Phase terminou com erro.
  echo Press any key to continue . . .
  pause >nul
  exit /b 1
)

echo [OK] Real Data Calibration and Reliability Phase terminada com sucesso.
echo Press any key to continue . . .
pause >nul
exit /b 0
