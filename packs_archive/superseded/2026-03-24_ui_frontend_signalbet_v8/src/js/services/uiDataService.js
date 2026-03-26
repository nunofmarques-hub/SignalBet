import { resolveProvider } from '../providers/providerRegistry.js';
import { adaptApp, adaptHome, adaptPool, adaptBankroll, adaptExecution, adaptHistory } from '../adapters/contractAdapters.js';
import { adaptRunState } from '../adapters/orchestratorAdapters.js';

function getContractRaw(){
  return resolveProvider('contract').getSnapshot();
}

function getOrchestratorProvider(){
  return resolveProvider('orchestrator');
}

export function getAppContext(){ const raw = getContractRaw(); return adaptApp(raw); }
export function getHomeModel(){ const raw = getContractRaw(); return adaptHome(raw); }
export function getPoolModel(){ const raw = getContractRaw(); return adaptPool(raw); }
export function getBankrollModel(){ const raw = getContractRaw(); return adaptBankroll(raw); }
export function getExecutionModel(){ const raw = getContractRaw(); return adaptExecution(raw); }
export function getHistoryModel(){ const raw = getContractRaw(); return adaptHistory(raw); }

export function getOrchestratorRunModel(status){
  const run = getOrchestratorProvider().getRunSnapshotByStatus(status);
  return adaptRunState(run);
}
