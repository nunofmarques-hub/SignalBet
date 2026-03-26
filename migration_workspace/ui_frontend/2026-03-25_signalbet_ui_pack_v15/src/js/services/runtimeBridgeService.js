import { providerRegistry } from '../providers/providerRegistry.js';
import { adaptContract } from '../adapters/contractAdapters.js';
import { adaptOrchestratorSnapshot } from '../adapters/orchestratorAdapters.js';

export async function readRuntime(modeRequested='orchestrator_mock'){
  let provider = providerRegistry[modeRequested] || providerRegistry.orchestrator_mock;
  let sourceObserved = provider.mode;
  let fallbackUsed = false;
  try {
    const raw = await provider.read();
    if (provider.mode === 'contract_mock') return adaptContract(raw);
    return adaptOrchestratorSnapshot(raw, sourceObserved, false);
  } catch (err) {
    if (modeRequested !== 'orchestrator_mock') {
      fallbackUsed = true;
      const fallback = await providerRegistry.orchestrator_mock.read();
      return adaptOrchestratorSnapshot(fallback, 'orchestrator_mock', fallbackUsed);
    }
    throw err;
  }
}
