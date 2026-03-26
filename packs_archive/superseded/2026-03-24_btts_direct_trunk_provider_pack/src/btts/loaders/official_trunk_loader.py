from ..models import MatchInput, TeamSnapshot

class BTTSOfficialTrunkLoader:
    def load(self, payload):
        return MatchInput(
            event_id=payload["event_id"],
            match_label=payload["match_label"],
            competition=payload["competition"],
            kickoff_datetime=payload["kickoff_datetime"],
            market_family=payload["market_family"],
            market=payload["market"],
            selection_hint=payload["selection_hint"],
            odds=payload["odds"],
            home_snapshot=TeamSnapshot(**payload["home_snapshot"]),
            away_snapshot=TeamSnapshot(**payload["away_snapshot"]),
            data_api_context=payload["data_api_context"],
        )
