from indicators import production_index, concession_index, frequency_index, role_behavior_index, reliability_index, under_control_index

def estimate_total(adapted):
    h = adapted["home"]; a = adapted["away"]
    base = (
        h["corners_for_home_away_avg"] +
        a["corners_for_home_away_avg"] +
        h["corners_against_home_away_avg"] +
        a["corners_against_home_away_avg"]
    ) / 2.0
    pace_boost = (adapted["context"]["expected_pace_shape"] - 50) / 18.0
    return round(max(0.0, base + pace_boost), 2)

def score_over(adapted):
    h = adapted["home"]; a = adapted["away"]; c = adapted["context"]
    blocks = {
        "prod_home": production_index(h),
        "prod_away": production_index(a),
        "conc_home": concession_index(h),
        "conc_away": concession_index(a),
        "freq_home": frequency_index(h),
        "freq_away": frequency_index(a),
        "role_home": role_behavior_index(h, adapted["home_role"]),
        "role_away": role_behavior_index(a, adapted["away_role"]),
        "pace": c["expected_pace_shape"],
        "volatility": c["expected_game_state_volatility"],
        "reliability": (reliability_index(h) + reliability_index(a)) / 2,
    }
    score = (
        blocks["prod_home"] * 0.18 +
        blocks["prod_away"] * 0.16 +
        blocks["conc_home"] * 0.14 +
        blocks["conc_away"] * 0.14 +
        blocks["freq_home"] * 0.10 +
        blocks["freq_away"] * 0.08 +
        blocks["role_home"] * 0.05 +
        blocks["role_away"] * 0.03 +
        blocks["pace"] * 0.08 +
        blocks["volatility"] * 0.02 +
        blocks["reliability"] * 0.02
    )
    return round(min(100.0, max(0.0, score)), 2), blocks

def score_under(adapted):
    h = adapted["home"]; a = adapted["away"]; c = adapted["context"]
    blocks = {
        "under_home": under_control_index(h),
        "under_away": under_control_index(a),
        "anti_conc_home": 100 - concession_index(h),
        "anti_conc_away": 100 - concession_index(a),
        "anti_freq_home": 100 - frequency_index(h),
        "anti_freq_away": 100 - frequency_index(a),
        "anti_pace": 100 - c["expected_pace_shape"],
        "anti_volatility": 100 - c["expected_game_state_volatility"],
        "reliability": (reliability_index(h) + reliability_index(a)) / 2,
    }
    score = (
        blocks["under_home"] * 0.18 +
        blocks["under_away"] * 0.16 +
        blocks["anti_conc_home"] * 0.14 +
        blocks["anti_conc_away"] * 0.14 +
        blocks["anti_freq_home"] * 0.08 +
        blocks["anti_freq_away"] * 0.08 +
        blocks["anti_pace"] * 0.12 +
        blocks["anti_volatility"] * 0.08 +
        blocks["reliability"] * 0.02
    )
    return round(min(100.0, max(0.0, score)), 2), blocks

def line_strength(direction, estimated_total, line):
    diff = estimated_total - line
    if direction == "Over":
        return round(max(0.0, min(100.0, 52 + diff * 20)), 2)
    else:
        return round(max(0.0, min(100.0, 52 + (-diff) * 20)), 2)

def apply_penalties(score, alerts, exclusions):
    penalties = []
    out = score
    if "rotação provável" in alerts:
        out -= 6; penalties.append("penalty_rotacao")
    if "perfil tático instável" in alerts:
        out -= 8; penalties.append("penalty_instabilidade")
    if exclusions:
        out -= 25; penalties.extend([f"penalty_exclusion::{x}" for x in exclusions])
    return round(max(0.0, out), 2), penalties
