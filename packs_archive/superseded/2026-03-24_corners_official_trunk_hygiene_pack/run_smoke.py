from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
print((ROOT/'examples'/'summary.json').read_text(encoding='utf-8'))
