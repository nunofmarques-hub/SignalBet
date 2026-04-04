from __future__ import annotations

import json
from pathlib import Path

from data_api.services.fixtures_service import get_fixtures_by_league_season
from data_api.services.events_service import get_fixture_events

LEAGUE_ID = 140
SEASON = 2024


def first_fixture_with_events(fixtures: list[dict], limit: int = 10) -> tuple[int | None, list[dict], dict]:
    for row in fixtures[:limit]:
        fixture_id = row.get("fixture", {}).get("id")
        if not fixture_id:
            continue
        events = get_fixture_events(fixture_id, LEAGUE_ID, SEASON)
        if events:
            return fixture_id, events, row
    return None, [], {}


def main() -> None:
    fixtures = get_fixtures_by_league_season(LEAGUE_ID, SEASON)
    fixture_id, events, fixture_row = first_fixture_with_events(fixtures, limit=10)

    card_events = [
        e for e in events
        if e.get("type") == "Card" or "card" in str(e.get("detail", "")).lower()
    ]

    report = {
        "module": "Cards",
        "source": "Data_API_Official_Trunk_v1",
        "fixtures_count": len(fixtures),
        "fixture_id": fixture_id,
        "events_found": bool(events),
        "events_count": len(events),
        "card_events_count": len(card_events),
        "home_team_id": fixture_row.get("teams", {}).get("home", {}).get("id") if fixture_row else None,
        "away_team_id": fixture_row.get("teams", {}).get("away", {}).get("id") if fixture_row else None,
        "result": None,
    }

    ok = (
        report["fixtures_count"] > 0
        and report["events_found"]
    )
    report["result"] = "green" if ok else "red"

    out_path = Path("smoke_test_cards_result.json")
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
