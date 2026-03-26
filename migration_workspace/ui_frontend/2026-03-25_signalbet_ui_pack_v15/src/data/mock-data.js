export const contractMockSnapshot = {
  source_mode: 'contract_mock',
  opportunities_today: 14,
  approved_today: 4,
  pending_execution: 2,
  pipeline_state: 'idle'
};

export const orchestratorMockSnapshot = {
  source_mode: 'orchestrator_mock',
  cta_state: 'ready',
  readiness_level: 'high',
  project_feed_coverage_ratio: 0.82,
  pipeline_state: 'idle',
  current_stage: 'ready_to_run',
  summary: { opportunities: 14, eligible: 8, approved: 4, executed: 2 },
  module_overview: [
    { name:'v12', status:'ready', items:4 },
    { name:'Cards', status:'ready', items:3 },
    { name:'BTTS', status:'ready', items:2 },
    { name:'Corners', status:'ready', items:3 }
  ],
  pipeline_steps:[
    { step:'data_api', status:'ready' },
    { step:'modules', status:'ready' },
    { step:'gps', status:'ready' },
    { step:'bankroll', status:'ready' },
    { step:'execution', status:'ready' }
  ],
  issues: [],
  final_result: null,
  pool_rows:[
    { fixture:'RB Leipzig vs Mainz', market:'Over 1.5 Equipa', module_source:'v12', global_score:88, confidence_norm:84, edge_norm:73, risk_norm:22, priority_tier:'A', eligibility:'eligible', decision_status:'approved', execution_status:'pending', data_quality_flag:'green' },
    { fixture:'Lazio vs Udinese', market:'Under 3.5', module_source:'v12', global_score:82, confidence_norm:79, edge_norm:64, risk_norm:28, priority_tier:'A', eligibility:'eligible', decision_status:'reduced', execution_status:'pending', data_quality_flag:'green' },
    { fixture:'Benfica vs Braga', market:'BTTS', module_source:'BTTS', global_score:76, confidence_norm:71, edge_norm:61, risk_norm:35, priority_tier:'B', eligibility:'eligible', decision_status:'reserve', execution_status:'not_sent', data_quality_flag:'amber' }
  ],
  history_rows:[
    { date:'2026-03-24', fixture:'PSV vs Heerenveen', market:'Over 1.5 Equipa', module_source:'v12', global_score:90, confidence_norm:86, edge_norm:75, risk_norm:20, decision_status:'approved', execution_status:'settled', result:'win', roi:'+0.27' },
    { date:'2026-03-24', fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:79, confidence_norm:74, edge_norm:58, risk_norm:31, decision_status:'approved', execution_status:'settled', result:'loss', roi:'-1.00' }
  ]
};

export const realProtectedSnapshotExample = {
  source_mode: 'real_read_protected',
  cta_state: 'ready',
  readiness_level: 'medium',
  project_feed_coverage_ratio: 0.67,
  pipeline_state: 'partial_ready',
  current_stage: 'module_checks',
  summary: { opportunities: 11, eligible: 6, approved: 3, executed: 1 },
  module_overview: [
    { name:'v12', status:'ready', items:4 },
    { name:'Cards', status:'ready', items:2 },
    { name:'BTTS', status:'degraded', items:1 },
    { name:'Corners', status:'ready', items:2 }
  ],
  pipeline_steps:[
    { step:'data_api', status:'ready' },
    { step:'modules', status:'partial' },
    { step:'gps', status:'ready' },
    { step:'bankroll', status:'ready' },
    { step:'execution', status:'ready' }
  ],
  issues:[{ level:'warning', message:'BTTS partial feed coverage' }],
  final_result:'partial'
};
