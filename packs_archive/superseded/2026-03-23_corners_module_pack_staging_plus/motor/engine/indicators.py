def production_index(team):
    return round(((team["corners_for_avg"]*10)+(team["corners_for_home_away_avg"]*10)+team["final_third_pressure"]+team["crossing_volume"])/4,2)

def concession_index(team):
    return round(((team["corners_against_avg"]*10)+(team["corners_against_home_away_avg"]*10)+team["defensive_width_tolerance"])/3,2)

def reliability_index(team):
    return round((team["opponent_adjustment_quality"]+min(100.0, team["sample_size"]*10)+(team["hit_rate_over_4_5"]*100)+(team["conceded_rate_over_4_5"]*100))/4,2)

def under_control_index(team):
    return round((((10-min(team["corners_for_avg"],10))*10)+((10-min(team["corners_for_home_away_avg"],10))*10)+(100-team["crossing_volume"])+(100-team["final_third_pressure"]))/4,2)
