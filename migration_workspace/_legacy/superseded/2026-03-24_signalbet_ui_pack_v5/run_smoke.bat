@echo off
set ROOT=%~dp0
echo [SMOKE] UI Frontend SignalBet v5
if not exist "%ROOT%README.md" goto fail
if not exist "%ROOT%manifest.json" goto fail
if not exist "%ROOT%src\index.html" goto fail
if not exist "%ROOT%src\styles\main.css" goto fail
if not exist "%ROOT%src\js\app.js" goto fail
if not exist "%ROOT%data\mock-data.js" goto fail
echo All required files exist.
echo Open src\index.html in a browser to verify navigation and states.
goto :eof
:fail
echo Missing required file.
exit /b 1
