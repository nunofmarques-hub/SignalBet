import { SnapshotProvider } from './providerInterfaces.js';
export class RealSystemPlaceholderProvider extends SnapshotProvider {
  getSystemSnapshot(){ return { status:'PLACEHOLDER_REAL_SOURCE', message:'Awaiting real provider binding' }; }
  getPipelineSnapshot(){ return { status:'PLACEHOLDER_REAL_SOURCE', message:'Awaiting orchestrator binding' }; }
}
