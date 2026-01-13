# Smart Task Manager

A complete task manager with AI-powered features, built entirely with PromptStack.

**No code. No database setup. No ML pipeline. Just text.**

## Features

### CRUD Commands
- `/add <task>` - Add a task with natural language
- `/list` - Show all tasks
- `/done <id or name>` - Complete a task
- `/edit <id or name>` - Update a task

### AI Commands
- `/suggest` - AI recommends what to work on next
- `/breakdown <task>` - AI breaks complex tasks into subtasks
- `/plan` - AI generates your daily plan
- `/reflect` - AI analyzes your productivity patterns

## Quick Start

```bash
# Navigate to this directory
cd examples/smart-task-manager

# Start Claude Code
claude

# Try it out
> /add Write project documentation - high priority, due Friday
> /add Review pull requests
> /add Refactor authentication module
> /list
> /suggest
```

## How It Works

This example demonstrates key PromptStack concepts:

| Concept | Implementation |
|---------|----------------|
| Commands as API | `/add`, `/list`, `/done`, `/suggest`, etc. |
| JSON as Database | `tasks.json`, `completed.json`, `patterns.json` |
| AI Features | `/suggest`, `/breakdown`, `/plan`, `/reflect` |
| Hooks | Auto-validation, backups on every write |

## Data Files

| File | Purpose |
|------|---------|
| `db/tasks.json` | Active tasks |
| `db/completed.json` | Completed tasks history |
| `db/patterns.json` | Productivity patterns (for /reflect) |

## The AI Difference

Traditional task managers just store and retrieve data. This one **thinks**:

- `/suggest` considers priority, deadlines, and context
- `/breakdown` intelligently decomposes complex tasks
- `/plan` creates an optimal daily schedule
- `/reflect` identifies your productivity patterns

All without any ML infrastructure - just instructions.
