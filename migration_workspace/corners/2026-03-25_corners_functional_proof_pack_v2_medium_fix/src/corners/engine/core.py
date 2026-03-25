def eval_case(adapted):
    h = adapted["home"]; a = adapted["away"]; c = adapted["context"]

    est = ((h["corners_for_home_away_avg"] + a["corners_for_home_away_avg"] +
            h["corners_against_home_away_avg"] + a["corners_against_home_away_avg"]) / 2.0)
    est += (c["expected_pace_shape"] - 50) / 18.0
    est = round(max(0.0, est), 2)

    over_raw = (
        h["corners_for_avg"] * 10 * 0.18 +
        a["corners_for_avg"] * 10 * 0.16 +
        h["shots_avg"] * 4 * 0.10 +
        a["shots_avg"] * 4 * 0.08 +
        h["final_third_pressure"] * 0.10 +
        a["final_third_pressure"] * 0.08 +
        h["territorial_proxy"] * 0.06 +
        a["territorial_proxy"] * 0.04 +
        h["hit_rate_over_9_5"] * 100 * 0.08 +
        a["hit_rate_over_9_5"] * 100 * 0.06 +
        c["expected_pace_shape"] * 0.04 +
        c["expected_game_state_volatility"] * 0.02
    )
    under_raw = (100 - over_raw) * 0.7

    direction = "Over" if over_raw >= under_raw else "Under"
    line = 10.5 if direction == "Over" and est >= 11.2 else (9.5 if direction == "Over" and est >= 10.0 else (8.5 if direction == "Over" else 10.5))
    line_strength = max(0, min(100, 52 + ((est - line) * 20 if direction == "Over" else (line - est) * 20)))

    score_pre = (over_raw if direction == "Over" else under_raw) * 0.66 + line_strength * 0.34

    alerts = []
    exclusions = []
    if c["low_data_quality"]:
        exclusions.append("qualidade de dados insuficiente")
    if h["sample_size"] < 4 or a["sample_size"] < 4:
        exclusions.append("amostra insuficiente")
    if h["opponent_adjustment_quality"] < 35 or a["opponent_adjustment_quality"] < 35:
        exclusions.append("ajustamento por adversário demasiado fraco")
    if c["likely_rotation"]:
        alerts.append("rotação provável")
    if c["unstable_tactical_profile"]:
        alerts.append("perfil tático instável")

    final = score_pre
    if "rotação provável" in alerts:
        final -= 6
    if "perfil tático instável" in alerts:
        final -= 8
    if exclusions:
        final -= 25
    final = round(max(0.0, final), 2)

    # surgical fix: Observação threshold 57 instead of 58
    band = "Elite" if final >= 86 else ("Forte" if final >= 72 else ("Observação" if final >= 57 else "Rejeitar"))
    status = "candidate" if (not exclusions and band in ("Elite", "Forte")) else ("watchlist" if (not exclusions and band == "Observação") else "rejected")

    conf_comp = final * 0.7 + line_strength * 0.3 - (6 if alerts else 0)
    confidence = "Alta" if conf_comp >= 80 else ("Média" if conf_comp >= 64 else "Baixa")

    risk_score = 100 - (final * 0.55 + line_strength * 0.25 + (0 if exclusions else 12) + (0 if not alerts else 6))
    risk = "Baixo" if risk_score <= 28 else ("Médio" if risk_score <= 48 else "Alto")

    profile = "Volume Alto" if est >= 11.2 else ("Volume Médio/Alto" if est >= 9.6 else "Volume Médio")
    bias = "Over" if est - line >= 1.2 else ("Under" if est - line <= -1.2 else "Zona Cinzenta")

    return {
        "fixture_id": adapted["fixture_id"],
        "game": f"{adapted['home_team_name']} vs {adapted['away_team_name']}",
        "competition": adapted["competition"],
        "market": f"{direction} {line} cantos jogo",
        "score": final,
        "confidence": confidence,
        "risk": risk,
        "eligible": status != "rejected",
        "candidate_status": status,
        "band": band,
        "estimated_total_corners": est,
        "main_drivers": ["produção combinada acima do padrão"] if direction == "Over" else ["produção combinada abaixo do ideal"],
        "alerts": alerts + exclusions,
        "team_scores": {
            "home": round((h["corners_for_avg"] * 10 + h["final_third_pressure"]) / 2, 2),
            "away": round((a["corners_for_avg"] * 10 + a["final_third_pressure"]) / 2, 2),
        },
        "game_profile": profile,
        "market_bias": bias,
        "line_grid": [
            {"market": f"{direction} 8.5 cantos", "score": round(max(0, min(100, 52 + ((est - 8.5) * 20 if direction == 'Over' else (8.5 - est) * 20))), 2)},
            {"market": f"{direction} 9.5 cantos", "score": round(max(0, min(100, 52 + ((est - 9.5) * 20 if direction == 'Over' else (9.5 - est) * 20))), 2)},
            {"market": f"{direction} 10.5 cantos", "score": round(max(0, min(100, 52 + ((est - 10.5) * 20 if direction == 'Over' else (10.5 - est) * 20))), 2)},
        ],
        "rationale": {
            "selected_line": line,
            "corner_projection": est,
            "candidate_status": status,
            "band": band,
        },
        "operational_conclusion": f"Projeção {est}, linha {line}, score {final}, confiança {confidence}, risco {risk}.",
    }
