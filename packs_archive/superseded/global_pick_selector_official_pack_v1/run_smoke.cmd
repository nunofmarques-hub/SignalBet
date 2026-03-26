@echo off
setlocal
cd /d "%~dp0"

python src\gps_smoke.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do GPS terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do GPS concluido.
pause
