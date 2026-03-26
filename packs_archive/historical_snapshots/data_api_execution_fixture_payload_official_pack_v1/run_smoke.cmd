@echo off
setlocal
cd /d "%~dp0"

python src\build_execution_fixture_payload.py
if errorlevel 1 (
  echo.
  echo [ERRO] A geracao do payload oficial de fixture terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Payload oficial de fixture gerado.
pause
