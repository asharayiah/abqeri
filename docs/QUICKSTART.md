# Quickstart

## Local (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m sdk.abqeri_mu --seed 42 --experiment bell_chsh --out out
```

## Docker
```bash
docker build -t abqeri/mu:demo .
docker run --rm -v "${PWD}/out:/out" abqeri/mu:demo --seed 42 --experiment bell_chsh --out /out
```

## Experiments (stub)
- `bell_chsh`
- `double_slit`
- `vacuum_matter`
