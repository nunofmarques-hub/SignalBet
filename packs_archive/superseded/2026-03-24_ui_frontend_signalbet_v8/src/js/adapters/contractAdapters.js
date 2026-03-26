function mapKpis(items){ return items.map(i => [i.label, i.value, i.foot || '']); }

export function adaptApp(raw){
  return {
    brand: raw.app.brand,
    backbone: raw.app.backbone,
    pages: raw.app.pages,
    readiness: {
      data_api: raw.orchestrator.readiness.data_api.status,
      modules: raw.orchestrator.readiness.modules.length,
      gps: raw.orchestrator.readiness.gps.status,
      bankroll: raw.orchestrator.readiness.bankroll.status,
      execution: raw.orchestrator.readiness.execution.status,
      orchestrator: raw.orchestrator.status
    },
    orchestrator: raw.orchestrator
  };
}

export function adaptHome(raw){
  return {
    hero: raw.home.hero,
    kpis: mapKpis(raw.home.kpis),
    highlights: raw.home.highlights,
    alerts: raw.home.alerts,
    modules: raw.orchestrator.readiness.modules.map(m => ({name:m.name, picks:m.picks, health:m.status}))
  };
}

export function adaptPool(raw){
  return {
    summary: raw.pool.summary.map(i => [i.label, i.value]),
    top: raw.pool.top,
    rows: raw.pool.rows
  };
}

export function adaptBankroll(raw){
  return {
    summary: raw.bankroll.summary.map(i => [i.label, i.value]),
    decisions: raw.bankroll.decisions,
    exposure: raw.bankroll.exposure_mix.map(i => [i.label, i.value]),
    alerts: raw.bankroll.alerts
  };
}

export function adaptExecution(raw){
  return {
    summary: raw.execution.summary.map(i => [i.label, i.value]),
    intake: raw.execution.intake,
    live: raw.execution.live,
    settled: raw.execution.settled,
    alerts: raw.execution.alerts
  };
}

export function adaptHistory(raw){
  return {
    summary: raw.history.summary.map(i => [i.label, i.value]),
    ledger: raw.history.ledger,
    insights: raw.history.insights
  };
}
