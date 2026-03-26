import { topbar } from '../components/layout.js';
import { poolTable } from '../components/tables.js';
import { poolCard } from '../components/cards.js';
export function renderPool(vm){
  const rows = vm.runtime.pool_rows || [];
  return `${topbar('Opportunity Pool','Ranking global de oportunidades')}
  <div class="grid cards">${rows.slice(0,3).map(poolCard).join('')}</div>
  <div class="card" style="margin-top:16px">${poolTable(rows)}</div>`;
}
