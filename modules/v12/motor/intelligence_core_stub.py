from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass
class MarketEvaluation:
    market_code: str
    tsi: float
    dci: float
    market_probability: float
    fair_odds: float
    edge_pct: float
    eligibility: bool
    rationale_short: str

def fair_odds(probability: float) -> float:
    if probability <= 0:
        raise ValueError("probability must be > 0")
    return round(1.0 / probability, 2)

def edge_pct(odd_real: float, fair: float) -> float:
    return round((odd_real / fair) - 1, 3)

def choose_best_market(evals: list[MarketEvaluation]) -> MarketEvaluation:
    eligible = [e for e in evals if e.eligibility]
    if not eligible:
        raise ValueError("no eligible markets")
    return max(eligible, key=lambda e: e.edge_pct)

def build_stub_output() -> dict[str, Any]:
    team_prob = 0.63
    match_prob = 0.69
    under_prob = 0.58

    evals = [
        MarketEvaluation("over15_team", 0.74, 0.42, team_prob, fair_odds(team_prob), edge_pct(1.72, fair_odds(team_prob)), True, "Favorito com base ofensiva suficiente para 2+ golos."),
        MarketEvaluation("over15_match", 0.68, 0.45, match_prob, fair_odds(match_prob), edge_pct(1.53, fair_odds(match_prob)), True, "Jogo com base ofensiva suficiente para 2+ golos."),
        MarketEvaluation("under35", 0.49, 0.66, under_prob, fair_odds(under_prob), edge_pct(1.70, fair_odds(under_prob)), False, "Corredor ainda controlado, mas com pressão ofensiva relevante."),
    ]
    best = choose_best_market(evals)
    return {
        "fixture_id": 1208499,
        "match_label": "Valencia vs Barcelona",
        "module_name": "v12",
        "markets": [e.__dict__ for e in evals],
        "best_market_code": best.market_code,
        "best_selection_label": "Barcelona Over 1.5 Equipa" if best.market_code == "over15_team" else "Over 1.5 Jogo",
        "best_market_probability": best.market_probability,
        "best_fair_odds": best.fair_odds,
        "best_edge_pct": best.edge_pct,
        "decision_summary": "Melhor mercado elegível por combinação de probabilidade, odd justa e edge.",
    }

if __name__ == "__main__":
    import json
    print(json.dumps(build_stub_output(), ensure_ascii=False, indent=2))
