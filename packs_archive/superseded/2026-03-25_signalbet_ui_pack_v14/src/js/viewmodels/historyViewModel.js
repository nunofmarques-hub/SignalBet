
export function buildHistoryViewModel(system) {
  return { rows: system.pool_rows.map((r,i)=>({ date: '2026-03-25', result: i===0 ? 'WIN' : (i===1?'LOSS':'VOID'), ...r })) };
}
