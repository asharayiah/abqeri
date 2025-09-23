param([string]$DocsRoot = ".\docs")
Write-Host ">>> Reorganizing to sections under $DocsRoot"
function Move-IfExists($src,$dst){ if(Test-Path $src){ New-Item -ItemType Directory -Path $dst -Force | Out-Null; robocopy $src $dst /E | Out-Null; Remove-Item -Recurse -Force $src } }
New-Item -ItemType Directory -Path "$DocsRoot\sections" -Force | Out-Null
New-Item -ItemType Directory -Path "$DocsRoot\ru\sections" -Force | Out-Null
New-Item -ItemType Directory -Path "$DocsRoot\zh\sections" -Force | Out-Null
Move-IfExists "$DocsRoot\mini-universe" "$DocsRoot\sections\mini-universe"
Move-IfExists "$DocsRoot\ru\mini-universe" "$DocsRoot\ru\sections\mini-universe"
Move-IfExists "$DocsRoot\zh\mini-universe" "$DocsRoot\zh\sections\mini-universe"
$files = Get-ChildItem $DocsRoot -Recurse -Filter *.html
foreach($f in $files){
 (Get-Content $f.FullName) `
  -replace 'href="/mini-universe/','href="/sections/mini-universe/' `
  -replace 'href="/ru/mini-universe/','href="/ru/sections/mini-universe/' `
  -replace 'href="/zh/mini-universe/','href="/zh/sections/mini-universe/' `
 | Set-Content -NoNewline $f.FullName
}
Write-Host ">>> Done. Review and commit."
