
import { SnapshotProvider } from './providerInterfaces.js';
export class RealOrchestratorProtectedProvider extends SnapshotProvider {
  constructor(runtimeBridgeService) { super(); this.runtimeBridgeService = runtimeBridgeService; }
  async getOrchestratorSnapshot() {
    const snapshot = this.runtimeBridgeService.getImportedRealSnapshot();
    if (!snapshot) throw new Error('No imported real snapshot available.');
    return snapshot;
  }
}
