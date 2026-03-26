export const appState = {
  pages: {
    home: 'success',
    pool: 'success',
    bankroll: 'success',
    execution: 'loading',
    history: 'empty'
  },
  readiness: {
    data_api: 'ready',
    modules: 4,
    gps: 'ready',
    bankroll: 'ready',
    execution: 'ready',
    orchestrator: 'visual_only'
  },
  runProgress: 72,
  runSummary: {
    opportunities: 18,
    eligible: 9,
    approved: 4,
    pending_execution: 2,
    open_executions: 3,
    alerts: 1
  }
};

export const homeData = {
  hero: {
    title: 'Best of the Day',
    fixture: 'Leverkusen vs Mainz',
    market: 'Over 1.5 Equipa Casa',
    module_source: 'v12',
    global_score: 91,
    confidence_norm: 88,
    edge_norm: 81,
    risk_norm: 22,
    priority_tier: 'T1',
    decision_status: 'approved',
    summary: 'Oportunidade prioritária com score alto, confiança forte e risco controlado. Pronta para handoff à banca e acompanhamento de execution.'
  },
  kpis: [
    ['Opportunities Today', '18', '4 módulos ativos'],
    ['Eligible Picks', '9', 'Após normalização GPS'],
    ['Approved by Bankroll', '4', '2 reduced / 1 reserve'],
    ['Pending Execution', '2', '1 atraso operacional'],
    ['Open Executions', '3', '2 live / 1 placed'],
    ['Alerts / Flags', '1', 'Data quality amarela']
  ],
  highlights: [
    { fixture:'PSV vs Zwolle', market:'Over 2.5 Jogo', score:88, confidence:84, edge:76, decision:'approved' },
    { fixture:'Roma vs Lecce', market:'Under 3.5', score:85, confidence:82, edge:70, decision:'reserve' },
    { fixture:'Benfica vs Casa Pia', market:'Over 1.5 Equipa Casa', score:84, confidence:80, edge:74, decision:'approved' }
  ],
  alerts: [
    { level:'warning', title:'Execution delay', text:'1 pick aprovada está há 19 minutos em pending intake.' }
  ],
  modules: [
    { name:'v12', picks:6, health:'fresh' },
    { name:'Corners', picks:4, health:'fresh' },
    { name:'BTTS', picks:3, health:'fresh' },
    { name:'Cards', picks:5, health:'staged' }
  ]
};

export const poolData = {
  summary: [
    ['Total Opportunities', '18'], ['Eligible', '9'], ['Approved', '4'], ['Reserve', '2'], ['Blocked', '3'], ['Avg Global Score', '82']
  ],
  top: {
    fixture:'Leverkusen vs Mainz', market:'Over 1.5 Equipa Casa', module_source:'v12', global_score:91, confidence_norm:88, edge_norm:81, risk_norm:22, priority_tier:'T1', decision_status:'approved', eligibility:'eligible', execution_status:'pending', data_quality_flag:'green'
  },
  rows: [
    ['Leverkusen vs Mainz','Over 1.5 Equipa Casa','v12',91,88,81,22,'T1','eligible','approved','pending','green'],
    ['PSV vs Zwolle','Over 2.5 Jogo','v12',88,84,76,28,'T1','eligible','approved','placed','green'],
    ['Roma vs Lecce','Under 3.5','v12',85,82,70,31,'T2','eligible','reserve','none','green'],
    ['Benfica vs Casa Pia','Over 1.5 Equipa Casa','v12',84,80,74,29,'T2','eligible','approved','live','green'],
    ['Atalanta vs Torino','BTTS','BTTS',82,77,68,36,'T2','eligible','reduced','none','amber'],
    ['Sevilla vs Valencia','Over Cantos','Corners',79,74,66,38,'T3','watchlist','blocked','none','amber']
  ]
};

export const bankrollData = {
  summary: [
    ['Bankroll Base','€2,500'], ['Available Exposure','€410'], ['Approved Today','4'], ['Reduced','2'], ['Blocked','3'], ['Reserve','2'], ['Allocated Stake','€190'], ['Remaining Capacity','€220']
  ],
  decisions: [
    ['Leverkusen vs Mainz','v12',91,88,81,22,'approved','€60','low','green','ready'],
    ['PSV vs Zwolle','v12',88,84,76,28,'approved','€50','medium','green','ready'],
    ['Roma vs Lecce','v12',85,82,70,31,'reserve','€0','none','amber','hold'],
    ['Atalanta vs Torino','BTTS',82,77,68,36,'reduced','€20','medium','amber','ready'],
    ['Sevilla vs Valencia','Corners',79,74,66,38,'blocked','€0','high','red','not_ready']
  ],
  exposure: [
    ['Mercado Over', 58], ['Under', 26], ['BTTS', 10], ['Corners', 6]
  ],
  alerts: [
    { level:'warning', title:'Correlation detected', text:'2 picks aprovadas no mesmo perfil ofensivo podem concentrar exposição.' },
    { level:'info', title:'Reserve available', text:'Roma vs Lecce pode avançar se remaining capacity subir após settlement.' }
  ]
};

export const executionData = {
  summary: [
    ['Pending Intake','2'], ['Placed','3'], ['Live','2'], ['Settled Today','5'], ['Issues','1'], ['Avg Delay','7m']
  ],
  intake: [
    ['Leverkusen vs Mainz','v12','approved','€60','ready','pending','21:15','19m'],
    ['Atalanta vs Torino','BTTS','reduced','€20','ready','queued','21:24','10m']
  ],
  live: [
    ['PSV vs Zwolle','Over 2.5 Jogo','20:42','placed','live','€50','€92.50','green'],
    ['Benfica vs Casa Pia','Over 1.5 Equipa Casa','20:51','placed','live','€40','€66.00','green'],
    ['Dortmund vs Bremen','Over 1.5 Equipa Casa','19:58','placed','watch','€35','€55.30','amber']
  ],
  settled: [
    ['Bayern vs Augsburg','win','20:58','+€28.40'],
    ['Roma vs Lecce','void','20:22','€0.00'],
    ['Lazio vs Udinese','loss','19:48','-€25.00']
  ],
  alerts: [
    { level:'warning', title:'Intake delayed', text:'Leverkusen vs Mainz está pronta, mas ainda não transitou para placed.' }
  ]
};

export const historyData = {
  summary: [
    ['Total Picks','126'], ['Settled','118'], ['Wins','69'], ['Losses','41'], ['Voids','8'], ['Strike Rate','58.5%'], ['ROI','+9.8%'], ['Avg Global Score','81']
  ],
  ledger: [
    ['2026-03-24','Bayern vs Augsburg','Over 1.5 Equipa Casa','v12',89,86,79,24,'approved','settled','win','+12.5%','green'],
    ['2026-03-24','Roma vs Lecce','Under 3.5','v12',85,82,70,31,'reserve','void','void','0%','green'],
    ['2026-03-23','Atalanta vs Torino','BTTS','BTTS',82,77,68,36,'reduced','settled','loss','-100%','amber'],
    ['2026-03-23','Sevilla vs Valencia','Over Cantos','Corners',79,74,66,38,'blocked','not_executed','na','na','amber']
  ],
  insights: [
    { level:'info', title:'v12 remains strongest', text:'Nos últimos 7 dias, v12 manteve o melhor equilíbrio entre strike rate e ROI.' },
    { level:'warning', title:'Amber quality drag', text:'Picks com data quality amber tiveram desempenho abaixo da média do período.' }
  ]
};
