from __future__ import annotations
from pathlib import Path
import os, sys

def run(project_root: str):
    root = Path(project_root)
    req = [root / 'data_api']
    writable = os.access(root, os.W_OK) if root.exists() else False
    return [
        {'check_id':'python_available','status':'PASS','message':f'Python {sys.version_info.major}.{sys.version_info.minor} disponível.','blocking':True},
        {'check_id':'project_root_valid','status':'PASS' if root.exists() else 'FAIL','message':'project_root válido.' if root.exists() else 'project_root em falta.','blocking':True},
        {'check_id':'required_folders_present','status':'PASS' if all(p.exists() for p in req) else 'FAIL','message':'Pastas base presentes.' if all(p.exists() for p in req) else 'Pastas base em falta.','blocking':True},
        {'check_id':'write_permissions_ok','status':'PASS' if writable else 'WARN','message':'Permissão de escrita confirmada.' if writable else 'Sem permissão de escrita.','blocking':False},
    ]
