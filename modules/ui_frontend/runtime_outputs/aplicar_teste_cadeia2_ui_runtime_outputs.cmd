@echo off
setlocal

echo ==========================================
echo SignalBet UI - Aplicar TESTE DE CADEIA 2
echo ==========================================

if not exist "app_phase1_protected_payload.json" (
  echo [ERRO] Nao encontrei app_phase1_protected_payload.json nesta pasta.
  pause
  exit /b 1
)

if not exist "app_phase1_protected_payload_CADEIA2_PORTO_BRAGA.json" (
  echo [ERRO] Nao encontrei app_phase1_protected_payload_CADEIA2_PORTO_BRAGA.json nesta pasta.
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

echo [2/3] A aplicar payload do Teste de Cadeia 2...
copy /Y "app_phase1_protected_payload_CADEIA2_PORTO_BRAGA.json" "app_phase1_protected_payload.json" >nul
if errorlevel 1 (
  echo [ERRO] Falhou a copia do payload do Teste de Cadeia 2.
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
echo TESTE DE CADEIA 2 aplicado.
echo Confirmar na app:
echo - Porto vs Braga
echo - Over 4.5 Cards
echo - GPS-CARDS-220004-MCOV-001
echo - 1.00u
echo - OPEN / OPEN / UNSETTLED
echo ==========================================
pause
