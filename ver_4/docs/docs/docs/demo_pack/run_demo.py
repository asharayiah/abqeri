import json, sys, hashlib, random
def make(seed, experiment):
    random.seed(seed)
    payload = {
        "seed": seed,
        "experiment": experiment,
        "metrics": {"toy_score": round(1.5 + random.random(), 6)},
        "artifact_sha256": hashlib.sha256(f"{seed}:{experiment}".encode()).hexdigest()
    }
    return payload
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python run_demo.py seed.json", file=sys.stderr); sys.exit(1)
    s = json.load(open(sys.argv[1],"r",encoding="utf-8"))
    print(json.dumps(make(s["seed"], s["experiment"]), ensure_ascii=False))
