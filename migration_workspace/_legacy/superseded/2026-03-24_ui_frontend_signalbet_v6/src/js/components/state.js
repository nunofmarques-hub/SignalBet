import { appState } from '../../data/mock-data.js';

export function getPageState(page) {
  return appState.pages[page] || 'success';
}

export function setPageState(page, state) {
  appState.pages[page] = state;
}
