import { topbar } from '../components/layout.js';
import { historyTable } from '../components/tables.js';
export function renderHistory(vm){
  return `${topbar('Histórico / Validação','Memória inteligente do sistema')}
  <div class="card">${historyTable(vm.runtime.history_rows || [])}</div>`;
}
