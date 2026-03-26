#!/usr/bin/env bash
set -e
test -f README.md
test -f manifest.json
test -f src/index.html
test -f src/js/services/runtimeBridgeService.js
test -f src/js/providers/realOrchestratorProtectedProvider.js
test -f docs/ui_runtime_read_bridge.md
echo "SMOKE_OK_UI_V14"
