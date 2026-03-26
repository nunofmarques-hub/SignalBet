from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
SRC = BASE / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from cards_module.core.orchestrator import run
from cards_module.io.loader import load_json
from cards_module.io.writer import write_json

EXAMPLES = BASE / "examples"
OUT = BASE / "out"


if __name__ == "__main__":
    match_input = load_json(EXAMPLES / "sample_input_fixture.json")
    odds_input = load_json(EXAMPLES / "sample_market_odds.json")

    payload, errors = run(match_input, odds_input)

    target = OUT / ("candidate_pick.json" if payload.get("eligibility") and not errors else "rejected_pick.json")
    write_json(target, payload)
    write_json(OUT / "validation_errors.json", {"errors": errors})

    print(f"Output written to: {target}")
    print(f"Validation errors: {errors}")
