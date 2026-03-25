from cards_module.core.validator import validate_payload


def run_test() -> None:
    payload = {
        "schema_version": "market_pick.v1.1",
        "pick_id": "x",
        "created_at": "2026-01-01T00:00:00Z",
        "module_id": "cards",
        "module_version": "cards.1.0.0",
        "event_id": 1,
        "match_label": "A vs B",
        "competition": "Test League",
        "market_family": "cards",
        "market": "match_cards_over",
        "selection": "Over 4.5 Cards",
        "eligibility": True,
        "score_raw": 80,
        "confidence_raw": 4,
        "risk_raw": 2,
        "edge_raw": "5.0%",
        "rationale_summary": "ok",
        "main_drivers": ["x", "y", "z"],
        "penalties": [],
        "data_quality_flag": "clean",
    }
    errors = validate_payload(payload)
    assert not errors, errors


if __name__ == "__main__":
    run_test()
    print("test_validator: OK")
