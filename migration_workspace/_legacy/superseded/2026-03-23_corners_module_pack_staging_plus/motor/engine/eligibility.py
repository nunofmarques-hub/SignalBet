def evaluate_eligibility(adapted):
    alerts = []
    home = adapted["home"]
    away = adapted["away"]
    ctx = adapted["context"]
    if ctx.get("low_data_quality"):
        alerts.append("qualidade de dados insuficiente")
    if home.get("sample_size", 0) < 4 or away.get("sample_size", 0) < 4:
        alerts.append("amostra insuficiente")
    if home.get("opponent_adjustment_quality", 0) < 35 or away.get("opponent_adjustment_quality", 0) < 35:
        alerts.append("ajustamento por adversário demasiado fraco")
    return len(alerts) == 0, alerts
