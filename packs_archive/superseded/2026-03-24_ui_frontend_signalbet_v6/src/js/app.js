import { sidebar, topbar, orchestratorDrawer } from './components/layout.js';
import { getPageState, setPageState } from './components/state.js';
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

function currentPage() {
  return location.hash.replace('#/','') || 'home';
}

function render() {
  const page = currentPage();
  const route = routes[page] || routes.home;
  const state = getPageState(page);
  sidebarEl.innerHTML = sidebar(page);
  topbarEl.innerHTML = topbar(route.title, state, page);
  contentEl.innerHTML = route.render(state);
  drawerEl.innerHTML = orchestratorDrawer();
  bind();
}

function bind() {
  sidebarEl.querySelectorAll('[data-page]').forEach(el => {
    el.addEventListener('click', () => { location.hash = `/${el.dataset.page}`; });
  });
  const open = document.getElementById('openOrchestrator');
  if (open) open.addEventListener('click', () => drawerEl.classList.add('open'));
  const close = document.getElementById('closeOrchestrator');
  if (close) close.addEventListener('click', () => drawerEl.classList.remove('open'));
  topbarEl.querySelectorAll('[data-state]').forEach(btn => {
    btn.addEventListener('click', () => {
      const page = currentPage();
      setPageState(page, btn.dataset.state);
      render();
    });
  });
  contentEl.querySelectorAll('.state-reload').forEach(btn => {
    btn.addEventListener('click', () => {
      const page = currentPage();
      setPageState(page, 'success');
      render();
    });
  });
}

window.addEventListener('hashchange', render);
render();
