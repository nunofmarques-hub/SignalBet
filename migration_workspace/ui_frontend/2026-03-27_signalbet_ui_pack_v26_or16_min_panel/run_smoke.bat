@echo off
setlocal
echo [UI] run_smoke.bat
if exist runtime_outputs\app_phase1_protected_payload.json (
  echo [OK] runtime_outputs\app_phase1_protected_payload.json encontrado
  echo [OK] src\index.html encontrado
  exit /b 0
) else (
  echo [FAIL] payload protegido nao encontrado
  exit /b 1
)
