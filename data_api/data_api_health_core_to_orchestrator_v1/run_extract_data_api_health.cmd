@echo off
setlocal
cd /d "%~dp0"
python src\extract_data_api_health.py
if errorlevel 1 (
  echo [ERRO] data_api_health_core_to_orchestrator_v1 terminou com erro.
  exit /b 1
)
echo [OK] data_api_health_core_to_orchestrator_v1 terminou com sucesso.
