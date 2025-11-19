# Medical Study Guide Automation

Automated study guide creation system with quality verification for **ALL medical specialties**: pharmacology, pathophysiology, clinical medicine, physical examination, and procedures.

## Quick Start

**Create a study guide** (choose based on content type):
```
/create-excel [source.txt]           # Pharmacology - 4-tab drug chart
/create-drug-html [source.txt]       # Pharmacology - interactive HTML
/create-lo-guide [source.txt]        # Any medical topic with LOs
/create-clinical-guide [source.txt]  # History & physical exam
/create-word [source.txt]            # Word format (any topic)
```

**Verify accuracy:**
```
/verify-accuracy [study-guide] [source]
```

## What This Does

Creates comprehensive study guides from source material with:
- **Source-only enforcement:** Prevents AI hallucinations by requiring verification against source files
- **Automatic quality gates:** Hooks block creation without verification
- **Multiple formats:** Word documents, Excel charts, HTML pages
- **Session-based tracking:** Tracks what was created and verified per session

## Directory Structure

**For Users:**
- **`user-docs/`** - Complete usage and maintenance documentation
  - `HOW_TO_USE.md` - How to create and verify study guides
  - `MAINTENANCE.md` - Customization and troubleshooting
- **`templates-and-examples/`** - Template files and example study guides
  - Template instructions (.txt)
  - Example study guides (.xlsx, .html)
  - Template code (.py)

**Infrastructure (Advanced):**
- **`infrastructure-docs/`** - Technical documentation for developers
  - Phase implementation details
  - Research and design decisions
  - Infrastructure extension guides
- **`.claude/`** - Claude Code configuration
  - `skills/` - Auto-activating knowledge (with resource libraries)
  - `agents/` - Specialized agents (mnemonic-researcher, study-guide-analyzer)
  - `hooks/` - Workflow automation (quality gates, tracking)
  - `scripts/` - Batch validation tools

## Template Types

**4 different templates for different content:**
1. **Drug Chart HTML** - Interactive pharmacology reference (mobile-friendly)
2. **Excel Drug Chart** - Comprehensive 4-tab drug analysis (print-friendly)
3. **HTML Learning Objectives** - Works for ANY medical topic with LOs
4. **Clinical Assessment Guide** - History-taking and physical exam by chief complaint

## Key Features

### Phase 1: Foundation
- Source-only enforcement skill (works for all specialties)
- Study guide verifier skill (content-agnostic)
- Slash commands for all 4 template types

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

### Phase 4: Specialized Agents
- **medical-mnemonic-researcher agent** - Finds established USMLE mnemonics from medical education sources
- **study-guide-analyzer agent** - Comprehensive 6-step verification with detailed analysis reports
- Automatic agent invocation by skills
- Time savings: Mnemonic research (5-10 min → 30-60 sec), Verification (10-15 min → 1-2 min)

### Phase 5: Advanced Infrastructure (NEW!)

**Phase 5.1: Hook Ecosystem Enhancement**
- Autonomous metadata tracking (source files, template types, file sizes)
- Quality validation at session end (missing sources, small files, accuracy warnings)
- Smart recommendations and auto-suggestions
- Session-based caching across context resets

**Phase 5.2: Progressive Disclosure Resource Libraries**
- 2,800+ lines of deep-dive reference material (9 resource files)
- Scalable knowledge base with on-demand loading
- Main skills stay lightweight (<500 lines)
- Comprehensive guides: validation, hallucination prevention, examples, checklists

**Phase 5.4: Automated Quality Gates**
- Batch validation scripts for CI/CD integration
- Standalone quality checks independent of Claude Code
- Check multiple study guides at once
- Clear Pass/Fail reporting

## Documentation

**Start Here (User Docs):**
- **[user-docs/START_HERE.md](user-docs/START_HERE.md)** ⭐ - 3-step quick start guide (read this first!)
- **[user-docs/HOW_TO_USE.md](user-docs/HOW_TO_USE.md)** - Complete guide to creating and verifying study guides
- **[user-docs/MAINTENANCE.md](user-docs/MAINTENANCE.md)** - Customization and troubleshooting
- **[templates-and-examples/README.md](templates-and-examples/README.md)** - Template reference guide

**Technical/Infrastructure (Advanced):**
- **[infrastructure-docs/](infrastructure-docs/)** - Technical documentation for developers
  - [PHASE_5_COMPLETION.md](infrastructure-docs/PHASE_5_COMPLETION.md) - Latest infrastructure status and features
  - [COMPREHENSIVE_INFRASTRUCTURE_ANALYSIS.md](infrastructure-docs/COMPREHENSIVE_INFRASTRUCTURE_ANALYSIS.md) - Research and design decisions
  - [PHASE_5.1_IMPLEMENTATION.md](infrastructure-docs/PHASE_5.1_IMPLEMENTATION.md) - Hook ecosystem details
- **[CLAUDE.md](CLAUDE.md)** - Instructions for Claude Code (not for users)

## Emergency Override

If verification hooks cause issues:

```bash
export SKIP_STUDY_GUIDE_VERIFICATION=1
```

## Infrastructure Status

- ✅ Phase 1: Foundation infrastructure (completed)
- ✅ Phase 2: Quality gate hooks (completed)
- ✅ Phase 3: Reliability improvements (completed)
- ✅ Phase 4: Specialized Agents (completed)
- ✅ Phase 5: Advanced Infrastructure (completed - 5.1, 5.2, 5.4)
  - ✅ Phase 5.1: Hook Ecosystem Enhancement
  - ✅ Phase 5.2: Progressive Disclosure Resource Libraries
  - ⏸️ Phase 5.3: MCP Integration (deferred)
  - ✅ Phase 5.4: Automated Quality Gates
