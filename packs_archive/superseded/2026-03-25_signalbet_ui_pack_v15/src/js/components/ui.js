export function badge(text, tone='cyan'){ return `<span class="badge ${tone}">${text}</span>`; }
export function kpi(label, value){ return `<div class="card"><div class="kpi-value">${value}</div><div class="kpi-label">${label}</div></div>`; }
export function progress(ratio){ const pct=Math.round((ratio||0)*100); return `<div class="progress"><span style="width:${pct}%"></span></div><div class="small muted">${pct}%</div>`; }
