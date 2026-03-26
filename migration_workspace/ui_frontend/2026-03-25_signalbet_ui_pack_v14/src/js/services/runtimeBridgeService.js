
import { validateRealRuntimeShape } from '../adapters/orchestratorAdapters.js';
export class RuntimeBridgeService {
  constructor(store) { this.store = store; this.importedRealSnapshot = null; }
  getImportedRealSnapshot() { return this.importedRealSnapshot; }
  async importRealSnapshotFromFile(file) {
    if (!file) { this.store.realReadMeta.lastReadStatus = 'no_file'; throw new Error('No snapshot file selected.'); }
    const text = await file.text();
    const parsed = JSON.parse(text);
    const validation = validateRealRuntimeShape(parsed);
    this.store.realReadMeta.importedFileName = file.name;
    if (!validation.valid) {
      this.store.realReadMeta.lastReadStatus = 'invalid_shape';
      this.store.error = `Invalid real snapshot shape. Missing: ${validation.missing.join(', ')}`;
      throw new Error(this.store.error);
    }
    this.importedRealSnapshot = parsed;
    this.store.realReadMeta.lastReadStatus = 'imported';
    this.store.error = null;
    return { imported: true, validation };
  }
  clearImportedRealSnapshot() {
    this.importedRealSnapshot = null;
    this.store.realReadMeta.importedFileName = null;
    this.store.realReadMeta.lastReadStatus = 'cleared';
  }
  getAvailableRuntimeModes() { return ['orchestrator_mock', 'real_read_protected', 'placeholder_live']; }
}
