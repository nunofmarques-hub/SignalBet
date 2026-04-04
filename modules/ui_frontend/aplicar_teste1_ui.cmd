@echo off
setlocal

echo ==========================================
echo SignalBet UI - Aplicar TESTE 1
echo ==========================================

if not exist "runtime_outputs\app_phase1_protected_payload.json" (
  echo [ERRO] Nao encontrei runtime_outputs\app_phase1_protected_payload.json
  pause
  exit /b 1
)

if not exist "app_phase1_protected_payload_TESTE1.json" (
  echo [ERRO] Nao encontrei app_phase1_protected_payload_TESTE1.json na pasta atual
  echo Coloca este ficheiro ao lado deste CMD e volta a correr.
  pause
  exit /b 1
)

echo [1/3] A criar backup do payload atual...
copy /Y "runtime_outputs\app_phase1_protected_payload.json" "runtime_outputs\app_phase1_protected_payload_backup.json" >nul
if errorlevel 1 (
  echo [ERRO] Falhou o backup do payload atual.
  pause
  exit /b 1
)

echo [2/3] A aplicar payload do TESTE 1...
copy /Y "app_phase1_protected_payload_TESTE1.json" "runtime_outputs\app_phase1_protected_payload.json" >nul
if errorlevel 1 (
  echo [ERRO] Falhou a copia do payload do TESTE 1.
  pause
  exit /b 1
)

echo [3/3] A correr run_smoke.bat...
if exist "run_smoke.bat" (
  call "run_smoke.bat"
) else (
  echo [AVISO] run_smoke.bat nao encontrado nesta pasta.
)

echo.
echo ==========================================
echo TESTE 1 aplicado.
echo Agora abre a app e confirma:
echo - Roma vs Lecce
echo - Under 3.5 Goals
echo - APPROVED
echo - 1.00u
echo - ROMA_LECCE_U35_T1
echo ==========================================
pause
