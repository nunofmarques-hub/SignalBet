import { rawContractData } from '../../data/mock-data.js';

export function getContractSnapshot(){
  return structuredClone ? structuredClone(rawContractData) : JSON.parse(JSON.stringify(rawContractData));
}
