from scoring import estimate_total, score_over, score_under
from interpretation import confidence_label, strength_label, risk_label, game_profile, market_bias

def build_engine_output(adapted, eligibility, eligibility_alerts):
    est_total = estimate_total(adapted)
    over = score_over(adapted)
    under = score_under(adapted)
    if over >= under:
        direction = "Over"; line = 9.5 if est_total >= 10.2 else 8.5; score = over
        drivers = ["produção combinada acima do padrão","perfil de concessão favorável","contexto de jogo favorável a volume"]
    else:
        direction = "Under"; line = 11.5 if est_total <= 10.8 else 10.5; score = under
        drivers = ["produção combinada abaixo do ideal","perfil de concessão baixo"]
    alerts = list(eligibility_alerts)
    bias = market_bias(est_total, line)
    if (bias == "Over" and direction == "Under") or (bias == "Under" and direction == "Over"):
        alerts.append("leitura contraditória entre grelha e contexto")
    if abs(est_total - line) <= 0.8:
        alerts.append("mercado de fronteira")
    conf = confidence_label(score)
    strength = strength_label(score)
    return {
        "fixture_id": adapted["fixture_id"],
        "game": f"{adapted['home_team_name']} vs {adapted['away_team_name']}",
        "competition": adapted["competition"],
        "market": f"{direction} {line} cantos jogo",
        "score": score,
        "confidence": conf,
        "risk": risk_label(score),
        "eligible": eligibility,
        "estimated_total_corners": est_total,
        "main_drivers": drivers,
        "alerts": alerts,
        "team_scores": {"home": round((adapted["home"]["corners_for_avg"]*10+adapted["home"]["final_third_pressure"])/2,2), "away": round((adapted["away"]["corners_for_avg"]*10+adapted["away"]["final_third_pressure"])/2,2)},
        "game_profile": game_profile(est_total),
        "market_bias": bias,
        "line_grid": [
            {"market": f"{direction} 8.5 cantos", "score": round(min(100.0, max(0.0, score+8)),2), "confidence": conf, "risk": risk_label(score), "eligible": eligibility},
            {"market": f"{direction} 9.5 cantos", "score": round(score,2), "confidence": conf, "risk": risk_label(score), "eligible": eligibility},
            {"market": f"{direction} 10.5 cantos", "score": round(min(100.0, max(0.0, score-8)),2), "confidence": conf, "risk": risk_label(score), "eligible": eligibility},
            {"market": f"{direction} 11.5 cantos", "score": round(min(100.0, max(0.0, score-16)),2), "confidence": conf, "risk": risk_label(score), "eligible": eligibility},
        ],
        "operational_conclusion": f"Jogo com perfil {game_profile(est_total).lower()} para cantos. O sinal principal aparece em {direction.lower()} {line} cantos jogo com força {strength.lower()}."
    }
