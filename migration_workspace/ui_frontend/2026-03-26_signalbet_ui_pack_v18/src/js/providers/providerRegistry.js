import data from '../data/mock-data.js';
import { getRealProtectedSnapshot } from './realOrchestratorProtectedProvider.js';

export const providerRegistry = {
  contract_mock: async ()=> data.contractSnapshot,
  orchestrator_mock: async ()=> data.orchestratorSnapshot,
  real_read_protected: async (options={}) => getRealProtectedSnapshot(options),
  placeholder_live: async ()=> null
};
