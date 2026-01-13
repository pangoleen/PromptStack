---
description: Update a task
allowed-tools: Read, Write, Edit
---

# /edit

Update an existing task.

## Input

Task ID or name, followed by changes - e.g.:
- `/edit 3 change priority to high`
- `/edit documentation due tomorrow`
- `/edit client call add tag #urgent`

## Protocol

1. **Load Data**
   - Read `db/tasks.json` (copy from `db-templates/tasks-template.json` if missing)

2. **Find Task**
   - If input starts with a number, look up by ID
   - If input is text, search by title (partial match, case-insensitive)
   - If multiple matches found, show options and ask user to specify
   - If not found, show error with list of active tasks

3. **Show Current State**
   ```
   📝 Editing Task #3:
      Title: Write documentation
      Priority: Medium
      Due: Friday
      Tags: #docs
   ```

4. **Parse Changes**
   - Title changes
   - Priority changes (high/medium/low)
   - Due date changes
   - Tag additions/removals
   - Description updates

5. **Apply Changes**
   - Update relevant fields
   - Set updated_at timestamp

6. **Confirm**
   ```
   ✅ Task #3 updated:
      Priority: Medium → High
      Due: Friday → Tomorrow

   📋 Use /list to see all tasks
   ```
