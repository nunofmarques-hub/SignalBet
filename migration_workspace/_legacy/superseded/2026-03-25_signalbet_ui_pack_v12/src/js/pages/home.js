import { buildHomeViewModel } from '../viewmodels/homeViewModel.js';
import { orchestratorPanel } from '../components/cards.js';
import { issuesList } from '../components/stateView.js';

export function renderHome(bridge) {
  const vm = buildHomeViewModel(bridge);
  return `
    <div class="topbar"><div><h1 style="margin:0">${vm.title}</h1><div class="muted">Camada visual principal da app</div></div><button class="button" ${vm.cta.disabled ? 'disabled' : ''}>${vm.cta.ctaLabel}</button></div>
    ${orchestratorPanel(vm)}
    <script>document.getElementById('issues-panel').innerHTML += ${JSON.stringify(issuesList(vm.issues))};</script>
  `;
}
