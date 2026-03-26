export const contractSnapshot = {
  topOpportunity: { fixture: 'RB Leipzig vs Mainz', market: 'Over 1.5 Equipa', module_source: 'v12', global_score: 87, confidence_norm: 82, edge_norm: 71, risk_norm: 24, priority_tier: 'A', eligibility: 'eligible', decision_status: 'approved', execution_status: 'pending', data_quality_flag: 'green' },
  kpis: { opportunities_today: 14, eligible: 8, approved: 4, pending_execution: 2, settled_today: 5 },
  pool: [
    { fixture: 'RB Leipzig vs Mainz', market: 'Over 1.5 Equipa', module_source: 'v12', global_score: 87, confidence_norm: 82, edge_norm: 71, risk_norm: 24, priority_tier: 'A', eligibility: 'eligible', decision_status: 'approved', execution_status: 'pending', data_quality_flag: 'green' },
    { fixture: 'Lazio vs Udinese', market: 'Under 3.5', module_source: 'v12', global_score: 79, confidence_norm: 77, edge_norm: 61, risk_norm: 29, priority_tier: 'A', eligibility: 'eligible', decision_status: 'reduced', execution_status: 'pending', data_quality_flag: 'amber' },
    { fixture: 'Porto vs Braga', market: 'BTTS', module_source: 'BTTS', global_score: 74, confidence_norm: 69, edge_norm: 58, risk_norm: 36, priority_tier: 'B', eligibility: 'watchlist', decision_status: 'reserve', execution_status: 'idle', data_quality_flag: 'green' }
  ],
  history: [
    { date: '2026-03-24', fixture: 'PSV vs Heerenveen', market: 'Over 1.5 Equipa', module_source: 'v12', global_score: 84, confidence_norm: 81, edge_norm: 67, risk_norm: 22, decision_status: 'approved', execution_status: 'settled', result: 'win', roi: '+0.42' },
    { date: '2026-03-24', fixture: 'Milan vs Torino', market: 'Under 3.5', module_source: 'v12', global_score: 77, confidence_norm: 73, edge_norm: 55, risk_norm: 30, decision_status: 'approved', execution_status: 'settled', result: 'loss', roi: '-1.00' }
  ]
};

export const orchestratorMockSnapshot = {
  source_mode: 'orchestrator_mock',
  cta_state: 'ready',
  readiness_level: 'high',
  project_feed_coverage_ratio: 0.83,
  pipeline_state: 'idle',
  current_stage: 'waiting',
  run_id: null,
  button_context: { label: 'Pôr tudo a correr', enabled: true, note: 'Sistema pronto para corrida controlada.' },
  summary: {
    data_api_state: 'ready',
    modules_ready: 4,
    modules_total: 4,
    gps_state: 'ready',
    bankroll_state: 'ready',
    execution_state: 'ready'
  },
  module_overview: [
    { module: 'Cards', status: 'ready', picks: 2 },
    { module: 'v12', status: 'ready', picks: 6 },
    { module: 'BTTS', status: 'ready', picks: 3 },
    { module: 'Corners', status: 'ready', picks: 3 }
  ],
  pipeline_steps: [
    { key: 'data_api', label: 'Data/API', status: 'ready' },
    { key: 'modules', label: 'Módulos', status: 'ready' },
    { key: 'gps', label: 'GPS', status: 'ready' },
    { key: 'bankroll', label: 'Banca', status: 'ready' },
    { key: 'execution', label: 'Execution', status: 'ready' }
  ],
  issues: [],
  final_result: null
};

export const partialRuntimeSnapshot = {
  source_mode: 'placeholder_live',
  cta_state: 'running',
  readiness_level: 'medium',
  project_feed_coverage_ratio: 0.61,
  pipeline_state: 'running',
  current_stage: 'gps',
  run_id: 'run_20260325_001',
  button_context: { label: 'Corrida em curso', enabled: false, note: 'Acompanhar progresso por etapa.' },
  summary: { data_api_state: 'ready', modules_ready: 4, modules_total: 4, gps_state: 'running', bankroll_state: 'waiting', execution_state: 'waiting' },
  module_overview: [
    { module: 'Cards', status: 'done', picks: 2 },
    { module: 'v12', status: 'done', picks: 6 },
    { module: 'BTTS', status: 'done', picks: 3 },
    { module: 'Corners', status: 'done', picks: 3 }
  ],
  pipeline_steps: [
    { key: 'data_api', label: 'Data/API', status: 'done' },
    { key: 'modules', label: 'Módulos', status: 'done' },
    { key: 'gps', label: 'GPS', status: 'running' },
    { key: 'bankroll', label: 'Banca', status: 'waiting' },
    { key: 'execution', label: 'Execution', status: 'waiting' }
  ],
  issues: [{ code: 'feed_partial', severity: 'warning', message: 'Cobertura parcial de feeds em runtime protegido.' }],
  final_result: null
};
