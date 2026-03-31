#!/usr/bin/env bash
set -e
echo "[UI] run_smoke.sh"
test -f runtime_outputs/app_phase1_protected_payload.json
test -f src/index.html
echo "[OK] payload protegido e index encontrados"
