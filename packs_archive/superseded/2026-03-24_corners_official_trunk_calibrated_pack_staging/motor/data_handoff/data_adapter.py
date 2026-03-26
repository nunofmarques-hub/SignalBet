def _n(v):
    if v is None: return 0.0
    if isinstance(v, str) and v.endswith('%'): return float(v[:-1])
    return float(v)

def _smap(rows):
    d = {}
    for r in rows: d[r['type']] = _n(r.get('value'))
    return d

def adapt_from_official_trunk(fixture_obj, fixture_statistics, case_ctx):
    home = fixture_obj['teams']['home']; away = fixture_obj['teams']['away']
    hs = _smap(next(x for x in fixture_statistics if x['team']['id']==home['id'])['statistics'])
    aw = _smap(next(x for x in fixture_statistics if x['team']['id']==away['id'])['statistics'])
    return {
        'case_id': case_ctx['case_id'],
        'fixture_id': fixture_obj['fixture']['id'],
        'competition': fixture_obj['league']['name'],
        'season': fixture_obj['league']['season'],
        'kickoff_datetime': None,
        'competitive_state': case_ctx['competitive_state'],
        'home_team_name': home['name'],
        'away_team_name': away['name'],
        'home_role': case_ctx['home_role'],
        'away_role': case_ctx['away_role'],
        'home': {'sample_size': case_ctx['sample_size'],'corners_for_avg': case_ctx['home_corners_for_avg'],'corners_against_avg': case_ctx['home_corners_against_avg'],'corners_for_home_away_avg': max(case_ctx['home_corners_for_avg'], hs.get('Corner Kicks',0)),'corners_against_home_away_avg': case_ctx['home_corners_against_avg'],'total_match_corners_avg': hs.get('Corner Kicks',0)+aw.get('Corner Kicks',0),'recent_corners_for': case_ctx['home_recent_for'],'recent_corners_against': case_ctx['home_recent_against'],'shots_avg': hs.get('Total Shots',0),'shots_on_target_avg': case_ctx['home_sot'],'crossing_volume': case_ctx['home_cross'],'final_third_pressure': case_ctx['home_pressure'],'territorial_proxy': hs.get('Ball Possession',0),'hit_rate_over_8_5': case_ctx['home_hr85'],'hit_rate_over_9_5': case_ctx['home_hr95'],'hit_rate_over_10_5': case_ctx['home_hr105'],'as_favorite_corner_delta': case_ctx['home_fav_delta'],'as_underdog_corner_delta': case_ctx['home_dog_delta'],'opponent_adjustment_quality': case_ctx['home_qa']},
        'away': {'sample_size': case_ctx['sample_size'],'corners_for_avg': case_ctx['away_corners_for_avg'],'corners_against_avg': case_ctx['away_corners_against_avg'],'corners_for_home_away_avg': max(case_ctx['away_corners_for_avg'], aw.get('Corner Kicks',0)),'corners_against_home_away_avg': case_ctx['away_corners_against_avg'],'total_match_corners_avg': hs.get('Corner Kicks',0)+aw.get('Corner Kicks',0),'recent_corners_for': case_ctx['away_recent_for'],'recent_corners_against': case_ctx['away_recent_against'],'shots_avg': aw.get('Total Shots',0),'shots_on_target_avg': case_ctx['away_sot'],'crossing_volume': case_ctx['away_cross'],'final_third_pressure': case_ctx['away_pressure'],'territorial_proxy': aw.get('Ball Possession',0),'hit_rate_over_8_5': case_ctx['away_hr85'],'hit_rate_over_9_5': case_ctx['away_hr95'],'hit_rate_over_10_5': case_ctx['away_hr105'],'as_favorite_corner_delta': case_ctx['away_fav_delta'],'as_underdog_corner_delta': case_ctx['away_dog_delta'],'opponent_adjustment_quality': case_ctx['away_qa']},
        'context': {'expected_pace_shape': case_ctx['pace'],'tactical_asymmetry': case_ctx['asym'],'expected_game_state_volatility': case_ctx['vol'],'likely_rotation': case_ctx['rotation'],'low_data_quality': case_ctx['lowq'],'weather_disruption': False,'unstable_tactical_profile': case_ctx['unstable']}
    }
