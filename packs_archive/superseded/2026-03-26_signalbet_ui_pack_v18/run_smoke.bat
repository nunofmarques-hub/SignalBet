@echo off
python tests\test_structure.py
if %errorlevel% neq 0 exit /b %errorlevel%
echo SMOKE_OK_UI_V18
