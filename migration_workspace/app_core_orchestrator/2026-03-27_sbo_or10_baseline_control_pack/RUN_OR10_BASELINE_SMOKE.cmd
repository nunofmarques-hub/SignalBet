@echo off
setlocal

REM OR10 baseline control smoke runner
REM Uso:
REM 1) Extrair o pack
REM 2) Colocar este ficheiro na raiz do pack extraído
REM 3) Fazer duplo clique

cd /d "%~dp0"

if not exist "run_smoke.py" (
    echo [ERRO] Nao encontrei run_smoke.py na pasta atual.
    echo Coloca este ficheiro .cmd na raiz do pack OR10 extraido.
    pause
    exit /b 1
)

where py >nul 2>nul
if %errorlevel%==0 (
    py run_smoke.py
    goto :end
)

where python >nul 2>nul
if %errorlevel%==0 (
    python run_smoke.py
    goto :end
)

echo [ERRO] Nao encontrei Python no sistema.
echo Instala Python ou usa o Python ja configurado no teu ambiente.
pause
exit /b 1

:end
echo.
echo Teste concluido.
pause
endlocal
