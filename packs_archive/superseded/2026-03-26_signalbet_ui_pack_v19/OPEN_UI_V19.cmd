@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo   SIGNALBET - OPEN UI V19
echo ==========================================
echo.

set UI_ROOT=U:\Users\genuser\Desktop\SignalBet\migration_workspace\ui_frontend
set PACK_DIR=

for /d %%D in ("%UI_ROOT%\*v19*" "%UI_ROOT%\*V19*" "%UI_ROOT%\*Nineteenth*" "%UI_ROOT%\*2026-03-26*") do (
    set PACK_DIR=%%~fD
)

if "%PACK_DIR%"=="" (
    echo ERRO: Nao encontrei automaticamente a pasta do pack v19.
    echo Verifica dentro de:
    echo %UI_ROOT%
    goto :end
)

if not exist "%PACK_DIR%\src\index.html" (
    echo ERRO: Nao encontrei:
    echo %PACK_DIR%\src\index.html
    goto :end
)

echo PACK_DIR=%PACK_DIR%
echo A abrir index.html...
start "" "%PACK_DIR%\src\index.html"

:end
pause
exit /b 0