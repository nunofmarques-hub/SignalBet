from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent

def find_registry():
    p = ROOT / "data_api" / "registry" / "official_entrypoints.json"
    return p if p.exists() else None

def main():
    print("=== Data/API shadow run check ===")
    print(f"ROOT={ROOT}")

    checks = []

    registry = find_registry()
    checks.append(("official_entrypoints.json", registry is not None))

    smoke_files = [
        ROOT / "smoke_test_v12_from_trunk.py",
        ROOT / "smoke_test_cards_from_trunk.py",
        ROOT / "smoke_test_btts_from_trunk.py",
    ]

    existing_smokes = [p for p in smoke_files if p.exists()]
    checks.append(("at_least_one_smoke_test", len(existing_smokes) > 0))

    trunk_folder = ROOT / "data_api"
    checks.append(("data_api_folder_exists", trunk_folder.exists()))

    for name, ok in checks:
        print(f"{name}={'OK' if ok else 'FAIL'}")

    if registry:
        try:
            data = json.loads(registry.read_text(encoding="utf-8"))
            print("registry_load=OK")
            if isinstance(data, dict):
                print(f"registry_top_keys={list(data.keys())[:10]}")
            else:
                print(f"registry_type={type(data).__name__}")
        except Exception as e:
            print(f"registry_load=FAIL ({e})")
            sys.exit(1)

    if not all(ok for _, ok in checks):
        print("DATA_API_SHADOW_CHECK=FAIL")
        sys.exit(1)

    print("DATA_API_SHADOW_CHECK=OK")
    sys.exit(0)

if __name__ == "__main__":
    main()