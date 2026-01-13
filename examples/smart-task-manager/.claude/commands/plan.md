---
description: Generate an AI-powered daily plan
allowed-tools: Read
---

# /plan

Generate an optimized daily plan based on your tasks.

## The AI Difference

Traditional planners just show due dates.
This one creates an **intelligent schedule** considering:
- Task priorities and deadlines
- Estimated effort
- Your productivity patterns
- Logical task grouping

## Protocol

1. **Load Data**
   - Read `db/tasks.json` (copy from `db-templates/tasks-template.json` if missing)
   - Read `db/patterns.json` (copy from `db-templates/patterns-template.json` if missing)
   - Read `db/completed.json` (copy from `db-templates/completed-template.json` if missing)

2. **Analyze Today's Candidates**
   - Due today or overdue
   - High priority items
   - Quick wins (can complete in <30 min)
   - Tasks with momentum (related to recent completions)

3. **Consider Capacity**
   - Typical daily completion: 3-5 tasks
   - Don't overload the plan
   - Leave buffer for unexpected work

4. **Generate Plan**
   ```
   📅 Your Plan for Today (Monday, Jan 13)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   🔴 MUST DO (overdue/due today)
   ┌────────────────────────────────────────┐
   │ • Fix critical bug (#3)         ~1 hr │
   │ • Submit report (#7)           ~30 min │
   └────────────────────────────────────────┘

   🟡 SHOULD DO (high priority)
   ┌────────────────────────────────────────┐
   │ • Write documentation (#1)      ~2 hrs │
   └────────────────────────────────────────┘

   🟢 COULD DO (if time permits)
   ┌────────────────────────────────────────┐
   │ • Review PR #123 (#2)          ~30 min │
   │ • Update dependencies (#5)     ~15 min │
   └────────────────────────────────────────┘

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   📊 Estimated total: ~4.5 hours

   💡 Start with "Fix critical bug" - it's overdue
      and blocking other work.
   ```

5. **Suggest First Action**
   - Recommend starting with highest impact item
   - Provide motivation
