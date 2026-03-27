#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TRUNK_ROOT="$SCRIPT_DIR/_trunk/Data_API_Official_Trunk_v1"
python "$SCRIPT_DIR/src/fixture_statistics_context_runner.py" "$TRUNK_ROOT"
echo "[OK] fixture_statistics_context_activation_v1 terminada com sucesso."
