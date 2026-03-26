import { buildVM } from '../viewmodels/historyViewModel.js';
import { simpleTable } from '../components/tables.js';

export function renderHistory(bridge) {
  const vm = buildVM(bridge);
  return `<div class="topbar"><div><h1 style="margin:0">${vm.title}</h1><div class="muted">Ecrã navegável em staging</div></div><button class="button">Pôr tudo a correr</button></div>${simpleTable(vm.title, vm.snapshot)}`;
}
