import { sidebar, topbar, orchestratorDrawer } from './components/layout.js';
import { getAppContext, getOrchestratorRunModel } from './services/uiDataService.js';
import { getPageState, setPageState, getOrchestratorStatus, cycleOrchestratorStatus, setSelected } from './core/store.js';
import { renderHome } from './pages/home.js';
import { renderPool } from './pages/pool.js';
import { renderBankroll } from './pages/bankroll.js';
import { renderExecution } from './pages/execution.js';
import { renderHistory } from './pages/history.js';

const sidebarEl = document.getElementById('sidebar');
const topbarEl = document.getElementById('topbar');
const contentEl = document.getElementById('content');
const drawerEl = document.getElementById('orchestratorDrawer');

const routes = {
  home: { title: 'Home / Dashboard', render: s => renderHome(s) },
  pool: { title: 'Opportunity Pool', render: s => renderPool(s) },
  bankroll: { title: 'Banca / Decision View', render: s => renderBankroll(s) },
  execution: { title: 'Execution / Tracking', render: s => renderExecution(s) },
  history: { title: 'Histórico / Validação', render: s => renderHistory(s) }
};

function currentPage(){ return location.hash.replace('#/','') || 'home'; }

function render(){
  const app = getAppContext();
  const page = currentPage();
  const route = routes[page] || routes.home;
  const state = getPageState(page);
  const run = getOrchestratorRunModel(getOrchestratorStatus());
  sidebarEl.innerHTML = sidebar(page, app);
  topbarEl.innerHTML = topbar(route.title, state);
  contentEl.innerHTML = route.render(state);
  drawerEl.innerHTML = orchestratorDrawer(run);
  bind();
}

function bind(){
  sidebarEl.querySelectorAll('[data-page]').forEach(el => el.addEventListener('click', () => { location.hash = `/${el.dataset.page}`; }));
  topbarEl.querySelectorAll('[data-state]').forEach(btn => btn.addEventListener('click', () => { const page = currentPage(); setPageState(page, btn.dataset.state); render(); }));
  contentEl.querySelectorAll('.state-reload').forEach(btn => btn.addEventListener('click', () => { const page = currentPage(); setPageState(page, 'success'); render(); }));
  contentEl.querySelectorAll('[data-select-row]').forEach(row => row.addEventListener('click', () => { setSelected(row.dataset.selectRow, Number(row.dataset.index)); render(); }));
  const open = document.getElementById('openOrchestrator'); if (open) open.addEventListener('click', () => drawerEl.classList.add('open'));
  const close = document.getElementById('closeOrchestrator'); if (close) close.addEventListener('click', () => drawerEl.classList.remove('open'));
  const cycle = document.getElementById('cycleRunState'); if (cycle) cycle.addEventListener('click', () => { cycleOrchestratorStatus(); render(); });
}

window.addEventListener('hashchange', render);
render();
