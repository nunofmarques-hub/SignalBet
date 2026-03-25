#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 src/gps_smoke.py
