import { topbar } from '../components/layout.js';
import { kpi } from '../components/ui.js';
import { renderSimpleTable } from '../components/tables.js';
export function renderHistory(vm){
  return `${topbar('Histórico / Validação', `<span class="chip green">Memória inteligente</span>`)}
  <div class="content">
    <div class="grid kpi">${kpi('Total Picks', vm.items.length)}${kpi('Wins', vm.wins)}${kpi('Losses', vm.losses)}${kpi('Strike Rate', Math.round((vm.wins/Math.max(vm.items.length,1))*100)+'%')}${kpi('ROI', '-0.69u')}${kpi('Settled', vm.items.length)}</div>
    <div class="card"><h3>Historical Ledger</h3>${renderSimpleTable(vm.items,[{key:'date',label:'Date'},{key:'fixture',label:'Fixture'},{key:'market',label:'Market'},{key:'module_source',label:'Module'},{key:'decision_status',label:'Decision'},{key:'execution_status',label:'Execution'},{key:'result',label:'Result'},{key:'roi',label:'ROI'}])}</div>
  </div>`;
}
