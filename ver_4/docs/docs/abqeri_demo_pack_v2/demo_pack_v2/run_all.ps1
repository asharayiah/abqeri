param(
  [int[]]$Seeds = @(42,123,7,9,314,271),
  [string[]]$Experiments = @("bell_chsh","double_slit","vacuum_matter","duality","black_hole_info","measurement_consciousness"),
  [string]$OutDir = "out"
)
foreach ($e in $Experiments) {
  foreach ($s in $Seeds) {
    python run_demo.py --seed $s --experiment $e --out $OutDir | Out-Host
  }
}
Write-Host ">>> Done. See '$OutDir'."
