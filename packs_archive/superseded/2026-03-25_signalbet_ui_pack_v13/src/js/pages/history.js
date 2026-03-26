import { shell } from '../components/layout.js';
import { kpiTile } from '../components/ui.js';
import { historyTable } from '../components/tables.js';

export function renderHistory(vm, route, sourceMode) {
  const wins = vm.system.history.filter(i=>i.result==='win').length;
  const body = `
    <div class="grid-4">
      ${kpiTile('Total Picks', vm.system.history.length)}
      ${kpiTile('Wins', wins)}
      ${kpiTile('Losses', vm.system.history.length - wins)}
      ${kpiTile('Strike Rate', Math.round((wins/vm.system.history.length)*100)+'%')}
    </div>
    <div class="card"><div class="section-title"><h3>Histórico / Validação</h3><small class="muted">Memória inteligente do sistema</small></div>${historyTable(vm.system.history)}</div>`;
  return shell('Histórico / Validação', 'Performance, memória e revisão', body, route, sourceMode);
}
