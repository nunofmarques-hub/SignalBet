import { contractMockProvider } from './contractMockProvider.js';
import { orchestratorMockProvider } from './orchestratorMockProvider.js';
import { realSystemPlaceholderProvider } from './realSystemPlaceholderProvider.js';
export const providerRegistry = {
  contract_mock: contractMockProvider,
  orchestrator_mock: orchestratorMockProvider,
  real_placeholder: realSystemPlaceholderProvider
};
