import { chip } from './ui.js';
export function issuesList(issues = []) {
  if (!issues.length) return '<div class="muted small">Sem issues ativas.</div>';
  return `<ul class="list">${issues.map(i => `<li>${chip(i.severity, i.severity)} ${i.message}</li>`).join('')}</ul>`;
}
