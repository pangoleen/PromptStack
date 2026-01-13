# PromptStack Reference

## Architecture

PromptStack supports two variants.

### Minimal (Commands Only)

Just commands and data.

```
my-app/
├── CLAUDE.md                 # All business logic here
├── .claude/
│   ├── commands/             # Your API endpoints
│   │   ├── add.md
│   │   ├── list.md
│   │   └── done.md
│   ├── hooks/                # Validation, backups
│   │   └── validate-data.py
│   └── settings.json         # Hook configuration
├── db/                     # JSON database (gitignored)
│   └── tasks.json
└── db-templates/            # Templates (committed)
    └── tasks-template.json
```

### Extended (Agents + Skills)

Adds agents and skills for reusable logic and delegation.

```
my-app/
├── CLAUDE.md                 # Core identity only
├── .claude/
│   ├── commands/             # Entry points (delegate to agents)
│   ├── agents/               # Specialized workers
│   │   ├── planning-agent.md
│   │   └── analytics-agent.md
│   ├── skills/               # Shared knowledge
│   │   └── productivity/
│   │       └── SKILL.md
│   ├── hooks/
│   └── settings.json
├── db/
└── db-templates/
```

### Choosing Your Architecture

| Factor | Minimal | Extended |
|--------|---------|----------|
| Components | Commands only | Commands + Agents + Skills |
| Reusable logic | No | Yes |
| Delegation | No | Yes |

---

## Commands

Commands are your API endpoints. Users invoke them with `/command-name`.

**Location:** `.claude/commands/{name}.md`

### Structure

```yaml
---
description: What this command does (shown in /help)
allowed-tools: Read, Write, Edit
---

# /command-name

## Purpose
Brief description of what this command does.

## Protocol
1. Load required JSON files
2. Validate data exists (copy from template if needed)
3. Execute the operation
4. Update data files
5. Show results and suggest next actions
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `description` | Yes | Shown when user runs `/help` |
| `allowed-tools` | No | Restricts which tools the command can use |

### Tool Restrictions

```yaml
# Read-only command
allowed-tools: Read

# CRUD command
allowed-tools: Read, Write, Edit

# System command (use sparingly)
allowed-tools: Read, Write, Edit, Bash
```

---

## JSON Data

JSON files are your database tables.

**Location:** `db/{name}.json`

### Conventions

- Store active data in `db/` (gitignored)
- Store templates in `db-templates/` (committed)
- Include `next_id` for auto-incrementing IDs
- Include timestamps for tracking

### Example Schema

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Example task",
      "status": "todo",
      "priority": "high",
      "created_at": "2025-01-12T10:00:00Z",
      "updated_at": "2025-01-12T10:00:00Z"
    }
  ],
  "next_id": 2,
  "last_updated": "2025-01-12T10:00:00Z"
}
```

### Data Templates

Store empty templates in `db-templates/`:

```json
{
  "tasks": [],
  "next_id": 1,
  "last_updated": null
}
```

Commands should check if data exists and copy from template if not.

---

## CLAUDE.md

Your app's identity and business logic.

### Minimal Architecture

All logic in one file:

```markdown
# My App

You are a task management assistant.

## Core Rules
- Always confirm before deleting
- Show task count after modifications
- Suggest next actions

## Data Files
- `db/tasks.json` - Active tasks
- `db/completed.json` - Completed tasks

## Available Commands
- /add - Add a task
- /list - Show tasks
- /done - Complete a task
```

### Extended Architecture

Core identity only (logic in agents):

```markdown
# My App

You are a task management assistant.

## Core Identity
- Helpful and encouraging
- Focus on productivity

## Agents
Delegate to specialized agents for specific tasks.
```

---

## Hooks

Hooks run automatically in response to events.

**Configuration:** `.claude/settings.json`

### Hook Types

| Hook | When It Fires | Use For |
|------|---------------|---------|
| `PostToolUse` | After Write/Edit | Validation, backups |
| `SessionStart` | Session begins | Welcome message, stats |
| `SessionEnd` | Session ends | Daily backup |
| `PreCompact` | Before compaction | Safety backup |

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

- `matcher`: Regex for which tools trigger the hook
- `timeout`: Seconds before timeout

### Exit Codes

