import { simpleTable } from '../components/tables.js';
export function renderHistory(vm){ return `<div class="screen-section"><h3 class="section-title">Histórico / Validação</h3><div class="chip">final_result=${vm.finalResult}</div>${simpleTable(['Data','Fixture','Result','Return'], vm.rows)}</div>`; }
