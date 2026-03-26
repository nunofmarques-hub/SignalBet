import { shell } from '../components/layout.js';
import { kpiTile } from '../components/ui.js';
import { poolTable } from '../components/tables.js';

export function renderPool(vm, route, sourceMode) {
  const body = `
    <div class="grid-4">
      ${kpiTile('Total Opportunities', vm.system.pool.length)}
      ${kpiTile('Eligible', vm.system.kpis.eligible)}
      ${kpiTile('Approved', vm.system.kpis.approved)}
      ${kpiTile('Avg Global Score', Math.round(vm.system.pool.reduce((a,b)=>a+b.global_score,0)/vm.system.pool.length))}
    </div>
    <div class="card"><div class="section-title"><h3>Ranking Global</h3><small class="muted">Comparação central</small></div>${poolTable(vm.system.pool)}</div>`;
  return shell('Opportunity Pool', 'Ranking global de oportunidades', body, route, sourceMode);
}
