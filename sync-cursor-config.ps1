# Cursor IDE Configuration Sync Script
# This script syncs Cursor configuration files between local and Git repository
# Author: Claude Code
# Date: 2025-12-29

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("backup", "restore", "status")]
    [string]$Action = "backup"
)

# Configuration paths
$CursorConfigPath = "$env:APPDATA\Cursor\User"
$CursorExtensionsPath = "$env:USERPROFILE\.cursor\extensions"
$BackupPath = Join-Path $PSScriptRoot "config"
$AhkPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\SwapCtrlAlt.ahk"

# Files to sync
$ConfigFiles = @(
    "settings.json",
    "keybindings.json",
    ".prettierrc"
)

# Create backup directory if not exists
function Ensure-BackupDirectory {
    if (-not (Test-Path $BackupPath)) {
        New-Item -ItemType Directory -Path $BackupPath -Force | Out-Null
        Write-Host "[INFO] Created backup directory: $BackupPath" -ForegroundColor Green
    }
}

# Backup configuration files
function Backup-Config {
    Ensure-BackupDirectory

    Write-Host "`n===== Backing up Cursor Configuration =====" -ForegroundColor Cyan

    # Backup main config files
    foreach ($file in $ConfigFiles) {
        $sourcePath = Join-Path $CursorConfigPath $file
        $destPath = Join-Path $BackupPath $file

        if (Test-Path $sourcePath) {
            Copy-Item $sourcePath $destPath -Force
            Write-Host "[OK] Backed up: $file" -ForegroundColor Green
        } else {
            Write-Host "[SKIP] Not found: $file" -ForegroundColor Yellow
        }
    }

    # Backup snippets directory
    $snippetsSource = Join-Path $CursorConfigPath "snippets"
    $snippetsDest = Join-Path $BackupPath "snippets"
    if (Test-Path $snippetsSource) {
        if (Test-Path $snippetsDest) { Remove-Item $snippetsDest -Recurse -Force }
        Copy-Item $snippetsSource $snippetsDest -Recurse -Force
        Write-Host "[OK] Backed up: snippets/" -ForegroundColor Green
    }

    # Backup AHK script
    if (Test-Path $AhkPath) {
        Copy-Item $AhkPath (Join-Path $BackupPath "SwapCtrlAlt.ahk") -Force
        Write-Host "[OK] Backed up: SwapCtrlAlt.ahk" -ForegroundColor Green
    }

    # Export installed extensions list
    $extensionsListPath = Join-Path $BackupPath "extensions-list.txt"
    if (Test-Path $CursorExtensionsPath) {
        Get-ChildItem $CursorExtensionsPath -Directory |
            Where-Object { $_.Name -ne "extensions.json" } |
            ForEach-Object { $_.Name } |
            Sort-Object |
            Out-File $extensionsListPath -Encoding UTF8
        Write-Host "[OK] Exported extensions list" -ForegroundColor Green
    }

    Write-Host "`n===== Backup Complete =====" -ForegroundColor Cyan
    Write-Host "Backup location: $BackupPath" -ForegroundColor White
    Write-Host "`nNext steps:" -ForegroundColor Yellow
    Write-Host "  cd $PSScriptRoot" -ForegroundColor White
    Write-Host "  git add ." -ForegroundColor White
    Write-Host "  git commit -m 'Update Cursor configuration'" -ForegroundColor White
    Write-Host "  git push" -ForegroundColor White
}

# Restore configuration files
function Restore-Config {
    Write-Host "`n===== Restoring Cursor Configuration =====" -ForegroundColor Cyan

    # Restore main config files
    foreach ($file in $ConfigFiles) {
        $sourcePath = Join-Path $BackupPath $file
        $destPath = Join-Path $CursorConfigPath $file

        if (Test-Path $sourcePath) {
            # Backup current file before restore
            if (Test-Path $destPath) {
                $backupName = "$destPath.restore_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
                Copy-Item $destPath $backupName -Force
            }
            Copy-Item $sourcePath $destPath -Force
            Write-Host "[OK] Restored: $file" -ForegroundColor Green
        } else {
            Write-Host "[SKIP] Not in backup: $file" -ForegroundColor Yellow
        }
    }

    # Restore snippets
    $snippetsSource = Join-Path $BackupPath "snippets"
    $snippetsDest = Join-Path $CursorConfigPath "snippets"
    if (Test-Path $snippetsSource) {
        if (Test-Path $snippetsDest) { Remove-Item $snippetsDest -Recurse -Force }
        Copy-Item $snippetsSource $snippetsDest -Recurse -Force
        Write-Host "[OK] Restored: snippets/" -ForegroundColor Green
    }

    # Restore AHK script
    $ahkBackup = Join-Path $BackupPath "SwapCtrlAlt.ahk"
    if (Test-Path $ahkBackup) {
        Copy-Item $ahkBackup $AhkPath -Force
        Write-Host "[OK] Restored: SwapCtrlAlt.ahk" -ForegroundColor Green
    }

    Write-Host "`n===== Restore Complete =====" -ForegroundColor Cyan
    Write-Host "Please restart Cursor to apply changes." -ForegroundColor Yellow
}

# Show sync status
function Show-Status {
    Write-Host "`n===== Cursor Configuration Sync Status =====" -ForegroundColor Cyan

    Write-Host "`nLocal Configuration:" -ForegroundColor Yellow
    Write-Host "  Cursor Config: $CursorConfigPath" -ForegroundColor White
    Write-Host "  Extensions: $CursorExtensionsPath" -ForegroundColor White
    Write-Host "  AHK Script: $AhkPath" -ForegroundColor White

    Write-Host "`nBackup Location:" -ForegroundColor Yellow
    Write-Host "  $BackupPath" -ForegroundColor White

    Write-Host "`nConfig Files Status:" -ForegroundColor Yellow
    foreach ($file in $ConfigFiles) {
        $localPath = Join-Path $CursorConfigPath $file
        $backupFilePath = Join-Path $BackupPath $file

        $localExists = Test-Path $localPath
        $backupExists = Test-Path $backupFilePath

        if ($localExists -and $backupExists) {
            $localHash = (Get-FileHash $localPath -Algorithm MD5).Hash
            $backupHash = (Get-FileHash $backupFilePath -Algorithm MD5).Hash
            if ($localHash -eq $backupHash) {
                Write-Host "  [SYNCED] $file" -ForegroundColor Green
            } else {
                Write-Host "  [CHANGED] $file" -ForegroundColor Yellow
            }
        } elseif ($localExists) {
            Write-Host "  [LOCAL ONLY] $file" -ForegroundColor Yellow
        } elseif ($backupExists) {
            Write-Host "  [BACKUP ONLY] $file" -ForegroundColor Yellow
        } else {
            Write-Host "  [MISSING] $file" -ForegroundColor Red
        }
    }

    # Count extensions
    if (Test-Path $CursorExtensionsPath) {
        $extCount = (Get-ChildItem $CursorExtensionsPath -Directory | Where-Object { $_.Name -ne "extensions.json" }).Count
        Write-Host "`nInstalled Extensions: $extCount" -ForegroundColor White
    }
}

# Main execution
switch ($Action) {
    "backup" { Backup-Config }
    "restore" { Restore-Config }
    "status" { Show-Status }
}
