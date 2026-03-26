import { topbar } from '../components/layout.js';
import { kpi } from '../components/ui.js';
import { renderSimpleTable } from '../components/tables.js';
export function renderBankroll(vm){
  return `${topbar('Banca / Decision View', `<span class="chip amber">Disciplina operacional</span>`)}
  <div class="content">
    <div class="grid kpi">${kpi('Approved', vm.counts.approved)}${kpi('Reduced', vm.counts.reduced)}${kpi('Blocked', vm.counts.blocked)}${kpi('Available Exposure', '3.5u')}${kpi('Allocated Stake', '1.5u')}${kpi('Remaining Capacity', '2.0u')}</div>
    <div class="card"><h3>Decision Queue</h3>${renderSimpleTable(vm.items,[{key:'fixture',label:'Fixture'},{key:'decision_status',label:'Decision'},{key:'stake',label:'Stake'},{key:'exposure_impact',label:'Exposure'},{key:'reason',label:'Rationale'},{key:'execution_readiness',label:'Readiness'}])}</div>
  </div>`;
}
