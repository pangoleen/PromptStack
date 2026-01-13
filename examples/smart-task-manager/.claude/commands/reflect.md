---
description: Analyze productivity patterns and get AI insights
allowed-tools: Read, Write
---

# /reflect

Get AI-powered insights about your productivity patterns.

## The AI Difference

Traditional analytics show basic stats.
This one provides **meaningful insights** and **actionable recommendations**.

## Protocol

1. **Load All Data**
   - Read `db/tasks.json` (copy from `db-templates/tasks-template.json` if missing)
   - Read `db/completed.json` (copy from `db-templates/completed-template.json` if missing)
   - Read `db/patterns.json` (copy from `db-templates/patterns-template.json` if missing)

2. **Analyze Patterns**

   **Completion Patterns:**
   - Tasks per day/week
   - Completion rate
   - Average time to complete by priority
   - Best performing days

   **Task Patterns:**
   - Most common tags
   - Priority distribution
   - Overdue frequency
   - Subtask usage

   **Productivity Trends:**
   - Week-over-week comparison
   - Streak tracking
   - Peak productivity periods

3. **Generate Insights**
   ```
   📊 Productivity Insights

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   THIS WEEK
   ┌────────────────────────────────────────┐
   │ Completed:     12 tasks                │
   │ Completion:    80% (12/15 created)     │
   │ Avg time:      1.8 days per task       │
   │ Streak:        🔥 5 days               │
   └────────────────────────────────────────┘

   TRENDS
   Week 1: ██████░░░░ 60%
   Week 2: ████████░░ 80%  (+20% ↑)
   Week 3: ████████░░ 80%  (stable)

   INSIGHTS

   ✨ Your most productive day is Tuesday
      (avg 3.2 tasks vs 1.8 overall)

   ⚠️  High-priority tasks take 2x longer than medium
      Consider breaking them down with /breakdown

   💡 You complete #work tasks 40% faster than #personal
      Try applying work techniques to personal tasks

   🎯 RECOMMENDATION
      You have 3 high-priority tasks pending.
      Based on your patterns, schedule them for Tuesday
      morning for best results.

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

4. **Update Patterns**
   - Save new calculations to patterns.json
   - Track weekly snapshots

5. **Suggest Actions**
   - Specific recommendations based on insights
   - Link to relevant commands
