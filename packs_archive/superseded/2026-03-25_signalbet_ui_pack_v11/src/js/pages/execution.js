import { simpleTable } from '../components/tables.js';
export function renderExecution(vm){ return `<div class="screen-section"><h3 class="section-title">Execution / Tracking</h3><div class="chip warn">current_stage=${vm.currentStage}</div>${simpleTable(['Fixture','Execution','State'], vm.rows)}</div>`; }
