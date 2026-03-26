from __future__ import annotations
from pathlib import Path
import os, sys

def run(project_root: str):
    root = Path(project_root)
    return [
        {'check_id':'python_available','status':'PASS','message':f'Python {sys.version_info.major}.{sys.version_info.minor} disponível.','blocking':True},
        {'check_id':'project_root_valid','status':'PASS' if root.exists() else 'FAIL','message':'Project root válido.' if root.exists() else 'Project root inválido.','blocking':True},
        {'check_id':'required_folders_present','status':'PASS' if (root/'data_api').exists() else 'FAIL','message':'Pastas base encontradas.' if (root/'data_api').exists() else 'Pastas base em falta.','blocking':True},
        {'check_id':'write_permissions_ok','status':'PASS' if os.access(root, os.W_OK) else 'WARN','message':'Permissão de escrita disponível.' if os.access(root, os.W_OK) else 'Sem confirmação de escrita no root.','blocking':False},
    ]
