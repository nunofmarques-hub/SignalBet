from __future__ import annotations
from pathlib import Path

def run(pack_root: str):
    root = Path(pack_root)
    envf = root / 'api.env.txt'
    profiles = root / 'src' / 'app_orch' / 'man' / 'profiles.json'
    api_key_ok = False
    if envf.exists():
        text = envf.read_text(encoding='utf-8').strip()
        api_key_ok = text.startswith('API_KEY=') and len(text) > len('API_KEY=')
    return [
        {'check_id':'api_env_present','status':'PASS' if envf.exists() else 'WARN','message':'api.env.txt presente.' if envf.exists() else 'api.env.txt em falta.','blocking':False},
        {'check_id':'api_key_present','status':'PASS' if api_key_ok else 'WARN','message':'API key configurada.' if api_key_ok else 'API key em falta ou placeholder.','blocking':False},
        {'check_id':'settings_file_present','status':'PASS' if profiles.exists() else 'FAIL','message':'profiles.json presente.' if profiles.exists() else 'profiles.json em falta.','blocking':True},
    ]
