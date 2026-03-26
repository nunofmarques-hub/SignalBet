import { partialRuntimeSnapshot } from '../../data/mock-data.js';
export async function getRuntimeSnapshot() {
  return JSON.parse(JSON.stringify(partialRuntimeSnapshot));
}
