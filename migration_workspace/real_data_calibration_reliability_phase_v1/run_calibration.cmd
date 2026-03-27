@echo off
setlocal
cd /d "%~dp0"

python src\real_data_calibration_runner.py
if errorlevel 1 (
  echo.
  echo [ERRO] Real Data Calibration & Reliability Phase terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Real Data Calibration & Reliability Phase concluida.
pause
