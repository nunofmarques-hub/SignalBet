import { chip } from './ui.js';
export function renderIssue(issue){
  const cls = issue.severity === 'critical' ? 'red' : issue.severity === 'warning' ? 'amber' : 'cyan';
  return `<div class="list-row"><div>${chip(issue.severity.toUpperCase(), cls)}</div><div class="muted">${issue.message}</div></div>`;
}
export function renderStage(stage){
  const map = { SUCCESS:'green', RUNNING:'lime', ERROR:'red', PARTIAL:'amber', IDLE:'' };
  return `<div class="stage ${stage.state==='RUNNING'?'active':''}">${chip(stage.label, map[stage.state]||'')}<div class="muted" style="margin-top:8px">${stage.state}</div></div>`;
}
