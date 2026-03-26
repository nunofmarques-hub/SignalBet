
import { SnapshotProvider } from './providerInterfaces.js';
export class RealSystemPlaceholderProvider extends SnapshotProvider {
  async getOrchestratorSnapshot() { throw new Error('Live orchestrator provider not connected yet.'); }
}
