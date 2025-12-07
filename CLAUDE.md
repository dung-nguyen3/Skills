# Skills Repository - Global Settings

This repository contains Claude Code infrastructure and study guide materials for pharmacy education.

## Personal Context

- I'm a physician assistant student learning to use Claude Code
- I use VS Code with Claude Code extension as my primary environment
- Explain technical concepts clearly - I'm learning

## General Rules

### File Management
- Never create files in home directory (use project directories)
- Always use absolute paths, not relative paths
- Ask before creating new files unless explicitly required

### Communication Style
- No emojis unless explicitly requested or unless it's critical information.
- Concise, clear explanations
- Technical accuracy over validation

### Research Before Guessing
- When unsure about technical details, ALWAYS use WebSearch first
- Do not guess or assume - verify with official documentation
- Especially for: command syntax, best practices, tool behavior, Claude Code features

## Repository Architecture

### Main Directories

**`.claude/`** - Claude Code Infrastructure
- `commands/` - Slash commands for study guide creation
- `skills/` - Skills for source verification and mnemonics
- `hooks/` - Automation hooks for quality control
- `agents/` - Specialized agents

**`study-guides/`** - Study Guide System
- `templates-and-examples/` - All templates and Python examples
- `user-docs/` - User documentation (HOW_TO_USE, START_HERE, etc.)
- `infrastructure-docs/` - Technical documentation
- `CLAUDE.md` - Study guide specific protocols

### Root Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Global settings (this file) |
| `COMMANDS.md` | Quick command reference |
| `QUICK_START.md` | Getting started guide |
| `README.md` | Repository overview |
| `SLASH_COMMANDS_REFERENCE.md` | Detailed command documentation |

## Git Operations Protocol

### Branch Naming Requirements

**Format:** `claude/claude-md-{session-id}-{unique-id}`

**IMPORTANT:**
- Branch MUST start with `claude/` and end with matching session ID
- Push will fail with 403 HTTP error if naming convention violated
- This is enforced by the remote repository

### Push/Pull Operations

**For git push:**
- Always use: `git push -u origin <branch-name>`
- On network failures, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
- Never use force push without explicit user permission

**For git fetch/pull:**
- Prefer specific branches: `git fetch origin <branch-name>`
- On network failures, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
- For pulls: `git pull origin <branch-name>`

### Automatic Backup Protocol

**Before modifying infrastructure files, automatically create a local backup branch:**

**Files that trigger backup:**
- `.claude/commands/` (slash commands)
- `.claude/skills/` (skills)
- `.claude/hooks/` (hooks)
- `study-guides/templates-and-examples/` (templates only, not output files)
- Root config files (CLAUDE.md, etc.)

**Do NOT backup for:**
- Creating study guide output files (Excel, Word, HTML, Anki, etc.)

**Backup commands to run:**
```bash
# Create timestamped backup branch
git branch backup-$(date +%Y%m%d-%H%M)

# Keep only 5 most recent backups, delete oldest
git branch | grep "backup-" | sort | head -n -5 | xargs -r git branch -d
```

**Restore if needed:**
```bash
git checkout backup-YYYYMMDD-HHMM
```

## Navigation Guide

### Finding Infrastructure Components

**Skills:** `.claude/skills/`
- `skill-rules.json` - Study guide verification triggers
- `source-only-enforcer/` - Source accuracy enforcement
- `study-guide-verifier/` - Verification protocols
- `mnemonic-researcher/` - Mnemonic research methodology

**Hooks:** `.claude/hooks/`
- Session start/end hooks
- Verification guard hooks
- Quality gate enforcement

**Commands:** `.claude/commands/`
- `/drugs-3-tab-excel` - 4-tab Excel drug charts
- `/master-chart-excel` - Single-sheet master chart
- `/key-comparisons-excel` - Excel comparison tables
- `/clinical-assessment-excel` - Clinical assessment Excel
- `/LO-word` - Word learning objectives
- `/LO-html` - HTML learning objectives
- `/drugs-html` - HTML drug reference charts
- `/clinical-assessment-html` - Clinical H&P guide (HTML)
- `/anki` - Anki flashcard decks
- `/autobiography-trick` - Drug autobiography stories
- `/word-excel-anki` - Multi-format study bundle
- `/verify-accuracy` - Accuracy verification

### Finding Templates

**All templates:** `study-guides/templates-and-examples/`
- `Excel_Drugs_Chart_11-1_REVISED.txt` - Excel drug chart template
- `Excel_Master_Chart_Only_REVISED.txt` - Excel master chart template
- `Word_LO_11-5_REVISED.txt` - Word LO template
- `HTML_LO_REVISED.txt` - HTML LO template
- `Clinical_Physical_Assessment_REVISED.txt` - Clinical template
- `Autobiography_Drug_Stories_REVISED.txt` - Biography template
- `Python_Examples/` - Python generation scripts

### Finding Documentation

**User Guides:**
- `study-guides/user-docs/START_HERE.md` - Getting started
- `study-guides/user-docs/HOW_TO_USE.md` - Detailed usage guide
- `study-guides/user-docs/MAINTENANCE.md` - Maintenance procedures

**Command Reference:**
- `SLASH_COMMANDS_REFERENCE.md` - Complete command documentation
- `QUICK_START.md` - Quick reference with examples

## When Working in Subdirectories

Each subdirectory may have its own CLAUDE.md with project-specific rules that supplement these global settings.

**Hierarchy:**
1. **Global CLAUDE.md** (this file) - applies everywhere
2. **Subdirectory CLAUDE.md** (e.g., in study-guides/) - supplements global rules
3. **README.md files** - documentation, not instructions

When working in a subdirectory, Claude loads both the global settings and the subdirectory-specific CLAUDE.md automatically.
