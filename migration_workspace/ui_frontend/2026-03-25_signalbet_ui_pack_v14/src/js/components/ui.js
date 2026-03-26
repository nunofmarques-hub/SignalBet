
export function badge(label, kind='cyan') { return `<span class="badge ${kind}">${label}</span>`; }
export function tile(label, value) { return `<div class="tile"><div class="label">${label}</div><div class="value">${value}</div></div>`; }
export function metric(label, value) { return `<div class="card-row"><span class="small">${label}</span><strong>${value}</strong></div>`; }
