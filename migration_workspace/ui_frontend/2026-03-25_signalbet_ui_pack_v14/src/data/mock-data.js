export const MOCK_ORCHESTRATOR_SNAPSHOT = {
  "source_mode": "orchestrator_mock",
  "cta_state": "ready",
  "readiness_level": "high",
  "project_feed_coverage_ratio": 0.86,
  "pipeline_state": "idle",
  "current_stage": "ready_to_run",
  "summary": {
    "modules_available": 4,
    "modules_ready": 4,
    "opportunities": 18,
    "approved": 6,
    "execution_open": 3
  },
  "module_overview": [
    {
      "module": "Cards",
      "status": "ready",
      "coverage": 0.92,
      "count": 5
    },
    {
      "module": "v12",
      "status": "ready",
      "coverage": 0.94,
      "count": 6
    },
    {
      "module": "BTTS",
      "status": "ready",
      "coverage": 0.81,
      "count": 4
    },
    {
      "module": "Corners",
      "status": "ready",
      "coverage": 0.77,
      "count": 3
    }
  ],
  "pipeline_steps": [
    {
      "name": "Data/API",
      "status": "ready"
    },
    {
      "name": "Modules",
      "status": "ready"
    },
    {
      "name": "GPS",
      "status": "ready"
    },
    {
      "name": "Bankroll",
      "status": "ready"
    },
    {
      "name": "Execution",
      "status": "ready"
    }
  ],
  "issues": [],
  "final_result": "not_run",
  "run_id": null
};
export const MOCK_SYSTEM_SNAPSHOT = {
  "readiness": "high",
  "source_mode": "contract_mock",
  "opportunities_today": 18,
  "eligible": 9,
  "approved": 6,
  "pending_execution": 2,
  "open_executions": 3,
  "alerts": 1,
  "top_opportunity": {
    "fixture": "RB Leipzig vs Mainz",
    "market": "Over 1.5 Golos",
    "module_source": "v12",
    "global_score": 91,
    "confidence_norm": 86,
    "edge_norm": 73,
    "risk_norm": 22,
    "priority_tier": "T1",
    "decision_status": "APPROVED"
  },
  "pool_rows": [
    {
      "fixture": "RB Leipzig vs Mainz",
      "market": "Over 1.5 Golos",
      "module_source": "v12",
      "global_score": 91,
      "confidence_norm": 86,
      "edge_norm": 73,
      "risk_norm": 22,
      "priority_tier": "T1",
      "eligibility": "ELIGIBLE",
      "decision_status": "APPROVED",
      "execution_status": "PENDING",
      "data_quality_flag": "GREEN"
    },
    {
      "fixture": "Lazio vs Udinese",
      "market": "Under 3.5",
      "module_source": "Cards",
      "global_score": 84,
      "confidence_norm": 78,
      "edge_norm": 66,
      "risk_norm": 28,
      "priority_tier": "T1",
      "eligibility": "ELIGIBLE",
      "decision_status": "REDUCED",
      "execution_status": "PENDING",
      "data_quality_flag": "GREEN"
    },
    {
      "fixture": "PSV vs Twente",
      "market": "BTTS",
      "module_source": "BTTS",
      "global_score": 82,
      "confidence_norm": 76,
      "edge_norm": 62,
      "risk_norm": 31,
      "priority_tier": "T2",
      "eligibility": "ELIGIBLE",
      "decision_status": "RESERVE",
      "execution_status": "IDLE",
      "data_quality_flag": "AMBER"
    }
  ]
};
