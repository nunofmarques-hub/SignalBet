
import { normalizeOrchestratorSnapshot } from '../adapters/orchestratorAdapters.js';
export class PipelineStatusService {
  constructor(providerRegistry, store) { this.providerRegistry = providerRegistry; this.store = store; }
  async getSnapshot(mode = 'orchestrator_mock') {
    const registry = this.providerRegistry[mode] ?? this.providerRegistry.orchestrator_mock;
    const raw = await registry.orchestrator.getOrchestratorSnapshot();
    const snapshot = normalizeOrchestratorSnapshot(raw, mode);
    this.store.orchestratorSnapshot = snapshot;
    this.store.observedSourceMode = mode;
    return snapshot;
  }
}
