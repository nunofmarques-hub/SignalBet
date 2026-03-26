#!/usr/bin/env bash
set -e
python3 tests/test_structure.py
printf 'SMOKE_OK\n'