| Code | Behavior |
|------|----------|
| `0` | Success - continue normally |
| `2` | Block operation, show error |
| Other | Log error, continue anyway |

### Making Hooks Executable

Hook scripts must be executable:

```bash
chmod +x .claude/hooks/*.py
```

### Example Hook

```python
#!/usr/bin/env python3
import sys, json, shutil
from pathlib import Path
from datetime import datetime

hook_input = json.load(sys.stdin)
file_path = hook_input.get("tool_input", {}).get("file_path", "")

if "db/" not in file_path or not file_path.endswith(".json"):
    sys.exit(0)

path = Path(file_path)
if not path.exists():
    sys.exit(0)

# Backup before validation
backup = path.with_suffix(f".backup-{datetime.now():%Y%m%d-%H%M%S}.json")
shutil.copy(path, backup)

# Validate JSON
try:
    json.load(open(path))
    print(f"[ok] Valid: {path.name}")
except json.JSONDecodeError as e:
    print(f"[error] Invalid JSON: {e}", file=sys.stderr)
    sys.exit(2)  # Block the operation
```

---

## Settings

**Location:** `.claude/settings.json`

### Structure

```json
{
  "hooks": {
    "PostToolUse": [...],
    "SessionStart": [...],
    "SessionEnd": [...]
  }
}
```

### Local Overrides

Create `.claude/settings.local.json` (gitignored) for local settings:

```json
{
  "permissions": {
    "allow": ["Bash(npm test)"],
    "deny": ["Bash(rm -rf *)"]
  }
}
```

---

## Advanced: Agents & Skills

For the Extended architecture, you can add agents and skills for reusable logic and delegation.

### The Layer Model

```
┌─────────────────────────────────────────────────────────────────┐
│  COMMANDS (Interface Layer)                                      │
│  /add, /list, /suggest - User-facing entry points                │
└─────────────────────────────────────────────────────────────────┘
                              ↓ delegates to
┌─────────────────────────────────────────────────────────────────┐
│  AGENTS (Service Layer)                                          │
│  planning-agent, analytics-agent - Domain-specific workers       │
└─────────────────────────────────────────────────────────────────┘
                              ↓ activates
┌─────────────────────────────────────────────────────────────────┐
│  SKILLS (Knowledge Layer)                                        │
│  productivity, patterns - Reusable domain expertise              │
└─────────────────────────────────────────────────────────────────┘
                              ↓ reads/writes
┌─────────────────────────────────────────────────────────────────┐
│  DATA (Persistence Layer)                                        │
│  tasks.json, completed.json - JSON files as database             │
└─────────────────────────────────────────────────────────────────┘
```

### Agents

Agents are specialized workers for specific domains.

**Location:** `.claude/agents/{name}.md`

#### Structure

```yaml
---
name: planning-agent
description: Handles daily planning and task suggestions
tools: Read, Write, Edit
model: sonnet
skills: productivity
---

# Planning Agent

You help users plan their day and prioritize tasks.

## Process
1. Load tasks and completed history
2. Analyze priorities and deadlines
3. Generate optimized daily plan
4. Update patterns tracking
```

#### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Agent identifier |
| `description` | Yes | When to use this agent |
| `tools` | No | Tools available (default: all) |
| `model` | No | Model to use (haiku/sonnet/opus) |
| `skills` | No | Skills to auto-activate |

#### Model Selection

| Model | Use For | Cost |
|-------|---------|------|
| `haiku` | Simple analysis, fast tasks | Low |
| `sonnet` | Complex reasoning, generation | Medium |
| `opus` | Most complex tasks | High |

### Skills

Skills are reusable knowledge modules.

**Location:** `.claude/skills/{name}/SKILL.md`

#### Structure

```yaml
---
name: productivity
description: Streaks, completion tracking, motivation
---

# Productivity Skill

## Streaks
- +1 for each day with task completion
- Reset to 0 if day missed
- Track longest streak

## Completion Tracking
- Tasks completed per day/week
- Completion rate (completed / created)
- Format: { date, count, rate }
```

#### How Skills Work

1. Agent declares skills in frontmatter: `skills: productivity`
2. When agent is invoked, skills are loaded automatically
3. Skill knowledge is available to the agent
