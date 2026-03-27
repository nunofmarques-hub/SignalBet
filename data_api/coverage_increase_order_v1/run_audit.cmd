@echo off
setlocal
set SCRIPT_DIR=%~dp0
set DEFAULT_TRUNK=U:\Users\genuser\Desktop\SignalBet\data_api\Data_API_Official_Trunk_v1
python "%SCRIPT_DIR%src\audit_fixture_catalog_coverage.py" --trunk-root "%DEFAULT_TRUNK%"
if errorlevel 1 (
  echo "[ERRO] Coverage audit terminou com erro."
  pause
  exit /b 1
)
echo "[OK] Coverage audit terminado."
pause
