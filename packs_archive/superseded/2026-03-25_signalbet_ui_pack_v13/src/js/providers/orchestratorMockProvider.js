import { orchestratorMockSnapshot } from '../../data/mock-data.js';
export async function getRuntimeSnapshot() {
  return JSON.parse(JSON.stringify(orchestratorMockSnapshot));
}
