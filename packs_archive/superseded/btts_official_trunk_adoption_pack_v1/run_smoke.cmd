@echo off
setlocal
cd /d "%~dp0"

python src\btts_trunk_smoke.py
if errorlevel 1 (
  echo.
  echo [ERRO] O smoke test do BTTS terminou com erro.
  pause
  exit /b %errorlevel%
)

echo.
echo [OK] Smoke test do BTTS concluido.
pause
