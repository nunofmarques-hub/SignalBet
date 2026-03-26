export const summary = {
  home: { opportunities: 18, eligible: 11, approved: 6, pending: 2, live: 4, alerts: 1 },
  pool: { total: 18, eligible: 11, approved: 6, reserve: 3, blocked: 4, avgScore: 82 },
  bankroll: { bankroll: 1250, available: 780, approved: 6, reduced: 2, blocked: 4, reserve: 3, allocated: 470, remaining: 780 },
  execution: { pendingIntake: 2, placed: 6, live: 4, settled: 8, issues: 1, delay: '04m' },
  history: { total: 84, settled: 80, wins: 49, losses: 25, voids: 6, strike: '61.3%', roi: '+8.4%', avgScore: 79 }
};

export const opportunities = [
  { fixture:'RB Leipzig vs Mainz', market:'Over 1.5 Equipa', module_source:'v12', global_score:91, confidence_norm:84, edge_norm:76, risk_norm:28, priority_tier:'A', eligibility:'eligible', decision_status:'approved', execution_status:'pending', data_quality_flag:'green', odd:1.42, rationale:'Ataque forte e adversário permissivo.' },
  { fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:88, confidence_norm:81, edge_norm:72, risk_norm:25, priority_tier:'A', eligibility:'eligible', decision_status:'approved', execution_status:'placed', data_quality_flag:'green', odd:1.33, rationale:'Perfil controlado e tendência under estável.' },
  { fixture:'PSV vs Groningen', market:'Over 1.5 Equipa', module_source:'v12', global_score:86, confidence_norm:82, edge_norm:71, risk_norm:31, priority_tier:'A', eligibility:'eligible', decision_status:'reduced', execution_status:'placed', data_quality_flag:'green', odd:1.29, rationale:'Força ofensiva alta, sizing reduzido por exposição.' },
  { fixture:'Inter vs Torino', market:'BTTS Não', module_source:'BTTS', global_score:78, confidence_norm:73, edge_norm:63, risk_norm:34, priority_tier:'B', eligibility:'watchlist', decision_status:'reserve', execution_status:'queued', data_quality_flag:'yellow', odd:1.71, rationale:'Leitura aceitável, mas qualidade de dado intermédia.' },
  { fixture:'Atlético vs Getafe', market:'Under 3.5', module_source:'Cards', global_score:74, confidence_norm:69, edge_norm:57, risk_norm:41, priority_tier:'B', eligibility:'blocked', decision_status:'blocked', execution_status:'none', data_quality_flag:'yellow', odd:1.38, rationale:'Conflito com exposição e edge insuficiente.' }
];

export const executionItems = [
  { fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', decision_status:'approved', execution_status:'placed', intake_status:'ok', created_at:'10:14', queue_age:'02m', placed_at:'10:16', settled_at:'', tracking_flag:'normal' },
  { fixture:'PSV vs Groningen', market:'Over 1.5 Equipa', module_source:'v12', decision_status:'reduced', execution_status:'live', intake_status:'ok', created_at:'10:20', queue_age:'00m', placed_at:'10:21', settled_at:'', tracking_flag:'watch' },
  { fixture:'RB Leipzig vs Mainz', market:'Over 1.5 Equipa', module_source:'v12', decision_status:'approved', execution_status:'pending', intake_status:'queued', created_at:'10:31', queue_age:'04m', placed_at:'', settled_at:'', tracking_flag:'attention' }
];

export const historyItems = [
  { date:'2026-03-21', fixture:'Bayern vs Köln', market:'Over 1.5 Equipa', module_source:'v12', global_score:89, confidence_norm:83, edge_norm:74, risk_norm:26, decision_status:'approved', execution_status:'settled', result:'win', return:'+0.36u', data_quality_flag:'green' },
  { date:'2026-03-21', fixture:'Lazio vs Udinese', market:'Over 2.5', module_source:'v12', global_score:75, confidence_norm:71, edge_norm:58, risk_norm:39, decision_status:'reduced', execution_status:'settled', result:'loss', return:'-0.50u', data_quality_flag:'green' },
  { date:'2026-03-22', fixture:'Inter vs Torino', market:'BTTS Não', module_source:'BTTS', global_score:78, confidence_norm:73, edge_norm:63, risk_norm:34, decision_status:'reserve', execution_status:'void', result:'void', return:'0.00u', data_quality_flag:'yellow' }
];
