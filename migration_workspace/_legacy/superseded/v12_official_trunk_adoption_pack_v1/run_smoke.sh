#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 src/v12_trunk_smoke.py
