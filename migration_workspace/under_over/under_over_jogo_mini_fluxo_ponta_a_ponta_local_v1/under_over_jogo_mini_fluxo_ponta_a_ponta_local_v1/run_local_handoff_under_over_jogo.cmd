@echo off
setlocal
title SignalBet - Under/Over Jogo - Mini Fluxo Local Ponta a Ponta
cd /d "%~dp0"

if not exist "src\run_local_handoff_under_over_jogo.py" (
    echo [ERRO] Nao foi encontrado src\run_local_handoff_under_over_jogo.py
    pause
    exit /b 1
)

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "src\run_local_handoff_under_over_jogo.py"
    echo.
    pause
    exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
    python "src\run_local_handoff_under_over_jogo.py"
    echo.
    pause
    exit /b %errorlevel%
)

echo [ERRO] Python nao encontrado.
pause
exit /b 1
