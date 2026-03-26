window.SignalBetMock = {
  meta: {
    appName: 'SignalBet',
    tag: 'Menos ruído. Mais sinal.'
  },
  home: {
    hero: {
      fixture: 'Inter vs Atalanta',
      market: 'Over 1.5 Equipa',
      module_source: 'v12',
      global_score: 88,
      confidence_norm: 0.84,
      edge_norm: 0.11,
      risk_norm: 0.28,
      priority_tier: 'Tier 1',
      decision_status: 'approved',
      execution_status: 'pending_intake',
      data_quality_flag: 'strong_data'
    },
    kpis: [
      ['Opportunities Today','26'],
      ['Eligible','14'],
      ['Approved','5'],
      ['Pending Execution','2'],
      ['Live','3'],
      ['Alerts','1']
    ],
    highlights: [
      {fixture:'Liverpool vs Brentford', market:'Over 2.5', global_score:84, confidence_norm:0.81, edge_norm:0.09, decision_status:'approved'},
      {fixture:'Benfica vs Casa Pia', market:'Under 3.5', global_score:79, confidence_norm:0.76, edge_norm:0.05, decision_status:'reserve'},
      {fixture:'PSV vs Utrecht', market:'Over 1.5 Equipa', global_score:82, confidence_norm:0.80, edge_norm:0.08, decision_status:'approved'}
    ],
    alerts: [
      {level:'warning', text:'1 pick com data_quality_flag amarela.'}
    ]
  },
  pool: [
    {fixture:'Liverpool vs Brentford', market:'Over 2.5', module_source:'v12', global_score:84, confidence_norm:0.81, edge_norm:0.09, risk_norm:0.31, priority_tier:'Tier 1', eligibility:'eligible', decision_status:'approved', execution_status:'pending_intake', data_quality_flag:'strong_data', odd:'1.88'},
    {fixture:'Atalanta vs Torino', market:'BTTS', module_source:'BTTS', global_score:78, confidence_norm:0.75, edge_norm:0.08, risk_norm:0.36, priority_tier:'Tier 1', eligibility:'eligible', decision_status:'pending', execution_status:'not_sent', data_quality_flag:'strong_data', odd:'1.75'},
    {fixture:'Sevilla vs Osasuna', market:'Under 3.5', module_source:'v12', global_score:74, confidence_norm:0.72, edge_norm:0.05, risk_norm:0.24, priority_tier:'Tier 2', eligibility:'eligible', decision_status:'reserve', execution_status:'not_sent', data_quality_flag:'ok', odd:'1.64'},
    {fixture:'Sporting vs Marítimo', market:'Over 10.5 Corners', module_source:'Corners', global_score:71, confidence_norm:0.67, edge_norm:0.07, risk_norm:0.41, priority_tier:'Tier 2', eligibility:'conditional', decision_status:'watch', execution_status:'not_sent', data_quality_flag:'warning', odd:'1.92'},
    {fixture:'Roma vs Napoli', market:'BTTS', module_source:'BTTS', global_score:69, confidence_norm:0.64, edge_norm:0.03, risk_norm:0.46, priority_tier:'Tier 3', eligibility:'blocked', decision_status:'blocked', execution_status:'not_sent', data_quality_flag:'ok', odd:'2.05'}
  ],
  banca: {
    summary: {
      bankroll_base: '112.75u',
      available_exposure: '18.50u',
      allocated_stake: '4.75u',
      remaining_capacity: '24.3u'
    },
    queue: [
      {fixture:'Inter vs Atalanta', module_source:'v12', market:'Over 1.5 Equipa', global_score:88, confidence_norm:0.84, edge_norm:0.11, risk_norm:0.28, decision_status:'approved', stake:'2.25u', exposure_impact:'+2.2%', execution_readiness:'ready', reason_code:'value_confirmed'},
      {fixture:'Liverpool vs Brentford', module_source:'v12', market:'Over 2.5', global_score:84, confidence_norm:0.81, edge_norm:0.09, risk_norm:0.31, decision_status:'approved', stake:'2.50u', exposure_impact:'+2.5%', execution_readiness:'ready', reason_code:'clear_edge'},
      {fixture:'Sevilla vs Osasuna', module_source:'v12', market:'Under 3.5', global_score:74, confidence_norm:0.72, edge_norm:0.05, risk_norm:0.24, decision_status:'reduced', stake:'1.00u', exposure_impact:'+0.8%', execution_readiness:'ready', reason_code:'value_moderate'},
      {fixture:'Roma vs Napoli', module_source:'BTTS', market:'BTTS', global_score:69, confidence_norm:0.64, edge_norm:0.03, risk_norm:0.46, decision_status:'blocked', stake:'0u', exposure_impact:'0%', execution_readiness:'blocked', reason_code:'risk_threshold'}
    ]
  },
  execution: {
    summary: [['Pending Intake','2'],['Placed','2'],['Live','1'],['Settled Today','8'],['Issues','1']],
    queue: [
      {fixture:'Inter vs Atalanta', market:'Over 1.5 Equipa', module_source:'v12', decision_status:'approved', intake_status:'pending', execution_status:'pending_intake', created_at:'14:02', queue_age:'12m'},
      {fixture:'Liverpool vs Brentford', market:'Over 2.5', module_source:'v12', decision_status:'approved', intake_status:'confirmed', execution_status:'placed', created_at:'13:54', queue_age:'20m'}
    ],
    live: [
      {fixture:'Benfica vs Casa Pia', market:'Under 3.5', placed_at:'13:40', execution_status:'live', live_status:'HT', stake:'1.50u', potential_return:'2.46u'},
      {fixture:'PSV vs Utrecht', market:'Over 1.5 Equipa', placed_at:'12:10', execution_status:'settled', live_status:'Closed', stake:'2.00u', potential_return:'+1.20u'}
    ]
  },
  history: {
    summary: [['Total Picks','154'],['Settled','95%'],['Strike Rate','60%'],['ROI','22%'],['Profit Factor','1.53']],
    ledger: [
      {date:'2026-03-22', fixture:'Porto vs Braga', market:'Over 1.5 Equipa', module_source:'v12', global_score:82, confidence_norm:0.79, edge_norm:0.08, risk_norm:0.30, decision_status:'approved', execution_status:'direct', result:'win', roi:'+1.20u', data_quality_flag:'strong_data'},
      {date:'2026-03-22', fixture:'Atalanta vs Torino', market:'BTTS', module_source:'BTTS', global_score:78, confidence_norm:0.75, edge_norm:0.08, risk_norm:0.36, decision_status:'approved', execution_status:'direct', result:'loss', roi:'-1.00u', data_quality_flag:'strong_data'},
      {date:'2026-03-21', fixture:'Sevilla vs Osasuna', market:'Under 3.5', module_source:'v12', global_score:74, confidence_norm:0.72, edge_norm:0.05, risk_norm:0.24, decision_status:'reduced', execution_status:'placed', result:'win', roi:'+0.62u', data_quality_flag:'ok'}
    ]
  }
};
