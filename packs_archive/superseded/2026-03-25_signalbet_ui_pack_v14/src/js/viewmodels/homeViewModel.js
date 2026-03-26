
export function buildHomeViewModel(system, orchestrator, metadata) {
  return {
    title: 'Home / Dashboard',
    hero: system.top_opportunity,
    kpis: [
      ['Opportunities Today', system.opportunities_today],
      ['Eligible', system.eligible],
      ['Approved', system.approved],
      ['Pending Execution', system.pending_execution],
      ['Open Executions', system.open_executions],
      ['Alerts', system.alerts]
    ],
    orchestrator, metadata
  };
}
