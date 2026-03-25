from scoring import estimate_total, score_over, score_under, line_strength, apply_penalties
from interpretation import confidence_label, risk_label, band_label, game_profile, market_bias

def choose_line(direction, estimated_total):
    if direction == "Over":
        if estimated_total >= 11.2: return 10.5
        if estimated_total >= 10.0: return 9.5
        return 8.5
    else:
        if estimated_total <= 8.8: return 9.5
        if estimated_total <= 10.0: return 10.5
        return 11.5

def status_from_band(eligible, band):
    if not eligible:
        return "rejected"
    if band in ("Elite", "Forte"):
        return "candidate"
    if band == "Observação":
        return "watchlist"
    return "rejected"

def build_engine_output(adapted, eligible, alerts, exclusions):
    est_total = estimate_total(adapted)
    over_raw, over_blocks = score_over(adapted)
    under_raw, under_blocks = score_under(adapted)

    if over_raw >= under_raw:
        direction = "Over"
        raw_score = over_raw
        blocks = over_blocks
        drivers = [
            "produção combinada acima do padrão",
            "perfil de concessão favorável",
            "contexto de jogo favorável a volume",
        ]
    else:
        direction = "Under"
        raw_score = under_raw
        blocks = under_blocks
        drivers = [
            "produção combinada abaixo do ideal",
            "perfil de concessão baixo",
            "contexto de jogo desfavorável a excesso de cantos",
        ]

    line = choose_line(direction, est_total)
    lstrength = line_strength(direction, est_total, line)
    score_pre_penalty = round(raw_score * 0.68 + lstrength * 0.32, 2)
    final_score, penalty_codes = apply_penalties(score_pre_penalty, alerts, exclusions)

    bias = market_bias(est_total, line)
    all_alerts = list(alerts) + list(exclusions)
    if (bias == "Over" and direction == "Under") or (bias == "Under" and direction == "Over"):
        all_alerts.append("leitura contraditória entre grelha e contexto")
    if abs(est_total - line) <= 0.8:
        all_alerts.append("mercado de fronteira")

    band = band_label(final_score)
    candidate_status = status_from_band(eligible, band)

    confidence = confidence_label(final_score, lstrength, all_alerts)
    risk = risk_label(final_score, lstrength, alerts, exclusions)

    return {
        "fixture_id": adapted["fixture_id"],
        "game": f"{adapted['home_team_name']} vs {adapted['away_team_name']}",
        "competition": adapted["competition"],
        "market": f"{direction} {line} cantos jogo",
        "score": final_score,
        "confidence": confidence,
        "risk": risk,
        "eligible": candidate_status != "rejected",
        "candidate_status": candidate_status,
        "band": band,
        "estimated_total_corners": est_total,
        "main_drivers": drivers,
        "alerts": all_alerts,
        "penalty_codes": penalty_codes,
        "team_scores": {
            "home": round((adapted["home"]["corners_for_avg"] * 10 + adapted["home"]["final_third_pressure"]) / 2, 2),
            "away": round((adapted["away"]["corners_for_avg"] * 10 + adapted["away"]["final_third_pressure"]) / 2, 2),
        },
        "game_profile": game_profile(est_total),
        "market_bias": bias,
        "line_grid": [
            {"market": f"{direction} 8.5 cantos", "score": round(line_strength(direction, est_total, 8.5), 2)},
            {"market": f"{direction} 9.5 cantos", "score": round(line_strength(direction, est_total, 9.5), 2)},
            {"market": f"{direction} 10.5 cantos", "score": round(line_strength(direction, est_total, 10.5), 2)},
            {"market": f"{direction} 11.5 cantos", "score": round(line_strength(direction, est_total, 11.5), 2)},
        ],
        "rationale": {
            "score_base_over": over_raw,
            "score_base_under": under_raw,
            "selected_direction": direction,
            "selected_line": line,
            "line_strength": lstrength,
            "score_pre_penalty": score_pre_penalty,
            "band": band,
            "candidate_status": candidate_status,
            "confidence_logic": confidence,
            "risk_logic": risk,
            "blocks": blocks,
        },
        "operational_conclusion": f"Jogo com perfil {game_profile(est_total).lower()} para cantos. A linha principal escolhida foi {line} porque a projeção estimada ficou em {est_total}. O score final caiu em banda {band.lower()}, a confiança ficou {confidence.lower()} e o risco ficou {risk.lower()}.",
    }
