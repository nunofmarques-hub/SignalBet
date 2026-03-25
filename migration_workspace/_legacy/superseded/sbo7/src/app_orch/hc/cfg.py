from __future__ import annotations
from pathlib import Path

def run(pack_root: str):
    root = Path(pack_root)
    api_env = root / 'api.env.txt'
    has_key = False
    if api_env.exists():
        text = api_env.read_text(encoding='utf-8', errors='ignore')
        has_key = 'API_KEY=' in text and len(text.split('API_KEY=',1)[1].strip()) > 0
    settings = root / 'examples' / 'req' / 'sample.json'
    return [
        {'check_id':'api_env_present','status':'PASS' if api_env.exists() else 'WARN','message':'api.env.txt encontrado.' if api_env.exists() else 'api.env.txt em falta no pack.','blocking':False},
        {'check_id':'api_key_present','status':'PASS' if has_key else 'WARN','message':'API key presente.' if has_key else 'API key não configurada no pack.','blocking':False},
        {'check_id':'settings_file_present','status':'PASS' if settings.exists() else 'FAIL','message':'settings/run request base encontrado.' if settings.exists() else 'run request base em falta.','blocking':True},
    ]
