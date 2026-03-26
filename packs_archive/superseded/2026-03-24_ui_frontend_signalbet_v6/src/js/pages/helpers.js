import { stateBox } from '../components/ui.js';

export function withPageState(state, views) {
  if (state === 'loading') {
    return stateBox('loading', 'A carregar estado do sistema', 'A UI está a representar a pipeline, mas esta vista ainda aguarda dados para ficar completa.');
  }
  if (state === 'empty') {
    return stateBox('empty', 'Sem resultados neste momento', 'Nenhum item corresponde ao filtro ou ao estado atual desta área.');
  }
  if (state === 'error') {
    return stateBox('error', 'Falha no carregamento da vista', 'A estrutura visual mantém-se disponível, mas os dados desta secção falharam nesta simulação.');
  }
  return views();
}
