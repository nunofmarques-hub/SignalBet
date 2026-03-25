import { opportunities, summary } from '../../../data/mock-data.js';
import { chip, score, tile, table } from '../components.js';

export function renderPool() {
  const top = opportunities[0];
  return `
    <section class="kpi-grid">
      ${tile('Total Opportunities', summary.pool.total)}
      ${tile('Eligible', summary.pool.eligible)}
      ${tile('Approved', summary.pool.approved)}
      ${tile('Reserve', summary.pool.reserve)}
      ${tile('Blocked', summary.pool.blocked)}
      ${tile('Avg Global Score', summary.pool.avgScore)}
    </section>
    <section class="split-2">
      <div class="panel hero">
        ${chip('Top Opportunity','lime')}
        <div class="hero-title">${top.fixture}</div>
        <div class="small">${top.market} · ${top.module_source}</div>
        <div class="row" style="margin-top:16px">${score('Global', top.global_score)} ${score('Confidence', top.confidence_norm)} ${score('Edge', top.edge_norm)} ${score('Risk', top.risk_norm)}</div>
      </div>
      <div class="panel">
        <h2 class="section-title">Inspector</h2>
        <div class="list">
          <div class="list-item"><strong>Eligibility:</strong> ${top.eligibility}</div>
          <div class="list-item"><strong>Decision:</strong> ${top.decision_status}</div>
          <div class="list-item"><strong>Execution:</strong> ${top.execution_status}</div>
          <div class="list-item"><strong>Rationale:</strong> ${top.rationale}</div>
        </div>
      </div>
    </section>
    <div class="filters">
      <span class="filter-chip active">Todos</span>
      <span class="filter-chip">v12</span>
      <span class="filter-chip">BTTS</span>
      <span class="filter-chip">Eligible</span>
      <span class="filter-chip">Approved</span>
      <span class="filter-chip">Mais filtros</span>
    </div>
    ${table(['Fixture','Market','Source','Global','Confidence','Edge','Risk','Tier','Eligibility','Decision','Execution','Quality'], opportunities.map(o => `<tr><td>${o.fixture}</td><td>${o.market}</td><td>${o.module_source}</td><td class="mono">${o.global_score}</td><td class="mono">${o.confidence_norm}</td><td class="mono">${o.edge_norm}</td><td class="mono">${o.risk_norm}</td><td>${chip(o.priority_tier,'gray')}</td><td>${chip(o.eligibility, o.eligibility==='eligible'?'green':o.eligibility==='watchlist'?'amber':'red')}</td><td>${chip(o.decision_status, o.decision_status==='approved'?'green':o.decision_status==='reduced'?'amber':o.decision_status==='blocked'?'red':'gray')}</td><td>${chip(o.execution_status, o.execution_status==='placed'?'green':o.execution_status==='live'?'lime':o.execution_status==='pending'?'amber':'gray')}</td><td>${chip(o.data_quality_flag, o.data_quality_flag==='green'?'green':'amber')}</td></tr>`))}`;
}
