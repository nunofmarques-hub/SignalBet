import { homeData } from '../../data/mock-data.js';
import { alertItem, kpiTile, scoreBadge, statusChip } from '../components/ui.js';
import { withPageState } from './helpers.js';

export function renderHome(state) {
  return withPageState(state, () => `
    <section class="hero">
      <div class="tile-label">${homeData.hero.title}</div>
      <div class="hero-title">${homeData.hero.fixture}</div>
      <div class="row">
        ${statusChip(homeData.hero.priority_tier)}
        ${statusChip(homeData.hero.decision_status)}
        ${scoreBadge('Score', homeData.hero.global_score)}
        ${scoreBadge('Confidence', homeData.hero.confidence_norm)}
        ${scoreBadge('Edge', homeData.hero.edge_norm)}
        ${scoreBadge('Risk', homeData.hero.risk_norm, 'risk')}
      </div>
      <p class="hero-subtitle">${homeData.hero.market} · Origem ${homeData.hero.module_source}. ${homeData.hero.summary}</p>
      <div class="hero-actions"><button class="btn">Abrir pick</button><button class="btn secondary">Ver na Pool</button></div>
    </section>

    <section class="kpi-grid">${homeData.kpis.map(([a,b,c]) => kpiTile(a,b,c)).join('')}</section>

    <section class="stack-3">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Opportunity highlights</h3><span class="small">Top picks do dia</span></div>
        <div class="list">
          ${homeData.highlights.map(h => `<div class="list-item"><div class="row" style="justify-content:space-between;"><strong>${h.fixture}</strong>${statusChip(h.decision)}</div><div class="small">${h.market}</div><div class="row" style="margin-top:10px;">${scoreBadge('Score', h.score)}${scoreBadge('Conf', h.confidence)}${scoreBadge('Edge', h.edge)}</div></div>`).join('')}
        </div>
      </div>
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Módulos ativos</h3></div>
        <div class="list">
          ${homeData.modules.map(m => `<div class="list-item"><div class="row" style="justify-content:space-between;"><strong>${m.name}</strong>${statusChip(m.health)}</div><div class="small">${m.picks} picks hoje</div></div>`).join('')}
        </div>
      </div>
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Alertas</h3></div>
        <div class="alert-list">${homeData.alerts.map(alertItem).join('')}</div>
      </div>
    </section>
  `);
}
