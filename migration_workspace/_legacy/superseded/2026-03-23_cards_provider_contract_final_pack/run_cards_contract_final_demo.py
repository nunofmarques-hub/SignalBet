from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "src"))

from providers.official_cards_provider import load_central_payload, map_to_engine_input
from cards_module.core.orchestrator import run_pipeline


CASES = [
    "official_hot_over.json",
    "official_partial_team.json",
    "official_under_reject.json",
]


def main() -> None:
    out_dir = BASE / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    for filename in CASES:
        payload = load_central_payload(BASE / "examples" / "official_base_inputs" / filename)
        engine_input, provider_errors = map_to_engine_input(payload)
        if provider_errors:
            print(filename, provider_errors)
            continue
        result, validation_errors = run_pipeline(engine_input)
        output_name = f"{Path(filename).stem}__{ 'candidate' if result['eligibility'] else 'rejected' }.json"
        (out_dir / output_name).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(filename)
        print("Provider errors:", provider_errors)
        print("Validation errors:", validation_errors)
        print("Output:", out_dir / output_name)


if __name__ == "__main__":
    main()
