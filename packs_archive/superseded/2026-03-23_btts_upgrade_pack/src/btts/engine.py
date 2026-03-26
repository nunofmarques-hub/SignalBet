from __future__ import annotations
from .models import MatchInput, MarketResult

def _clamp(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))

def _bos(team):
    score = (
        22 * team.goals_for_90
        + 20 * min(100.0, team.shots_on_target_90 / 6.5 * 100) / 100
        + 10 * min(100.0, team.shots_90 / 16 * 100) / 100
        + 13 * team.score_rate_1plus
        + 5 * (team.home_away_attack_split / 100)
    )
    return _clamp(score)

def _bvs(team):
    cs_inv = 1 - team.clean_sheet_rate
    score = (
        24 * team.goals_against_90
        + 18 * min(100.0, team.shots_on_target_against_90 / 6.0 * 100) / 100
        + 10 * min(100.0, team.shots_against_90 / 16 * 100) / 100
        + 16 * team.concede_rate_1plus
        + 6 * cs_inv
        + 4 * (team.home_away_defense_split / 100)
    )
    return _clamp(score)

def _sbi(home, away, odds):
    pos_gap = abs(home.league_position - away.league_position)
    points_gap = abs(home.league_points - away.league_points)
    odd_gap = abs((odds.get("home") or 0) - (odds.get("away") or 0))
    underdog = home if home.league_points < away.league_points else away
    underdog_presence = (
        0.4 * (underdog.score_rate_1plus * 100)
        + 0.3 * min(100.0, underdog.shots_on_target_90 / 5.0 * 100)
        + 0.3 * min(100.0, underdog.goals_for_90 / 2.0 * 100)
    )
    balance = max(0.0, 100 - (pos_gap * 4 + points_gap * 1.2 + odd_gap * 8))
    return _clamp(0.55 * balance + 0.45 * underdog_presence)

def _ami(team):
    recent_goals = 0.7 * team.recent_goals_for_3 + 0.3 * team.recent_goals_for_5
    trend = 60 if team.recent_goals_for_3 >= team.recent_goals_for_5 else 40
    return _clamp(
        32 * team.recent_score_rate_1plus
        + 28 * min(100.0, recent_goals / 2.2 * 100) / 100
        + 24 * min(100.0, team.recent_sot / 6 * 100) / 100
        + 16 * (trend / 100)
    )

def _fgt(team):
    deadlock = 100 * team.halftime_0_0_rate
    early = 100 * team.first_goal_u30_rate
    first_half = 100 * team.first_half_goal_rate
    response = 100 * team.response_after_concede_rate
    both_halves = 100 * team.goals_both_halves_rate
    return _clamp(0.28*early + 0.22*first_half + 0.20*response + 0.15*both_halves + 0.15*(100-deadlock))

def _tsi(team):
    variance_penalty = 100 - abs(team.btts_rate - 0.55) * 120
    return _clamp(0.45 * (team.btts_rate * 100) + 0.35 * variance_penalty + 0.20 * (team.score_rate_1plus * 100))

def _xg_gap_proxy(team):
    proxy = (team.shots_on_target_90 * 8 + team.shots_90 * 2) / 100
    finishing = min(100.0, team.goals_for_90 / max(proxy, 0.8) * 60)
    hidden = 100 - finishing
    return _clamp(0.5 * hidden + 0.5 * team.score_rate_1plus * 100)

