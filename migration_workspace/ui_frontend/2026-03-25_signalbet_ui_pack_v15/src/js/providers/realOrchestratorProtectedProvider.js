import { createProvider } from './providerInterfaces.js';
import { realProtectedSnapshotExample } from '../data/mock-data.js';
export const realOrchestratorProtectedProvider = createProvider('realOrchestratorProtectedProvider', 'real_read_protected', async () => {
  // Simula leitura externa controlada já preparada para futura substituição por fonte real.
  return realProtectedSnapshotExample;
});
