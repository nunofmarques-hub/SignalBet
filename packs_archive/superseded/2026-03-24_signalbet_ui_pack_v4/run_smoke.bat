@echo off
set ROOT=%~dp0
if not exist "%ROOT%src\index.html" (
  echo [FAIL] index.html nao encontrado em src/
  exit /b 1
)
if not exist "%ROOT%manifest.json" (
  echo [FAIL] manifest.json nao encontrado
  exit /b 1
)
if not exist "%ROOT%data\mock-data.js" (
  echo [FAIL] mock-data.js nao encontrado
  exit /b 1
)
echo [OK] Estrutura base encontrada
echo [OK] Pack pronto para abrir no browser
