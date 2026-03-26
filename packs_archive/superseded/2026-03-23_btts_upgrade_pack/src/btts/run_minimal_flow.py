from __future__ import annotations
import json
from pathlib import Path
from .loaders import load_match_input
from .engine import evaluate
from .exporter import export_market_pick

def main():
    root = Path(__file__).resolve().parents[3]
    input_path = root / "sample_input" / "official_data_api_input.json"
    output_path = root / "sample_output" / "market_pick_v1_1_btts.json"
    match = load_match_input(input_path)
    result = evaluate(match)
    payload = export_market_pick(match, result)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated: {output_path}")
    print(f"Score: {payload['score_raw']} | Eligibility: {payload['eligibility']} | Drivers: {payload['main_drivers']}")

if __name__ == "__main__":
    main()
