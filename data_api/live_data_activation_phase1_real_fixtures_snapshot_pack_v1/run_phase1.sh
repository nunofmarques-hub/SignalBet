#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 src/phase1_real_fixtures_snapshot.py
