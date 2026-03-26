import { runtimeSnapshots } from '../../data/mock-data.js';
import { RuntimeProvider } from './providerInterfaces.js';

export class RealSystemPlaceholderProvider extends RuntimeProvider {
  getRuntimeSnapshot() { return structuredClone(runtimeSnapshots.placeholder_live); }
}
