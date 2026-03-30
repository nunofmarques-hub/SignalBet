from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def build_game_cards(module_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return short v12 game_cards for Orchestrator consumption."""
    allowed = {"over15_team", "over15_match", "under35"}
    cards: List[Dict[str, Any]] = []
    for row in module_rows:
        if row.get("market_code") not in allowed:
            continue
        cards.append(
            {
                "fixture_id": row["fixture_id"],
                "match_label": row["match_label"],
                "module_name": "v12",
                "market_code": row["market_code"],
                "selection_label": row["selection_label"],
                "raw_module_score": row["raw_module_score"],
                "score_band": row["score_band"],
                "eligibility": row["eligibility"],
                "candidate_status": row["candidate_status"],
                "rationale_short": row["rationale_short"],
                "risk_flags": row.get("risk_flags", []),
            }
        )
    return cards


if __name__ == "__main__":
    here = Path(__file__).resolve().parents[1]
    example = here / "examples" / "game_cards_v12.json"
    data = json.loads(example.read_text(encoding="utf-8"))
    print(json.dumps(build_game_cards(data), ensure_ascii=False, indent=2))
