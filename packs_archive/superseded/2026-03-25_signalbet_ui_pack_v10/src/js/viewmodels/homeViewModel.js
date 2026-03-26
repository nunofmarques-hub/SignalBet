export function createHomeViewModel(data){ return { ...data.home, readiness:data.readiness, run:data.run, providerStatus:data.providerStatus }; }
