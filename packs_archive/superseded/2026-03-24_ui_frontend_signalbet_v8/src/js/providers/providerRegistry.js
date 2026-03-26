import { getContractSnapshot } from './contractMockProvider.js';
import { getOrchestratorSnapshot, getRunSnapshotByStatus } from './orchestratorMockProvider.js';

export const providerRegistry = {
  contract: {
    id: 'contract',
    getSnapshot: () => getContractSnapshot()
  },
  orchestrator: {
    id: 'orchestrator',
    getSnapshot: () => getOrchestratorSnapshot(),
    getRunSnapshotByStatus: (status) => getRunSnapshotByStatus(status)
  }
};

export function resolveProvider(name){
  return providerRegistry[name];
}
