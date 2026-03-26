import { contractMockProvider } from './contractMockProvider.js';
import { orchestratorMockProvider } from './orchestratorMockProvider.js';
import { realSystemPlaceholderProvider } from './realSystemPlaceholderProvider.js';
import { realOrchestratorProtectedProvider } from './realOrchestratorProtectedProvider.js';
export const providerRegistry = {
  contract_mock: contractMockProvider,
  orchestrator_mock: orchestratorMockProvider,
  placeholder_live: realSystemPlaceholderProvider,
  real_read_protected: realOrchestratorProtectedProvider,
};
