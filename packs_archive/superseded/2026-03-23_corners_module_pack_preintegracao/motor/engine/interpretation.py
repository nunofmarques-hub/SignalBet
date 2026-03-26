from __future__ import annotations

def confidence_label(score: float) -> str:
    if score >= 78: return "Alta"
    if score >= 60: return "Média"
    return "Baixa"

def strength_label(score: float) -> str:
    if score >= 86: return "Muito Forte"
    if score >= 72: return "Forte"
    if score >= 60: return "Aceitável"
    if score >= 50: return "Marginal"
    return "Fraco"

def risk_label() -> str:
    return "Baixo"

def game_profile(estimated_total: float) -> str:
    if estimated_total >= 11.2: return "Volume Alto"
    if estimated_total >= 9.6: return "Volume Médio/Alto"
    if estimated_total >= 8.3: return "Volume Médio"
    return "Volume Baixo"

def market_bias(estimated_total: float, line: float) -> str:
    diff = estimated_total - line
    if diff >= 1.2: return "Over"
    if diff <= -1.2: return "Under"
    return "Zona Cinzenta"
