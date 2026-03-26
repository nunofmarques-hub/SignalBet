import * as contractMockProvider from './contractMockProvider.js';
import * as orchestratorMockProvider from './orchestratorMockProvider.js';
import * as realSystemPlaceholderProvider from './realSystemPlaceholderProvider.js';

export const providerRegistry = {
  contract_mock: { contract: contractMockProvider, runtime: orchestratorMockProvider },
  orchestrator_mock: { contract: contractMockProvider, runtime: orchestratorMockProvider },
  placeholder_live: { contract: contractMockProvider, runtime: realSystemPlaceholderProvider }
};
