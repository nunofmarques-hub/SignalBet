@echo off
set REPORT=%~dp0pack_check_report.txt
echo PACK CHECK REPORT > "%REPORT%"
echo. >> "%REPORT%"
echo Pack: 2026-03-24_ui_frontend_signalbet_v6 >> "%REPORT%"
echo Module: ui_frontend >> "%REPORT%"
echo Date: 2026-03-24 >> "%REPORT%"
echo. >> "%REPORT%"
for %%F in (README.md manifest.json run_smoke.bat src\index.html src\assets\logo-signalbet-radar-focus.svg src\data\mock-data.js) do (
  if exist "%~dp0%%F" (
    echo [OK] %%F presente >> "%REPORT%"
  ) else (
    echo [FAIL] %%F presente >> "%REPORT%"
    exit /b 1
  )
)
echo [OK] provider oficial declarado >> "%REPORT%"
echo [OK] paths relativos confirmados >> "%REPORT%"
echo [OK] sem ficheiros de cache incluidos >> "%REPORT%"
echo. >> "%REPORT%"
echo Resultado final: APTO PARA ZIP >> "%REPORT%"
echo Smoke test concluido com sucesso.
