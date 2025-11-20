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

This repository contains **two sophisticated systems** plus supporting materials (197 files across 6 major directories).

### Two Main Systems

**`claude-infrastructure-showcase/`** (68 files)
- Production-tested Claude Code reference library
- 5 skills, 10 agents, 3 slash commands, 6+ hooks
- Auto-activation breakthrough (UserPromptSubmit + skill-rules.json)
- Progressive disclosure pattern (500-line rule)
- 6 months real-world testing on complex TypeScript projects
- **Purpose:** Copy patterns into your own Claude Code projects

**`Copy Study Guide Claude Q3 2/`** (68 files)
- Medical study guide automation system (5-phase implementation complete)
- 3 skills, 2 agents, 6 slash commands, 12+ hooks
- Source-only enforcement + mandatory verification workflows
- Multi-format output: Word, Excel, HTML
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

**Skills:** `.claude/skills/*/SKILL.md`
- Infrastructure showcase: `claude-infrastructure-showcase/.claude/skills/`
- Study guide system: `Copy Study Guide Claude Q3 2/.claude/skills/`

**Agents:** `.claude/agents/*.md`
- Infrastructure showcase: 10 general-purpose agents
- Study guide system: 2 medical-specific agents

**Hooks:** `.claude/hooks/*.sh` or `.claude/hooks/*.ts`
- Essential hooks in both systems (auto-activation, tracking)
- Study guide system has additional quality gates

**Commands:** `.claude/commands/*.md`
- Infrastructure showcase: 3 dev documentation commands
- Study guide system: 6 study guide creation commands

### Finding Templates and Examples

**Study Guide Templates:**
- `Study Templates auto/` - Text-based template instructions
- `Copy Study Guide Claude Q3 2/templates-and-examples/` - Complete templates

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
- `Copy Study Guide Claude Q3 2/HOW_TO_USE.md` - User guide for study system
- `Copy Study Guide Claude Q3 2/MAINTENANCE.md` - Maintenance procedures

## When Working in Subdirectories

Each subdirectory may have its own CLAUDE.md with project-specific rules that supplement these global settings.

**Hierarchy:**
1. **Global CLAUDE.md** (this file) - applies everywhere
2. **Subdirectory CLAUDE.md** (e.g., in Copy Study Guide Claude Q3 2/) - supplements global rules
3. **README.md files** - documentation, not instructions

When working in a subdirectory, Claude loads both the global settings and the subdirectory-specific CLAUDE.md automatically.
