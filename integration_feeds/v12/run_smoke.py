from __future__ import annotations
import json
from pathlib import Path

REQUIRED_TOP = {
    "module_name", "module_version", "contract_version", "generated_at",
    "provider_name", "provider_source", "input_profile",
    "observed_mode", "readiness_level", "game_cards"
}
REQUIRED_CARD = {
    "fixture_id","match_label","module_name","market_code","selection_label",
    "raw_module_score","score_band","eligibility","candidate_status",
    "rationale_short","risk_flags"
}

def main() -> None:
    base = Path(__file__).resolve().parent
    feed_path = base / "integration_feeds" / "v12" / "latest.json"
    data = json.loads(feed_path.read_text(encoding="utf-8"))
    missing_top = sorted(REQUIRED_TOP - set(data))
    if missing_top:
        raise SystemExit(f"hard_fail: missing top-level fields {missing_top}")
    cards = data["game_cards"]
    if not isinstance(cards, list) or not cards:
        raise SystemExit("hard_fail: game_cards must be a non-empty list")
    for i, card in enumerate(cards, start=1):
        missing_card = sorted(REQUIRED_CARD - set(card))
        if missing_card:
            raise SystemExit(f"hard_fail: card {i} missing fields {missing_card}")
    print(f"v12 integration feed smoke = OK | cards={len(cards)} | feed={feed_path}")

if __name__ == "__main__":
    main()
