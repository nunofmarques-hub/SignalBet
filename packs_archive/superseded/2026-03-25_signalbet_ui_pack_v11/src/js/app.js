import { uiDataService } from './services/uiDataService.js';
import { setHeader } from './components/layout.js';
import { renderRunPanel, renderBasicState } from './components/stateView.js';
import { homeViewModel } from './viewmodels/homeViewModel.js';
import { poolViewModel } from './viewmodels/poolViewModel.js';
import { bankrollViewModel } from './viewmodels/bankrollViewModel.js';
import { executionViewModel } from './viewmodels/executionViewModel.js';
import { historyViewModel } from './viewmodels/historyViewModel.js';
import { renderHome } from './pages/home.js';
import { renderPool } from './pages/pool.js';
import { renderBankroll } from './pages/bankroll.js';
import { renderExecution } from './pages/execution.js';
import { renderHistory } from './pages/history.js';
const pipeline = uiDataService.bootstrap();
document.getElementById('run-panel').innerHTML = renderRunPanel(pipeline);
const renderers = {
  home: () => renderHome(homeViewModel(uiDataService.getPage('home'), pipeline)),
  pool: () => renderPool(poolViewModel(uiDataService.getPage('pool'), pipeline)),
  bankroll: () => renderBankroll(bankrollViewModel(uiDataService.getPage('bankroll'), pipeline)),
  execution: () => renderExecution(executionViewModel(uiDataService.getPage('execution'), pipeline)),
  history: () => renderHistory(historyViewModel(uiDataService.getPage('history'), pipeline))
};
function go(page){
  setHeader(page === 'home' ? 'Home / Dashboard' : page === 'pool' ? 'Opportunity Pool' : page === 'bankroll' ? 'Banca / Decision View' : page === 'execution' ? 'Execution / Tracking' : 'Histórico / Validação', 'UI v11 pronta para snapshots e estados reais');
  document.getElementById('content').innerHTML = renderers[page] ? renderers[page]() : renderBasicState('error','Página não encontrada');
}
document.querySelectorAll('[data-page]').forEach(btn => btn.addEventListener('click', () => go(btn.dataset.page)));
go('home');
