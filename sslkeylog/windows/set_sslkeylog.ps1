# PowerShell script to set SSLKEYLOGFILE for the current session
# Usage: .\set_sslkeylog.ps1 [log_file]

param(
    [string]$LogFile = "$env:USERPROFILE\sslkeylog.log"
)
$env:SSLKEYLOGFILE = $LogFile
Write-Output "SSLKEYLOGFILE set to $env:SSLKEYLOGFILE"
