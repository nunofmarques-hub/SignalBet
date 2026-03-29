@echo off
setlocal
title SignalBet - Under/Over Jogo - Prototipo Offline Forte
cd /d "%~dp0"
if not exist "src\run_under_over_jogo_offline.py" (
    echo [ERRO] Nao foi encontrado src\run_under_over_jogo_offline.py
    pause
    exit /b 1
)
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "src\run_under_over_jogo_offline.py"
    echo.
    pause
    exit /b %errorlevel%
)
where python >nul 2>nul
if %errorlevel%==0 (
    python "src\run_under_over_jogo_offline.py"
    echo.
    pause
    exit /b %errorlevel%
)
echo [ERRO] Python nao encontrado.
pause
exit /b 1
