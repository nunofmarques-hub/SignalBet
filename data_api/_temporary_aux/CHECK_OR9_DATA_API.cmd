@echo off
setlocal

set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet
set TRUNK_ROOT=%PROJECT_ROOT%\data_api\Data_API_Official_Trunk_v1

echo ==========================================
echo   SIGNALBET - CHECK OR9 DATA_API READINESS
echo ==========================================
echo.

echo [1/5] A verificar trunk root...
if not exist "%TRUNK_ROOT%" (
    echo FAIL - Trunk root nao encontrado:
    echo %TRUNK_ROOT%
    goto :end
) else (
    echo PASS - Trunk root encontrado
)

echo.
echo [2/5] A verificar providers registry literal...
set PROVIDERS_OK=0

if exist "%TRUNK_ROOT%\providers\providers.json" (
    echo PASS - Encontrado: %TRUNK_ROOT%\providers\providers.json
    set PROVIDERS_OK=1
)

if exist "%TRUNK_ROOT%\providers\registry.json" (
    echo PASS - Encontrado: %TRUNK_ROOT%\providers\registry.json
    set PROVIDERS_OK=1
)

if "%PROVIDERS_OK%"=="0" (
    echo FAIL - Nao encontrei nem providers.json nem registry.json em:
    echo %TRUNK_ROOT%\providers\
)

echo.
echo [3/5] A verificar contracts .json...
dir /b "%TRUNK_ROOT%\contracts\*.json" >nul 2>nul
if errorlevel 1 (
    echo FAIL - Nao encontrei .json em %TRUNK_ROOT%\contracts\
) else (
    echo PASS - Existe pelo menos 1 .json em contracts\
    dir /b "%TRUNK_ROOT%\contracts\*.json"
)

echo.
echo [4/5] A verificar services .json...
dir /b "%TRUNK_ROOT%\services\*.json" >nul 2>nul
if errorlevel 1 (
    echo WARN - Nao encontrei .json em %TRUNK_ROOT%\services\
) else (
    echo PASS - Existe pelo menos 1 .json em services\
    dir /b "%TRUNK_ROOT%\services\*.json"
)

echo.
echo [5/5] A verificar storage .json...
dir /b "%TRUNK_ROOT%\storage\*.json" >nul 2>nul
if errorlevel 1 (
    echo WARN - Nao encontrei .json em %TRUNK_ROOT%\storage\
) else (
    echo PASS - Existe pelo menos 1 .json em storage\
    dir /b "%TRUNK_ROOT%\storage\*.json"
)

echo.
echo ==========================================
echo CHECK CONCLUIDO
echo ==========================================
echo.
echo Leitura esperada para o OR9u2:
echo - providers.json ou registry.json = obrigatorio
echo - contracts com .json = obrigatorio
echo - services com .json = recomendado
echo - storage com .json = recomendado

:end
pause
exit /b 0