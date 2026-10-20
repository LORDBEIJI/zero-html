# 根据当前八个页面生成自托管的思源宋体子集。
$ErrorActionPreference = 'Stop'
Push-Location (Split-Path $PSScriptRoot -Parent)
try { node scripts/subset-fonts.mjs } finally { Pop-Location }
