import { topbar } from '../components/layout.js';
import { kpi } from '../components/ui.js';
import { runtimeStatePanel } from '../components/stateView.js';
import { summarizeSnapshot } from '../services/systemSnapshotService.js';
import { pipelineReadiness } from '../services/pipelineStatusService.js';
export function renderHome(vm){
  const s = summarizeSnapshot(vm.runtime); const p = pipelineReadiness(vm.runtime);
  return `${topbar('Home / Dashboard','Camada visual principal da app')}
  <div class="grid two">
    ${runtimeStatePanel(vm)}
    <div class="card"><div class="section-head"><strong>Bridge scope</strong></div><div class="panel-list"><div class="state-box"><strong>Real:</strong> snapshot protegido parcial</div><div class="state-box"><strong>Mock:</strong> contract_mock e orchestrator_mock</div><div class="state-box"><strong>Limite:</strong> sem live contínua</div></div></div>
  </div>
  <div class="grid kpis">${kpi('Opportunities',s.opportunities)}${kpi('Eligible',s.eligible)}${kpi('Approved',s.approved)}${kpi('Pipeline ready',`${Math.round(p.ratio*100)}%`)}</div>`;
}
