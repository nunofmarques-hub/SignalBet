import { topbar } from '../components/layout.js';
import { kpi, badge } from '../components/ui.js';
export function renderBankroll(vm){
  const rows = vm.runtime.pool_rows || [];
  const approved = rows.filter(r=>r.decision_status==='approved').length;
  return `${topbar('Banca / Decision View','Decisão operacional e gestão de exposição')}
  <div class="grid kpis">${kpi('Approved',approved)}${kpi('Reserve',rows.filter(r=>r.decision_status==='reserve').length)}${kpi('Reduced',rows.filter(r=>r.decision_status==='reduced').length)}${kpi('Blocked',rows.filter(r=>r.decision_status==='blocked').length)}</div>
  <div class="card"><div class="section-head"><strong>Decision summary</strong>${badge(vm.runtime.final_result || 'n/a','cyan')}</div><div class="muted">A leitura usa o runtime já adaptado. Continuação de fallback limpa quando a fonte protegida não estiver disponível.</div></div>`;
}
