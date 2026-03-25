from cards_module.core.mapper import map_to_contract
from cards_module.types import RawAssessment


def run_test() -> None:
    payload = map_to_contract(
        {
            "event_id": 100,
            "match_label": "A vs B",
            "competition": "Test",
            "kickoff_datetime": "2026-01-01T12:00:00Z",
        },
        RawAssessment(
            market="match_cards_over",
            selection="Over 4.5 Cards",
            line=4.5,
            odds=1.9,
            score_raw=81.0,
            confidence_raw=4,
            risk_raw=2,
            edge_raw="6.0%",
            eligibility=True,
            rationale_summary="ok",
            main_drivers=["a", "b", "c"],
            penalties=[],
            module_specific_payload={"discipline_profile": "hot"},
        ),
    )
    assert payload["module_id"] == "cards"
    assert payload["market_family"] == "cards"
    assert payload["module_specific_payload"]["discipline_profile"] == "hot"


if __name__ == "__main__":
    run_test()
    print("test_mapper: OK")
