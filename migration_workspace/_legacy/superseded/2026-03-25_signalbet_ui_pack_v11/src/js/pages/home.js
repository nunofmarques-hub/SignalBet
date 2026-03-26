import { kpiTile } from '../components/ui.js';
import { heroCard } from '../components/cards.js';
export function renderHome(vm){
  return `<div class="hero">${heroCard(vm.hero)}<div class="screen-section"><h3 class="section-title">Readiness e Fontes</h3><div class="muted">Estado visual oficial do sistema antes da corrida.</div><div class="grid" style="margin-top:12px">${vm.pipeline.moduleOverview.map(m=>`<div><strong>${m.module}</strong><div class="small muted">${m.status} · ${m.picks} picks</div></div>`).join('')}</div></div></div><div class="grid kpis">${vm.kpis.map(([l,v])=>kpiTile(l,v)).join('')}</div>`;
}
