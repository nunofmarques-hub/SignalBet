from __future__ import annotations

def avg(*vals: float) -> float:
    return sum(vals) / len(vals)

def production_score(team: dict) -> float:
    return round(avg(team["corners_for_avg"] * 10, team["corners_for_home_away_avg"] * 10, team["final_third_pressure"], team["crossing_volume"]) / 2.0, 2)

def concession_score(team: dict) -> float:
    return round(avg(team["corners_against_avg"] * 10, team["corners_against_home_away_avg"] * 10, team["defensive_width_tolerance"]) / 2.0, 2)

def consistency_score(team: dict) -> float:
    return round(avg(team["hit_rate_over_4_5"] * 100, team["hit_rate_over_5_5"] * 100, team["opponent_adjustment_quality"]), 2)

def under_shape_score(team: dict) -> float:
    return round(avg((10 - min(team["corners_for_avg"], 10)) * 10, (10 - min(team["corners_for_home_away_avg"], 10)) * 10, 100 - team["crossing_volume"]), 2)
