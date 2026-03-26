window.SIGNALBET_DATA = {
  app: {
    productName: 'SignalBet',
    internalSystem: 'ABC PRO',
    orchestratorStatus: 'standby',
    dataApiReference: 'Data_API_Official_Trunk_v1'
  },
  home: {
    hero: {
      pick_name: 'PSV vs Utrecht — Over 1.5 Equipa',
      market: 'Over 1.5 Equipa',
      module_source: 'v12',
      global_score: 92,
      confidence_norm: 86,
      edge_norm: 77,
      risk_norm: 24,
      priority_tier: 'T1',
      decision_status: 'approved'
    },
    kpis: [
      ['Opportunities Today', 24],
      ['Eligible', 11],
      ['Approved', 6],
      ['Pending Execution', 2],
      ['Open Executions', 3],
      ['Alerts', 1]
    ],
    highlights: [
      { pick_name:'Ajax vs Sparta — Over 1.5 Equipa', market:'Over 1.5', module_source:'v12', global_score:90, confidence_norm:84, edge_norm:71, decision_status:'approved' },
      { pick_name:'Lazio vs Udinese — Under 3.5', market:'Under 3.5', module_source:'v12', global_score:87, confidence_norm:80, edge_norm:68, decision_status:'reserve' },
      { pick_name:'Atalanta vs Lecce — BTTS', market:'BTTS', module_source:'BTTS', global_score:79, confidence_norm:74, edge_norm:63, decision_status:'reduced' }
    ]
  },
  pool: {
    summary: [
      ['Total Opportunities', 24],
      ['Eligible', 11],
      ['Approved', 6],
      ['Reserve', 3],
      ['Blocked', 5],
      ['Avg Global Score', 81]
    ],
    top: {
      fixture:'PSV vs Utrecht', market:'Over 1.5 Equipa', module_source:'v12', global_score:92, confidence_norm:86, edge_norm:77, risk_norm:24, priority_tier:'T1', eligibility:'eligible', decision_status:'approved', execution_status:'pending', data_quality_flag:'green'
    },
    rows: [
      ['PSV vs Utrecht','Over 1.5 Equipa','v12',92,86,77,24,'T1','eligible','approved','pending','green'],
      ['Ajax vs Sparta','Over 1.5 Equipa','v12',90,84,71,26,'T1','eligible','approved','pending','green'],
      ['Lazio vs Udinese','Under 3.5','v12',87,80,68,31,'T2','eligible','reserve','none','green'],
      ['Atalanta vs Lecce','BTTS','BTTS',79,74,63,39,'T2','eligible','reduced','none','yellow'],
      ['Benfica vs Braga','Over 9.5 Cantos','Corners',76,69,58,45,'T3','watchlist','blocked','none','yellow']
    ]
  },
  bank: {
    summary: [
      ['Bankroll Base','€1,000'],
      ['Available Exposure','€320'],
      ['Approved Today',6],
      ['Reduced',2],
      ['Blocked',5],
      ['Reserve',3],
      ['Allocated Stake','€180'],
      ['Remaining Capacity','€140']
    ],
    decisions: [
      ['PSV vs Utrecht','v12',92,86,77,24,'approved','€40','low','ready'],
      ['Ajax vs Sparta','v12',90,84,71,26,'approved','€35','low','ready'],
      ['Lazio vs Udinese','v12',87,80,68,31,'reserve','€0','none','hold'],
      ['Atalanta vs Lecce','BTTS',79,74,63,39,'reduced','€15','medium','ready'],
      ['Benfica vs Braga','Corners',76,69,58,45,'blocked','€0','high','no']
    ]
  },
  execution: {
    summary: [
      ['Pending Intake',2],
      ['Placed',4],
      ['Live',3],
      ['Settled Today',7],
      ['Issues',1],
      ['Avg Settlement Delay','4m']
    ],
    queue: [
      ['PSV vs Utrecht','v12','approved','€40','ready','pending','09:12','12m'],
      ['Ajax vs Sparta','v12','approved','€35','ready','pending','09:16','08m'],
      ['Atalanta vs Lecce','BTTS','reduced','€15','ready','placed','08:55','—']
    ],
    live: [
      ['Roma vs Lecce','Under 3.5','08:10','live','1H 27\'','€30','€39','green'],
      ['PSG vs Nantes','Over 1.5 Equipa','08:00','placed','NS','€25','€33','none'],
      ['Dortmund vs Mainz','Over 1.5 Equipa','07:40','settled','FT','€20','€0','loss']
    ]
  },
  history: {
    summary: [
      ['Total Picks',148],
      ['Settled',129],
      ['Wins',77],
      ['Losses',46],
      ['Voids',6],
      ['Strike Rate','59.7%'],
      ['ROI','11.8%'],
      ['Avg Global Score',79]
    ],
    validations: [
      ['v12','62%','14.2%'],
      ['BTTS','54%','8.1%'],
      ['Corners','51%','5.4%'],
      ['Approved','64%','15.0%']
    ],
    rows: [
      ['2026-03-21','PSV vs Twente','Over 1.5 Equipa','v12',91,85,74,25,'approved','settled','win','+€11','green'],
      ['2026-03-21','Roma vs Lecce','Under 3.5','v12',84,78,66,30,'approved','settled','win','+€7','green'],
      ['2026-03-20','Atalanta vs Bologna','BTTS','BTTS',77,72,60,40,'reduced','settled','loss','-€15','yellow'],
      ['2026-03-20','Benfica vs Porto','Over 9.5 Cantos','Corners',75,67,56,47,'blocked','none','no bet','€0','yellow']
    ]
  }
};
