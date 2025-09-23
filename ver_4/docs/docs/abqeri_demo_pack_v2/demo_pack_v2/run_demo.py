#!/usr/bin/env python3
import argparse, json, os, hashlib, random, pathlib, sys

EXPERIMENTS = {
    "bell_chsh": "Entanglement correlation placeholder",
    "double_slit": "Interference placeholder",
    "vacuum_matter": "Vacuum↔Matter placeholder",
    "duality": "Wave/particle duality placeholder",
    "black_hole_info": "Information loss/gain placeholder",
    "measurement_consciousness": "Measurement flag placeholder",
}

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def ensure_dir(p):
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)

def deterministic_rng(seed):
    random.seed(seed)
    # derived floats
    return {
        "a": round(0.5 + random.random()/2, 6),
        "b": round(0.25 + random.random()/2, 6),
        "c": round(0.75 + random.random()/4, 6),
    }

def write_csv(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(",".join(map(str, r)) + "\n")

def artifact_for(experiment, seed, outdir):
    # Produce tiny, deterministic CSV content per experiment
    rng = deterministic_rng(seed)
    artifacts = []
    if experiment == "bell_chsh":
        # Placeholder: correlation table
        rows = [("setting_a","setting_b","corr"),
                (0,0, rng["a"]), (0,1, rng["b"]), (1,0, rng["b"]), (1,1, rng["c"])]
        p = os.path.join(outdir, f"events_bell_seed{seed}.csv")
        write_csv(p, rows)
        artifacts.append(p)
    elif experiment == "double_slit":
        # Placeholder: simple fringe intensities
        rows = [("position","intensity")]
        for x in range(-5,6):
            val = round(rng["a"]*abs(((-1)**x)) + rng["b"]*(x*x)/25, 6)  # toy
            rows.append((x, val))
        p = os.path.join(outdir, f"interference_seed{seed}.csv")
        write_csv(p, rows)
        artifacts.append(p)
    elif experiment == "vacuum_matter":
        # Placeholder: energy bins and virtual counts
        rows = [("energy_bin","virtual_count")]
        for ebin in range(1,6):
            rows.append((ebin, int(100*rng["b"] + ebin*seed % 17)))
        p = os.path.join(outdir, f"vacuum_matter_seed{seed}.csv")
        write_csv(p, rows)
        artifacts.append(p)
    elif experiment == "duality":
        # Placeholder: two views for same seed
        rows1 = [("k","wave_amp")]
        rows2 = [("n","particle_hits")]
        for k in range(0,6):
            rows1.append((k, round(rng["a"]*k + rng["b"], 6)))
            rows2.append((k, int(10*rng["c"] + k)))
        p1 = os.path.join(outdir, f"duality_wave_seed{seed}.csv")
        p2 = os.path.join(outdir, f"duality_particle_seed{seed}.csv")
        write_csv(p1, rows1); write_csv(p2, rows2)
        artifacts.extend([p1,p2])
    elif experiment == "black_hole_info":
        # Placeholder: compression summary
        rows = [("segment","bits_in","bits_out")]
        for i in range(1,6):
            bits_in = 1000 + i*seed%97
            bits_out = int(bits_in * (0.9 + (rng["b"]/10)))
            rows.append((i, bits_in, bits_out))
        p = os.path.join(outdir, f"blackhole_info_seed{seed}.csv")
        write_csv(p, rows)
        artifacts.append(p)
    elif experiment == "measurement_consciousness":
        # Placeholder: measurement flag toggles distribution
        rows = [("trial","measured","value")]
        for i in range(1,11):
            measured = 1 if i % 2 == 0 else 0
            val = round((rng["a"] if measured else rng["c"]) * (i/10), 6)
            rows.append((i, measured, val))
        p = os.path.join(outdir, f"measurement_seed{seed}.csv")
        write_csv(p, rows)
        artifacts.append(p)
    else:
        raise SystemExit(f"Unknown experiment: {experiment}")
    return artifacts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed_file", nargs="?", help="JSON seed file with {seed:int, experiment:str}")
    ap.add_argument("--seed", type=int, help="Seed")
    ap.add_argument("--experiment", type=str, choices=list(EXPERIMENTS.keys()), help="Experiment name")
    ap.add_argument("--out", type=str, default="out", help="Output directory")
    args = ap.parse_args()

    if args.seed_file:
        with open(args.seed_file, "r", encoding="utf-8") as f:
            obj = json.load(f)
        seed = int(obj["seed"])
        exp = str(obj["experiment"])
    else:
        if args.seed is None or args.experiment is None:
            ap.error("Provide a seed file OR --seed and --experiment")
        seed = args.seed
        exp = args.experiment

    outdir = os.path.abspath(args.out)
    ensure_dir(outdir)

    arts = artifact_for(exp, seed, outdir)
    art_objs = [{"path": os.path.relpath(p, outdir), "sha256": sha256_of(p)} for p in arts]
    rng = deterministic_rng(seed)
    result = {
        "seed": seed,
        "experiment": exp,
        "artifacts": art_objs,
        "metrics": {
            "toy_score": round(1.0 + rng["a"] + rng["b"]/2, 6),
            "notes": EXPERIMENTS[exp]
        }
    }
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()
