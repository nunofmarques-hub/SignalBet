#!/usr/bin/env bash
set -e
python3 tests/test_structure.py > pack_check_report.txt
printf "smoke_ok
" >> pack_check_report.txt
