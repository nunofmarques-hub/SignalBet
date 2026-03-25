@echo off
setlocal

REM Raiz do projeto
set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet

REM Pasta do pack Corners
set PACK_DIR=%PROJECT_ROOT%\migration_workspace\corners\2026-03-25_corners_functional_proof_pack_v2_medium_fix

echo ==========================================
echo   SIGNALBET - CORNERS SMOKE TEST
echo ==========================================
echo.

echo [1/4] A verificar Python...
python --version
if errorlevel 1 (
    echo ERRO: Python nao encontrado no PATH.
    pause
    exit /b 1
)

echo.
echo [2/4] A verificar pack Corners...
if not exist "%PACK_DIR%\run_smoke.py" (
    echo ERRO: Nao encontrei run_smoke.py em:
    echo %PACK_DIR%\run_smoke.py
    pause
    exit /b 1
)

echo.
echo [3/4] A correr smoke do Corners...
cd /d "%PACK_DIR%"
python run_smoke.py
if errorlevel 1 (
    echo ERRO: O smoke do Corners falhou.
    pause
    exit /b 1
)

echo.
echo [4/4] Teste concluido.
echo Confirma agora no terminal e/ou outputs:
echo - forte = candidate
echo - medio = watchlist
echo - rejeitado = rejected
echo.

if exist examples start "" "examples"

pause
exit /b 0