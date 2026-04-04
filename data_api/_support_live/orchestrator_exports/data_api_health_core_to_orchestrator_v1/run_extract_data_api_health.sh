#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
python3 src/extract_data_api_health.py
