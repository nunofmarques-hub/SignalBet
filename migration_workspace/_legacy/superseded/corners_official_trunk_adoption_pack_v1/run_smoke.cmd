@echo off
setlocal
cd /d "%~dp0"

python src\corners_trunk_smoke.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do Corners terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do Corners concluido.
pause
