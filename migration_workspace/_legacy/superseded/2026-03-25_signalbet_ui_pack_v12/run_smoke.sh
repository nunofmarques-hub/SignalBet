#!/usr/bin/env bash
set -e
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
for f in README.md manifest.json pack_check_report.txt src/index.html src/js/app.js src/js/providers/providerRegistry.js src/js/adapters/orchestratorAdapters.js src/js/services/systemSnapshotService.js src/js/viewmodels/homeViewModel.js; do
  if [ ! -f "$ROOT_DIR/$f" ]; then
    echo "SMOKE FAIL: missing $f"
    exit 1
  fi
done
echo "SMOKE OK: structure present"
