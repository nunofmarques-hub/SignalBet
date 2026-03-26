@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo SignalBet / ABC PRO - Corners Master 2024
echo ============================================
echo.

if not exist "..\data_api_football" (
    echo ERRO: nao foi encontrada a pasta ..\data_api_football
    echo Corre primeiro o pipeline base ou usa o pack com dados.
    pause
    exit /b 1
)

python build_true_corners_master_2024.py --root ..
if errorlevel 1 (
    echo.
    echo [ERRO] O processo de Cantos terminou com erro.
    pause
    exit /b %errorlevel%
)

echo.
echo [OK] Corners master gerado.
pause
