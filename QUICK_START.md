# Skills Repository - Quick Start Guide

**Welcome!** This file auto-opens when you launch the workspace.

---

## Table of Contents (Click to Jump)

### Quick Reference
- [Slash Commands Cheat Sheet](#slash-commands-cheat-sheet)
- [When to Use What](#when-to-use-what)
- [Keyboard Shortcuts](#keyboard-shortcuts)

### Study Guides
- [Create Study Guide (3 Steps)](#create-study-guide-3-steps)
- [Verify Study Guide (2 Steps)](#verify-study-guide-2-steps)
- [Create Anki Flashcards](#create-anki-flashcards)
- [Study Guide Decision Tree](#study-guide-decision-tree)

### Infrastructure
- [Skills - What Auto-Activates](#skills---what-auto-activates)
- [Hooks - What Runs Automatically](#hooks---what-runs-automatically)
- [Agents - When to Invoke](#agents---when-to-invoke)

### Documentation
- [Full Documentation Links](#full-documentation-links)
- [Troubleshooting](#troubleshooting)

---

## Slash Commands Cheat Sheet

### Study Guides (Copy & Paste)

```bash
# Word Study Guide
/LO-word "path/to/lecture.txt"

# Excel Drug Chart
/4-tab-excel "path/to/drugs.txt"

# HTML Learning Objectives (any medical topic)
/LO-html "path/to/lecture.txt"

# HTML Drug Reference (mobile-friendly)
/drugs-html "path/to/drugs.txt"

# Clinical Assessment Guide
/clinical-assessment-html "path/to/source.txt" "Chief Complaint"

# Anki Flashcards
/anki "path/to/lecture.txt"

# Verify Accuracy
/verify-accuracy "path/to/study-guide.xlsx" "path/to/source.txt"
```

### Infrastructure (Copy & Paste)

```bash
# Plan complex development task
/dev-docs "describe your task here"

# Update docs before session ends
/dev-docs-update "task name"

# Research API routes
/route-research-for-testing
```

---

## When to Use What

### Study Guide Decision Tree

**START HERE:**
1. **Is it about drugs?** → YES: Go to #2 | NO: Go to #4
2. **Do you want Excel or HTML?**
   - Excel (comprehensive tables): `/4-tab-excel`
   - HTML (mobile reference): `/drugs-html`
3. **DONE!**

4. **Is it about clinical exams (history & physical)?** → YES: `/clinical-assessment-html` | NO: Go to #5
5. **Do you need Word format?** → YES: `/LO-word` | NO: Go to #6
6. **Use:** `/LO-html` (works for ANY medical topic)

### Quick Reference Table

| I Have... | Use This Command |
|-----------|------------------|
| Drug lecture notes | `/4-tab-excel` OR `/drugs-html` |
| Non-drug lecture with LOs | `/LO-html` |
| Clinical exam notes | `/clinical-assessment-html` |
| Need Word format | `/LO-word` |
| Need Anki flashcards | `/anki` |
| Existing study guide to check | `/verify-accuracy` |

---

## Create Study Guide (3 Steps)

### Step 1: Prepare Your Source File
- Extract lecture notes to `.txt` file
- Location: `[Class]/[Exam]/Extract/[Lecture].txt`

### Step 2: Run Slash Command
```bash
/4-tab-excel "Pharmacology/Exam 3/Extract/HIV Drugs.txt"
```
**On Mac:** Press `Cmd + V` to paste the command

### Step 3: Review Output
- Saves to: `[Class]/[Exam]/Claude Study Tools/`
- Claude automatically:
  - States verification checklist
  - Reads entire source
  - Researches mnemonics via web
  - Creates study guide
  - Runs post-verification

**That's it!** No manual steps needed.

---

## Verify Study Guide (2 Steps)

### Step 1: Run Verification
```bash
/verify-accuracy "Study Tools/Guide.xlsx" "Extract/Source.txt"
```

### Step 2: Review Report
Claude will:
- Find all issues (Critical/Important/Minor)
- Fix everything automatically
- Re-verify the file
- State "Re-verification complete"

**Use before exams** to ensure 100% accuracy!

---

## Create Anki Flashcards

### Basic Usage
```bash
/anki "Pharmacology/Exam 3/Extract/HIV Drugs.txt"
```

### Auto-Import Feature (Optional)

**Enable auto-import** to skip manual File → Import steps:

**1. Create/edit** `.claude/settings.local.json`:
```json
{
  "anki_auto_import": {
    "enabled": true
  }
}
```

**2. Requirements:**
- Anki must be running
- AnkiConnect add-on installed (code: `2055492159`)
- Run: `pip install requests`

**3. Use:**
```bash
/anki "path/to/lecture.txt"
# Deck automatically imports into Anki!
```

**See:** [ANKI_AUTO_IMPORT.md](study-guides/user-docs/ANKI_AUTO_IMPORT.md) for setup and troubleshooting

---

## Skills - What Auto-Activates

**You don't manually trigger skills** - they activate automatically based on what you say.

| Skill Name | Activates When You Say | What It Does |
|------------|------------------------|--------------|
| **source-only-enforcer** | "create excel", "create study guide" | Forces verification checklist before creation |
| **mnemonic-researcher** | "find mnemonic", "help remember" | Reminds Claude to WebSearch (not invent) mnemonics |
| **study-guide-verifier** | "verify", "check accuracy" | Runs 6-step verification protocol |
| **template-compliance** | "format", "colors", "template" | Ensures template compliance |
| **drug-classification** | "drug class", "MOA", "first-line" | Helps verify drug-specific vs class-wide info |

**Skills Priority:**
- CRITICAL: source-only-enforcer, study-guide-verifier (must run)
- HIGH: mnemonic-researcher, template-compliance (should run)
- MEDIUM: drug-classification (nice to have)

**What you do:** Nothing! Just make your request normally.

---

## Hooks - What Runs Automatically

**Hooks run in the background** - you never see them.

### Before Creating Study Guide
**verification-guard.sh** (Pre-creation gate)
- Checks if verification checklist was stated
- BLOCKS file creation if not verified
- Ensures source-only policy enforced

### After Creating Study Guide
**post-verification-trigger.sh** (Post-creation reminder)
- Reminds Claude to verify the file
- Shows 4 required verification checks
- Suggests `/verify-accuracy` for deep analysis

### When Session Ends
**verification-completion-check.sh** (Stop hook)
- Checks if verification was completed
- Warns about unverified files
- Lists files needing verification

**What you do:** Nothing! Hooks enforce quality automatically.

---

## Agents - When to Invoke

**Agents are optional** - use them for complex analysis.

### medical-mnemonic-researcher
**You say:** "Find mnemonics for [topic]"
**Agent does:**
- WebSearches 5-10 query variations
- Finds top 3 established mnemonics
- Provides sources and reliability scores
- Returns in 30-60 seconds

**Use when:** Creating study guide (auto-invoked) or researching mnemonics separately

### study-guide-analyzer
**You say:** "Verify accuracy of [filename]"
**Agent does:**
- 6-step systematic verification
- Documents all issues with severity
- Saves analysis report to file
- Returns summary with recommendations

**Use when:** Verifying existing study guide, before exams, after manual edits

**Agents vs Commands:**
- Commands: Simple, direct tasks
- Agents: Complex multi-step analysis

---

## Keyboard Shortcuts

### Mac Shortcuts

| Action | Shortcut |
|--------|----------|
| Command Palette | `Cmd + Shift + P` |
| Quick File Open | `Cmd + P` |
| Search Files | `Cmd + Shift + F` |
| Terminal | `Ctrl + ~` |
| Split Editor | `Cmd + \` |
| Close Editor | `Cmd + W` |

### Useful Commands via Palette (Cmd+Shift+P)

Type these in Command Palette:
- `Markdown: Open Preview` - Preview this file
- `Snippets: Insert Snippet` - Insert slash command
- `File: Open Recent` - Recent workspaces
- `Preferences: Open Workspace Settings` - Edit workspace config

---

## Full Documentation Links

**Essential Reading:**
- [Slash Commands Reference](SLASH_COMMANDS_REFERENCE.md) - All 9 commands detailed
- [Study Guide How-To](study-guides/user-docs/HOW_TO_USE.md) - Complete usage guide
- [Study Guide System](study-guides/README.md) - System overview

**Infrastructure:**
- Skills: `.claude/skills/`
- Hooks: `.claude/hooks/`
- Commands: `.claude/commands/`

**Templates:**
- All templates: `study-guides/templates-and-examples/`

---

## Troubleshooting

### Slash Command Not Working?

**Check 1:** Did you include the slash?
```bash
# ✓ Correct
/4-tab-excel path.txt

# ✗ Wrong
4-tab-excel path.txt
```

**Check 2:** Does the file exist?
```bash
ls "path/to/source.txt"
```

**Check 3:** Did you quote paths with spaces?
```bash
# ✓ Correct
/LO-word "Clinical Medicine/Exam 1/Lecture.txt"

# ✗ Wrong
/LO-word Clinical Medicine/Exam 1/Lecture.txt
```

### Skills Not Activating?

**Solution:** Start a new Claude Code session
- Skills activate at session start
- Check: `.claude/settings.json` exists
- Check: `.claude/skills/skill-rules.json` exists

### Claude Not Following Template?

**Solution:** Always use slash commands
- Commands automatically load templates
- Direct requests might skip template loading
- Slash commands guarantee compliance

### Need Help?

1. **Command Palette** (`Cmd+Shift+P`) → Type "Claude"
2. **Read full docs** in links above
3. **Check settings**: `.claude/settings.json`

---

## Tips for Success

### 1. Always Use Slash Commands
- Saves ~700-1,100 lines of context
- Guarantees template compliance
- Ensures verification runs

### 2. Organize Your Files
```
Pharmacology/
  Exam 3/
    Extract/           # Your source files
    Claude Study Tools/  # Generated files (auto-created)
```

### 3. Verify Before Exams
```bash
# 1 day before exam
/verify-accuracy "Study Tools/Topic1.xlsx" "Extract/Topic1.txt"
/verify-accuracy "Study Tools/Topic2.docx" "Extract/Topic2.txt"
```

### 4. Let Claude Research Mnemonics
- Don't ask manually for mnemonics
- Slash commands auto-research them
- WebSearch finds established mnemonics only

### 5. Create Multiple Guides Per Session
- First guide: Full overhead (~1,500 lines)
- Second guide: Minimal overhead (~600 lines)
- Skills already loaded, no re-trigger

---

## Quick Action Checklist

**Before Creating Study Guide:**
- [ ] Extract lecture to `.txt` file
- [ ] Note file path
- [ ] Choose correct slash command

**During Creation:**
- [ ] Nothing! Claude handles everything

**After Creation:**
- [ ] Review output file
- [ ] (Optional) Run `/verify-accuracy` before exam

**That's it!** The infrastructure handles all quality checks automatically.

---

## Navigation Tips

**Table of Contents Navigation:**
- Click any link above to jump to that section
- Use `Cmd + Click` to open in new editor
- Press `Ctrl + -` to go back

**Search This File:**
- Press `Cmd + F` to search
- Type keyword (e.g., "excel", "verify", "skills")
- Press Enter to jump to matches

**Markdown Preview:**
- Press `Cmd + Shift + V` to preview this file
- Or: `Cmd + K` then `V` for side-by-side

---

**Last Updated:** 2025-11-19
**Quick Start Version:** 1.0

---

**Ready to create your first study guide?** Copy a slash command from [Slash Commands Cheat Sheet](#slash-commands-cheat-sheet) and paste it into Claude!
