from __future__ import annotations


def fair_odd(probability: float) -> float:
    probability = max(0.0001, min(0.9999, probability))
    return round(1.0 / probability, 2)


def calculate_edge(market_odd: float, model_fair_odd: float) -> float:
    if model_fair_odd <= 0:
        return 0.0
    return round((market_odd / model_fair_odd) - 1.0, 4)


def classify_value(edge: float) -> str:
    if edge >= 0.08:
        return 'VALUE STRONG'
    if edge >= 0.05:
        return 'VALUE'
    return 'NO VALUE'


def estimated_market_odd(market_name: str, probability: float) -> float:
    if market_name == 'Over 1.5 jogo':
        factor = 1.038
    elif market_name == 'Under 3.5':
        factor = 1.048
    elif market_name.endswith('Over 1.5'):
        factor = 1.068
    else:
        factor = 1.05
    return round(fair_odd(probability) * factor, 2)


def enrich_market_with_value(probability_row: dict, market_odd: float | None = None, odd_source: str = 'ESTIMATED') -> dict:
    probability = float(probability_row['probability'])
    fair = fair_odd(probability)
    odd = market_odd if market_odd is not None else estimated_market_odd(probability_row['market'], probability)
    source = odd_source if market_odd is not None else 'ESTIMATED'
    edge = calculate_edge(odd, fair)
    return {**probability_row, 'fair_odd': fair, 'market_odd': odd, 'odds_source': source, 'edge': edge, 'value_label': classify_value(edge)}
