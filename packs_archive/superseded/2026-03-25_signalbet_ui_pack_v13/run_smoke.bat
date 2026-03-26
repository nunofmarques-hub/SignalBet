@echo off
python tests\test_structure.py
IF %ERRORLEVEL% NEQ 0 EXIT /B %ERRORLEVEL%
echo SMOKE_OK
