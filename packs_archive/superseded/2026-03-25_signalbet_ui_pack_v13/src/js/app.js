import { store } from './core/store.js';
import { bootstrapUiData } from './services/uiDataService.js';
import { buildHomeViewModel } from './viewmodels/homeViewModel.js';
import { buildPoolViewModel } from './viewmodels/poolViewModel.js';
import { buildBankrollViewModel } from './viewmodels/bankrollViewModel.js';
import { buildExecutionViewModel } from './viewmodels/executionViewModel.js';
import { buildHistoryViewModel } from './viewmodels/historyViewModel.js';
import { renderHome } from './pages/home.js';
import { renderPool } from './pages/pool.js';
import { renderBankroll } from './pages/bankroll.js';
import { renderExecution } from './pages/execution.js';
import { renderHistory } from './pages/history.js';

const app = document.getElementById('app');

async function render() {
  const route = (location.hash || '#home').replace('#','');
  const bundle = await bootstrapUiData(store.sourceMode);
  const map = {
    home: () => renderHome(buildHomeViewModel(bundle), 'home', store.sourceMode),
    pool: () => renderPool(buildPoolViewModel(bundle), 'pool', store.sourceMode),
    bankroll: () => renderBankroll(buildBankrollViewModel(bundle), 'bankroll', store.sourceMode),
    execution: () => renderExecution(buildExecutionViewModel(bundle), 'execution', store.sourceMode),
    history: () => renderHistory(buildHistoryViewModel(bundle), 'history', store.sourceMode)
  };
  app.innerHTML = (map[route] || map.home)();
  const select = document.getElementById('sourceModeSelect');
  if (select) {
    select.value = store.sourceMode;
    select.addEventListener('change', (e)=> { store.sourceMode = e.target.value; render(); });
  }
  document.getElementById('reloadBtn')?.addEventListener('click', render);
  document.querySelectorAll('[data-route]').forEach(a => a.addEventListener('click', (e) => {
    e.preventDefault(); location.hash = a.dataset.route;
  }));
}
window.addEventListener('hashchange', render);
render();
