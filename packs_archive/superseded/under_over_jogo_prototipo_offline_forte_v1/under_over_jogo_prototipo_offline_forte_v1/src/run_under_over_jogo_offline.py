import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "examples" / "inputs"
OUTPUT_DIR = ROOT / "examples" / "outputs"

def poisson_pmf(k, lam):
    return math.exp(-lam) * (lam ** k) / math.factorial(k)

def over_prob(line, lam):
    threshold = int(math.floor(line)) + 1
    return 1 - sum(poisson_pmf(k, lam) for k in range(threshold))

def under_prob(line, lam):
    threshold = int(math.floor(line))
    return sum(poisson_pmf(k, lam) for k in range(threshold + 1))

def fair_odds(p):
    return round(1 / p, 2) if p > 0 else None

def edge(market_odds, fair):
    return round((market_odds / fair) - 1, 3)

def build_base_state(inp):
    required = ["lambda_league","GPI_M","DRI_M","OPI_M","NRI_M","AttackAdj","DefenseAdj","PaceAdj","RiskAdj","a","b","c","d"]
    missing = [k for k in required if k not in inp]
    if missing:
        raise ValueError(f"Missing critical input(s): {', '.join(missing)}")
    score = round(
        0.35 * inp["GPI_M"]
        + 0.25 * (100 - inp["DRI_M"])
        + 0.20 * inp["OPI_M"]
        + 0.20 * inp["NRI_M"]
    )
    lam = (
        inp["lambda_league"]
        + inp["a"] * inp["AttackAdj"]
        - inp["b"] * inp["DefenseAdj"]
        + inp["c"] * inp["PaceAdj"]
        - inp["d"] * inp["RiskAdj"]
    )
    lam = max(0.8, min(4.2, round(lam, 2)))
    if lam < 1.80:
        profile = "very_controlled"
    elif lam < 2.25:
        profile = "controlled"
    elif lam < 2.70:
        profile = "corridor_2_3"
    elif lam < 3.15:
        profile = "offensive"
    else:
        profile = "explosive"
    return {"OU_Base_Score": score, "lambda_match": lam, "profile": profile}

def evaluate_line(base, line_key, market_odds, risk_flags):
    score = base["OU_Base_Score"]
    lam = base["lambda_match"]
    line = float(line_key.split("_")[1] + "." + line_key.split("_")[2])
    p = over_prob(line, lam) if line_key.startswith("over_") else under_prob(line, lam)
    f = fair_odds(p)
    e = edge(market_odds, f)
    status = "rejected"
    if line_key == "over_1_5":
        if lam >= 2.00 and score >= 70 and p >= 0.69 and e >= -0.01:
            status = "candidate"
        elif lam >= 1.90 and score >= 66 and p >= 0.64:
            status = "watchlist"
    elif line_key == "over_2_5":
        if lam >= 2.50 and score >= 74 and p >= 0.47 and e >= 0.015:
            status = "candidate"
        elif lam >= 2.32 and score >= 69 and p >= 0.43:
            status = "watchlist"
    elif line_key == "under_3_5":
        if lam <= 2.90 and score <= 76 and p >= 0.67 and e >= -0.01:
            status = "candidate"
        elif lam <= 3.05 and score <= 80 and p >= 0.62:
            status = "watchlist"
    elif line_key == "under_2_5":
        if lam <= 2.15 and score <= 66 and p >= 0.49 and e >= 0.04:
            status = "candidate"
        elif lam <= 2.30 and score <= 70 and p >= 0.44 and e >= 0.00:
            status = "watchlist"
    elif line_key == "over_3_5":
        if lam >= 3.10 and score >= 80 and p >= 0.30 and e >= 0.05:
            status = "candidate"
        elif lam >= 2.90 and score >= 76 and p >= 0.25:
            status = "watchlist"
    txt = " ".join(risk_flags).lower()
    if "grave" in txt:
        status = {"candidate":"watchlist","watchlist":"rejected","rejected":"rejected"}[status]
    elif "moderado" in txt:
        if status == "candidate":
            weak_edge = e < 0.02
            near_threshold = (
                (line_key == "over_1_5" and lam < 2.08) or
                (line_key == "over_2_5" and lam < 2.60) or
                (line_key == "under_3_5" and lam > 2.82) or
                (line_key == "under_2_5" and lam > 2.18) or
                (line_key == "over_3_5" and lam < 3.18)
            )
            if weak_edge or near_threshold:
                status = "watchlist"
    return {
        "market_code": line_key,
        "selection_label": line_key.replace("_", " ").upper(),
        "lambda_match": lam,
        "probability": round(p, 3),
        "fair_odds": f,
        "market_odds": market_odds,
        "edge": e,
        "eligibility": status != "rejected",
        "candidate_status": status,
        "risk_flags": risk_flags,
    }

def apply_family_coherence(results):
    r = {k: dict(v) for k, v in results.items()}
    if r["over_2_5"]["candidate_status"] == "candidate":
        r["over_1_5"]["candidate_status"] = "candidate"
        r["under_2_5"]["candidate_status"] = "rejected"
        r["under_2_5"]["eligibility"] = False
    if r["under_2_5"]["candidate_status"] == "candidate":
        r["under_3_5"]["candidate_status"] = "candidate"
        r["over_2_5"]["candidate_status"] = "rejected"
        r["over_2_5"]["eligibility"] = False
        r["over_3_5"]["candidate_status"] = "rejected"
        r["over_3_5"]["eligibility"] = False
    if r["over_3_5"]["candidate_status"] == "candidate":
        r["over_2_5"]["candidate_status"] = "candidate"
        r["over_1_5"]["candidate_status"] = "candidate"
        r["under_3_5"]["candidate_status"] = "rejected"
        r["under_3_5"]["eligibility"] = False
    lam = next(iter(r.values()))["lambda_match"]
    if 2.25 <= lam < 2.70:
        r["over_1_5"]["candidate_status"] = "rejected"
        r["over_1_5"]["eligibility"] = False
        r["over_2_5"]["candidate_status"] = "rejected"
        r["over_2_5"]["eligibility"] = False
    return r

def run_scenario(payload):
    base = build_base_state(payload["inputs"])
    results = {}
    for line_key, market_odds in payload["market_odds"].items():
        results[line_key] = evaluate_line(base, line_key, market_odds, payload.get("risk_flags", []))
    final = apply_family_coherence(results)
    return {
        "module_name": "under_over_jogo",
        "module_version": "offline_prototype_v1",
        "scenario_name": payload["scenario_name"],
        "base_state": base,
        "results": final
    }

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, payload):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def main():
    input_files = sorted(INPUT_DIR.glob("*.json"))
    if not input_files:
        raise SystemExit("No input scenarios found in examples/inputs")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Under/Over Jogo - prototipo offline forte")
    print()
    for path in input_files:
        payload = load_json(path)
        result = run_scenario(payload)
        out_name = path.stem.replace("input_", "output_") + "_v1.json"
        out_path = OUTPUT_DIR / out_name
        save_json(out_path, result)
        print(f"[OK] {payload['scenario_name']}")
        print(f"     score={result['base_state']['OU_Base_Score']} | lambda={result['base_state']['lambda_match']} | profile={result['base_state']['profile']}")
        for key in ["over_1_5","over_2_5","under_3_5","under_2_5","over_3_5"]:
            row = result["results"][key]
            print(f"     {key:<10} -> {row['candidate_status']:<9} prob={row['probability']:.3f} edge={row['edge']:+.3f}")
        print()

if __name__ == "__main__":
    main()
