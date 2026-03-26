import { topbar } from '../components/layout.js';
import { kpi } from '../components/ui.js';
import { renderSimpleTable } from '../components/tables.js';
export function renderExecution(vm){
  return `${topbar('Execution / Tracking', `<span class="chip cyan">Operational flow</span>`)}
  <div class="content">
    <div class="grid kpi">${kpi('Pending Intake', vm.pending)}${kpi('Live', vm.live)}${kpi('Settled', vm.settled)}${kpi('Placed', vm.items.filter(i=>i.intake_status==='PLACED').length)}${kpi('Issues', 0)}${kpi('Avg Queue Age', '1m')}</div>
    <div class="card"><h3>Execution Queue</h3>${renderSimpleTable(vm.items,[{key:'fixture',label:'Fixture'},{key:'execution_status',label:'Execution'},{key:'intake_status',label:'Intake'},{key:'queue_age',label:'Queue Age'}])}</div>
  </div>`;
}
