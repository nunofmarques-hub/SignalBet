def band_label(score):
    if score >= 86: return "Elite"
    if score >= 72: return "Forte"
    if score >= 58: return "Observação"
    return "Rejeitar"

def confidence_label(score, line_strength, alerts):
    penalty = 0
    if alerts:
        penalty += 1
    composite = score * 0.7 + line_strength * 0.3 - penalty * 6
    if composite >= 80: return "Alta"
    if composite >= 64: return "Média"
    return "Baixa"

def risk_label(score, line_strength, alerts, exclusions):
    risk_score = 100 - (score * 0.55 + line_strength * 0.25 + (0 if exclusions else 12) + (0 if not alerts else 6))
    if risk_score <= 28: return "Baixo"
    if risk_score <= 48: return "Médio"
    return "Alto"

def game_profile(estimated_total):
    if estimated_total >= 11.2: return "Volume Alto"
    if estimated_total >= 9.6: return "Volume Médio/Alto"
    if estimated_total >= 8.3: return "Volume Médio"
    return "Volume Baixo"

def market_bias(estimated_total, line):
    diff = estimated_total - line
    if diff >= 1.2: return "Over"
    if diff <= -1.2: return "Under"
    return "Zona Cinzenta"
