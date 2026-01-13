---
description: Add a new task
allowed-tools: Read, Write
---

# /add

Add a new task to your task list.

## Input Format

Natural language description. Examples:
- "Write documentation"
- "Review PR #123 - high priority"
- "Submit report by Friday"
- "Call client tomorrow - urgent"

## Protocol

1. **Load Data**
   - Read `db/tasks.json` (copy from `db-templates/tasks-template.json` if missing)

2. **Parse Input**
   - Extract title (required)
   - Extract priority: high, medium (default), low
   - Extract due date: parse natural language (today, tomorrow, Friday, etc.)
   - Extract tags: any #hashtags or [brackets]

3. **Create Task**
   ```json
   {
     "id": <next_id>,
     "title": "...",
     "description": "",
     "status": "todo",
     "priority": "medium",
     "tags": [],
     "due_date": null,
     "created_at": "<ISO timestamp>",
     "updated_at": "<ISO timestamp>",
     "subtasks": []
   }
   ```

4. **Save**
   - Add to tasks array
   - Increment next_id
   - Update last_updated

5. **Confirm**
   ```
   ✅ Task added: "Write documentation"
      Priority: High | Due: Tomorrow

      📊 You now have X active tasks (Y high priority)
   ```
