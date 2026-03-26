
import { store } from './core/store.js';
import { shellTemplate } from './components/layout.js';
import { RuntimeBridgeService } from './services/runtimeBridgeService.js';
import { buildProviderRegistry } from './providers/providerRegistry.js';
import { SystemSnapshotService } from './services/systemSnapshotService.js';
import { PipelineStatusService } from './services/pipelineStatusService.js';
import { UIDataService } from './services/uiDataService.js';
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

const runtimeBridgeService = new RuntimeBridgeService(store);
const providerRegistry = buildProviderRegistry(runtimeBridgeService);
const systemSnapshotService = new SystemSnapshotService(providerRegistry, store);
const pipelineStatusService = new PipelineStatusService(providerRegistry, store);
const uiDataService = new UIDataService(systemSnapshotService, pipelineStatusService, runtimeBridgeService, store);

async function render() {
  const page = location.hash.replace('#','') || 'home';
  store.page = page;
  const runtimeMode = store.runtimeMode || 'orchestrator_mock';
  const payload = await uiDataService.bootstrap(runtimeMode);
  let content = '';
  if (page === 'home') content = renderHome(buildHomeViewModel(payload.system, payload.orchestrator, payload.metadata));
  if (page === 'pool') content = renderPool(buildPoolViewModel(payload.system));
  if (page === 'bankroll') content = renderBankroll(buildBankrollViewModel(payload.system));
  if (page === 'execution') content = renderExecution(buildExecutionViewModel(payload.system, payload.orchestrator));
  if (page === 'history') content = renderHistory(buildHistoryViewModel(payload.system));
  document.getElementById('app').innerHTML = shellTemplate(page, content);
  wire();
}
function wire() {
  document.querySelectorAll('[data-page]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); location.hash = a.dataset.page; }));
  const select = document.getElementById('runtime-mode-select');
  if (select) {
    select.value = store.runtimeMode;
    select.addEventListener('change', async (e) => { store.runtimeMode = e.target.value; await render(); });
  }
  document.getElementById('btn-refresh')?.addEventListener('click', render);
  document.getElementById('btn-import-real')?.addEventListener('click', async () => {
    const file = document.getElementById('real-snapshot-file')?.files?.[0];
    try {
      await runtimeBridgeService.importRealSnapshotFromFile(file);
      store.runtimeMode = 'real_read_protected';
      await render();
      alert('Snapshot real importado com sucesso.');
    } catch (err) {
      await render();
      alert(`Falha ao ler snapshot real: ${err.message}`);
    }
  });
  document.getElementById('btn-clear-real')?.addEventListener('click', async () => {
    runtimeBridgeService.clearImportedRealSnapshot();
    store.runtimeMode = 'orchestrator_mock';
    await render();
  });
}
window.addEventListener('hashchange', render);
render();
