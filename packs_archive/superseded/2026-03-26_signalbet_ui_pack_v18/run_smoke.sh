#!/usr/bin/env bash
set -e
python3 tests/test_structure.py
printf 'SMOKE_OK_UI_V18\n'
