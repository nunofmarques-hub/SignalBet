from indicators import production_index, concession_index, reliability_index, under_control_index

def estimate_total(adapted):
    h = adapted["home"]; a = adapted["away"]
    est = (h["corners_for_home_away_avg"]+a["corners_for_home_away_avg"]+h["corners_against_home_away_avg"]+a["corners_against_home_away_avg"])/2.0
    pace_boost = (adapted["context"]["expected_pace_shape"] - 50) / 25.0
    return round(max(0.0, est + pace_boost), 2)

def score_over(adapted):
    h = adapted["home"]; a = adapted["away"]; ctx = adapted["context"]
    score = production_index(h)*0.22+production_index(a)*0.18+concession_index(h)*0.14+concession_index(a)*0.14+reliability_index(h)*0.08+reliability_index(a)*0.08+ctx["expected_pace_shape"]*0.10+ctx["expected_game_state_volatility"]*0.06
    return round(min(100.0,max(0.0,score)),2)

def score_under(adapted):
    h = adapted["home"]; a = adapted["away"]; ctx = adapted["context"]
    score = under_control_index(h)*0.22+under_control_index(a)*0.18+(100-concession_index(h))*0.14+(100-concession_index(a))*0.14+reliability_index(h)*0.08+reliability_index(a)*0.08+(100-ctx["expected_pace_shape"])*0.10+(100-ctx["expected_game_state_volatility"])*0.06
    return round(min(100.0,max(0.0,score)),2)
