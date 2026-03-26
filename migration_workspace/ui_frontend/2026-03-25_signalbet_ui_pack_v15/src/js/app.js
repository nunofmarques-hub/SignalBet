import { store } from './core/store.js';
import { getUiRuntime } from './services/uiDataService.js';
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

const routes = {
  home: { label:'Home', render: (vm)=>renderHome(buildHomeViewModel(vm)) },
  pool: { label:'Opportunity Pool', render: (vm)=>renderPool(buildPoolViewModel(vm)) },
  bankroll: { label:'Banca', render: (vm)=>renderBankroll(buildBankrollViewModel(vm)) },
  execution: { label:'Execution', render: (vm)=>renderExecution(buildExecutionViewModel(vm)) },
  history: { label:'Histórico', render: (vm)=>renderHistory(buildHistoryViewModel(vm)) },
};

function renderNav(){
  const nav = document.getElementById('nav');
  nav.innerHTML = Object.entries(routes).map(([key,route]) => `<a href="#${key}" data-route="${key}" class="${store.state.page===key?'active':''}">${route.label}</a>`).join('')+
  `<div class="card" style="margin-top:16px"><div class="small muted">Source mode</div><select id="sourceMode" style="width:100%;margin-top:8px;background:#111827;color:#F5F7FA;padding:10px;border-radius:12px;border:1px solid rgba(255,255,255,.08)"><option value="orchestrator_mock">orchestrator_mock</option><option value="real_read_protected">real_read_protected</option><option value="placeholder_live">placeholder_live</option><option value="contract_mock">contract_mock</option></select></div>`;
  nav.querySelectorAll('a').forEach(a => a.onclick = (e)=>{ e.preventDefault(); store.set({ page: a.dataset.route }); });
  const sel = document.getElementById('sourceMode'); sel.value = store.state.sourceModeRequested; sel.onchange = ()=> store.set({ sourceModeRequested: sel.value });
}

async function render(){
  renderNav();
  const payload = await getUiRuntime(store.state.sourceModeRequested);
  document.getElementById('page').innerHTML = routes[store.state.page].render(payload);
}
store.subscribe(render);
render();
