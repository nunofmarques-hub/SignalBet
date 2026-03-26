import { getSystemSnapshot } from './systemSnapshotService.js';
import { getPipelineSnapshot } from './pipelineStatusService.js';
import { adaptHome, adaptPool, adaptBankroll, adaptExecution, adaptHistory } from '../adapters/contractAdapters.js';
import { adaptReadiness, adaptRun } from '../adapters/orchestratorAdapters.js';
export function bootstrapUI(){
  const system = getSystemSnapshot('contract_mock');
  const pipeline = getPipelineSnapshot('contract_mock');
  return {
    home: adaptHome(system),
    pool: adaptPool(system),
    bankroll: adaptBankroll(system),
    execution: adaptExecution(system),
    history: adaptHistory(system),
    readiness: adaptReadiness(pipeline),
    run: adaptRun(pipeline),
    providerStatus: { contract:'contract_mock', orchestrator:'orchestrator_mock', real:'real_placeholder' }
  };
}
