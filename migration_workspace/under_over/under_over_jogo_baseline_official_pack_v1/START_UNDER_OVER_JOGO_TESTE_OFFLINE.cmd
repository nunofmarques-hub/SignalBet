@echo off
setlocal

title SignalBet - Under/Over Jogo - Primeiro Teste Offline

echo ===============================================
echo  SignalBet / Under-Over Jogo
echo  Primeiro teste offline da baseline congelada
echo ===============================================
echo.

set SCRIPT=test_under_over_jogo_offline.py

if not exist "%SCRIPT%" (
    echo [ERRO] Nao foi encontrado o ficheiro %SCRIPT%
    echo.
    echo Cria primeiro o script de teste offline na mesma pasta deste .cmd
    echo e depois volta a correr este launcher.
    echo.
    pause
    exit /b 1
)

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
echo Instala Python ou garante que o comando "py" ou "python" esta disponivel.
echo.
pause
exit /b 1
