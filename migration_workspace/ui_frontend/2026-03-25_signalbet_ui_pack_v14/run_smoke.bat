@echo off
if not exist README.md exit /b 1
if not exist manifest.json exit /b 1
if not exist src\index.html exit /b 1
if not exist src\js\services\runtimeBridgeService.js exit /b 1
if not exist src\js\providers\realOrchestratorProtectedProvider.js exit /b 1
if not exist docs\ui_runtime_read_bridge.md exit /b 1
echo SMOKE_OK_UI_V14
