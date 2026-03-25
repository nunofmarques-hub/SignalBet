from __future__ import annotations
from indicators import production_score, concession_score, consistency_score, under_shape_score

def estimate_total(adapted: dict) -> float:
    h = adapted["home"]
    a = adapted["away"]
    est = (h["corners_for_home_away_avg"] + a["corners_for_home_away_avg"] + h["corners_against_home_away_avg"] + a["corners_against_home_away_avg"]) / 2.0
    pace_boost = (adapted["context"]["expected_pace_shape"] - 50) / 25.0
    return round(max(0.0, est + pace_boost), 2)

def score_over(adapted: dict) -> float:
    h = adapted["home"]; a = adapted["away"]; ctx = adapted["context"]
    score = production_score(h) * 0.25 + production_score(a) * 0.20 + concession_score(h) * 0.15 + concession_score(a) * 0.15 + consistency_score(h) * 0.10 + consistency_score(a) * 0.05 + ctx["expected_pace_shape"] * 0.10
    return round(min(100.0, max(0.0, score)), 2)

def score_under(adapted: dict) -> float:
    h = adapted["home"]; a = adapted["away"]; ctx = adapted["context"]
    score = under_shape_score(h) * 0.25 + under_shape_score(a) * 0.20 + (100 - concession_score(h)) * 0.15 + (100 - concession_score(a)) * 0.15 + (100 - ctx["expected_pace_shape"]) * 0.15 + (100 - ctx["expected_game_state_volatility"]) * 0.10
    return round(min(100.0, max(0.0, score)), 2)
