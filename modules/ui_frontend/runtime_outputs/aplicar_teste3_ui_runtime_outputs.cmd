@echo off
setlocal

echo ==========================================
echo SignalBet UI - Aplicar TESTE 3 (runtime_outputs)
echo ==========================================

if not exist "app_phase1_protected_payload.json" (
  echo [ERRO] Nao encontrei app_phase1_protected_payload.json nesta pasta.
  pause
  exit /b 1
)

if not exist "app_phase1_protected_payload_TESTE3.json" (
  echo [ERRO] Nao encontrei app_phase1_protected_payload_TESTE3.json nesta pasta.
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

echo [2/3] A aplicar payload do TESTE 3...
copy /Y "app_phase1_protected_payload_TESTE3.json" "app_phase1_protected_payload.json" >nul
if errorlevel 1 (
  echo [ERRO] Falhou a copia do payload do TESTE 3.
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
echo TESTE 3 aplicado.
echo Agora abre a app e confirma:
echo - Osasuna vs Girona
echo - Under 10.5 Corners
echo - APPROVED_REDUCED
echo - 0.50u
echo - OSASUNA_GIRONA_U105C_T3
echo ==========================================
pause
