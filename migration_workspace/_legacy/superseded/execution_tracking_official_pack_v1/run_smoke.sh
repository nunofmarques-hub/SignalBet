#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 src/execution_smoke.py
