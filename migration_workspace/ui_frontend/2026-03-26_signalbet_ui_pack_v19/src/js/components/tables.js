export function stepsTable(steps=[]){
  return `<table class="table"><thead><tr><th>Step</th><th>Status</th><th>Note</th></tr></thead><tbody>${
    steps.map(step=>`<tr><td>${step.step}</td><td>${step.status}</td><td>${step.note || ''}</td></tr>`).join('')
  }</tbody></table>`;
}
