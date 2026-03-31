from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ALLOWED_MARKETS = {"over15_team", "over15_match", "under35"}
REQUIRED_FIELDS = {
    "fixture_id",
    "match_label",
    "module_name",
    "market_code",
    "selection_label",
    "raw_module_score",
    "score_band",
    "eligibility",
    "candidate_status",
    "rationale_short",
    "risk_flags",
}

def validate_game_card(card: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_FIELDS - set(card))
    if missing:
        raise ValueError(f"missing required fields: {missing}")
    if card["module_name"] != "v12":
        raise ValueError("module_name must be 'v12'")
    if card["market_code"] not in ALLOWED_MARKETS:
        raise ValueError(f"unsupported market_code: {card['market_code']}")
    if not isinstance(card["risk_flags"], list):
        raise ValueError("risk_flags must be a list")

def export_game_cards(source_path: str | Path, target_path: str | Path) -> None:
    source = Path(source_path)
    target = Path(target_path)
    data = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("expected a list of game_cards")
    for card in data:
        validate_game_card(card)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"game_cards export = OK | cards={len(data)} | output={target}")

if __name__ == "__main__":
    base = Path(__file__).resolve().parents[1]
    source = base / "examples" / "game_card_v12_examples.json"
    target = base / "examples" / "game_card_v12_export.json"
    export_game_cards(source, target)
