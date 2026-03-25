from __future__ import annotations

from typing import Any, Dict, List


class OfficialLiveProviderError(RuntimeError):
    pass


class OfficialLiveProvider:
    def __init__(self, fixtures_service=None, events_service=None) -> None:
        if fixtures_service is None or events_service is None:
            try:
                from data_api.services.fixtures_service import get_fixtures_by_league_season
                from data_api.services.events_service import get_fixture_events
            except Exception as exc:  # pragma: no cover - exercised in live environment
                raise OfficialLiveProviderError(
                    "Data_API_Official_Trunk_v1 indisponível no ambiente. Monte `data_api/` antes do modo live."
                ) from exc
            fixtures_service = get_fixtures_by_league_season
            events_service = get_fixture_events
        self.fixtures_service = fixtures_service
        self.events_service = events_service

    def fetch_fixture_bundle(self, league: int, season: int, fixture_index: int = 0) -> Dict[str, Any]:
        fixtures = self.fixtures_service(league, season)
        if not fixtures:
            raise OfficialLiveProviderError("Nenhum fixture devolvido pelo trunk oficial.")
        try:
            fixture = fixtures[fixture_index]
        except IndexError as exc:
            raise OfficialLiveProviderError("fixture_index fora do intervalo devolvido pelo trunk.") from exc
        fixture_id = fixture["fixture"]["id"]
        events = self.events_service(fixture_id, league, season)
        card_events = self._extract_card_events(events)
        return {
            "league": league,
            "season": season,
            "fixture": fixture,
            "events": events,
            "card_events": card_events,
            "fixture_id": fixture_id,
        }

    @staticmethod
    def _extract_card_events(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        extracted = []
        for event in events:
            event_type = str(event.get("type", ""))
            detail = str(event.get("detail", ""))
            if event_type.lower() == "card" or "card" in detail.lower():
                extracted.append(event)
        return extracted
