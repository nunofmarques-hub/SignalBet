import { runtimeSnapshots } from '../../data/mock-data.js';
import { RuntimeProvider } from './providerInterfaces.js';

export class OrchestratorMockProvider extends RuntimeProvider {
  getRuntimeSnapshot() { return structuredClone(runtimeSnapshots.orchestrator_mock); }
}
