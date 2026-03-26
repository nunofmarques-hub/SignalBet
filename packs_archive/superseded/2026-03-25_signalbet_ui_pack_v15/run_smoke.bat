@echo off
python tests	est_structure.py
if errorlevel 1 exit /b 1
echo SMOKE_OK_UI_V15
