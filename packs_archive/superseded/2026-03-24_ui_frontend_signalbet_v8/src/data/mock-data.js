export const rawContractData = {
  app: {
    brand: 'SignalBet',
    backbone: 'ABC PRO',
    pages: { home: 'success', pool: 'success', bankroll: 'success', execution: 'loading', history: 'empty' }
  },
  orchestrator: {
    status: 'partial',
    readiness: {
      data_api: { status: 'ready', provider: 'Data_API_Official_Trunk_v1' },
      modules: [
        { name: 'v12', status: 'ready', picks: 6 },
        { name: 'Corners', status: 'ready', picks: 4 },
        { name: 'BTTS', status: 'ready', picks: 3 },
        { name: 'Cards', status: 'staged', picks: 5 }
      ],
      gps: { status: 'ready', shortlisted: 9 },
      bankroll: { status: 'ready', approved: 4 },
      execution: { status: 'ready', pending: 2 }
    },
    steps: [
      { key: 'data_api', title: 'Data/API', status: 'success', description: 'Providers oficiais verificados e estrutura pronta a consumo.' },
      { key: 'modules', title: 'Módulos', status: 'success', description: 'v12, Corners, BTTS e Cards disponíveis para corrida.' },
      { key: 'gps', title: 'GPS', status: 'success', description: 'Normalização multi-módulo e shortlist central gerada.' },
      { key: 'bankroll', title: 'Banca', status: 'success', description: 'Approved / Reduced / Blocked / Reserve aplicados.' },
      { key: 'execution', title: 'Execution', status: 'warning', description: 'Intake real pronto, com 2 itens ainda em pending.' }
    ],
    progress: 82,
    summary: {
      opportunities: 18,
      eligible: 9,
      approved: 4,
      pending_execution: 2,
      open_executions: 3,
      alerts: 1
    }
  },
  home: {
    hero: {
      fixture: 'Leverkusen vs Mainz', market: 'Over 1.5 Equipa Casa', module_source: 'v12',
      global_score: 91, confidence_norm: 88, edge_norm: 81, risk_norm: 22,
      priority_tier: 'T1', decision_status: 'approved', eligibility: 'eligible', execution_status: 'pending',
      summary: 'Oportunidade prioritária com score alto, confiança forte e risco controlado. Pronta para handoff à banca e acompanhamento de execution.'
    },
    kpis: [
      { label: 'Opportunities Today', value: '18', foot: '4 módulos ativos' },
      { label: 'Eligible Picks', value: '9', foot: 'Após normalização GPS' },
      { label: 'Approved by Bankroll', value: '4', foot: '2 reduced / 1 reserve' },
      { label: 'Pending Execution', value: '2', foot: '1 atraso operacional' },
      { label: 'Open Executions', value: '3', foot: '2 live / 1 placed' },
      { label: 'Alerts / Flags', value: '1', foot: 'Data quality amarela' }
    ],
    highlights: [
      { fixture:'PSV vs Zwolle', market:'Over 2.5 Jogo', module_source:'v12', global_score:88, confidence_norm:84, edge_norm:76, risk_norm:28, decision_status:'approved' },
      { fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:85, confidence_norm:82, edge_norm:70, risk_norm:31, decision_status:'reserve' },
      { fixture:'Benfica vs Casa Pia', market:'Over 1.5 Equipa Casa', module_source:'v12', global_score:84, confidence_norm:80, edge_norm:74, risk_norm:29, decision_status:'approved' }
    ],
    alerts: [
      { level:'warning', title:'Execution delay', text:'1 pick aprovada está há 19 minutos em pending intake.' }
    ]
  },
  pool: {
    summary: [
      { label:'Total Opportunities', value:'18' }, { label:'Eligible', value:'9' }, { label:'Approved', value:'4' }, { label:'Reserve', value:'2' }, { label:'Blocked', value:'3' }, { label:'Avg Global Score', value:'82' }
    ],
    top: { fixture:'Leverkusen vs Mainz', market:'Over 1.5 Equipa Casa', module_source:'v12', global_score:91, confidence_norm:88, edge_norm:81, risk_norm:22, priority_tier:'T1', decision_status:'approved', eligibility:'eligible', execution_status:'pending', data_quality_flag:'green', odd:'1.42' },
    rows: [
      { fixture:'Leverkusen vs Mainz', market:'Over 1.5 Equipa Casa', module_source:'v12', global_score:91, confidence_norm:88, edge_norm:81, risk_norm:22, priority_tier:'T1', eligibility:'eligible', decision_status:'approved', execution_status:'pending', data_quality_flag:'green' },
      { fixture:'PSV vs Zwolle', market:'Over 2.5 Jogo', module_source:'v12', global_score:88, confidence_norm:84, edge_norm:76, risk_norm:28, priority_tier:'T1', eligibility:'eligible', decision_status:'approved', execution_status:'placed', data_quality_flag:'green' },
      { fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:85, confidence_norm:82, edge_norm:70, risk_norm:31, priority_tier:'T2', eligibility:'eligible', decision_status:'reserve', execution_status:'none', data_quality_flag:'green' },
      { fixture:'Benfica vs Casa Pia', market:'Over 1.5 Equipa Casa', module_source:'v12', global_score:84, confidence_norm:80, edge_norm:74, risk_norm:29, priority_tier:'T2', eligibility:'eligible', decision_status:'approved', execution_status:'live', data_quality_flag:'green' },
      { fixture:'Atalanta vs Torino', market:'BTTS', module_source:'BTTS', global_score:82, confidence_norm:77, edge_norm:68, risk_norm:36, priority_tier:'T2', eligibility:'eligible', decision_status:'reduced', execution_status:'none', data_quality_flag:'amber' },
      { fixture:'Sevilla vs Valencia', market:'Over Cantos', module_source:'Corners', global_score:79, confidence_norm:74, edge_norm:66, risk_norm:38, priority_tier:'T3', eligibility:'watchlist', decision_status:'blocked', execution_status:'none', data_quality_flag:'amber' }
    ]
  },
  bankroll: {
    summary: [
      { label:'Bankroll Base', value:'€2,500' }, { label:'Available Exposure', value:'€410' }, { label:'Approved Today', value:'4' }, { label:'Reduced', value:'2' }, { label:'Blocked', value:'3' }, { label:'Reserve', value:'2' }, { label:'Allocated Stake', value:'€190' }, { label:'Remaining Capacity', value:'€220' }
    ],
    decisions: [
      { fixture:'Leverkusen vs Mainz', module_source:'v12', global_score:91, confidence_norm:88, edge_norm:81, risk_norm:22, decision_status:'approved', stake:'€60', exposure_impact:'low', reason_code:'edge_plus_low_risk', execution_readiness:'ready' },
      { fixture:'PSV vs Zwolle', module_source:'v12', global_score:88, confidence_norm:84, edge_norm:76, risk_norm:28, decision_status:'approved', stake:'€50', exposure_impact:'medium', reason_code:'approved_core', execution_readiness:'ready' },
      { fixture:'Roma vs Lecce', module_source:'v12', global_score:85, confidence_norm:82, edge_norm:70, risk_norm:31, decision_status:'reserve', stake:'€0', exposure_impact:'none', reason_code:'capacity_hold', execution_readiness:'hold' },
      { fixture:'Atalanta vs Torino', module_source:'BTTS', global_score:82, confidence_norm:77, edge_norm:68, risk_norm:36, decision_status:'reduced', stake:'€20', exposure_impact:'medium', reason_code:'risk_trim', execution_readiness:'ready' },
      { fixture:'Sevilla vs Valencia', module_source:'Corners', global_score:79, confidence_norm:74, edge_norm:66, risk_norm:38, decision_status:'blocked', stake:'€0', exposure_impact:'high', reason_code:'conflict_exposure', execution_readiness:'not_ready' }
    ],
    exposure_mix: [
      { label:'Mercado Over', value:58 }, { label:'Under', value:26 }, { label:'BTTS', value:10 }, { label:'Corners', value:6 }
    ],
    alerts: [
      { level:'warning', title:'Correlation detected', text:'2 picks aprovadas no mesmo perfil ofensivo podem concentrar exposição.' },
      { level:'info', title:'Reserve available', text:'Roma vs Lecce pode avançar se remaining capacity subir após settlement.' }
    ]
  },
  execution: {
    summary: [
      { label:'Pending Intake', value:'2' }, { label:'Placed', value:'3' }, { label:'Live', value:'2' }, { label:'Settled Today', value:'5' }, { label:'Issues', value:'1' }, { label:'Avg Delay', value:'7m' }
    ],
    intake: [
      { fixture:'Leverkusen vs Mainz', module_source:'v12', decision_status:'approved', stake:'€60', execution_readiness:'ready', intake_status:'pending', created_at:'21:15', queue_age:'19m' },
      { fixture:'Atalanta vs Torino', module_source:'BTTS', decision_status:'reduced', stake:'€20', execution_readiness:'ready', intake_status:'queued', created_at:'21:24', queue_age:'10m' }
    ],
    live: [
      { fixture:'PSV vs Zwolle', market:'Over 2.5 Jogo', placed_at:'20:42', execution_status:'placed', live_status:'live', stake:'€50', potential_return:'€92.50', tracking_flag:'green' },
      { fixture:'Benfica vs Casa Pia', market:'Over 1.5 Equipa Casa', placed_at:'20:51', execution_status:'placed', live_status:'live', stake:'€40', potential_return:'€66.00', tracking_flag:'green' },
      { fixture:'Dortmund vs Bremen', market:'Over 1.5 Equipa Casa', placed_at:'19:58', execution_status:'placed', live_status:'watch', stake:'€35', potential_return:'€55.30', tracking_flag:'amber' }
    ],
    settled: [
      { fixture:'Bayern vs Augsburg', result:'win', settled_at:'20:58', delta:'+€28.40' },
      { fixture:'Roma vs Lecce', result:'void', settled_at:'20:22', delta:'€0.00' },
      { fixture:'Lazio vs Udinese', result:'loss', settled_at:'19:48', delta:'-€25.00' }
    ],
    alerts: [
      { level:'warning', title:'Intake delayed', text:'Leverkusen vs Mainz está pronta, mas ainda não transitou para placed.' }
    ]
  },
  history: {
    summary: [
      { label:'Total Picks', value:'126' }, { label:'Settled', value:'118' }, { label:'Wins', value:'69' }, { label:'Losses', value:'41' }, { label:'Voids', value:'8' }, { label:'Strike Rate', value:'58.5%' }, { label:'ROI', value:'+9.8%' }, { label:'Avg Global Score', value:'81' }
    ],
    ledger: [
      { date:'2026-03-24', fixture:'Bayern vs Augsburg', market:'Over 1.5 Equipa Casa', module_source:'v12', global_score:89, confidence_norm:86, edge_norm:79, risk_norm:24, decision_status:'approved', execution_status:'settled', result:'win', roi:'+12.5%', data_quality_flag:'green' },
      { date:'2026-03-24', fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:85, confidence_norm:82, edge_norm:70, risk_norm:31, decision_status:'reserve', execution_status:'void', result:'void', roi:'0%', data_quality_flag:'green' },
      { date:'2026-03-23', fixture:'Atalanta vs Torino', market:'BTTS', module_source:'BTTS', global_score:82, confidence_norm:77, edge_norm:68, risk_norm:36, decision_status:'reduced', execution_status:'settled', result:'loss', roi:'-100%', data_quality_flag:'amber' },
      { date:'2026-03-23', fixture:'Sevilla vs Valencia', market:'Over Cantos', module_source:'Corners', global_score:79, confidence_norm:74, edge_norm:66, risk_norm:38, decision_status:'blocked', execution_status:'not_executed', result:'na', roi:'na', data_quality_flag:'amber' }
    ],
    insights: [
      { level:'info', title:'v12 remains strongest', text:'Nos últimos 7 dias, v12 manteve o melhor equilíbrio entre strike rate e ROI.' },
      { level:'warning', title:'Amber quality drag', text:'Picks com data quality amber tiveram desempenho abaixo da média do período.' }
    ]
  }
};
