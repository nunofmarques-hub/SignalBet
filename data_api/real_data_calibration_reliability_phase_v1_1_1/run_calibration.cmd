@echo off
setlocal
cd /d "%~dp0"
python src\real_data_calibration_runner.py
if errorlevel 1 (
  echo.
  echo [ERRO] Real Data Calibration and Reliability Phase terminou com erro.
  pause
  exit /b 1
)
echo.
echo [OK] Real Data Calibration and Reliability Phase terminou com sucesso.
pause
