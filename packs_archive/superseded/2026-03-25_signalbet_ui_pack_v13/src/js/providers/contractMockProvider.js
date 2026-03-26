import { contractSnapshot } from '../../data/mock-data.js';
export async function getContractSnapshot() {
  return JSON.parse(JSON.stringify(contractSnapshot));
}
