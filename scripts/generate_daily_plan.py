from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tracker.database import ROOT, atomic_write_json, load_questions, read_json
from tracker.scheduler import build_daily_plan


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a five-item daily study plan.")
    parser.add_argument("--date", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    plan = build_daily_plan(load_questions(), args.date)
    path = ROOT / "tracker/study_plan.json"
    plans = read_json(path, [])
    plans = [item for item in plans if item.get("date") != plan["date"]] + [plan]
    atomic_write_json(path, plans)
    print(json.dumps(plan, indent=2))


if __name__ == "__main__":
    main()
