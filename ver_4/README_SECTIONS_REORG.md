# Abqeri Sections Reorg Patch
- Adds /docs/sections/* skeletons (EN/RU/中文) for mini-universe, ai-classical, music-ai, hybrid-cloud, health
- Script to move existing mini-universe into sections and update links

## Use
1) Unzip into your repo root (contains 'docs' + 'scripts').
2) PowerShell:
   cd <repo>
   git fetch origin
   git checkout main
   git pull
   .\scripts\reorg_sections.ps1
   $RELEASES = "https://github.com/asharayiah/mini-universe-engine/releases"
   Get-ChildItem .\docs -Recurse -Filter *.html | % {
     (Get-Content $_.FullName) -replace 'https://github.com/YOUR_GH_USER/YOUR_REPO/releases',$RELEASES | Set-Content -NoNewline $_.FullName
   }
   git add .
   git commit -m "Reorganize site into /sections/* + move Mini‑Universe"
   git push origin main
