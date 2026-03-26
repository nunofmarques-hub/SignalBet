export const store = {
  route: 'home',
  sourceMode: 'orchestrator_mock',
  listeners: [],
  set(partial) { Object.assign(this, partial); this.listeners.forEach(fn => fn(this)); },
  subscribe(fn) { this.listeners.push(fn); }
};
