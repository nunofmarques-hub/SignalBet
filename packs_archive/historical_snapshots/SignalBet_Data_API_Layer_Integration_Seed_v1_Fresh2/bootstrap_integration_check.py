from data_api.paths import ensure_base_dirs
from data_api.services.fixtures_service import get_fixtures_by_league_season

def main() -> None:
    ensure_base_dirs()
    print("[OK] Base dirs ensured")
    print("[OK] Services importados")
    fixtures = get_fixtures_by_league_season(140, 2024)
    print(f"[INFO] Fixtures em cache: {len(fixtures)}")

if __name__ == "__main__":
    main()
