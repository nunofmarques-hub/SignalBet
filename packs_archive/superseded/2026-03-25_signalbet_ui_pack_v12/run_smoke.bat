@echo off
set ROOT_DIR=%~dp0
for %%F in (README.md manifest.json pack_check_report.txt src\index.html src\js\app.js src\js\providers\providerRegistry.js src\js\adapters\orchestratorAdapters.js src\js\services\systemSnapshotService.js src\js\viewmodels\homeViewModel.js) do (
  if not exist "%ROOT_DIR%%%F" (
    echo SMOKE FAIL: missing %%F
    exit /b 1
  )
)
echo SMOKE OK: structure present
