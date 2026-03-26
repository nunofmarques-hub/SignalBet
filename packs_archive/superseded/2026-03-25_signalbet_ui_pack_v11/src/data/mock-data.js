export const orchestratorSnapshot = {
  run_id: 'run_20260325_001',
  cta_state: 'ready',
  readiness_level: 'high',
  project_feed_coverage_ratio: 0.86,
  pipeline_state: 'idle',
  current_stage: 'precheck',
  final_result: null,
  summary: {opportunities: 18, eligible: 9, approved: 4, execution_ready: 4},
  module_overview: [
    {module: 'Cards', status: 'ready', picks: 3},
    {module: 'v12', status: 'ready', picks: 5},
    {module: 'BTTS', status: 'ready', picks: 4},
    {module: 'Corners', status: 'degraded', picks: 6}
  ],
  pipeline_steps: [
    {key: 'data_api', label: 'Data/API', status: 'done'},
    {key: 'modules', label: 'Módulos', status: 'done'},
    {key: 'gps', label: 'GPS', status: 'done'},
    {key: 'bankroll', label: 'Banca', status: 'ready'},
    {key: 'execution', label: 'Execution', status: 'ready'}
  ],
  issues: [
    {level:'warning', text:'Corners com cobertura parcial em parte da corrida.'}
  ]
};
export const pages = {
  home: {kpis:[['Opportunities Today',18],['Eligible',9],['Approved',4],['Pending Execution',2]], hero:{title:'Best of the Day', fixture:'RB Leipzig vs Mainz', market:'Over 1.5 Golos', score:91, confidence:87, edge:18, risk:22}},
  pool: {rows:[['RB Leipzig vs Mainz','Over 1.5','v12',91,'HIGH','APPROVED'],['Lazio vs Udinese','Under 3.5','Cards',84,'MED','RESERVE']]},
  bankroll: {rows:[['RB Leipzig vs Mainz','APPROVED','1.25u','low'],['Lazio vs Udinese','REDUCED','0.50u','med']]},
  execution: {rows:[['RB Leipzig vs Mainz','placed','live'],['Lazio vs Udinese','pending','queued']]},
  history: {rows:[['2026-03-24','PSV vs Twente','WIN','+0.85u'],['2026-03-24','Roma vs Lecce','LOSS','-1.00u']]}
};
