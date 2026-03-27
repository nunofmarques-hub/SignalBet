# UI v25 — Operational Stability Matrix

| Scenario | Entry condition | Expected decision | Observed decision | PASS/FAIL | Key observed fields | Short consistency note |
|---|---|---|---|---|---|---|
| Fresh snapshot reused | persisted snapshot exists and freshness is valid | reuse | reuse | PASS | requested_mode, observed_mode, snapshot_reused, freshness_state, bridge_decision_reason | Stable and repeatable in controlled runs |
| Stale snapshot with successful refresh | snapshot stale, refresh available, protected read succeeds | refresh | refresh | PASS | snapshot_freshness, refresh_attempted, refresh_succeeded, observed_mode | Refresh path behaves as intended |
| Stale snapshot with failed refresh | snapshot stale, refresh attempted, protected read fails | controlled reuse or fallback | controlled reuse | PASS | refresh_attempted, refresh_succeeded=false, snapshot_reused, reuse_reason | Controlled degradation without UX break |
| Fallback to orchestrator_mock | protected source unavailable | fallback | fallback | PASS | fallback_used, observed_mode=orchestrator_mock, bridge_status | Fallback remains clean and explicit |
| forceRefresh | explicit forceRefresh=true | bypass reuse and attempt refresh | refresh attempted | PASS | force_refresh, refresh_attempted, reuse_blocked, read_preference_reason | Force path is explicit and governed |
| requested_mode vs observed_mode transition | requested protected read but source not accepted | controlled transition | requested != observed | PASS | requested_mode, observed_mode, source_transition | Transition is visible and understandable |
| Explicit invalidation | snapshot invalidated by rule/trigger | block reuse | reuse blocked | PASS | snapshot_invalidated, invalidation_trigger, reuse_blocked | Invalidation properly blocks stale reuse |
| Repeated scenario run | same conditions repeated | same decision | same decision | PASS | stability_status, stability_repeat_count, stability_repeat_result | Repeated behavior is increasingly predictable |
