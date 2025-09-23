#!/usr/bin/env bash
set -euo pipefail
SEEDS=(42 123 7 9 314 271)
EXPERIMENTS=(bell_chsh double_slit vacuum_matter duality black_hole_info measurement_consciousness)
OUT_DIR="${1:-out}"
for e in "${EXPERIMENTS[@]}"; do
  for s in "${SEEDS[@]}"; do
    python run_demo.py --seed "$s" --experiment "$e" --out "$OUT_DIR"
  done
done
echo ">>> Done. See '$OUT_DIR'."
