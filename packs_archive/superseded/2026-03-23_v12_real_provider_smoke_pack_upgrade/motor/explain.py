from __future__ import annotations

from typing import Any


def explain_indicators(indicators: dict[str, Any], engine: str) -> str:
    if engine == 'O15_TEAM':
        favorite = indicators.get('favorite_team') or 'sem favorito claro'
        return f"FDI {indicators.get('fdi',0.0):.2f}, TSI do favorito forte e margem {indicators.get('favorite_margin',0.0):+.2f}; favorito {favorite}"
    if engine == 'U35':
        return f"ULI {indicators.get('uli',0.0):.2f}, LTR {indicators.get('ltr',0.0):.2f} e TLI {indicators.get('tli',0.0):.2f} favorecem controlo"
    return f"TSI combinado {indicators.get('attack_total',0.0):.2f}, IPO combinado {indicators.get('ipo_combined',0.0):.2f} e TPD {indicators.get('tpd',0.0):.2f} sustentam o jogo"


def explain_market_choice(best_market: dict[str, Any]) -> str:
    return (
        f"{best_market['market']} via motor {best_market.get('engine','')} com score {best_market.get('engine_score',0.0):.2f}; "
        f"odd justa {best_market.get('fair_odd')} vs mercado {best_market.get('market_odd')} ({best_market.get('odds_source','ESTIMATED')}); "
        f"edge {best_market.get('edge',0.0)*100:+.1f}%"
    )


def build_pick_reason(match_obj: dict[str, Any], best_market: dict[str, Any], indicators: dict[str, Any]) -> str:
    return f"{match_obj['game']}: {explain_indicators(indicators, best_market.get('engine',''))}. {explain_market_choice(best_market)}."
