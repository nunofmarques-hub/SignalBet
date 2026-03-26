export function adaptContractSnapshot(raw) {
  return {
    topOpportunity: raw.topOpportunity,
    kpis: raw.kpis,
    pool: raw.pool,
    history: raw.history
  };
}
