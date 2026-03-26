export function adaptHome(snapshot){ return snapshot.home; }
export function adaptPool(snapshot){ return snapshot.pool || []; }
export function adaptBankroll(snapshot){ return snapshot.bankroll || []; }
export function adaptExecution(snapshot){ return snapshot.execution || []; }
export function adaptHistory(snapshot){ return snapshot.history || []; }
