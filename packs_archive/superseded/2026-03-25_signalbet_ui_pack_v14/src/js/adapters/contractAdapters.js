
export function normalizeSystemSnapshot(raw = {}) {
  return {
    readiness: raw.readiness ?? 'unknown',
    source_mode: raw.source_mode ?? 'contract_mock',
    opportunities_today: Number(raw.opportunities_today ?? 0),
    eligible: Number(raw.eligible ?? 0),
    approved: Number(raw.approved ?? 0),
    pending_execution: Number(raw.pending_execution ?? 0),
    open_executions: Number(raw.open_executions ?? 0),
    alerts: Number(raw.alerts ?? 0),
    top_opportunity: raw.top_opportunity ?? null,
    pool_rows: Array.isArray(raw.pool_rows) ? raw.pool_rows : []
  };
}
