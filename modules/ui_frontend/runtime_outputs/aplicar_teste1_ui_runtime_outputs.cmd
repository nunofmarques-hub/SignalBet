@echo off
setlocal

echo ==========================================
echo SignalBet UI - Aplicar TESTE 1 (runtime_outputs)
echo ==========================================

if not exist "app_phase1_protected_payload.json" (
  echo [ERRO] Nao encontrei app_phase1_protected_payload.json nesta pasta.
  pause
  exit /b 1
)

if not exist "app_phase1_protected_payload_TESTE1.json" (
  echo [ERRO] Nao encontrei app_phase1_protected_payload_TESTE1.json nesta pasta.
  pause
  exit /b 1
)

echo [1/3] A criar backup do payload atual...
copy /Y "app_phase1_protected_payload.json" "app_phase1_protected_payload_backup.json" >nul
if errorlevel 1 (
  echo [ERRO] Falhou o backup do payload atual.
  pause
  exit /b 1
)

echo [2/3] A aplicar payload do TESTE 1...
copy /Y "app_phase1_protected_payload_TESTE1.json" "app_phase1_protected_payload.json" >nul
if errorlevel 1 (
  echo [ERRO] Falhou a copia do payload do TESTE 1.
  pause
  exit /b 1
)

echo [3/3] A correr run_smoke.bat na pasta acima...
if exist "..\run_smoke.bat" (
  pushd ..
  call "run_smoke.bat"
  popd
) else (
  echo [AVISO] ..\run_smoke.bat nao encontrado.
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
