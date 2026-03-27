#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 src/real_data_calibration_runner.py
