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

def edge_value(market_odds, fair):
    if market_odds is None or fair is None:
        return None
    return round((market_odds / fair) - 1, 3)

def adapt_protected_input(payload):
    required_top = [
        "fixture_id", "league_id", "season", "home_team_id", "away_team_id",
        "provider_name", "provider_source", "protected_match_context"
    ]
    missing_top = [k for k in required_top if k not in payload]
    if missing_top:
        return {"runtime_state": "hard_fail", "missing_fields": missing_top}

    ctx = payload["protected_match_context"]
    required_ctx = [
        "lambda_league", "GPI_M", "DRI_M", "OPI_M", "NRI_M",
        "AttackAdj", "DefenseAdj", "PaceAdj", "RiskAdj"
    ]
    missing_ctx = [k for k in required_ctx if k not in ctx]
    if missing_ctx:
        return {"runtime_state": "hard_fail", "missing_fields": missing_ctx}

    odds = payload.get("market_odds")
    runtime_state = "ready" if odds is not None else "degraded_run"

    return {
        "runtime_state": runtime_state,
        "input_profile": payload.get("input_profile", "protected_min_v1"),
        "fixture_id": payload["fixture_id"],
        "league_id": payload["league_id"],
        "season": payload["season"],
        "home_team_id": payload["home_team_id"],
        "away_team_id": payload["away_team_id"],
        "provider_name": payload["provider_name"],
        "provider_source": payload["provider_source"],
        "runtime_profile": payload.get("runtime_profile", "mock_handoff_run"),
        "risk_flags": payload.get("risk_flags", []),
        "context_note": payload.get("context_note"),
        "market_odds": odds or {},
        "model_inputs": {
            "lambda_league": ctx["lambda_league"],
            "GPI_M": ctx["GPI_M"],
            "DRI_M": ctx["DRI_M"],
            "OPI_M": ctx["OPI_M"],
            "NRI_M": ctx["NRI_M"],
            "AttackAdj": ctx["AttackAdj"],
            "DefenseAdj": ctx["DefenseAdj"],
            "PaceAdj": ctx["PaceAdj"],
            "RiskAdj": ctx["RiskAdj"],
            "a": payload.get("coefficients", {}).get("a", 0.50),
            "b": payload.get("coefficients", {}).get("b", 0.30),
            "c": payload.get("coefficients", {}).get("c", 0.20),
            "d": payload.get("coefficients", {}).get("d", 0.15),
        }
    }

def build_base_state(inp):
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
    e = edge_value(market_odds, f)
    status = "rejected"

    if line_key == "over_1_5":
        if lam >= 2.00 and score >= 70 and p >= 0.69 and (e is None or e >= -0.01):
            status = "candidate"
        elif lam >= 1.90 and score >= 66 and p >= 0.64:
            status = "watchlist"
    elif line_key == "over_2_5":
        if lam >= 2.50 and score >= 74 and p >= 0.47 and (e is None or e >= 0.015):
            status = "candidate"
        elif lam >= 2.32 and score >= 69 and p >= 0.43:
            status = "watchlist"
    elif line_key == "under_3_5":
        if lam <= 2.90 and score <= 76 and p >= 0.67 and (e is None or e >= -0.01):
            status = "candidate"
        elif lam <= 3.05 and score <= 80 and p >= 0.62:
            status = "watchlist"
    elif line_key == "under_2_5":
        if lam <= 2.15 and score <= 66 and p >= 0.49 and (e is None or e >= 0.04):
            status = "candidate"
        elif lam <= 2.30 and score <= 70 and p >= 0.44 and (e is None or e >= 0.00):
            status = "watchlist"
    elif line_key == "over_3_5":
        if lam >= 3.10 and score >= 80 and p >= 0.30 and (e is None or e >= 0.05):
            status = "candidate"
        elif lam >= 2.90 and score >= 76 and p >= 0.25:
            status = "watchlist"

    txt = " ".join(risk_flags).lower()
    if "grave" in txt:
        status = {"candidate":"watchlist","watchlist":"rejected","rejected":"rejected"}[status]
    elif "moderado" in txt and status == "candidate":
        if e is not None:
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

def emit_output(adapted):
    if adapted["runtime_state"] == "hard_fail":
        return {
            "module_name": "under_over_jogo",
            "module_version": "mock_local_handoff_v1",
            "runtime_state": "hard_fail",
            "missing_fields": adapted["missing_fields"]
        }

    base = build_base_state(adapted["model_inputs"])
    odds = adapted["market_odds"]
    risk_flags = adapted.get("risk_flags", [])

    lines = ["over_1_5", "over_2_5", "under_3_5", "under_2_5", "over_3_5"]
    results = {}
    for line in lines:
        results[line] = evaluate_line(base, line, odds.get(line), risk_flags)

    final = apply_family_coherence(results)

    return {
        "module_name": "under_over_jogo",
        "module_version": "mock_local_handoff_v1",
        "runtime_state": adapted["runtime_state"],
        "fixture_id": adapted["fixture_id"],
        "provider_name": adapted["provider_name"],
        "provider_source": adapted["provider_source"],
        "input_profile": adapted["input_profile"],
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
        raise SystemExit("No input mock files found.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Under/Over Jogo - mini fluxo local ponta a ponta")
    print()

    for path in input_files:
        raw = load_json(path)
        adapted = adapt_protected_input(raw)
        emitted = emit_output(adapted)
        out_name = path.stem.replace("input_", "output_") + "_v1.json"
        save_json(OUTPUT_DIR / out_name, emitted)

        print(f"[OK] {path.name}")
        print(f"     runtime_state={emitted['runtime_state']}")
        if emitted["runtime_state"] != "hard_fail":
            print(f"     score={emitted['base_state']['OU_Base_Score']} | lambda={emitted['base_state']['lambda_match']} | profile={emitted['base_state']['profile']}")
            for key in ["over_1_5","over_2_5","under_3_5","under_2_5","over_3_5"]:
                row = emitted["results"][key]
                edge_txt = "null" if row["edge"] is None else f"{row['edge']:+.3f}"
                print(f"     {key:<10} -> {row['candidate_status']:<9} prob={row['probability']:.3f} edge={edge_txt}")
        else:
            print(f"     missing={emitted['missing_fields']}")
        print()

if __name__ == "__main__":
    main()
