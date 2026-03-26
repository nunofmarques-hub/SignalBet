
import { poolTable } from '../components/tables.js';
export function renderPool(vm){
  return `<div class="grid"><div class="panel"><h3>Opportunity Pool</h3><div class="small">Ranking global de oportunidades</div></div>${poolTable(vm.rows)}</div>`;
}
