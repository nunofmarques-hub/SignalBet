#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 src/build_execution_fixture_payload.py
