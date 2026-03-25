from .models import MarketResult

def _clamp(x, lo=0.0, hi=100.0):
    return max(lo, min(hi, x))

def _bos(t):
    return _clamp(22*t.goals_for_90 + 20*min(100.0, t.shots_on_target_90/6.5*100)/100 + 10*min(100.0, t.shots_90/16*100)/100 + 13*t.score_rate_1plus + 5*(t.home_away_attack_split/100))

def _bvs(t):
    return _clamp(24*t.goals_against_90 + 18*min(100.0, t.shots_on_target_against_90/6.0*100)/100 + 10*min(100.0, t.shots_against_90/16*100)/100 + 16*t.concede_rate_1plus + 6*(1-t.clean_sheet_rate) + 4*(t.home_away_defense_split/100))

def _sbi(h, a, odds):
    pos_gap = abs(h.league_position - a.league_position)
    points_gap = abs(h.league_points - a.league_points)
    odd_gap = abs((odds.get('home') or 0) - (odds.get('away') or 0))
    underdog = h if h.league_points < a.league_points else a
    underdog_presence = 0.4*(underdog.score_rate_1plus*100) + 0.3*min(100.0, underdog.shots_on_target_90/5.0*100) + 0.3*min(100.0, underdog.goals_for_90/2.0*100)
    balance = max(0.0, 100 - (pos_gap*4 + points_gap*1.2 + odd_gap*8))
    return _clamp(0.55*balance + 0.45*underdog_presence)

def _ami(t):
    recent_goals = 0.7*t.recent_goals_for_3 + 0.3*t.recent_goals_for_5
    trend = 60 if t.recent_goals_for_3 >= t.recent_goals_for_5 else 40
    return _clamp(32*t.recent_score_rate_1plus + 28*min(100.0, recent_goals/2.2*100)/100 + 24*min(100.0, t.recent_sot/6*100)/100 + 16*(trend/100))

def _fgt(t):
    return _clamp(0.28*(100*t.first_goal_u30_rate) + 0.22*(100*t.first_half_goal_rate) + 0.20*(100*t.response_after_concede_rate) + 0.15*(100*t.goals_both_halves_rate) + 0.15*(100-(100*t.halftime_0_0_rate)))

def _tsi(t):
    variance_penalty = 100 - abs(t.btts_rate - 0.55)*120
    return _clamp(0.45*(t.btts_rate*100) + 0.35*variance_penalty + 0.20*(t.score_rate_1plus*100))

def _xgg_proxy(t):
    proxy = (t.shots_on_target_90*8 + t.shots_90*2)/100
    finishing = min(100.0, t.goals_for_90/max(proxy, 0.8)*60)
    hidden = 100 - finishing
    return _clamp(0.5*hidden + 0.5*t.score_rate_1plus*100)

def evaluate(match):
    hb, ab = _bos(match.home_snapshot), _bos(match.away_snapshot)
    hv, av = _bvs(match.home_snapshot), _bvs(match.away_snapshot)
    ha, aa = _ami(match.home_snapshot), _ami(match.away_snapshot)
    ht, at = _tsi(match.home_snapshot), _tsi(match.away_snapshot)
    hx, ax = _xgg_proxy(match.home_snapshot), _xgg_proxy(match.away_snapshot)
    bos = 0.4*hb + 0.4*ab + 0.2*min(hb, ab)
    bvs = 0.4*hv + 0.4*av + 0.2*min(hv, av)
    sbi = _sbi(match.home_snapshot, match.away_snapshot, match.odds)
    ami = 0.42*ha + 0.42*aa + 0.16*min(ha, aa)
    fgt = 0.5*_fgt(match.home_snapshot) + 0.5*_fgt(match.away_snapshot)
    tsi = 0.42*ht + 0.42*at + 0.16*min(ht, at)
    xgg = 0.42*hx + 0.42*ax + 0.16*min(hx, ax)
    raw = 0.28*bos + 0.28*bvs + 0.16*sbi + 0.10*ami + 0.07*fgt + 0.05*tsi + 0.06*xgg
    penalties = []
    risk_raw = 2
    underdog = match.home_snapshot if match.home_snapshot.league_points < match.away_snapshot.league_points else match.away_snapshot
    if underdog.score_rate_1plus < 0.45 and underdog.shots_on_target_90 < 3.0:
        raw -= 10; penalties.append('underdog_dead'); risk_raw = max(risk_raw, 4)
    if sbi < 45:
        raw -= 6; penalties.append('dominance'); risk_raw = max(risk_raw, 4)
    if (match.home_snapshot.halftime_0_0_rate + match.away_snapshot.halftime_0_0_rate)/2 > 0.28:
        raw -= 5; penalties.append('under'); risk_raw = max(risk_raw, 3)
    score_raw = round(_clamp(raw), 2)
    confidence_raw = 4 if score_raw >= 72 else 3 if score_raw >= 60 else 2 if score_raw >= 45 else 1
    edge_raw = 'strong' if score_raw >= 80 else 'acceptable' if score_raw >= 65 else 'weak'
    eligibility = score_raw >= 60
    drivers = []
    if bos >= 70: drivers.append('bos_strong')
    if bvs >= 70: drivers.append('bvs_supportive')
    if fgt >= 65: drivers.append('fgt_positive')
    if tsi >= 60: drivers.append('tsi_stable_enough')
    rationale = 'Bilateralidade ofensiva suficiente, concessão útil dos dois lados e timing favorável sem bloqueio estrutural forte.' if eligibility else 'Perfil BTTS ainda sem robustez suficiente para elegibilidade, com limitações estruturais ou de risco.'
    return MarketResult(market=match.market, score_raw=score_raw, confidence_raw=confidence_raw, risk_raw=risk_raw, edge_raw=edge_raw, eligibility=eligibility, rationale_summary=rationale, main_drivers=drivers, penalties=penalties, data_quality_flag=match.data_api_context.get('data_quality_flag', 'partial'), module_specific_payload={'btts_direction': match.selection_hint, 'scoring_support': {'bos': round(bos,2), 'ami_bilateral': round(ami,2), 'xg_gap_aggregated': round(xgg,2)}, 'concession_support': {'bvs': round(bvs,2), 'fgt_btts': round(fgt,2), 'sbi': round(sbi,2)}, 'tsi_bilateral': round(tsi,2), 'input_context': match.data_api_context})
