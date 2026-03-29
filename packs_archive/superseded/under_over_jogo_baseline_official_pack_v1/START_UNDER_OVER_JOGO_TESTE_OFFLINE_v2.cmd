@echo off
setlocal

title SignalBet - Under/Over Jogo - Primeiro Teste Offline

echo ===============================================
echo  SignalBet / Under-Over Jogo
echo  Primeiro teste offline da baseline congelada
echo ===============================================
echo.

set SCRIPT=test_under_over_jogo_offline.py

if exist "%SCRIPT%" goto RUN_LOCAL

if exist "under_over_jogo_baseline_official_pack_v1\%SCRIPT%" (
    cd /d "under_over_jogo_baseline_official_pack_v1"
    goto RUN_LOCAL
)

echo [ERRO] Nao foi encontrado o ficheiro %SCRIPT%
echo.
echo Coloca este .cmd:
echo - na mesma pasta do test_under_over_jogo_offline.py
echo ou
echo - ao lado da pasta under_over_jogo_baseline_official_pack_v1
echo.
pause
exit /b 1

:RUN_LOCAL
where py >nul 2>nul
if %errorlevel%==0 (
    echo [OK] A correr com: py -3 "%SCRIPT%"
    echo.
    py -3 "%SCRIPT%"
    echo.
    pause
    exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
    echo [OK] A correr com: python "%SCRIPT%"
    echo.
    python "%SCRIPT%"
    echo.
    pause
    exit /b %errorlevel%
)

echo [ERRO] Python nao foi encontrado no sistema.
echo.
pause
exit /b 1
