
export function statusChip(value) {
  const map = {
    approved: 'green', reduced: 'amber', blocked: 'red', reserve: 'gray',
    eligible: 'lime', watchlist: 'amber', pending: 'amber', placed: 'cyan', live: 'green',
    settled: 'gray', green: 'green', amber: 'amber', red: 'red', ready: 'lime', hold: 'amber',
    none: 'gray', not_ready: 'red', queued: 'amber', void: 'gray', win: 'green', loss: 'red',
    not_executed: 'gray', fresh: 'green', staged: 'amber', na: 'gray', watch: 'amber', success:'green', partial:'amber', error:'red', idle:'gray'
  };
  const cls = map[value] || 'gray';
  return `<span class="chip ${cls}">${String(value).replace(/_/g,' ')}</span>`;
}

export function scoreBadge(label, value, type='score') {
  const cls = type === 'risk' ? 'risk' : 'score';
  const prefix = label ? `${label}: ` : '';
  return `<span class="pill ${cls}">${prefix}<strong>${value}</strong></span>`;
}

export function kpiTile(label, value, foot='') {
  return `<div class="tile"><div class="tile-label">${label}</div><div class="tile-value mono">${value}</div>${foot ? `<div class="tile-foot">${foot}</div>` : ''}</div>`;
}

export function alertItem(a) {
  return `<div class="alert ${a.level}"><div><strong>${a.title}</strong><div class="small">${a.text}</div></div></div>`;
}

export function detailKV(items) {
  return `<div class="kv">${items.map(([l,v]) => `<div class="kv-item"><div class="kv-label">${l}</div><div class="kv-value">${v}</div></div>`).join('')}</div>`;
}

export function stateBox(kind, title, text, cta='Recarregar estado') {
  return `<div class="state-box ${kind}"><h3>${title}</h3><p>${text}</p><button class="btn ghost state-reload">${cta}</button></div>`;
}

export function tableCellScore(value, type='score') {
  return scoreBadge('', value, type).replace('class="pill score"','class="pill score mono"').replace('class="pill risk"','class="pill risk mono"');
}
