import { SnapshotProvider } from './providerInterfaces.js';
import { orchestratorSnapshot } from '../data/mock-data.js';
export class OrchestratorMockProvider extends SnapshotProvider {
  getSystemSnapshot(){ return null; }
  getPipelineSnapshot(){ return orchestratorSnapshot; }
}
