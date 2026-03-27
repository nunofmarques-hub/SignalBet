#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
python3 src/real_data_calibration_runner.py
