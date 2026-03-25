from __future__ import annotations

"""Thin wrapper describing the active v12 core engines.

This file documents the current state:
- active core: O15_TEAM, O15_GAME, U35
- future derived lines: team/match over and under 0.5..5.5
"""

ACTIVE_CORE_ENGINES = {
    "O15_TEAM": {
        "motor_id": "TEAM_OVER_ENGINE",
        "market_variant": "TEAM_OVER_15",
        "description": "Over 1.5 equipa",
        "current_core_status": "active_core",
    },
    "O15_GAME": {
        "motor_id": "MATCH_OVER_ENGINE",
        "market_variant": "MATCH_OVER_15",
        "description": "Over 1.5 jogo",
        "current_core_status": "active_core",
    },
    "U35": {
        "motor_id": "MATCH_UNDER_ENGINE",
        "market_variant": "MATCH_UNDER_35",
        "description": "Under 3.5",
        "current_core_status": "active_core",
    },
}
