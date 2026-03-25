@echo off
python tests	est_structure.py > pack_check_report.txt
if errorlevel 1 exit /b 1
echo smoke_ok>>pack_check_report.txt
