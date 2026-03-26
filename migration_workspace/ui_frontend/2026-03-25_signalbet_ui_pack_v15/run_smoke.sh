#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
for f in README.md manifest.json src/index.html src/js/services/runtimeBridgeService.js docs/ui_real_bridge_scope.md docs/ui_mock_scope.md docs/ui_bridge_limits.md docs/ui_real_read_expansion_plan.md; do
  test -f "$ROOT/$f"
done
python "$ROOT/tests/test_structure.py"
echo SMOKE_OK_UI_V15
