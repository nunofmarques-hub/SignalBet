from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Tuple
import os

def _req_root(req: Dict[str, Any], pack_root: Path):
    value = req.get('project_root')
    if not value:
        return None
    p = Path(value)
    return p if p.is_absolute() else (pack_root / p).resolve()

def _env_root():
    value = os.getenv('SIGNALBET_PROJECT_ROOT')
    return Path(value).resolve() if value else None

def _cfg_root(pack_root: Path):
    cfg = pack_root / 'examples' / 'req' / 'project_root.txt'
    if not cfg.exists():
        return None
    value = cfg.read_text(encoding='utf-8').strip()
    if not value:
        return None
    p = Path(value)
    return p if p.is_absolute() else (pack_root / value).resolve()

def _demo(pack_root: Path):
    return (pack_root / 'examples' / 'project').resolve()

def resolve_project_root(req: Dict[str, Any], pack_root: Path) -> Tuple[Path, str, List[str]]:
    checked: List[str] = []
    for mode, candidate in [
        ('request', _req_root(req, pack_root)),
        ('env', _env_root()),
        ('project_root_txt', _cfg_root(pack_root)),
    ]:
        if candidate is None:
            continue
        checked.append(f'{mode}:{candidate}')
        if candidate.exists() and (candidate / 'data_api').exists():
            return candidate.resolve(), mode, checked
    demo = _demo(pack_root)
    checked.append(f'demo:{demo}')
    return demo, 'demo', checked
