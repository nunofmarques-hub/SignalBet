from pathlib import Path
import os, sys

def resolve_trunk_root(explicit=None):
    candidates = []
    if explicit:
        candidates.append(Path(explicit).resolve())
    env_value = os.environ.get("SIGNALBET_TRUNK_ROOT")
    if env_value:
        candidates.append(Path(env_value).resolve())
    here = Path(__file__).resolve().parent.parent
    candidates.append((here / ".." / ".." / "data_api" / "Data_API_Official_Trunk_v1").resolve())
    candidates.append((here / ".." / "Data_API_Official_Trunk_v1").resolve())
    for candidate in candidates:
        if (candidate / "data_api").exists():
            return candidate
    raise FileNotFoundError("Nao encontrei o Data_API_Official_Trunk_v1. Usa --trunk-root ou SIGNALBET_TRUNK_ROOT.")

def bootstrap_trunk_imports(trunk_root):
    trunk_str = str(trunk_root)
    if trunk_str not in sys.path:
        sys.path.insert(0, trunk_str)
