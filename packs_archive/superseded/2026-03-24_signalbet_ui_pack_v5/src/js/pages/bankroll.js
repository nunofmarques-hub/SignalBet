import { opportunities, summary } from '../../../data/mock-data.js';
import { chip, tile, table } from '../components.js';

export function renderBankroll() {
  return `
    <section class="kpi-grid">
      ${tile('Bankroll Base', summary.bankroll.bankroll)}
      ${tile('Available Exposure', summary.bankroll.available)}
      ${tile('Approved', summary.bankroll.approved)}
      ${tile('Reduced', summary.bankroll.reduced)}
      ${tile('Blocked', summary.bankroll.blocked)}
      ${tile('Reserve', summary.bankroll.reserve)}
    </section>
    <section class="split-2">
      <div class="panel">
        <h2 class="section-title">Decision Queue</h2>
        ${table(['Fixture','Decision','Stake','Exposure','Readiness'], opportunities.map((o, i) => `<tr><td>${o.fixture}</td><td>${chip(o.decision_status, o.decision_status==='approved'?'green':o.decision_status==='reduced'?'amber':o.decision_status==='blocked'?'red':'gray')}</td><td class="mono">${['1.00u','0.50u','0.75u','0.00u','0.00u'][i]}</td><td class="mono">${['12%','7%','10%','0%','0%'][i]}</td><td>${chip(o.decision_status==='approved'?'ready':'review', o.decision_status==='approved'?'green':'amber')}</td></tr>`))}
      </div>
      <div class="panel">
        <h2 class="section-title">Exposure & Alerts</h2>
        <div class="list">
          <div class="list-item"><strong>Allocated:</strong> ${summary.bankroll.allocated}</div>
          <div class="list-item"><strong>Remaining capacity:</strong> ${summary.bankroll.remaining}</div>
          <div class="list-item"><strong>Conflict:</strong> 1 correlação em observação</div>
          <div class="list-item"><strong>Trigger:</strong> reserve picks aguardam janela melhor</div>
        </div>
      </div>
    </section>`;
}
