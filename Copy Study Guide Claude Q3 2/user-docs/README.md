# User Documentation

This folder contains all documentation for **using** the study guide creation system.

---

## Quick Start

**New user? Start here:**
1. **[START_HERE.md](START_HERE.md)** ⭐ - 3-step quick start guide (read this first!)
2. **[HOW_TO_USE.md](HOW_TO_USE.md)** - Complete guide with all features
3. **[MAINTENANCE.md](MAINTENANCE.md)** - Customization and troubleshooting

---

## Documentation Files

### START_HERE.md ⭐
**3-step quick start guide**

**What's inside:**
- What the system does
- 3-step quick start
- Format selection guide
- Common questions
- Support resources

**Who it's for:** First-time users who need to create their first study guide

**Read this first!**

---

### HOW_TO_USE.md
**Complete user guide for creating and verifying study guides**

**What's inside:**
- Quick start guide
- Template overview (Excel Drug Chart, HTML LO Guide, Clinical Assessment, Word LO)
- Slash commands reference (/create-excel, /create-word, etc.)
- Source-only enforcement explanation
- Post-creation verification steps
- Using specialized agents (mnemonic-researcher, study-guide-analyzer)
- Troubleshooting guide

**Who it's for:** Anyone creating study guides with Claude Code

---

### MAINTENANCE.md
**Maintenance, customization, and troubleshooting guide**

**What's inside:**
- File structure overview
- Template customization
- Skill activation patterns
- Hook system details
- Emergency overrides
- Common issues and solutions
- Analytics and usage tracking

**Who it's for:** Users who need to customize the system or fix issues

---

## Where to Find Other Documentation

**Templates and Examples:**
- See `../templates-and-examples/` for actual template files and examples

**Technical/Infrastructure Documentation:**
- See repository root for implementation docs:
  - `PHASE_5_COMPLETION.md` - Latest infrastructure status
  - `COMPREHENSIVE_INFRASTRUCTURE_ANALYSIS.md` - Research and analysis
  - `CLAUDE.md` - Instructions for Claude Code (not for users)

**Infrastructure Code:**
- See `.claude/` directory for skills, agents, hooks, and scripts

---

## Support

**If you need help:**

1. **Check HOW_TO_USE.md** - Covers most common questions
2. **Check MAINTENANCE.md** - Troubleshooting section
3. **Emergency override** - If hooks are blocking you:
   ```bash
   export SKIP_STUDY_GUIDE_VERIFICATION=1
   ```

---

**Last Updated:** 2025-11-19 (Phase 5 completion)
