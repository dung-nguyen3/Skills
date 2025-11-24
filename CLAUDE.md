# Skills Repository - Global Settings

This repository contains Claude Code infrastructure examples and study guide materials.

## Personal Context

- I'm a pharmacy student learning to use Claude Code
- I use VS Code with Claude Code extension as my primary environment
- Explain technical concepts clearly - I'm learning

## General Rules

### File Management
- Never create files in home directory (use project directories)
- Always use absolute paths, not relative paths
- Ask before creating new files unless explicitly required

### Communication Style
- No emojis unless explicitly requested
- Concise, clear explanations
- Technical accuracy over validation

## Repository Architecture

**`infrastructure-examples/`**
- Examples of skills, hooks, commands, and agents
- Reference material for creating Claude Code automation
- Study these before building new skills/hooks

**`study-guides/`**
- Study guide materials
- Has its own CLAUDE.md with detailed study guide protocols
- **Purpose:** Create pharmacy study guides from source materials

### Supporting Directories

**`Example claude study guides/`** (43 files)
- 12 subdirectories with completed study guide examples
- Reference for various output formats (HTML, Excel, Word, PDF)
- Template instructions and real examples

**`Py for Claude/`** (5 files)
- Python utilities for study guide generation
- Template generators for Excel, HTML, and Word formats

**`Study Templates auto/`** (6 files)
- Template and example documents
- Text-based template instructions

**Root Documentation** (9 markdown files)
- CLAUDE_INFRASTRUCTURE_ANALYSIS.md (1,307 lines - comprehensive technical analysis)
- QUICK_REFERENCE_GUIDE.md (350 lines - quick lookup)
- INFRASTRUCTURE_ANALYSIS_INDEX.md (navigation guide)
- GIT_WORKFLOW.md (git operations protocol)
- TEMPLATE_TYPES.md (study guide template reference)
- Other planning and analysis documents

## Git Operations Protocol

### CRITICAL: Branch Naming Requirements

**Format:** `claude/claude-md-{session-id}-{unique-id}`

**Example:** `claude/claude-md-mi7tfcycz4m95d0u-01Qu3uxnpnhuQf82Kr6iE6YS`

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

**Example with retry:**
```bash
# First attempt
git push -u origin claude/claude-md-example

# If fails, wait 2s and retry
# If fails, wait 4s and retry
# If fails, wait 8s and retry
# If fails, wait 16s and retry (final attempt)
```

## Navigation Guide

### Finding Infrastructure Components

**Skills:** `.claude/skills/`
- Root level: `skill-rules.json` for study guide verification triggers

**Hooks:** `.claude/hooks/*.sh`
- Study guide verification hooks (pre/post creation, session end)
- Quality gates for source-only policy

**Commands:** `.claude/commands/*.md`
- Study guide commands: `/excel`, `/word`, `/html`, `/clinical`, `/anki`, `/biography`, `/lo-guide`
- Verification: `/verify-accuracy`

### Finding Templates and Examples

**Study Guide Templates:**
- `study-guides/templates-and-examples/` - Complete templates and examples

**Study Guide Examples:**
- `Example claude study guides/` - 12 subdirectories organized by format
- Shows HTML, Excel, Word, PDF outputs

**Python Generators:**
- `Py for Claude/` - Automated template generators

### Finding Documentation

**Comprehensive Analysis:**
- `CLAUDE_INFRASTRUCTURE_ANALYSIS.md` - Deep technical dive (1,307 lines)
- Covers: skills, hooks, agents, patterns, integration, troubleshooting

**Quick Reference:**
- `QUICK_REFERENCE_GUIDE.md` - Fast lookup (350 lines)
- Copy-paste configurations, troubleshooting, common patterns

**Specific Protocols:**
- `GIT_WORKFLOW.md` - Clone, pull, push procedures
- `TEMPLATE_TYPES.md` - 4 study guide template types
- `study-guides/HOW_TO_USE.md` - User guide for study system
- `study-guides/MAINTENANCE.md` - Maintenance procedures

**`analysis-docs/`**
- Analysis and planning documents
- Template improvement documentation
- Historical record of decisions and changes

**`scripts/`**
- Standalone utility scripts
- One-off automation tools

## When Working in Subdirectories

Each subdirectory may have its own CLAUDE.md with project-specific rules that supplement these global settings.

**Hierarchy:**
1. **Global CLAUDE.md** (this file) - applies everywhere
2. **Subdirectory CLAUDE.md** (e.g., in study-guides/) - supplements global rules
3. **README.md files** - documentation, not instructions

When working in a subdirectory, Claude loads both the global settings and the subdirectory-specific CLAUDE.md automatically.
