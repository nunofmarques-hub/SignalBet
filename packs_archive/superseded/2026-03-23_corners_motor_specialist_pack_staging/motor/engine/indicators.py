def avg(*vals): return sum(vals)/len(vals)

def production_index(team):
    return round(avg(team["corners_for_avg"]*10, team["corners_for_home_away_avg"]*10, team["shots_avg"]*4, team["shots_on_target_avg"]*8, team["final_third_pressure"], team["crossing_volume"], team["territorial_proxy"])/3.0, 2)

def concession_index(team):
    return round(avg(team["corners_against_avg"]*10, team["corners_against_home_away_avg"]*10, team["total_match_corners_avg"]*8)/2.0, 2)

def frequency_index(team):
    return round(avg(team["hit_rate_over_8_5"]*100, team["hit_rate_over_9_5"]*100, team["hit_rate_over_10_5"]*100), 2)

def role_behavior_index(team, role):
    delta = team["as_favorite_corner_delta"] if role == "favorite" else team["as_underdog_corner_delta"]
    return round(50 + (delta*25), 2)

def reliability_index(team):
    return round(avg(min(100.0, team["sample_size"]*10), team["opponent_adjustment_quality"], frequency_index(team)), 2)

def under_control_index(team):
    return round(avg((10-min(team["corners_for_avg"],10))*10, (10-min(team["corners_for_home_away_avg"],10))*10, 100-team["crossing_volume"], 100-team["final_third_pressure"], 100-team["territorial_proxy"]), 2)
