---
description: Get AI recommendation for what to work on next
allowed-tools: Read
---

# /suggest

Get an intelligent recommendation for what task to work on next.

## The AI Difference

This is where PromptStack shines. Traditional task managers just show a list.
This one **thinks** about what you should do next.

## Scoring Algorithm

Score each task by:

1. **Priority Score** (1-3)
   - High: 3 points
   - Medium: 2 points
   - Low: 1 point

2. **Deadline Score** (1-5)
   - Overdue: 5 points
   - Due today: 4 points
   - Due tomorrow: 3 points
   - Due this week: 2 points
   - Later/none: 1 point

3. **Age Score** (0-3)
   - +1 for every 3 days since creation
   - Max 3 points (prevents old low-priority from dominating)

4. **Context Bonus** (0-2)
   - +1 if similar to recently completed task (momentum)
   - +1 if blocking other tasks

**Total Score** = Priority + Deadline + Age + Context

## Protocol

1. **Load Data**
   - Read `db/tasks.json` (copy from `db-templates/tasks-template.json` if missing)
   - Read `db/completed.json` for context (copy from `db-templates/completed-template.json` if missing)

2. **Score All Tasks**
   - Calculate score for each active task
   - Track the factors for explanation

3. **Select Top Recommendation**
   - Highest scoring task wins
   - Include runner-ups

4. **Present Recommendation**
   ```
   🎯 Recommended: Fix critical bug (#3)

   Why this task?
   • High priority (+3)
   • Due today (+4)
   • Created 2 days ago (+0)

   Score: 7/11

   ───────────────────────

   Also consider:
   • Write documentation (#1) - Score: 6
   • Review PR #123 (#2) - Score: 5

   💡 Use /done 3 when complete
   ```

5. **Handle Edge Cases**
   - No tasks: "No tasks to suggest. Use /add to create one."
   - All completed: "All caught up! 🎉"
   - Tied scores: Prefer higher priority, then earlier due date
