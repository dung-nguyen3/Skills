# Pharmacy Study Guide Automation

Automated study guide creation system with quality verification for pharmacy school.

## Quick Start

**Create a study guide:**
```
/create-word [source.txt]
/create-excel [source.txt]
```

**Verify accuracy:**
```
/verify-accuracy
```

## What This Does

Creates comprehensive study guides from source material with:
- **Source-only enforcement:** Prevents AI hallucinations by requiring verification against source files
- **Automatic quality gates:** Hooks block creation without verification
- **Multiple formats:** Word documents, Excel charts, HTML pages
- **Session-based tracking:** Tracks what was created and verified per session

## Directory Structure

- `.claude/` - Claude Code configuration (hooks, skills, commands, settings)
- `study-guides/` - Generated study guides organized by session
- `sources/` - Source material (lecture notes, PDFs, transcripts)
- `templates/` - Word/Excel/HTML templates for study guides

## Key Features

### Phase 1: Foundation
- Source-only enforcement skill
- Study guide verifier skill
- Slash commands for creating Word/Excel guides

### Phase 2: Quality Gates
- PreToolUse hook blocks creation without verification
- PostToolUse hook reminds to verify after creation
- Stop hook validates work at session end
- SessionStart hook displays requirements

### Phase 3: Reliability
- Error resilience (jq dependency checks, fallback session IDs)
- Environment variable overrides (`SKIP_STUDY_GUIDE_VERIFICATION=1`)
- Native SKILL.md files for better activation rates
- TypeScript support for hooks

## Documentation

- **[HOW_TO_USE.md](HOW_TO_USE.md)** - Complete user guide for creating and verifying study guides
- **[MAINTENANCE.md](MAINTENANCE.md)** - Maintenance and customization guide
- **[CLAUDE.md](CLAUDE.md)** - Project-specific rules and protocols for Claude

## Emergency Override

If verification hooks cause issues:

```bash
export SKIP_STUDY_GUIDE_VERIFICATION=1
```

## Infrastructure Status

- ✅ Phase 1: Foundation infrastructure (completed)
- ✅ Phase 2: Quality gate hooks (completed)
- ✅ Phase 3: Reliability improvements (completed)
