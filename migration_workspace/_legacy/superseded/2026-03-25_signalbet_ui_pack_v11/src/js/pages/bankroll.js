import { simpleTable } from '../components/tables.js';
export function renderBankroll(vm){ return `<div class="screen-section"><h3 class="section-title">Banca / Decision View</h3><div class="chip live">pipeline=${vm.pipelineState}</div>${simpleTable(['Fixture','Decision','Stake','Risk'], vm.rows)}</div>`; }
