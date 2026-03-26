
import { getHomeModel } from '../services/uiDataService.js';
import { alertItem, kpiTile, scoreBadge, statusChip } from '../components/ui.js';
import { compactOpportunityCard, moduleCard } from '../components/cards.js';
import { withPageState } from '../components/stateView.js';

export function renderHome(state) {
  const homeData = getHomeModel();
  return withPageState(state, () => `
    <section class="hero">
      <div class="tile-label">Best of the Day</div>
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
        <div class="list">${homeData.highlights.map(compactOpportunityCard).join('')}</div>
      </div>
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Módulos ativos</h3></div>
        <div class="list">${homeData.modules.map(moduleCard).join('')}</div>
      </div>
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Alertas</h3></div>
        <div class="alert-list">${homeData.alerts.map(alertItem).join('')}</div>
      </div>
    </section>
  `);
}
