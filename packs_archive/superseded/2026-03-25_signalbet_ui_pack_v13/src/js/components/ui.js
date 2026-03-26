export function badge(text, tone='') { return `<span class="badge ${tone}">${text}</span>`; }
export function chip(text, tone='') { return `<span class="chip ${tone}">${text}</span>`; }
export function kpiTile(label, value, tone='') {
  return `<div class="card"><small>${label}</small><div class="kpi ${tone}">${value}</div></div>`;
}
export function progress(value) { return `<div class="progress"><span style="width:${Math.round(value*100)}%"></span></div>`; }
