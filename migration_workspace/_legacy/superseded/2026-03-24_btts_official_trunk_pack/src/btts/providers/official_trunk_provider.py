import json
from pathlib import Path

class BTTSOfficialTrunkProvider:
    """Provider direto do Data_API_Official_Trunk_v1.

    Em ambiente real:
    - get_fixtures_by_league_season()
    - get_fixture_events()
    - get_team_statistics()
    - get_standings_snapshot()
    """

    def __init__(self, fallback_sample_path):
        self.fallback_sample_path = Path(fallback_sample_path)

    def build_official_input(self, league_id: int, season: int, fixture_index: int = 0) -> dict:
        # Fluxo alvo com tronco oficial documentado no HANDOFF_BTTS.md
        return json.loads(self.fallback_sample_path.read_text(encoding='utf-8'))
