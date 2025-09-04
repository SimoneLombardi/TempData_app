@echo off
title Avvio Programma Python

:: --- Rileva architettura sistema ---
set ARCH=x64
if "%PROCESSOR_ARCHITECTURE%"=="x86" (
    if not defined PROCESSOR_ARCHITEW6432 (
        set ARCH=x86
    )
)

echo [INFO] Sistema rilevato: %ARCH%

:: --- Definisci versione Python consigliata ---
set PYTHON_VERSION=3.12.5

if "%ARCH%"=="x64" (
    set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
) else (
    set PYTHON_INSTALLER=python-%PYTHON_VERSION%.exe
)

set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%

:: --- Controllo se Python è già installato ---
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRORE] Python non trovato sul sistema!
    echo Scarica e installa Python %PYTHON_VERSION% da:
    echo %PYTHON_URL%
    pause
    exit /b
)

:: --- Aggiorna pip e installa pacchetti richiesti ---
echo Controllo e installazione pacchetti richiesti...
python -m pip install --upgrade pip
python -m pip install pytz pandas matplotlib numpy

:: --- Avvia il programma principale ---
echo Avvio programma...
python main.py

pause
exit /b
