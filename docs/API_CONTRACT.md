# Engine API Contract (stdin/stdout JSON lines)

The SDK spawns `engine/abqeri_mu_engine` (or `.exe` on Windows) and communicates via **one JSON line** on stdin/stdout.

## Request (stdin)
```json
{"seed": 42, "experiment": "bell_chsh", "out_dir": "/abs/out"}
```

## Response (stdout)
```json
{"status":"ok","artifacts":[{"path":"/abs/out/file.csv","sha256":"..."}],"metrics":{"S":2.7}}
```

Rules:
- Exit with code **0** on success; non‑zero on error (explain on stderr).
- **Determinism**: same `seed` → identical outputs & hashes.
- Paths returned in `artifacts[].path` should be **absolute** where possible.
