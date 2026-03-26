
export function buildBankrollViewModel(system) {
  return {
    approved: system.pool_rows.filter(r => r.decision_status === 'APPROVED'),
    reduced: system.pool_rows.filter(r => r.decision_status === 'REDUCED'),
    reserve: system.pool_rows.filter(r => r.decision_status === 'RESERVE')
  };
}
