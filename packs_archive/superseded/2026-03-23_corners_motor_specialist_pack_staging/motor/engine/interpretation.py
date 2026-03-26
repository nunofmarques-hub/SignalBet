def confidence_label(score):
    if score >= 78: return "Alta"
    if score >= 62: return "Média"
    return "Baixa"

def risk_label(score):
    if score >= 78: return "Baixo"
    if score >= 62: return "Médio"
    return "Alto"

def band_label(score):
    if score >= 86: return "Elite"
    if score >= 72: return "Forte"
    if score >= 58: return "Observação"
    return "Rejeitar"

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
