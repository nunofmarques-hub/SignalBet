import { executionData } from '../../data/mock-data.js';
import { alertItem, detailKV, kpiTile, statusChip } from '../components/ui.js';
import { withPageState } from './helpers.js';

export function renderExecution(state) {
  return withPageState(state, () => `
    <section class="kpi-grid">${executionData.summary.map(([a,b]) => kpiTile(a,b)).join('')}</section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Intake / queue</h3><span class="chip amber">estado operacional</span></div>
        <div class="table-wrap"><table><thead><tr><th>Pick</th><th>Module</th><th>Decision</th><th>Stake</th><th>Readiness</th><th>Intake</th><th>Created</th><th>Queue age</th></tr></thead><tbody>${executionData.intake.map(r=>`<tr><td><strong>${r[0]}</strong></td><td>${r[1]}</td><td>${statusChip(r[2])}</td><td>${r[3]}</td><td>${statusChip(r[4])}</td><td>${statusChip(r[5])}</td><td>${r[6]}</td><td>${r[7]}</td></tr>`).join('')}</tbody></table></div>
      </div>
      <div class="section-card detail-panel">
        <div class="section-head"><h3 class="section-title">Audit panel</h3></div>
        ${detailKV([
          ['Selected pick', executionData.intake[0][0]], ['Decision', executionData.intake[0][2]], ['Intake', executionData.intake[0][5]], ['Queue age', executionData.intake[0][7]], ['Placed', 'no'], ['Settled', 'no']
        ])}
        <div class="detail-box"><strong>Trail resumido</strong><div class="small">Received from bankroll → queued for intake → awaiting placement → not yet settled.</div></div>
      </div>
    </section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Open / live tracking</h3></div>
        <div class="table-wrap"><table><thead><tr><th>Pick</th><th>Market</th><th>Placed</th><th>Status</th><th>Live</th><th>Stake</th><th>Return</th><th>Flag</th></tr></thead><tbody>${executionData.live.map(r=>`<tr><td><strong>${r[0]}</strong></td><td>${r[1]}</td><td>${r[2]}</td><td>${statusChip(r[3])}</td><td>${statusChip(r[4])}</td><td>${r[5]}</td><td>${r[6]}</td><td>${statusChip(r[7])}</td></tr>`).join('')}</tbody></table></div>
      </div>
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Recent settlement</h3></div>
        <div class="list">${executionData.settled.map(r => `<div class="list-item"><div class="row" style="justify-content:space-between;"><strong>${r[0]}</strong>${statusChip(r[1])}</div><div class="small">${r[2]} · ${r[3]}</div></div>`).join('')}</div>
      </div>
    </section>
    <section class="section-card"><div class="section-head"><h3 class="section-title">Alertas operacionais</h3></div><div class="alert-list">${executionData.alerts.map(alertItem).join('')}</div></section>
  `);
}
