#!/usr/bin/env python3
"""
Smart Task Manager - Data Validation Hook

Validates JSON files after writes and creates timestamped backups.
"""

import sys
import json
import shutil
from datetime import datetime
from pathlib import Path

def main():
    try:
        hook_input = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if "db/" not in file_path or not file_path.endswith(".json"):
        sys.exit(0)

    path = Path(file_path)
    if not path.exists():
        sys.exit(0)

    # Create timestamped backup
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = path.with_suffix(f".bak.{timestamp}")
    shutil.copy(path, backup_path)

    # Validate JSON
    try:
        with open(path, 'r') as f:
            data = json.load(f)

        # Additional validation for tasks.json
        if "tasks" in str(path):
            if "tasks" not in data:
                raise ValueError("Missing 'tasks' array")
            if "next_id" not in data:
                raise ValueError("Missing 'next_id'")

        print(f"[ok] Validated: {path.name}")
        sys.exit(0)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"[error] Invalid: {path.name} - {e}", file=sys.stderr)
        shutil.copy(backup_path, path)
        sys.exit(2)

if __name__ == "__main__":
    main()
