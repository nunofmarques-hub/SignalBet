export default {
  "contractSnapshot": {
    "ok": true
  },
  "orchestratorSnapshot": {
    "source_mode": "orchestrator_mock",
    "bridge_status": "fallback_ok",
    "bridge_scope": "protected_real_partial_v19",
    "degraded_mode": false,
    "read_attempt": 1,
    "snapshot_persisted": false,
    "snapshot_reused": false,
    "snapshot_freshness": "fresh",
    "freshness_state": "fresh",
    "snapshot_invalidated": false,
    "reuse_allowed": true,
    "reuse_reason": "mock_default",
    "new_read_attempted": false,
    "bridge_decision_reason": "mock_fallback",
    "cta_state": "ready",
    "readiness_level": "medium",
    "project_feed_coverage_ratio": 0.67,
    "pipeline_state": "partial",
    "current_stage": "bankroll",
    "summary": {
      "opportunities": 14,
      "eligible": 8,
      "approved": 5,
      "executed": 3
    },
    "module_overview": [
      {
        "module": "v12",
        "status": "ok"
      },
      {
        "module": "BTTS",
        "status": "ok"
      }
    ],
    "pipeline_steps": [
      {
        "step": "readiness",
        "status": "done",
        "note": "mock"
      },
      {
        "step": "modules",
        "status": "done",
        "note": "mock"
      },
      {
        "step": "gps",
        "status": "done",
        "note": "mock"
      },
      {
        "step": "bankroll",
        "status": "running",
        "note": "mock"
      }
    ],
    "issues": [
      "fallback ativo para orchestrator_mock"
    ],
    "final_result": "partial"
  },
  "realProtectedSnapshot": {
    "source_mode": "real_read_protected",
    "source_line": "embedded_real_fixture_v19",
    "bridge_status": "ok",
    "bridge_scope": "protected_real_partial_v19",
    "degraded_mode": false,
    "read_attempt": 1,
    "snapshot_persisted": true,
    "snapshot_reused": false,
    "snapshot_freshness": "fresh",
    "freshness_state": "fresh",
    "snapshot_invalidated": false,
    "reuse_allowed": true,
    "reuse_reason": "fresh_snapshot_available",
    "new_read_attempted": true,
    "bridge_decision_reason": "new_protected_read_ok",
    "cta_state": "ready",
    "readiness_level": "high",
    "project_feed_coverage_ratio": 0.91,
    "pipeline_state": "running",
    "current_stage": "execution",
    "summary": {
      "opportunities": 22,
      "eligible": 13,
      "approved": 7,
      "executed": 4
    },
    "module_overview": [
      {
        "module": "v12",
        "status": "ok"
      },
      {
        "module": "Cards",
        "status": "ok"
      },
      {
        "module": "BTTS",
        "status": "ok"
      },
      {
        "module": "Corners",
        "status": "ok"
      }
    ],
    "pipeline_steps": [
      {
        "step": "readiness",
        "status": "done",
        "note": "protected read"
      },
      {
        "step": "modules",
        "status": "done",
        "note": "protected read"
      },
      {
        "step": "gps",
        "status": "done",
        "note": "protected read"
      },
      {
        "step": "bankroll",
        "status": "done",
        "note": "protected read"
      },
      {
        "step": "execution",
        "status": "running",
        "note": "protected read"
      }
    ],
    "issues": [],
    "final_result": "in_progress",
    "captured_at": "2026-03-26T10:00:00Z"
  },
  "staleProtectedSnapshot": {
    "source_mode": "real_read_protected",
    "source_line": "persisted_protected_snapshot",
    "bridge_status": "stale_reuse",
    "bridge_scope": "protected_real_partial_v19",
    "degraded_mode": false,
    "read_attempt": 1,
    "snapshot_persisted": true,
    "snapshot_reused": true,
    "snapshot_freshness": "stale",
    "freshness_state": "stale",
    "snapshot_invalidated": false,
    "reuse_allowed": true,
    "reuse_reason": "reuse_allowed_until_revalidation",
    "new_read_attempted": false,
    "bridge_decision_reason": "reused_stale_protected_snapshot",
    "cta_state": "review",
    "readiness_level": "high",
    "project_feed_coverage_ratio": 0.85,
    "pipeline_state": "running",
    "current_stage": "gps",
    "summary": {
      "opportunities": 20,
      "eligible": 12,
      "approved": 6,
      "executed": 4
    },
    "module_overview": [
      {
        "module": "v12",
        "status": "ok"
      },
      {
        "module": "Cards",
        "status": "ok"
      }
    ],
    "pipeline_steps": [
      {
        "step": "readiness",
        "status": "done",
        "note": "persisted snapshot"
      },
      {
        "step": "modules",
        "status": "done",
        "note": "persisted snapshot"
      },
      {
        "step": "gps",
        "status": "running",
        "note": "persisted snapshot"
      }
    ],
    "issues": [
      "snapshot protegido reutilizado e a aguardar revalida\u00e7\u00e3o"
    ],
    "final_result": "in_progress",
    "captured_at": "2026-03-26T09:40:00Z"
  }
,
  "realProtectedSnapshotV19": {
    "source_mode": "real_read_protected",
    "source_line": "embedded_real_fixture_v19",
    "bridge_status": "refresh_ok",
    "bridge_scope": "protected_real_partial_v19",
    "degraded_mode": false,
    "read_attempt": 1,
    "snapshot_persisted": true,
    "snapshot_reused": false,
    "snapshot_freshness": "fresh",
    "freshness_state": "fresh",
    "snapshot_invalidated": false,
    "reuse_allowed": true,
    "reuse_reason": "fresh_snapshot_available",
    "new_read_attempted": true,
    "refresh_attempted": true,
    "refresh_succeeded": true,
    "reuse_preferred": false,
    "reuse_blocked": false,
    "invalidation_trigger": "stale_snapshot",
    "read_preference_reason": "stale_snapshot_refresh_preferred",
    "bridge_decision_reason": "stale_snapshot_refreshed_successfully",
    "cta_state": "ready",
    "readiness_level": "high",
    "project_feed_coverage_ratio": 0.93,
    "pipeline_state": "running",
    "current_stage": "execution",
    "summary": {"opportunities": 24, "eligible": 14, "approved": 8, "executed": 5},
    "module_overview": [{"module":"v12","status":"ok"},{"module":"Cards","status":"ok"},{"module":"BTTS","status":"ok"},{"module":"Corners","status":"ok"}],
    "pipeline_steps": [{"step":"readiness","status":"done","note":"protected refresh"},{"step":"modules","status":"done","note":"protected refresh"},{"step":"gps","status":"done","note":"protected refresh"},{"step":"bankroll","status":"done","note":"protected refresh"},{"step":"execution","status":"running","note":"protected refresh"}],
    "issues": [],
    "final_result": "in_progress",
    "captured_at": "2026-03-26T10:15:00Z"
  }
};