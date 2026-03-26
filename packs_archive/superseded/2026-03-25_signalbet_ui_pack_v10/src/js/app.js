import { bootstrapUI } from './services/uiDataService.js';
import { createHomeViewModel } from './viewmodels/homeViewModel.js';
import { createPoolViewModel } from './viewmodels/poolViewModel.js';
import { createBankrollViewModel } from './viewmodels/bankrollViewModel.js';
import { createExecutionViewModel } from './viewmodels/executionViewModel.js';
import { createHistoryViewModel } from './viewmodels/historyViewModel.js';
import { renderLayout } from './components/layout.js';
import { renderHome } from './pages/home.js';
import { renderPool } from './pages/pool.js';
import { renderBankroll } from './pages/bankroll.js';
import { renderExecution } from './pages/execution.js';
import { renderHistory } from './pages/history.js';

const root = document.getElementById('app');
const data = bootstrapUI();
function getRoute(){ return (location.hash || '#home').replace('#',''); }
function render(){
  const route = getRoute();
  let page='';
  if(route==='home') page = renderHome(createHomeViewModel(data));
  else if(route==='pool') page = renderPool(createPoolViewModel(data));
  else if(route==='bankroll') page = renderBankroll(createBankrollViewModel(data));
  else if(route==='execution') page = renderExecution(createExecutionViewModel(data));
  else if(route==='history') page = renderHistory(createHistoryViewModel(data));
  else page = renderHome(createHomeViewModel(data));
  root.innerHTML = renderLayout(route, page);
  const btn = document.getElementById('runBtn');
  if(btn){ btn.addEventListener('click', ()=> alert('UI only: ponto de entrada visual. A coordenação técnica pertence ao App Core / Orchestrator.')); }
}
window.addEventListener('hashchange', render);
render();
