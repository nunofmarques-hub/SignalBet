export const runtimeSnapshots = {
  contract_mock: {
    run_id: 'contract_mock_001',
    cta_state: 'ready',
    readiness_level: 'medium',
    project_feed_coverage_ratio: 0.72,
    pipeline_state: 'idle',
    current_stage: 'preflight',
    final_result: null,
    summary: { opportunities: 12, eligible: 6, approved: 3, sent_to_execution: 2 },
    module_overview: [
      { module: 'v12', status: 'ready', count: 4 },
      { module: 'cards', status: 'ready', count: 2 },
      { module: 'btts', status: 'warning', count: 3 },
      { module: 'corners', status: 'warning', count: 1 },
    ],
    pipeline_steps: [
      { step: 'data_api', status: 'ready' },
      { step: 'modules', status: 'running' },
      { step: 'gps', status: 'idle' },
      { step: 'bankroll', status: 'idle' },
      { step: 'execution', status: 'idle' },
    ],
    issues: [{ severity: 'warning', message: 'BTTS sample provider still mocked' }]
  },
  orchestrator_mock: {
    run_id: 'orch_mock_1442',
    cta_state: 'running',
    readiness_level: 'high',
    project_feed_coverage_ratio: 0.91,
    pipeline_state: 'running',
    current_stage: 'bankroll',
    final_result: null,
    summary: { opportunities: 18, eligible: 9, approved: 4, sent_to_execution: 3 },
    module_overview: [
      { module: 'v12', status: 'ready', count: 5 },
      { module: 'cards', status: 'ready', count: 3 },
      { module: 'btts', status: 'ready', count: 4 },
      { module: 'corners', status: 'degraded', count: 2 },
    ],
    pipeline_steps: [
      { step: 'data_api', status: 'success' },
      { step: 'modules', status: 'success' },
      { step: 'gps', status: 'success' },
      { step: 'bankroll', status: 'running' },
      { step: 'execution', status: 'idle' },
    ],
    issues: [{ severity: 'warning', message: 'Corners feed coverage partial' }]
  },
  placeholder_live: {
    run_id: 'live_placeholder',
    cta_state: 'blocked',
    readiness_level: 'low',
    project_feed_coverage_ratio: 0.0,
    pipeline_state: 'idle',
    current_stage: 'preflight',
    final_result: null,
    summary: { opportunities: 0, eligible: 0, approved: 0, sent_to_execution: 0 },
    module_overview: [
      { module: 'v12', status: 'unknown', count: 0 },
      { module: 'cards', status: 'unknown', count: 0 },
      { module: 'btts', status: 'unknown', count: 0 },
      { module: 'corners', status: 'unknown', count: 0 },
    ],
    pipeline_steps: [
      { step: 'data_api', status: 'idle' },
      { step: 'modules', status: 'idle' },
      { step: 'gps', status: 'idle' },
      { step: 'bankroll', status: 'idle' },
      { step: 'execution', status: 'idle' },
    ],
    issues: [{ severity: 'info', message: 'Live connection not enabled in this pack' }]
  }
};
