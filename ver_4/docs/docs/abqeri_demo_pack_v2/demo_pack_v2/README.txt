Abqeri Mini‑Universe — Demo Pack v2 (Placeholders for All Aspects)
====================================================================
This demo shows a SINGLE black‑box CLI that supports multiple experiments:
- bell_chsh                  (entanglement placeholder)
- double_slit                (interference placeholder)
- vacuum_matter              (vacuum↔matter placeholder)
- duality                    (wave/particle duality placeholder)
- black_hole_info            (information loss/gain placeholder)
- measurement_consciousness  (measurement flag placeholder)

Deterministic by seed. Artifacts are CSV/JSON files; a JSON summary is printed to stdout.

USAGE
-----
Option A: seed file (legacy)
  python run_demo.py seeds/bell_seed42.json --out out

Option B: CLI args
  python run_demo.py --seed 42 --experiment bell_chsh --out out

Batch (Windows PowerShell):
  .\run_all.ps1

Batch (Linux/macOS):
  bash run_all.sh

JSON CONTRACT
-------------
Input (stdin) is NOT used in this stub. The CLI accepts either a JSON seed file or flags.
Output (stdout) is a single JSON object:
{
  "seed": <int>,
  "experiment": "<name>",
  "artifacts": [{"path":"out/<...>.csv","sha256":"..."}],
  "metrics": {"toy_score": <float>, "notes": "<string>"}
}

SWAP‑IN REAL ENGINE
-------------------
Later, replace this script with your compiled binary that obeys the same interface:
  run_demo.exe --seed <int> --experiment <name> --out <dir>
