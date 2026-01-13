#!/usr/bin/env python3
"""
Smart Task Manager - Session End Hook

Creates daily backup and updates patterns.
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

def main():
    project_dir = Path(__file__).parent.parent.parent
    data_dir = project_dir / "db"
    backup_dir = project_dir / "_backup" / datetime.now().strftime("%Y%m%d")

    if not data_dir.exists():
        return

    # Create daily backup
    backup_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for json_file in data_dir.glob("*.json"):
        shutil.copy(json_file, backup_dir / json_file.name)
        count += 1

    if count > 0:
        print(f"Backup complete: {count} files saved")

    # Quick stats
    tasks_file = data_dir / "tasks.json"
    if tasks_file.exists():
        try:
            with open(tasks_file) as f:
                data = json.load(f)
            active = len([t for t in data.get("tasks", []) if t.get("status") != "done"])
            print(f"Open tasks: {active}")
        except:
            pass

if __name__ == "__main__":
    main()
