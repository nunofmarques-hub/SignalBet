import { opportunities, summary } from '../../../data/mock-data.js';
import { chip, score, tile, table } from '../components.js';

export function renderHome() {
  const hero = opportunities[0];
  return `
    <section class="panel hero">
      ${chip('Best of the Day','lime')}
      <div class="hero-title">${hero.fixture}</div>
      <div class="small">${hero.market} · módulo ${hero.module_source} · odd ${hero.odd}</div>
      <div class="row" style="margin-top:16px">${score('Global', hero.global_score)} ${score('Confidence', hero.confidence_norm)} ${score('Edge', hero.edge_norm)} ${score('Risk', hero.risk_norm)}</div>
      <div class="button-row"><button class="btn">Abrir pick</button><button class="btn secondary">Ver na pool</button></div>
    </section>
    <section class="kpi-grid">
      ${tile('Opportunities Today', summary.home.opportunities)}
      ${tile('Eligible', summary.home.eligible)}
      ${tile('Approved', summary.home.approved)}
      ${tile('Pending Execution', summary.home.pending)}
      ${tile('Live', summary.home.live)}
      ${tile('Alerts', summary.home.alerts)}
    </section>
    <section class="card-grid">
      <div class="panel">
        <h2 class="section-title">Opportunity Highlights</h2>
        ${table(['Fixture','Market','Score','Decision'], opportunities.slice(0,4).map(o => `<tr><td>${o.fixture}</td><td>${o.market}</td><td class="mono">${o.global_score}</td><td>${chip(o.decision_status, o.decision_status==='approved'?'green':o.decision_status==='reduced'?'amber':o.decision_status==='blocked'?'red':'gray')}</td></tr>`))}
      </div>
      <div class="panel">
        <h2 class="section-title">System Snapshot</h2>
        <div class="list">
          <div class="list-item"><strong>Banca:</strong> 6 approved, 2 reduced, 4 blocked</div>
          <div class="list-item"><strong>Execution:</strong> 2 pending intake, 4 live</div>
          <div class="list-item"><strong>Quality:</strong> 1 alert ativo na pool</div>
          <div class="list-item"><strong>Módulos:</strong> v12 em foco, BTTS watchlist</div>
        </div>
      </div>
    </section>`;
}
