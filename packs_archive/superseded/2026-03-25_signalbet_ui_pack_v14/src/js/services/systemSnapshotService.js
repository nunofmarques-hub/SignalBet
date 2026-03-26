
import { normalizeSystemSnapshot } from '../adapters/contractAdapters.js';
export class SystemSnapshotService {
  constructor(providerRegistry, store) { this.providerRegistry = providerRegistry; this.store = store; }
  async getSnapshot(mode = 'contract_mock') {
    const registry = this.providerRegistry[mode] ?? this.providerRegistry.contract_mock;
    const raw = await registry.system.getSystemSnapshot();
    const snapshot = normalizeSystemSnapshot(raw);
    this.store.systemSnapshot = snapshot;
    return snapshot;
  }
}
