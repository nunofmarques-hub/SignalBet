import { ContractMockProvider } from './contractMockProvider.js';
import { OrchestratorMockProvider } from './orchestratorMockProvider.js';
import { RealSystemPlaceholderProvider } from './realSystemPlaceholderProvider.js';

const providers = {
  contract_mock: new ContractMockProvider(),
  orchestrator_mock: new OrchestratorMockProvider(),
  placeholder_live: new RealSystemPlaceholderProvider(),
};

export const runtimeSourceRegistry = {
  get(mode) {
    return providers[mode] || providers.orchestrator_mock;
  },
  modes: Object.keys(providers)
};
