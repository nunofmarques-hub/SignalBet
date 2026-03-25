#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 src/cards_trunk_smoke.py
