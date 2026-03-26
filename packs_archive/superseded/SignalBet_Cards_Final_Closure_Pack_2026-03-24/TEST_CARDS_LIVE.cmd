@echo off
setlocal

echo ==========================================
echo   SIGNALBET - CARDS LIVE TEST
echo ==========================================
echo.

REM Vai para a pasta onde está este .cmd
cd /d "%~dp0"

echo [1/4] A verificar Python...
python --version
if errorlevel 1 (
    echo.
    echo ERRO: Python nao encontrado no PATH.
    pause
    exit /b 1
)

echo.
echo [2/4] A correr smoke basico...
python run_smoke.py
if errorlevel 1 (
    echo.
    echo ERRO: O smoke basico falhou.
    pause
    exit /b 1
)

echo.
echo [3/4] A correr smoke live...
python run_smoke.py --mode live --league 140 --season 2024
if errorlevel 1 (
    echo.
    echo ERRO: O smoke live falhou.
    pause
    exit /b 1
)

echo.
echo [4/4] Teste concluido com sucesso.
echo Verifica agora:
echo - logs no terminal
echo - ficheiros gerados/atualizados em out\
echo - uso do official_live_provider
echo.

if exist out (
    echo A abrir pasta out...
    start "" "out"
)

pause
exit /b 0