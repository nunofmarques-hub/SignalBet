
import { ContractMockProvider } from './contractMockProvider.js';
import { OrchestratorMockProvider } from './orchestratorMockProvider.js';
import { RealSystemPlaceholderProvider } from './realSystemPlaceholderProvider.js';
import { RealOrchestratorProtectedProvider } from './realOrchestratorProtectedProvider.js';
export function buildProviderRegistry(runtimeBridgeService){
  return {
    contract_mock: { system: new ContractMockProvider(), orchestrator: new OrchestratorMockProvider() },
    orchestrator_mock: { system: new ContractMockProvider(), orchestrator: new OrchestratorMockProvider() },
    placeholder_live: { system: new ContractMockProvider(), orchestrator: new RealSystemPlaceholderProvider() },
    real_read_protected: { system: new ContractMockProvider(), orchestrator: new RealOrchestratorProtectedProvider(runtimeBridgeService) }
  };
}
