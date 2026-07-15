"""Migration is intentionally review-driven; see docs/MIGRATION_REPORT.md for the inventory."""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    print(f"Legacy material remains preserved at {root / 'Senior Data Engineer Interview Prep'}")
    print("Move one reviewed question at a time and update the migration report and tracker.")


if __name__ == "__main__":
    main()
