@echo off
setlocal EnableDelayedExpansion

:: Professional colors: black background, light gray text
color 07
title DozKooki YouTube Downloader

echo --------------------------------------------------------
echo    DozKooki YouTube Downloader & Converter - Launcher
echo --------------------------------------------------------
echo.

:: Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo ERROR: Python is not installed or not added to PATH.
    echo Please install Python 3.9 or higher from https://www.python.org.
    pause
    exit /b
)

:: Check if requirements are installed (simple yt-dlp check)
echo Verifying Python packages...
pip show yt-dlp >nul 2>&1
if errorlevel 1 (
    echo Dependencies not found. Installing from requirements.txt...
    pip install -r requirements.txt
)

:: Ready to run
echo.
echo All dependencies are installed.
echo --------------------------------------------------------
echo Starting DozKooki YouTube Downloader...
echo --------------------------------------------------------
echo.

python main.py

echo.
echo --------------------------------------------------------
echo DozKooki YouTube Downloader execution completed.
echo --------------------------------------------------------
pause
