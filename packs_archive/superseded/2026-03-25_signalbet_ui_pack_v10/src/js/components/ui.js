export function chip(label, cls=''){ return `<span class="chip ${cls}">${label}</span>`; }
export function kpi(title, value, tone=''){ return `<div class="card"><div class="muted">${title}</div><div class="kpi-number ${tone}">${value}</div></div>`; }
export function stateBox(title, body){ return `<div class="state-box"><h3>${title}</h3><div class="muted">${body}</div></div>`; }
