from __future__ import annotations

from typing import Any


def rank_markets(markets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        markets,
        key=lambda row: (
            1 if row.get('odds_source') != 'ESTIMATED' else 0,
            row.get('engine_score', 0.0),
            row.get('edge', 0.0),
            row.get('probability', 0.0),
        ),
        reverse=True,
    )


def evaluate_market(market_row: dict[str, Any], *, for_best_of_day: bool = False) -> dict[str, Any]:
    engine = market_row.get('engine', '')
    edge = market_row.get('edge', 0.0)
    probability = market_row.get('probability', 0.0)
    risk_balance = market_row.get('risk_balance', 0.0)
    engine_score = market_row.get('engine_score', 0.0)
    favorite_margin = abs(market_row.get('favorite_margin', 0.0))
    fdi = market_row.get('fdi', 0.0)
    uli = market_row.get('uli', 0.0)
    ltr = market_row.get('ltr', 0.0)

    base_edge_min = 0.032 if not for_best_of_day else 0.048
    base_prob_min = 0.47 if not for_best_of_day else 0.51
    engine_score_min = 4.9 if not for_best_of_day else 5.7

    if engine == 'O15_TEAM':
        base_prob_min = 0.50 if not for_best_of_day else 0.55
        engine_score_min = 5.2 if not for_best_of_day else 5.9
        if fdi >= 6.6:
            base_edge_min -= 0.003
            engine_score_min -= 0.15
        if favorite_margin >= 0.65:
            base_prob_min -= 0.01
    elif engine == 'U35':
        base_prob_min = 0.52 if not for_best_of_day else 0.55
        base_edge_min = 0.027 if not for_best_of_day else 0.039
        engine_score_min = 4.75 if not for_best_of_day else 5.35
        if uli >= 5.7 and ltr >= 4.9:
            base_edge_min -= 0.004
            engine_score_min -= 0.18
        if favorite_margin < 0.55 and risk_balance <= 0.90:
            base_edge_min -= 0.003
            engine_score_min -= 0.10
    elif engine == 'O15_GAME':
        base_prob_min = 0.54 if not for_best_of_day else 0.58
        engine_score_min = 5.35 if not for_best_of_day else 6.05
        if risk_balance >= 0.85:
            base_edge_min += 0.004

    if edge < base_edge_min:
        return {'valid': False, 'reason': 'Bloqueado por edge', 'detail': f'edge {edge:.1%} abaixo do mínimo {base_edge_min:.1%}.', 'near_miss': edge >= base_edge_min - 0.01}
    if probability < base_prob_min:
        return {'valid': False, 'reason': 'Bloqueado por probabilidade', 'detail': f'probabilidade {probability:.1%} abaixo do mínimo {base_prob_min:.1%}.', 'near_miss': probability >= base_prob_min - 0.025}
    if engine_score < engine_score_min:
        return {'valid': False, 'reason': 'Bloqueado por score do motor', 'detail': f'score {engine_score:.2f} abaixo do mínimo {engine_score_min:.2f}.', 'near_miss': engine_score >= engine_score_min - 0.4}
    if engine == 'O15_TEAM' and favorite_margin < 0.20:
        return {'valid': False, 'reason': 'Bloqueado por favorito fraco', 'detail': 'margem do favorito ainda demasiado curta.', 'near_miss': favorite_margin >= 0.16}
    if engine == 'O15_GAME' and risk_balance > (1.05 if not for_best_of_day else 0.95) and edge < (0.048 if not for_best_of_day else 0.058):
        return {'valid': False, 'reason': 'Bloqueado por risco', 'detail': f'jogo demasiado equilibrado para O15 jogo (risk {risk_balance:.2f}).', 'near_miss': edge >= (0.043 if not for_best_of_day else 0.053)}
    if engine == 'U35' and market_row.get('over_game_strength', 0.0) > 7.0 and edge < (0.036 if not for_best_of_day else 0.048):
        return {'valid': False, 'reason': 'Bloqueado por conflito ofensivo', 'detail': 'força ofensiva global demasiado alta para under com este edge.', 'near_miss': edge >= (0.032 if not for_best_of_day else 0.044)}
    return {'valid': True, 'reason': 'Válido', 'detail': 'Passou nos filtros do motor.', 'near_miss': False}


