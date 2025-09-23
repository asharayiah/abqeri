# API_CONTRACT.md — Mini‑Universe Black‑Box CLI

## CLI
```
run_demo --seed <int> --experiment <bell_chsh|double_slit|vacuum_matter|duality|black_hole_info|measurement_consciousness> --out <dir>
```

## Output (stdout JSON)
- `seed`: integer
- `experiment`: string
- `artifacts`: list of objects with:
  - `path`: relative path under `--out`
  - `sha256`: lowercase hex digest of the artifact file
- `metrics`: freeform numbers/strings (deterministic by seed)

Artifacts SHOULD be content‑addressed deterministically so peers can verify SHA256 across machines.
