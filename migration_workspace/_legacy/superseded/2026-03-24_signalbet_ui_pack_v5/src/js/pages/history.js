import { historyItems, summary } from '../../../data/mock-data.js';
import { chip, tile, table, stateBlock } from '../components.js';

export function renderHistory(state='normal') {
  if (state==='empty') return stateBlock('Sem histórico para este filtro','Ajusta o período ou o módulo para voltar a obter resultados.');
  return `
    <section class="kpi-grid">
      ${tile('Total Picks', summary.history.total)}
      ${tile('Settled', summary.history.settled)}
      ${tile('Wins', summary.history.wins)}
      ${tile('Losses', summary.history.losses)}
      ${tile('Strike Rate', summary.history.strike)}
      ${tile('ROI', summary.history.roi)}
    </section>
    <section class="split-2">
      <div class="panel">
        <h2 class="section-title">Historical Ledger</h2>
        ${table(['Date','Fixture','Market','Source','Result','Return','Quality'], historyItems.map(h => `<tr><td>${h.date}</td><td>${h.fixture}</td><td>${h.market}</td><td>${h.module_source}</td><td>${chip(h.result, h.result==='win'?'green':h.result==='loss'?'red':'gray')}</td><td class="mono">${h.return}</td><td>${chip(h.data_quality_flag, h.data_quality_flag==='green'?'green':'amber')}</td></tr>`))}
      </div>
      <div class="panel">
        <h2 class="section-title">Validation Insights</h2>
        <div class="list">
          <div class="list-item"><strong>v12:</strong> estabilidade acima da média no período.</div>
          <div class="list-item"><strong>BTTS:</strong> precisa de mais amostra e melhor qualidade de dado.</div>
          <div class="list-item"><strong>Reduced picks:</strong> melhor controlo de risco, mas menor retorno agregado.</div>
        </div>
      </div>
    </section>`;
}
