import { getAppContext } from '../services/uiDataService.js';

const appContext = getAppContext();

export const store = {
  ui: {
    pageStates: { ...appContext.pages },
    selected: { pool: 0, bankroll: 0, executionIntake: 0, history: 0 },
    filters: { period: 'Hoje', query: '' },
    orchestratorStatus: appContext.orchestrator.status,
    providerMode: 'contract'
  }
};

export function getPageState(page){ return store.ui.pageStates[page] || 'success'; }
export function setPageState(page, state){ store.ui.pageStates[page] = state; }
export function getSelected(scope){ return store.ui.selected[scope] || 0; }
export function setSelected(scope, value){ store.ui.selected[scope] = value; }
export function getOrchestratorStatus(){ return store.ui.orchestratorStatus; }
export function setOrchestratorStatus(status){ store.ui.orchestratorStatus = status; }
export function cycleOrchestratorStatus(){
  const order = ['idle','running','partial','success','error'];
  const idx = order.indexOf(store.ui.orchestratorStatus);
  store.ui.orchestratorStatus = order[(idx + 1) % order.length];
  return store.ui.orchestratorStatus;
}
export function getProviderMode(){ return store.ui.providerMode; }