def _engine_priority_bonus(market: dict[str, Any]) -> float:
    engine = market.get('engine', '')
    bonus = 0.0
    if engine == 'O15_TEAM':
        bonus += max(0.0, (market.get('fdi', 0.0) - 6.0) * 0.15)
        bonus += max(0.0, abs(market.get('favorite_margin', 0.0)) - 0.55) * 0.22
    elif engine == 'U35':
        bonus += max(0.0, (market.get('uli', 0.0) - 5.0) * 0.28)
        bonus += max(0.0, (market.get('ltr', 0.0) - 4.4) * 0.26)
        if abs(market.get('favorite_margin', 0.0)) < 0.60:
            bonus += 0.18
        if market.get('risk_balance', 0.0) <= 0.90:
            bonus += 0.14
        if market.get('mtd', 0.0) <= 2.2:
            bonus += 0.12
    elif engine == 'O15_GAME':
        bonus -= max(0.0, market.get('risk_balance', 0.0) - 0.80) * 0.38
    return round(bonus, 3)


def _winner_score(market: dict[str, Any]) -> float:
    return round(
        market.get('engine_score', 0.0)
        + market.get('edge', 0.0) * 100 * 0.12
        + market.get('probability', 0.0) * 10 * 0.06
        + _engine_priority_bonus(market),
        3,
    )


def analyze_match_markets(markets: list[dict[str, Any]]) -> dict[str, Any]:
    ranked = rank_markets(markets)
    analysis = {'selected': None, 'top_candidate': ranked[0] if ranked else None, 'status': 'Sem mercados', 'detail': 'Sem leitura acionável.', 'near_miss': False}

    valid_by_engine: dict[str, dict[str, Any]] = {}
    best_invalid = None
    for market in ranked:
        check = evaluate_market(market, for_best_of_day=False)
        enriched = dict(market)
        enriched['decision_reason'] = check['reason']
        enriched['winner_score'] = _winner_score(enriched)
        if check['valid']:
            current = valid_by_engine.get(market.get('engine', ''))
            if current is None or enriched['winner_score'] > current['winner_score']:
                valid_by_engine[market.get('engine', '')] = enriched
        else:
            if best_invalid is None:
                best_invalid = check
                analysis['status'] = check['reason']
                analysis['detail'] = check['detail']
                analysis['near_miss'] = check['near_miss']

    if valid_by_engine:
        champions = sorted(valid_by_engine.values(), key=lambda row: row.get('winner_score', 0.0), reverse=True)
        selected = champions[0]
        analysis['selected'] = selected
        analysis['status'] = 'Mercado válido'
        analysis['detail'] = f"{selected.get('market','')} venceu entre motores pelo score final {selected.get('winner_score', 0.0):.2f}."
        return analysis

    if best_invalid is None:
        analysis['status'] = 'Sem mercados'
        analysis['detail'] = 'Sem leitura acionável.'
    return analysis


def select_best_of_day(match_picks: list[dict[str, Any]], limit: int = 2) -> list[dict[str, Any]]:
    valid = []
    for pick in match_picks:
        check = evaluate_market(pick, for_best_of_day=True)
        if check['valid']:
            enriched = dict(pick)
            enriched['best_of_day_reason'] = check['reason']
            enriched['winner_score'] = _winner_score(enriched)
            valid.append(enriched)
    return sorted(valid, key=lambda row: (1 if row.get('odds_source') != 'ESTIMATED' else 0, row.get('winner_score', 0.0), row.get('edge', 0.0), row.get('probability', 0.0)), reverse=True)[:limit]
