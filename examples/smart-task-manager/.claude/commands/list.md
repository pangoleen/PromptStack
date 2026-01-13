---
description: Show all tasks
allowed-tools: Read
---

# /list

Display all active tasks.

## Protocol

1. **Load Data**
   - Read `db/tasks.json` (copy from `db-templates/tasks-template.json` if missing)
   - If empty, show "No tasks yet. Use /add to create one."

2. **Filter**
   - Show only non-completed tasks by default
   - If user specifies "all", include completed
   - If user specifies a status, filter by that

3. **Sort**
   - By priority (high first), then by due date (earliest first)

4. **Format Output**
   ```
   📋 Your Tasks (5 active)

   HIGH PRIORITY
   [1] Write documentation          Due: Tomorrow
   [3] Fix critical bug             Due: Today ⚠️

   MEDIUM PRIORITY
   [2] Review PR #123               Due: Friday
   [5] Update dependencies          No due date

   LOW PRIORITY
   [4] Refactor utils               Due: Next week

   💡 Use /suggest to get a recommendation
   ```

5. **Summary**
   - Total count by status
   - Overdue count if any
   - Suggest /suggest if many tasks
