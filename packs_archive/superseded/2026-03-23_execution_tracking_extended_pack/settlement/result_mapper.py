from __future__ import annotations


class ResultMapper:
    def resolve_market_result(self, market: str, selection: str, line: float | None, fixture_data: dict) -> str:
        return fixture_data.get("settlement_status", "UNSETTLED")
