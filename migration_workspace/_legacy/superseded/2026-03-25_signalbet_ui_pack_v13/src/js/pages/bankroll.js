import { shell } from '../components/layout.js';
import { kpiTile, chip } from '../components/ui.js';

export function renderBankroll(vm, route, sourceMode) {
  const approved = vm.system.pool.filter(i=>i.decision_status==='approved');
  const body = `
    <div class="grid-4">
      ${kpiTile('Approved Today', approved.length)}
      ${kpiTile('Reduced', vm.system.pool.filter(i=>i.decision_status==='reduced').length)}
      ${kpiTile('Reserve', vm.system.pool.filter(i=>i.decision_status==='reserve').length)}
      ${kpiTile('Remaining Capacity', '62%')}
    </div>
    <div class="card"><div class="section-title"><h3>Decision Queue</h3><small class="muted">Approved / reduced / reserve</small></div><div class="list">${vm.system.pool.map(i=>`<div class="list-item row"><div><strong>${i.fixture}</strong><div class="muted">${i.market} · ${i.module_source}</div></div><div>${chip(i.decision_status, i.decision_status==='approved'?'green':'amber')}</div></div>`).join('')}</div></div>`;
  return shell('Banca / Decision View', 'Decisão operacional e gestão de exposição', body, route, sourceMode);
}
