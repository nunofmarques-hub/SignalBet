import { shell } from '../components/layout.js';
import { kpiTile } from '../components/ui.js';
import { heroOpportunityCard, orchestratorPanel } from '../components/cards.js';

export function renderHome(vm, route, sourceMode) {
  const body = `
    <div class="grid-2">
      <div class="stack">
        ${heroOpportunityCard(vm.system.topOpportunity)}
        <div class="grid-4">
          ${kpiTile('Opportunities Today', vm.system.kpis.opportunities_today)}
          ${kpiTile('Eligible', vm.system.kpis.eligible)}
          ${kpiTile('Approved', vm.system.kpis.approved)}
          ${kpiTile('Pending Execution', vm.system.kpis.pending_execution)}
        </div>
      </div>
      ${orchestratorPanel(vm.runtime, vm.bridge)}
    </div>`;
  return shell('Home / Dashboard', 'Cockpit principal do sistema', body, route, sourceMode);
}
