from scoring import estimate_total, score_over, score_under, apply_penalties
from interpretation import confidence_label, risk_label, band_label, game_profile, market_bias

def choose_line(direction, estimated_total):
    if direction == "Over":
        if estimated_total >= 11.0: return 10.5
        if estimated_total >= 9.8: return 9.5
        return 8.5
    else:
        if estimated_total <= 8.8: return 9.5
        if estimated_total <= 10.0: return 10.5
        return 11.5

def build_engine_output(adapted, eligible, alerts, exclusions):
    est_total = estimate_total(adapted)
    over_raw, over_blocks = score_over(adapted)
    under_raw, under_blocks = score_under(adapted)
    if over_raw >= under_raw:
        direction = "Over"; raw_score = over_raw; blocks = over_blocks
        drivers = ["produção combinada acima do padrão","perfil de concessão favorável","contexto de jogo favorável a volume"]
    else:
        direction = "Under"; raw_score = under_raw; blocks = under_blocks
        drivers = ["produção combinada abaixo do ideal","perfil de concessão baixo","contexto de jogo desfavorável a excesso de cantos"]
    final_score, penalty_codes = apply_penalties(raw_score, alerts, exclusions)
    line = choose_line(direction, est_total)
    bias = market_bias(est_total, line)
    all_alerts = list(alerts) + list(exclusions)
    if (bias == "Over" and direction == "Under") or (bias == "Under" and direction == "Over"):
        all_alerts.append("leitura contraditória entre grelha e contexto")
    if abs(est_total - line) <= 0.8:
        all_alerts.append("mercado de fronteira")
    band = band_label(final_score)
    candidate_status = "candidate" if eligible and band in ("Elite","Forte") else ("watchlist" if eligible and band == "Observação" else "rejected")
    return {
        "fixture_id": adapted["fixture_id"],
        "game": f"{adapted['home_team_name']} vs {adapted['away_team_name']}",
        "competition": adapted["competition"],
        "market": f"{direction} {line} cantos jogo",
        "score": final_score,
        "confidence": confidence_label(final_score),
        "risk": risk_label(final_score),
        "eligible": eligible and candidate_status != "rejected",
        "candidate_status": candidate_status,
        "band": band,
        "estimated_total_corners": est_total,
        "main_drivers": drivers,
        "alerts": all_alerts,
        "penalty_codes": penalty_codes,
        "team_scores": {"home": round((adapted["home"]["corners_for_avg"]*10 + adapted["home"]["final_third_pressure"])/2,2), "away": round((adapted["away"]["corners_for_avg"]*10 + adapted["away"]["final_third_pressure"])/2,2)},
        "game_profile": game_profile(est_total),
        "market_bias": bias,
        "line_grid": [{"market": f"{direction} 8.5 cantos", "score": round(min(100.0, max(0.0, final_score+8)),2)}, {"market": f"{direction} 9.5 cantos", "score": round(final_score,2)}, {"market": f"{direction} 10.5 cantos", "score": round(min(100.0, max(0.0, final_score-8)),2)}, {"market": f"{direction} 11.5 cantos", "score": round(min(100.0, max(0.0, final_score-16)),2)}],
        "rationale": {"score_base_over": over_raw, "score_base_under": under_raw, "selected_direction": direction, "selected_line": line, "band": band, "candidate_status": candidate_status, "blocks": blocks},
        "operational_conclusion": f"Jogo com perfil {game_profile(est_total).lower()} para cantos. O sinal principal aparece em {direction.lower()} {line} cantos jogo com banda {band.lower()}."
    }
