---
description: Complete a task
allowed-tools: Read, Write
---

# /done

Mark a task as complete.

## Input

Task ID or name - e.g.:
- `/done 3`
- `/done call with client`
- `/done documentation`

## Protocol

1. **Load Data**
   - Read `db/tasks.json` (copy from `db-templates/tasks-template.json` if missing)
   - Read `db/completed.json` (copy from `db-templates/completed-template.json` if missing)

2. **Find Task**
   - If input is a number, look up by ID
   - If input is text, search by title (partial match, case-insensitive)
   - If multiple matches found, show options and ask user to specify
   - If not found, show error with list of active tasks

3. **Complete Task**
   - Set status to "done"
   - Set completed_at timestamp
   - Calculate duration (created_at to now)

4. **Move to History**
   - Add to completed.json with:
     - Original task data
     - completed_at timestamp
     - duration_days
   - Update completed.json stats

5. **Update Patterns**
   - Read `db/patterns.json` (copy from `db-templates/patterns-template.json` if missing)
   - Increment completion counts
   - Update averages

6. **Remove from Active**
   - Remove from tasks.json tasks array

7. **Celebrate!**
   ```
   🎉 Completed: "Write documentation"
      Time to complete: 2 days

      📊 Stats: 15 tasks completed this week
      🔥 Streak: 3 days in a row!

      💡 Great momentum! Consider tackling "Review PR" next.
   ```
