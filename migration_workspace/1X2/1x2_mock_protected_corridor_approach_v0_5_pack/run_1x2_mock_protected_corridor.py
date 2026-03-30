#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, obj):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def validate_protected_input(data):
    required = [
        ("protected_match_context", "fixture_id"),
        ("protected_match_context", "league_id"),
        ("protected_match_context", "season"),
        ("protected_match_context", "home_team"),
        ("protected_match_context", "away_team"),
        ("protected_market_context", "odd_home"),
        ("protected_market_context", "odd_draw"),
        ("protected_market_context", "odd_away"),
        ("protected_team_strength_context", "home_attack_rating"),
        ("protected_team_strength_context", "home_defense_rating"),
        ("protected_team_strength_context", "away_attack_rating"),
        ("protected_team_strength_context", "away_defense_rating"),
        ("protected_form_context", "home_form_points_last5"),
        ("protected_form_context", "away_form_points_last5"),
    ]
    for parent, child in required:
        if parent not in data or child not in data[parent]:
            return False
    return True

def adapt(data):
    pm = data["protected_match_context"]
    pmark = data["protected_market_context"]
    pts = data["protected_team_strength_context"]
    pform = data["protected_form_context"]
    prisk = data["protected_risk_context"]
    adapted = {
        "fixture_id": pm["fixture_id"],
        "league_id": pm["league_id"],
        "season": pm["season"],
        "home_team_id": pm["home_team"]["id"],
        "away_team_id": pm["away_team"]["id"],
        "home_team_name": pm["home_team"]["name"],
        "away_team_name": pm["away_team"]["name"],
        "odd_home": pmark["odd_home"],
        "odd_draw": pmark["odd_draw"],
        "odd_away": pmark["odd_away"],
        "home_attack_rating": pts["home_attack_rating"],
        "home_defense_rating": pts["home_defense_rating"],
        "away_attack_rating": pts["away_attack_rating"],
        "away_defense_rating": pts["away_defense_rating"],
        "home_form_points_last5": pform["home_form_points_last5"],
        "away_form_points_last5": pform["away_form_points_last5"],
        "market_warning_flag": prisk.get("market_warning_flag", False),
        "injury_noise_flag": prisk.get("injury_noise_flag", False),
        "rotation_noise_flag": prisk.get("rotation_noise_flag", False),
    }
    adaptation_status = "adapted_ok"
    return adapted, adaptation_status

def softmax3(a, b, c):
    m = max(a, b, c)
    ea, eb, ec = math.exp(a-m), math.exp(b-m), math.exp(c-m)
    s = ea + eb + ec
    return ea/s, eb/s, ec/s

