import math
import json

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

    return {
        "OU_Base_Score": score,
        "lambda_match": lam,
        "profile": profile,
    }

def evaluate_line(base, line_key, market_odds, risk_flags):
    score = base["OU_Base_Score"]
    lam = base["lambda_match"]

    line = float(line_key.split("_")[1] + "." + line_key.split("_")[2])
    p = over_prob(line, lam) if line_key.startswith("over_") else under_prob(line, lam)
    f = fair_odds(p)
    e = edge(market_odds, f)
    status = "rejected"

    # baseline congelada
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
        status = {"candidate": "watchlist", "watchlist": "rejected", "rejected": "rejected"}[status]
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
        "lambda_match": lam,
        "probability": round(p, 3),
        "fair_odds": f,
        "market_odds": market_odds,
        "edge": e,
        "candidate_status": status,
        "risk_flags": risk_flags,
    }

def apply_family_coherence(results):
    r = {k: dict(v) for k, v in results.items()}

    if r["over_2_5"]["candidate_status"] == "candidate":
        r["over_1_5"]["candidate_status"] = "candidate"
        r["under_2_5"]["candidate_status"] = "rejected"

    if r["under_2_5"]["candidate_status"] == "candidate":
        r["under_3_5"]["candidate_status"] = "candidate"
        r["over_2_5"]["candidate_status"] = "rejected"
        r["over_3_5"]["candidate_status"] = "rejected"

    if r["over_3_5"]["candidate_status"] == "candidate":
        r["over_2_5"]["candidate_status"] = "candidate"
        r["over_1_5"]["candidate_status"] = "candidate"
        r["under_3_5"]["candidate_status"] = "rejected"

    # regra congelada do corredor intermédio
    if r["over_1_5"]["lambda_match"] >= 2.25 and r["over_1_5"]["lambda_match"] < 2.70:
        r["over_1_5"]["candidate_status"] = "rejected"
        r["over_2_5"]["candidate_status"] = "rejected"

    return r

SCENARIOS = {
    "cenario_controlado": {
        "inputs": {
            "lambda_league": 2.35, "GPI_M": 54, "DRI_M": 63, "OPI_M": 48, "NRI_M": 72,
            "AttackAdj": 0.12, "DefenseAdj": 0.52, "PaceAdj": 0.08, "RiskAdj": 0.12,
            "a": 0.55, "b": 0.35, "c": 0.25, "d": 0.20
        },
        "odds": {"over_1_5": 1.42, "over_2_5": 2.22, "under_3_5": 1.29, "under_2_5": 2.66, "over_3_5": 3.65},
        "risk_flags": ["ruído baixo"]
    },
    "cenario_intermedio_2_3": {
        "inputs": {
            "lambda_league": 2.45, "GPI_M": 69, "DRI_M": 46, "OPI_M": 63, "NRI_M": 70,
            "AttackAdj": 0.48, "DefenseAdj": 0.28, "PaceAdj": 0.30, "RiskAdj": 0.10,
            "a": 0.50, "b": 0.30, "c": 0.20, "d": 0.15
        },
        "odds": {"over_1_5": 1.36, "over_2_5": 2.03, "under_3_5": 1.49, "under_2_5": 2.54, "over_3_5": 3.10},
        "risk_flags": ["ruído moderado"]
    },
    "cenario_explosivo": {
        "inputs": {
            "lambda_league": 2.55, "GPI_M": 82, "DRI_M": 31, "OPI_M": 78, "NRI_M": 76,
            "AttackAdj": 0.80, "DefenseAdj": 0.10, "PaceAdj": 0.55, "RiskAdj": 0.08,
            "a": 0.55, "b": 0.25, "c": 0.25, "d": 0.10
        },
        "odds": {"over_1_5": 1.24, "over_2_5": 1.74, "under_3_5": 1.66, "under_2_5": 3.05, "over_3_5": 2.68},
        "risk_flags": ["ruído baixo"]
    }
}

def run_scenario(name, cfg):
    base = build_base_state(cfg["inputs"])
    results = {
        line_key: evaluate_line(base, line_key, market_odds, cfg["risk_flags"])
        for line_key, market_odds in cfg["odds"].items()
    }
    final = apply_family_coherence(results)
    return {
        "scenario": name,
        "base_state": base,
        "results": final,
    }

def print_scenario_output(payload):
    print("=" * 64)
    print(payload["scenario"])
    print("- OU_Base_Score:", payload["base_state"]["OU_Base_Score"])
    print("- lambda_match :", payload["base_state"]["lambda_match"])
    print("- profile      :", payload["base_state"]["profile"])
    print()
    print(f"{'LINE':<14} {'PROB':>6} {'FAIR':>6} {'ODDS':>6} {'EDGE':>7} {'STATUS':>12}")
    print("-" * 64)
    ordered = ["over_1_5", "over_2_5", "under_3_5", "under_2_5", "over_3_5"]
    for key in ordered:
        row = payload["results"][key]
        print(f"{key:<14} {row['probability']:>6.3f} {row['fair_odds']:>6.2f} {row['market_odds']:>6.2f} {row['edge']:>7.3f} {row['candidate_status']:>12}")
    print()

def main():
    print("SignalBet / Under-Over Jogo")
    print("Teste offline da baseline congelada")
    print()

    outputs = []
    for name, cfg in SCENARIOS.items():
        payload = run_scenario(name, cfg)
        outputs.append(payload)
        print_scenario_output(payload)

    out_file = "under_over_jogo_offline_test_output.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(outputs, f, ensure_ascii=False, indent=2)

    print("Output JSON guardado em:", out_file)
    print("Teste concluído.")

if __name__ == "__main__":
    main()
