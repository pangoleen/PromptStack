---
description: Break a complex task into subtasks
allowed-tools: Read, Write
---

# /breakdown

Use AI to break a complex task into manageable subtasks.

## The AI Difference

Traditional task managers require you to manually create subtasks.
This one analyzes your task and **intelligently decomposes it**.

## Input

Either:
- Task ID: `/breakdown 3`
- Task name: `/breakdown documentation`
- New task description: `/breakdown Implement user authentication`

## Protocol

1. **Identify Task**
   - If number provided, look up by ID
   - If matches existing task title (partial, case-insensitive), load that task
   - Otherwise, treat as new task description

2. **Analyze Complexity**
   Consider:
   - Technical components involved
   - Logical sequence of steps
   - Dependencies between steps
   - Estimated effort per step

3. **Generate Subtasks**
   Create 3-7 subtasks that:
   - Are actionable and specific
   - Follow a logical order
   - Can be completed independently
   - Have clear completion criteria

4. **Present Breakdown**
   ```
   🔨 Breaking down: "Implement user authentication"

   Subtasks:
   ┌─────────────────────────────────────────────┐
   │ 1. [ ] Set up authentication library        │
   │ 2. [ ] Create user model and migrations     │
   │ 3. [ ] Implement registration endpoint      │
   │ 4. [ ] Implement login endpoint             │
   │ 5. [ ] Add session/token management         │
   │ 6. [ ] Create protected route middleware    │
   │ 7. [ ] Write tests for auth flows           │
   └─────────────────────────────────────────────┘

   Estimated total effort: Medium-High

   💡 Add these as subtasks? (yes/no)
   ```

5. **Save if Confirmed**
   - If existing task: Add subtasks to task.subtasks array
   - If new task: Create task with subtasks

6. **Show Result**
   ```
   ✅ Created 7 subtasks for "Implement user authentication"

   📋 Use /list to see your updated tasks
   ```
