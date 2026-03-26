import { topbar } from '../components/layout.js';
import { badge } from '../components/ui.js';
export function renderExecution(vm){
  const steps = vm.runtime.pipeline_steps || [];
  return `${topbar('Execution / Tracking','Fluxo operacional e rastreabilidade')}
  <div class="card"><div class="section-head"><strong>Pipeline steps</strong>${badge(vm.runtime.pipeline_state,'cyan')}</div><div class="panel-list">${steps.map(s=>`<div class="state-box"><strong>${s.step}</strong> · ${s.status}</div>`).join('')}</div></div>`;
}
