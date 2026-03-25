import { sidebar, topbar } from './components.js';
import { renderHome } from './pages/home.js';
import { renderPool } from './pages/pool.js';
import { renderBankroll } from './pages/bankroll.js';
import { renderExecution } from './pages/execution.js';
import { renderHistory } from './pages/history.js';

const sidebarEl = document.getElementById('sidebar');
const topbarEl = document.getElementById('topbar');
const contentEl = document.getElementById('content');

const routes = {
  home: { title: 'Home / Dashboard', render: () => renderHome() },
  pool: { title: 'Opportunity Pool', render: () => renderPool() },
  bankroll: { title: 'Banca / Decision View', render: () => renderBankroll() },
  execution: { title: 'Execution / Tracking', render: () => renderExecution('normal') },
  history: { title: 'Histórico / Validação', render: () => renderHistory('normal') }
};

function setPage(page) {
  const route = routes[page] || routes.home;
  sidebarEl.innerHTML = sidebar(page);
  topbarEl.innerHTML = topbar(route.title);
  contentEl.innerHTML = route.render();
  sidebarEl.querySelectorAll('[data-page]').forEach(el => {
    el.addEventListener('click', () => setPage(el.dataset.page));
  });
}

setPage('home');
