export const MOCK_DATA = {
  "runtime_snapshot": {
    "cta_state": "ready",
    "readiness_level": "medium",
    "project_feed_coverage_ratio": 0.74,
    "pipeline_state": "idle",
    "current_stage": "preflight",
    "summary": {
      "modules_available": 4,
      "approved": 3,
      "pending": 1
    },
    "module_overview": [
      {
        "name": "v12",
        "state": "ready"
      },
      {
        "name": "cards",
        "state": "ready"
      },
      {
        "name": "btts",
        "state": "ready"
      },
      {
        "name": "corners",
        "state": "degraded"
      }
    ],
    "pipeline_steps": [
      {
        "step": "data",
        "status": "ok"
      },
      {
        "step": "modules",
        "status": "ok"
      },
      {
        "step": "gps",
        "status": "ok"
      },
      {
        "step": "bankroll",
        "status": "ok"
      },
      {
        "step": "execution",
        "status": "pending"
      }
    ],
    "issues": [
      "corners_feed_partial"
    ],
    "final_result": "partial"
  }
};
