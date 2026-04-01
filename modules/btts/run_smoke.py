from pathlib import Path
import json

base = Path(__file__).resolve().parent
latest = base / "latest.json"
obj = json.loads(latest.read_text(encoding="utf-8"))
assert "game_cards" in obj and isinstance(obj["game_cards"], list) and obj["game_cards"], "missing game_cards"
card = obj["game_cards"][0]
required = [
    "fixture_id", "match_label", "module_name", "market_code", "selection_label",
    "raw_module_score", "score_band", "eligibility", "candidate_status",
    "rationale_short", "risk_flags"
]
missing = [k for k in required if k not in card]
assert not missing, f"missing fields: {missing}"
print("BTTS smoke OK")
