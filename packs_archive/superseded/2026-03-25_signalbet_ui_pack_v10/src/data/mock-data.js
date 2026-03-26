export const contractSnapshot = {
  home: { opportunities_today: 14, eligible_today: 8, approved_today: 5, pending_execution: 2, alerts: 1,
    hero: { fixture: 'RB Leipzig vs Mainz', market: 'Over 1.5 Equipa', module_source:'v12', global_score: 88, confidence_norm: 84, edge_norm: 76, risk_norm: 28, priority_tier:'T1', decision_status:'APPROVED' } },
  pool: [
    { fixture:'RB Leipzig vs Mainz', market:'Over 1.5 Equipa', module_source:'v12', global_score:88, confidence_norm:84, edge_norm:76, risk_norm:28, priority_tier:'T1', eligibility:'ELIGIBLE', decision_status:'APPROVED', execution_status:'PENDING', data_quality_flag:'GREEN' },
    { fixture:'Atalanta vs Bologna', market:'Over 1.5 Jogo', module_source:'v12', global_score:82, confidence_norm:79, edge_norm:71, risk_norm:34, priority_tier:'T1', eligibility:'ELIGIBLE', decision_status:'REDUCED', execution_status:'PENDING', data_quality_flag:'GREEN' },
    { fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:80, confidence_norm:77, edge_norm:68, risk_norm:31, priority_tier:'T2', eligibility:'ELIGIBLE', decision_status:'APPROVED_REDUCED', execution_status:'PLACED', data_quality_flag:'YELLOW' }
  ],
  bankroll: [
    { fixture:'RB Leipzig vs Mainz', decision_status:'APPROVED', stake:'1.00u', exposure_impact:'Low', reason:'Strong score + acceptable risk', execution_readiness:'READY' },
    { fixture:'Atalanta vs Bologna', decision_status:'REDUCED', stake:'0.50u', exposure_impact:'Medium', reason:'Correlated exposure managed', execution_readiness:'READY' },
    { fixture:'Roma vs Lecce', decision_status:'BLOCKED', stake:'0u', exposure_impact:'Blocked', reason:'Lineup uncertainty', execution_readiness:'NO' }
  ],
  execution: [
    { fixture:'RB Leipzig vs Mainz', execution_status:'PENDING', intake_status:'QUEUED', queue_age:'3m' },
    { fixture:'Atalanta vs Bologna', execution_status:'LIVE', intake_status:'PLACED', queue_age:'0m' },
    { fixture:'Roma vs Lecce', execution_status:'SETTLED', intake_status:'PLACED', queue_age:'0m' }
  ],
  history: [
    { date:'2026-03-24', fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:80, confidence_norm:77, edge_norm:68, risk_norm:31, decision_status:'APPROVED_REDUCED', execution_status:'SETTLED', result:'WIN', roi:'+0.31u' },
    { date:'2026-03-24', fixture:'PSV vs Twente', market:'Over 1.5 Equipa', module_source:'v12', global_score:86, confidence_norm:83, edge_norm:74, risk_norm:29, decision_status:'APPROVED', execution_status:'SETTLED', result:'LOSS', roi:'-1.00u' }
  ]
};
export const orchestratorSnapshot = {
  readiness: { data_api:'READY', modules: { cards:'READY', v12:'READY', btts:'READY', corners:'READY' }, gps:'READY', bankroll:'READY', execution:'READY' },
  run: { run_id:'run_20260325_001', pipeline_state:'RUNNING', current_stage:'BANKROLL', final_result:null, progress_pct:64,
    stages:[
      { key:'DATA_API', label:'Data/API', state:'SUCCESS' },
      { key:'MODULES', label:'Módulos', state:'SUCCESS' },
      { key:'GPS', label:'GPS', state:'SUCCESS' },
      { key:'BANKROLL', label:'Banca', state:'RUNNING' },
      { key:'EXECUTION', label:'Execution', state:'IDLE' }
    ],
    issues:[{ severity:'warning', message:'BTTS returned reduced eligible volume' }],
    summary:{ opportunities_generated:14, eligible:8, approved:5, sent_to_execution:2 }
  }
};
