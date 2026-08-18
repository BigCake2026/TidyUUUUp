[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$TargetPath,
    [Parameter(Mandatory = $true)][string]$ShortcutPath,
    [Parameter(Mandatory = $true)][string]$IconPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $TargetPath -PathType Leaf)) {
    throw "Target executable does not exist: $TargetPath"
}

$shortcutDirectory = Split-Path -Path $ShortcutPath -Parent
if (-not (Test-Path -LiteralPath $shortcutDirectory)) {
    New-Item -ItemType Directory -Path $shortcutDirectory -Force | Out-Null
}

$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($ShortcutPath)
$shortcut.TargetPath = $TargetPath
$shortcut.WorkingDirectory = Split-Path -Path $TargetPath -Parent
$shortcut.IconLocation = "$IconPath,0"
$shortcut.Description = 'TidyUUUUp — 桌面整理工具'
$shortcut.Save()

Write-Output "Created shortcut: $ShortcutPath"
