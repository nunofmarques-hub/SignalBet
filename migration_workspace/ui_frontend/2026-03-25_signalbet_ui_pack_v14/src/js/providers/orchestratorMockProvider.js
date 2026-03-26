
import { MOCK_ORCHESTRATOR_SNAPSHOT } from '../../data/mock-data.js';
import { SnapshotProvider } from './providerInterfaces.js';
export class OrchestratorMockProvider extends SnapshotProvider {
  async getOrchestratorSnapshot() { return structuredClone(MOCK_ORCHESTRATOR_SNAPSHOT); }
}
