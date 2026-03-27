#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$SCRIPT_DIR/src/audit_fixture_catalog_coverage.py" --trunk-root "${1:-$PWD}"
