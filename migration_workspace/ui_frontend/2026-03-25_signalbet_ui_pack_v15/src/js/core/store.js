export const store = {
  state: { page: 'home', sourceModeRequested: 'orchestrator_mock' },
  listeners: [],
  set(patch){ this.state = {...this.state, ...patch}; this.listeners.forEach(l => l(this.state)); },
  subscribe(fn){ this.listeners.push(fn); }
};
