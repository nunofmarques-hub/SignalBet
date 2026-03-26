@echo off
cd /d %~dp0
python signalbet_btts_data_collector.py full-bootstrap --league 140 --season 2024 --status FT-AET-PEN
pause
