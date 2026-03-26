export function kpiTile(label, value){ return `<div class="kpi"><div class="label">${label}</div><div class="value">${value}</div></div>`; }
export function chips(items){ return items.map(([text, cls='']) => `<span class="chip ${cls}">${text}</span>`).join(''); }
