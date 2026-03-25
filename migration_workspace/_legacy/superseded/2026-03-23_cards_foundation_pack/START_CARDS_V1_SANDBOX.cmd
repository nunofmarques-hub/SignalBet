@echo off
cd /d "%~dp0"
if exist python\python.exe (
  python\python.exe run_cards_demo.py
) else (
  python run_cards_demo.py
)
pause
