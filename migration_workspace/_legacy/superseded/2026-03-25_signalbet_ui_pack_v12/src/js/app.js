import { store } from './core/store.js';
import { bootstrapUiData } from './services/uiDataService.js';
import { shell } from './components/layout.js';
import { renderHome } from './pages/home.js';
import { renderPool } from './pages/pool.js';
import { renderBankroll } from './pages/bankroll.js';
import { renderExecution } from './pages/execution.js';
import { renderHistory } from './pages/history.js';

const app = document.getElementById('app');

function getRoute() {
  const hash = window.location.hash.replace('#', '');
  return hash || 'home';
}

function render() {
  store.setRoute(getRoute());
  const bridge = bootstrapUiData(store.providerMode);
  const views = {
    home: renderHome,
    pool: renderPool,
    bankroll: renderBankroll,
    execution: renderExecution,
    history: renderHistory,
  };
  const content = views[store.route](bridge);
  app.innerHTML = shell({ active: store.route, content, providerMode: store.providerMode });
  const issuesPanel = document.getElementById('issues-panel');
  if (issuesPanel && bridge.snapshot.issues?.length) {
    issuesPanel.innerHTML += `<ul class="list">${bridge.snapshot.issues.map(i => `<li><span class="chip ${i.severity}">${i.severity}</span> ${i.message}</li>`).join('')}</ul>`;
  }
}

window.addEventListener('hashchange', render);
render();
