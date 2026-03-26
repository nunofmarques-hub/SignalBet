import { ContractMockProvider } from './contractMockProvider.js';
import { OrchestratorMockProvider } from './orchestratorMockProvider.js';
import { RealSystemPlaceholderProvider } from './realSystemPlaceholderProvider.js';
const registry = {
  contract_mock: new ContractMockProvider(),
  orchestrator_mock: new OrchestratorMockProvider(),
  real_placeholder: new RealSystemPlaceholderProvider()
};
export function getProvider(name){ return registry[name]; }
export function getDefaultProvider(){ return registry.contract_mock; }
