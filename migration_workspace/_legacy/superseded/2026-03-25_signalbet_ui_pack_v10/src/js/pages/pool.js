import { topbar } from '../components/layout.js';
import { kpi } from '../components/ui.js';
import { renderPoolTable } from '../components/tables.js';
export function renderPool(vm){
  return `${topbar('Opportunity Pool', `<span class="chip lime">Ranking global</span><button class="btn secondary">Mais filtros</button>`)}
  <div class="content">
    <div class="grid kpi">${kpi('Total Opportunities', vm.total)}${kpi('Eligible', vm.items.filter(i=>i.eligibility==='ELIGIBLE').length)}${kpi('Approved', vm.items.filter(i=>i.decision_status.includes('APPROVED')).length)}${kpi('Blocked', vm.items.filter(i=>i.decision_status==='BLOCKED').length)}${kpi('Avg Score', Math.round(vm.items.reduce((a,b)=>a+b.global_score,0)/vm.items.length))}${kpi('Top Tier', vm.items.filter(i=>i.priority_tier==='T1').length)}</div>
    <div class="card"><h3>Ranking Table</h3>${renderPoolTable(vm.items)}</div>
  </div>`;
}
