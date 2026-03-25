import json
from pathlib import Path

class OfficialDataAPIProvider:
    def __init__(self, sample_path):
        self.sample_path = Path(sample_path)

    def get_event_payload(self):
        return json.loads(self.sample_path.read_text(encoding="utf-8"))
