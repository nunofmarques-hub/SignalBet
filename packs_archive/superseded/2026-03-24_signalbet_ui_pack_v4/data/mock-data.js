window.SignalBetData = {
  home: {
    hero: {
      fixture: 'PSV vs Utrecht',
      market: 'Over 1.5 Equipa',
      module_source: 'v12',
      global_score: 91,
      confidence_norm: 84,
      edge_norm: 73,
      risk_norm: 28,
      priority_tier: 'A+',
      decision_status: 'approved'
    },
    kpis: [
      ['Opportunities Today', '18'],
      ['Eligible', '11'],
      ['Approved', '6'],
      ['Pending Execution', '3'],
      ['Live', '4'],
      ['Alerts', '1']
    ]
  },
  pool: [
    {fixture:'PSV vs Utrecht', market:'Over 1.5 Equipa', module_source:'v12', global_score:91, confidence_norm:84, edge_norm:73, risk_norm:28, priority_tier:'A+', eligibility:'eligible', decision_status:'approved', execution_status:'pending', data_quality_flag:'green'},
    {fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', global_score:88, confidence_norm:80, edge_norm:68, risk_norm:24, priority_tier:'A', eligibility:'eligible', decision_status:'approved', execution_status:'placed', data_quality_flag:'green'},
    {fixture:'Benfica vs Braga', market:'BTTS', module_source:'BTTS', global_score:81, confidence_norm:76, edge_norm:64, risk_norm:41, priority_tier:'B+', eligibility:'watch', decision_status:'reserve', execution_status:'none', data_quality_flag:'yellow'},
    {fixture:'Real Madrid vs Getafe', market:'Corners Over', module_source:'Corners', global_score:79, confidence_norm:71, edge_norm:61, risk_norm:39, priority_tier:'B', eligibility:'eligible', decision_status:'reduced', execution_status:'pending', data_quality_flag:'green'}
  ],
  banking: [
    {fixture:'PSV vs Utrecht', decision_status:'approved', stake:'1.00u', exposure_impact:'low', execution_readiness:'ready', reason:'High score + low risk'},
    {fixture:'Roma vs Lecce', decision_status:'approved', stake:'0.75u', exposure_impact:'low', execution_readiness:'ready', reason:'Stable under profile'},
    {fixture:'Benfica vs Braga', decision_status:'reserve', stake:'0.25u', exposure_impact:'medium', execution_readiness:'hold', reason:'Correlation caution'},
    {fixture:'Real Madrid vs Getafe', decision_status:'reduced', stake:'0.50u', exposure_impact:'medium', execution_readiness:'ready', reason:'Edge ok, risk moderate'}
  ],
  execution: [
    {fixture:'PSV vs Utrecht', intake_status:'pending', execution_status:'pending', queue_age:'08m'},
    {fixture:'Roma vs Lecce', intake_status:'accepted', execution_status:'placed', queue_age:'00m'},
    {fixture:'Inter vs Atalanta', intake_status:'accepted', execution_status:'live', queue_age:'--'},
    {fixture:'Sporting vs Casa Pia', intake_status:'accepted', execution_status:'settled', queue_age:'--'}
  ],
  history: [
    {date:'2026-03-21', fixture:'Roma vs Lecce', market:'Under 3.5', module_source:'v12', result:'win', roi:'+0.31u', decision_status:'approved', execution_status:'settled'},
    {date:'2026-03-21', fixture:'Sporting vs Casa Pia', market:'Over 1.5 Equipa', module_source:'v12', result:'win', roi:'+0.42u', decision_status:'approved', execution_status:'settled'},
    {date:'2026-03-20', fixture:'Benfica vs Braga', market:'BTTS', module_source:'BTTS', result:'loss', roi:'-0.50u', decision_status:'reserve', execution_status:'none'}
  ]
};