def decide(inp):
    home_strength = (inp["home_attack_rating"] - inp["away_defense_rating"]) + 0.08 * (inp["home_form_points_last5"] - inp["away_form_points_last5"])
    away_strength = (inp["away_attack_rating"] - inp["home_defense_rating"]) + 0.08 * (inp["away_form_points_last5"] - inp["home_form_points_last5"])
    draw_bias = 0.60 - abs(home_strength - away_strength) * 0.35

    odds_home = 1.0 / inp["odd_home"]
    odds_draw = 1.0 / inp["odd_draw"]
    odds_away = 1.0 / inp["odd_away"]
    total = odds_home + odds_draw + odds_away
    odds_home, odds_draw, odds_away = odds_home/total, odds_draw/total, odds_away/total

    # Fusion layer: 70% internal, 30% market normalized
    int_home, int_draw, int_away = softmax3(home_strength, draw_bias, away_strength)
    p_home = 0.70 * int_home + 0.30 * odds_home
    p_draw = 0.70 * int_draw + 0.30 * odds_draw
    p_away = 0.70 * int_away + 0.30 * odds_away
    s = p_home + p_draw + p_away
    p_home, p_draw, p_away = p_home/s, p_draw/s, p_away/s

    risk_flags = []
    if inp.get("market_warning_flag"):
        risk_flags.append("market_warning_flag")
    if inp.get("injury_noise_flag"):
        risk_flags.append("injury_noise_flag")
    if inp.get("rotation_noise_flag"):
        risk_flags.append("rotation_noise_flag")

    lead = max(p_home, p_away)
    direction = "1" if p_home >= p_away else "2"
    # score
    score = 50 + (lead - p_draw) * 100 + abs(p_home - p_away) * 30 - len(risk_flags) * 6
    score = max(0, min(100, round(score)))

    if inp.get("market_warning_flag") and score < 65:
        return {
            "selection_label": "REJECTED",
            "eligibility": False,
            "decision_status": "rejected_decision",
            "candidate_status": "rejected",
            "score_band": "avoid",
            "raw_module_score": score,
            "p_home": round(p_home, 4),
            "p_draw": round(p_draw, 4),
            "p_away": round(p_away, 4),
            "risk_flags": risk_flags,
            "rationale_short": "Mercado com warning e base insuficiente para decisão disciplinada."
        }

    if lead >= 0.48 and p_draw <= 0.29 and score >= 78:
        return {
            "selection_label": direction,
            "eligibility": True,
            "decision_status": "primary_decision",
            "candidate_status": "candidate",
            "score_band": "A" if score < 90 else "A+",
            "raw_module_score": score,
            "p_home": round(p_home, 4),
            "p_draw": round(p_draw, 4),
            "p_away": round(p_away, 4),
            "risk_flags": risk_flags,
            "rationale_short": "Direção principal suficientemente dominante para decisão seca."
        }

    if ((p_home > p_away and p_home >= 0.37) or (p_away > p_home and p_away >= 0.37)) and p_draw >= 0.23 and score >= 60:
        return {
            "selection_label": "1X" if p_home >= p_away else "X2",
            "eligibility": True,
            "decision_status": "degraded_decision",
            "candidate_status": "watchlist",
            "score_band": "B" if score >= 70 else "C",
            "raw_module_score": score,
            "p_home": round(p_home, 4),
            "p_draw": round(p_draw, 4),
            "p_away": round(p_away, 4),
            "risk_flags": risk_flags,
            "rationale_short": "Há direção principal, mas o empate continua demasiado vivo; degradar para dupla possibilidade."
        }

    return {
        "selection_label": "REJECTED",
        "eligibility": False,
        "decision_status": "rejected_decision",
        "candidate_status": "rejected",
        "score_band": "avoid",
        "raw_module_score": score,
        "p_home": round(p_home, 4),
        "p_draw": round(p_draw, 4),
        "p_away": round(p_away, 4),
        "risk_flags": risk_flags,
        "rationale_short": "Probabilidades demasiado achatadas ou sem direção disciplinada suficiente."
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data = load_json(args.input)
    if not validate_protected_input(data):
        out = {
            "module_name": "1X2",
            "module_version": "0.5",
            "contract_version": "1.1",
            "input_status": "hard_fail",
            "adaptation_status": "adaptation_fail",
            "run_status": "runtime_fail",
            "decision_status": "rejected_decision",
            "candidate_status": "rejected",
            "selection_label": "REJECTED"
        }
        save_json(args.output, out)
        return

    adapted, adaptation_status = adapt(data)
    result = decide(adapted)

    out = {
        "module_name": "1X2",
        "module_version": "0.5",
        "contract_version": "1.1",
        "fixture_id": adapted["fixture_id"],
        "league_id": adapted["league_id"],
        "season": adapted["season"],
        "market_family": "1x2",
        "market_code": "1x2_or_double_chance_mock",
        "selection_label": result["selection_label"],
        "p_home": result["p_home"],
        "p_draw": result["p_draw"],
        "p_away": result["p_away"],
        "raw_module_score": result["raw_module_score"],
        "score_band": result["score_band"],
        "eligibility": result["eligibility"],
        "input_status": "ok",
        "adaptation_status": adaptation_status,
        "run_status": "success",
        "decision_status": result["decision_status"],
        "candidate_status": result["candidate_status"],
        "risk_flags": result["risk_flags"],
        "rationale_short": result["rationale_short"],
        "provider_name": "mock_orchestrator_protected_shape",
        "provider_source": "mock_only",
        "input_profile": "protected_mock_input",
        "runtime_profile": "protected_mock",
        "readiness_level": "mock_ready"
    }
    save_json(args.output, out)

if __name__ == "__main__":
    main()
