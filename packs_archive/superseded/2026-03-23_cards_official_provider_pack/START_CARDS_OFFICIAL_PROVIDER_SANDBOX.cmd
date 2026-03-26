@echo off
cd /d "%~dp0"
python run_cards_official_provider_demo.py
if errorlevel 1 pause
pause