def evaluate(match: MatchInput) -> MarketResult:
    home_bos = _bos(match.home_snapshot); away_bos = _bos(match.away_snapshot)
    home_bvs = _bvs(match.home_snapshot); away_bvs = _bvs(match.away_snapshot)
    home_ami = _ami(match.home_snapshot); away_ami = _ami(match.away_snapshot)
    home_tsi = _tsi(match.home_snapshot); away_tsi = _tsi(match.away_snapshot)
    home_xgg = _xg_gap_proxy(match.home_snapshot); away_xgg = _xg_gap_proxy(match.away_snapshot)

    bos = 0.4 * home_bos + 0.4 * away_bos + 0.2 * min(home_bos, away_bos)
    bvs = 0.4 * home_bvs + 0.4 * away_bvs + 0.2 * min(home_bvs, away_bvs)
    sbi = _sbi(match.home_snapshot, match.away_snapshot, match.odds)
    ami = 0.42 * home_ami + 0.42 * away_ami + 0.16 * min(home_ami, away_ami)
    fgt = 0.5 * _fgt(match.home_snapshot) + 0.5 * _fgt(match.away_snapshot)
    tsi = 0.42 * home_tsi + 0.42 * away_tsi + 0.16 * min(home_tsi, away_tsi)
    xgg = 0.42 * home_xgg + 0.42 * away_xgg + 0.16 * min(home_xgg, away_xgg)

    raw = 0.28*bos + 0.28*bvs + 0.16*sbi + 0.10*ami + 0.07*fgt + 0.05*tsi + 0.06*xgg
    penalties = []
    risk_raw = 2

    underdog = match.home_snapshot if match.home_snapshot.league_points < match.away_snapshot.league_points else match.away_snapshot
    if underdog.score_rate_1plus < 0.45 and underdog.shots_on_target_90 < 3.0:
        raw -= 10
        penalties.append("underdog_dead")
        risk_raw = max(risk_raw, 4)
    if sbi < 45:
        raw -= 6
        penalties.append("dominance")
        risk_raw = max(risk_raw, 4)
    avg_deadlock = (match.home_snapshot.halftime_0_0_rate + match.away_snapshot.halftime_0_0_rate)/2
    if avg_deadlock > 0.28:
        raw -= 5
        penalties.append("under")
        risk_raw = max(risk_raw, 3)

    score_raw = round(_clamp(raw), 2)
    confidence_raw = 4 if score_raw >= 72 else 3 if score_raw >= 60 else 2 if score_raw >= 45 else 1
    edge_raw = "strong" if score_raw >= 80 else "acceptable" if score_raw >= 65 else "weak"
    eligibility = score_raw >= 60
    data_quality_flag = match.data_api_context.get("data_quality_flag", "partial")

    drivers = []
    if bos >= 70: drivers.append("bos_strong")
    if bvs >= 70: drivers.append("bvs_supportive")
    if fgt >= 65: drivers.append("fgt_positive")
    if tsi >= 60: drivers.append("tsi_stable_enough")

    missing_fields = match.data_api_context.get("missing_fields", [])
    rationale = (
        "Bilateralidade ofensiva suficiente, concessão útil dos dois lados e timing favorável sem bloqueio estrutural forte."
        if eligibility else
        "Perfil BTTS ainda sem robustez suficiente para elegibilidade, com limitações estruturais ou de risco."
    )

    return MarketResult(
        market=match.market,
        score_raw=score_raw,
        confidence_raw=confidence_raw,
        risk_raw=risk_raw,
        edge_raw=edge_raw,
        eligibility=eligibility,
        rationale_summary=rationale,
        main_drivers=drivers,
        penalties=penalties,
        data_quality_flag=data_quality_flag,
        module_specific_payload={
            "btts_direction": match.selection_hint,
            "scoring_support": {"bos": round(bos, 2), "ami_bilateral": round(ami, 2), "xg_gap_aggregated": round(xgg, 2)},
            "concession_support": {"bvs": round(bvs, 2), "fgt_btts": round(fgt, 2), "sbi": round(sbi, 2)},
            "tsi_bilateral": round(tsi, 2),
            "input_context": {
                "provider": match.data_api_context.get("provider"),
                "provider_version": match.data_api_context.get("provider_version"),
                "source_profile": match.data_api_context.get("source_profile"),
                "missing_fields": missing_fields,
            },
        },
    )
