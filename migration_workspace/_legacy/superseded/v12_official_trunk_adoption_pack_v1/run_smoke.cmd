@echo off
setlocal
cd /d "%~dp0"

python src\v12_trunk_smoke.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do v12 terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do v12 concluido.
pause
