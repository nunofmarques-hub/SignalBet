import { poolData } from '../../data/mock-data.js';
import { detailKV, kpiTile, scoreBadge, statusChip } from '../components/ui.js';
import { withPageState } from './helpers.js';

export function renderPool(state) {
  return withPageState(state, () => `
    <section class="kpi-grid">${poolData.summary.map(([a,b]) => kpiTile(a,b)).join('')}</section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Top opportunity</h3><span class="chip lime">GPS live ranking</span></div>
        <div class="hero" style="min-height:160px; padding:18px;">
          <div class="hero-title" style="font-size:28px;">${poolData.top.fixture}</div>
          <div class="small">${poolData.top.market} · ${poolData.top.module_source}</div>
          <div class="row" style="margin-top:12px;">
            ${scoreBadge('Score', poolData.top.global_score)}${scoreBadge('Confidence', poolData.top.confidence_norm)}${scoreBadge('Edge', poolData.top.edge_norm)}${scoreBadge('Risk', poolData.top.risk_norm, 'risk')}
          </div>
          <div class="row" style="margin-top:12px;">${statusChip(poolData.top.priority_tier)}${statusChip(poolData.top.eligibility)}${statusChip(poolData.top.decision_status)}${statusChip(poolData.top.execution_status)}${statusChip(poolData.top.data_quality_flag)}</div>
        </div>
      </div>
      <div class="section-card detail-panel">
        <div class="section-head"><h3 class="section-title">Inspector</h3></div>
        ${detailKV([
          ['Global score', poolData.top.global_score], ['Confidence', poolData.top.confidence_norm],
          ['Edge', poolData.top.edge_norm], ['Risk', poolData.top.risk_norm],
          ['Eligibility', poolData.top.eligibility], ['Decision', poolData.top.decision_status]
        ])}
        <div class="detail-box"><strong>Motivo da prioridade</strong><div class="small">A pick reúne score forte, confiança elevada e risco controlado, mantendo-se na shortlist principal do dia.</div></div>
      </div>
    </section>
    <section class="section-card">
      <div class="section-head"><h3 class="section-title">Filtros da pool</h3><div class="filters"><span class="filter-chip active">Todos</span><span class="filter-chip">Eligible</span><span class="filter-chip">Approved</span><span class="filter-chip">T1</span><span class="filter-chip">Amber quality</span></div></div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Fixture / Pick</th><th>Market</th><th>Module</th><th>Score</th><th>Confidence</th><th>Edge</th><th>Risk</th><th>Tier</th><th>Eligibility</th><th>Decision</th><th>Execution</th><th>Quality</th></tr></thead>
          <tbody>
            ${poolData.rows.map(r => `<tr><td><strong>${r[0]}</strong></td><td>${r[1]}</td><td>${r[2]}</td><td>${scoreBadge('', r[3]).replace('class="pill score"','class="pill score mono"')}</td><td>${r[4]}</td><td>${r[5]}</td><td>${r[6]}</td><td>${statusChip(r[7])}</td><td>${statusChip(r[8])}</td><td>${statusChip(r[9])}</td><td>${statusChip(r[10])}</td><td>${statusChip(r[11])}</td></tr>`).join('')}
          </tbody>
        </table>
      </div>
    </section>
  `);
}
