import { executionItems, summary } from '../../../data/mock-data.js';
import { chip, tile, table, stateBlock } from '../components.js';

export function renderExecution(state='normal') {
  if (state==='loading') return stateBlock('Loading execution…','A preparar queue, tracking e settlement.');
  if (state==='error') return stateBlock('Erro de sincronização','Não foi possível carregar o estado da execution.', 'Tentar novamente');
  return `
    <section class="kpi-grid">
      ${tile('Pending Intake', summary.execution.pendingIntake)}
      ${tile('Placed', summary.execution.placed)}
      ${tile('Live', summary.execution.live)}
      ${tile('Settled Today', summary.execution.settled)}
      ${tile('Issues', summary.execution.issues)}
      ${tile('Avg Delay', summary.execution.delay)}
    </section>
    <div class="filters">
      <span class="filter-chip active">Pending</span>
      <span class="filter-chip">Placed</span>
      <span class="filter-chip">Live</span>
      <span class="filter-chip">Settled</span>
      <span class="filter-chip">Issues</span>
    </div>
    ${table(['Fixture','Market','Decision','Execution','Intake','Created','Queue Age'], executionItems.map(e => `<tr><td>${e.fixture}</td><td>${e.market}</td><td>${chip(e.decision_status, e.decision_status==='approved'?'green':'amber')}</td><td>${chip(e.execution_status, e.execution_status==='placed'?'green':e.execution_status==='live'?'lime':'amber')}</td><td>${chip(e.intake_status, e.intake_status==='ok'?'green':'amber')}</td><td>${e.created_at}</td><td>${e.queue_age}</td></tr>`))}`;
}
