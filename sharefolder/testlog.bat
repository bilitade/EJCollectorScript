@echo off
set "folderPath=C:\backupej"
set "shareName=EeJLOGS"

:: Check if the script is running as an administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Script must be run as administrator. Please run the batch file as an administrator and try again.
    exit /b 1
)

:: Check if the share already exists
net share %shareName% >nul 2>&1
if %errorLevel% equ 0 (
    echo Share '%shareName%' already exists. Exiting.
    exit /b 1
)

:: Create a new share
net share %shareName%=%folderPath% /grant:Everyone,FULL
if %errorLevel% neq 0 (
    echo Error creating the share.
    exit /b 1
)

:: Set NTFS permissions on the folder
icacls %folderPath% /grant Everyone:(OI)(CI)R
if %errorLevel% neq 0 (
    echo Error setting NTFS permissions.
    exit /b 1
)

echo Folder '%folderPath%' has been shared as '%shareName%' with Everyone having Full access.
exit /b 0
