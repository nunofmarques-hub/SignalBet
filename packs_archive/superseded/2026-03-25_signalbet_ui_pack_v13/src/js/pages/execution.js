import { shell } from '../components/layout.js';
import { kpiTile, chip } from '../components/ui.js';

export function renderExecution(vm, route, sourceMode) {
  const body = `
    <div class="grid-4">
      ${kpiTile('Pending Intake', 2)}
      ${kpiTile('Placed', 1)}
      ${kpiTile('Live', vm.runtime.pipeline_state==='running' ? 1 : 0)}
      ${kpiTile('Issues', vm.runtime.issues.length)}
    </div>
    <div class="card"><div class="section-title"><h3>Pipeline Runtime</h3><small class="muted">Estado operacional</small></div>
      <div class="list">${vm.runtime.pipeline_steps.map(s=>`<div class="list-item row"><strong>${s.label}</strong>${chip(s.status, s.status==='ready'||s.status==='done'?'green':s.status==='running'?'cyan':'amber')}</div>`).join('')}</div>
    </div>`;
  return shell('Execution / Tracking', 'Fluxo operacional e rastreabilidade', body, route, sourceMode);
}
