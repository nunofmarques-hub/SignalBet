const baseRun = {
  checks: [
    { key: 'data_api', label: 'Data/API', status: 'ready', detail: 'Data_API_Official_Trunk_v1 disponível em staging forte.' },
    { key: 'modules', label: 'Módulos', status: 'ready', detail: 'v12, Cards, BTTS e GPS materializados em staging forte.' },
    { key: 'gps', label: 'Global Pick Selector', status: 'ready', detail: 'Ranking e shortlist disponíveis para handoff.' },
    { key: 'bankroll', label: 'Banca', status: 'ready', detail: 'Rules e payload para execution prontos em staging.' },
    { key: 'execution', label: 'Execution', status: 'staged', detail: 'Execution pronta em staging com intake real esperado da banca.' }
  ],
  stages: [
    { key: 'bootstrap', title: 'Bootstrap', status: 'done', detail: 'Ambiente e config validados.' },
    { key: 'data', title: 'Data/API', status: 'done', detail: 'Providers e snapshots disponíveis.' },
    { key: 'modules', title: 'Módulos', status: 'done', detail: 'Outputs consolidados para GPS.' },
    { key: 'gps', title: 'GPS', status: 'done', detail: 'Pool global e shortlist produzidas.' },
    { key: 'bankroll', title: 'Banca', status: 'active', detail: 'Decisões operacionais e sizing em curso.' },
    { key: 'execution', title: 'Execution', status: 'queued', detail: 'A aguardar approved payloads.' }
  ],
  summary: {
    opportunities: 28,
    eligible: 17,
    approved: 6,
    pending_execution: 3,
    reserve: 5,
    blocked: 6
  }
};

const variants = {
  idle: {
    status: 'idle',
    progress: 0,
    title: 'Sistema pronto a iniciar',
    message: 'A UI está pronta para mostrar readiness e arrancar a corrida quando o Orchestrator o mandar.',
    checks: baseRun.checks,
    stages: baseRun.stages.map(s => ({...s, status: s.key === 'bootstrap' ? 'ready' : 'queued'})),
    summary: baseRun.summary,
    issues: []
  },
  running: {
    status: 'running',
    progress: 58,
    title: 'Corrida em progresso',
    message: 'Data/API, módulos e GPS já avançaram. Banca e Execution estão a consumir estados intermédios.',
    checks: baseRun.checks,
    stages: baseRun.stages,
    summary: baseRun.summary,
    issues: []
  },
  partial: {
    status: 'partial',
    progress: 78,
    title: 'Corrida parcial',
    message: 'A corrida completou a shortlist e a banca, mas existem pendências de execution e warnings de quality.',
    checks: baseRun.checks.map(c => c.key === 'execution' ? {...c, status: 'warning', detail: 'Execution recebeu payload parcial e mantém pendências.'} : c),
    stages: baseRun.stages.map(s => s.key === 'execution' ? {...s, status: 'warning', detail: '2 picks pendentes por intake delay.'} : s.key === 'bankroll' ? {...s, status: 'done'} : s),
    summary: {...baseRun.summary, pending_execution: 2},
    issues: [
      { level: 'warning', title: 'Execution partial intake', text: 'Duas picks approved continuam pendentes por readiness parcial.' },
      { level: 'warning', title: 'Data quality flag', text: 'Uma pick elegível mantém flag amarela e ficou em reserve.' }
    ]
  },
  success: {
    status: 'success',
    progress: 100,
    title: 'Corrida concluída com sucesso',
    message: 'O pipeline visual está completo: readiness, módulos, GPS, banca e execution já reportam fecho consistente.',
    checks: baseRun.checks.map(c => ({...c, status: 'ready'})),
    stages: baseRun.stages.map(s => ({...s, status: 'done'})),
    summary: {...baseRun.summary, pending_execution: 0},
    issues: []
  },
  error: {
    status: 'error',
    progress: 34,
    title: 'Corrida interrompida',
    message: 'A Data/API respondeu, mas o handoff para GPS falhou nesta simulação de erro controlado.',
    checks: baseRun.checks.map(c => c.key === 'gps' ? {...c, status: 'error', detail: 'GPS não consolidou shortlist.'} : c.key === 'bankroll' || c.key === 'execution' ? {...c, status: 'not_ready', detail: 'Dependência anterior falhou.'} : c),
    stages: baseRun.stages.map(s => s.key === 'gps' ? {...s, status: 'error', detail: 'Falha de consolidação do ranking global.'} : (s.key === 'bankroll' || s.key === 'execution') ? {...s, status: 'blocked', detail: 'Dependência não concluída.'} : s),
    summary: {...baseRun.summary, approved: 0, pending_execution: 0},
    issues: [
      { level: 'critical', title: 'GPS handoff failed', text: 'Sem shortlist válida, a banca não recebe universo final.' },
      { level: 'warning', title: 'Execution blocked by dependency', text: 'Execution aguarda novo ciclo com GPS válido.' }
    ]
  }
};

export function getOrchestratorSnapshot(){
  return JSON.parse(JSON.stringify(variants.success));
}

export function getRunSnapshotByStatus(status='success'){
  return JSON.parse(JSON.stringify(variants[status] || variants.success));
}
