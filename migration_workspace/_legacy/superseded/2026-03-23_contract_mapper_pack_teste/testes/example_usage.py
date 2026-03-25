from __future__ import annotations

import json
from pathlib import Path
from candidate_pick_builder import build_candidate_pick

corners_output = {
    "fixture_id": 878320,
    "game": "Espanyol vs Almeria",
    "competition": "La Liga",
    "market": "Over 9.5 cantos jogo",
    "score": 100.0,
    "confidence": "Alta",
    "risk": "Baixo",
    "eligible": True,
    "estimated_total_corners": 15.17,
    "main_drivers": [
        "produção combinada acima do padrão",
        "perfil de concessão favorável",
        "contexto de jogo favorável a volume",
    ],
    "alerts": [],
    "team_scores": {"home": 76.86, "away": 54.94},
    "game_profile": "Volume Alto",
    "market_bias": "Over",
    "line_grid": [
        {"market": "Over 9.5 cantos", "score": 100.0, "confidence": "Alta", "risk": "Baixo", "eligible": True}
    ],
    "operational_conclusion": "Jogo com perfil volume alto para cantos. O sinal principal aparece em over 9.5 cantos jogo com força muito forte.",
}

pick = build_candidate_pick(
    corners_output,
    module_version="corners.v2_logicfix",
    kickoff_datetime=None,
    odds=None,
    edge_raw=None,
    expiry_context="pre_match_same_day",
)

Path("example_market_pick.json").write_text(
    json.dumps(pick, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(json.dumps(pick, ensure_ascii=False, indent=2))
