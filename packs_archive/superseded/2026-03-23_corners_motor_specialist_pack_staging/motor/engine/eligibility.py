def evaluate_eligibility(adapted):
    alerts = []
    exclusions = []
    home = adapted["home"]; away = adapted["away"]; ctx = adapted["context"]
    if ctx.get("low_data_quality"): exclusions.append("qualidade de dados insuficiente")
    if home.get("sample_size",0) < 4 or away.get("sample_size",0) < 4: exclusions.append("amostra insuficiente")
    if home.get("opponent_adjustment_quality",0) < 35 or away.get("opponent_adjustment_quality",0) < 35: exclusions.append("ajustamento por adversário demasiado fraco")
    if ctx.get("likely_rotation"): alerts.append("rotação provável")
    if ctx.get("unstable_tactical_profile"): alerts.append("perfil tático instável")
    return len(exclusions) == 0, alerts, exclusions
