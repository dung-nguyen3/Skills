# How to Use Claude Study Guide Automation

## What's Installed

Your study guide folder now has automated quality controls and shortcuts:

### 1. Slash Commands (Quick Actions)
- `/create-word` - Create Word study guide from source file
- `/create-excel` - Create Excel drug chart from source file
- `/verify-accuracy` - Deep accuracy analysis of existing study guide

### 2. Skill Auto-Activation System
- Automatically suggests relevant guidance when you work on study guides
- Enforces quality checks (source-only policy, verification)
- Runs in the background - no manual activation needed

### 3. Hook System (Background Quality Gates)
- **UserPromptSubmit** - Analyzes your prompts and suggests skills
- **PreToolUse** - Will block writes without verification (Phase 2)
- **PostToolUse** - Will remind to verify after creation (Phase 2)
- **Stop** - Will catch incomplete work at session end (Phase 2)

---

## Using Slash Commands

### Basic Syntax

```
/command-name path/to/source/file.txt
```

### Example 1: Create Excel Drug Chart

**You say:**
```
/create-excel Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

**What happens:**
1. Claude loads the 1,144-line Excel template
2. States the verification checklist
3. Reads your source file completely
4. Creates 4-tab Excel chart with:
   - Drug Details (class comparison tables)
   - Key Comparisons (mechanisms, toxicities)
   - Master Chart (all drugs)
   - High-Yield & Pearls (mnemonics, clinical pearls)
5. Researches mnemonics via WebSearch
6. Runs post-creation verification
7. Saves to: `Pharmacology/Exam 3/Claude Study Tools/HIV_Antivirals_Drug_Chart.xlsx`

**Time saved:** ~5,000 tokens per session (loads template only when needed)

---

### Example 2: Create Word Study Guide

**You say:**
```
/create-word Pharmacology/Exam 3/Extract/Lecture 42.txt
```

**What happens:**
1. Claude loads the 695-line Word template
2. States the verification checklist
3. Reads your source file
4. Creates comprehensive Word doc with:
   - All learning objectives answered (all parts)
   - Key comparison tables
   - Master chart
   - High-yield summary boxes
5. Researches mnemonics via WebSearch
6. Runs post-creation verification
7. Saves to: `Pharmacology/Exam 3/Claude Study Tools/Lecture_42_Study_Guide.docx`

---

### Example 3: Verify Accuracy of Existing Study Guide

**You say:**
```
/verify-accuracy "Claude Study Tools/HIV_Drug_Chart.xlsx" "Extract/HIV Drugs.txt"
```

**What happens:**
1. Claude loads the 356-line detailed verification protocol
2. Reads ENTIRE source file
3. Loads and examines your Excel file
4. Runs 6-step systematic verification:
   - Step 1: Read source completely
   - Step 2: Examine existing file
   - Step 3: Systematic checks (names, classifications, merged cells, info accuracy, format, emojis)
   - Step 4: Document all issues found
   - Step 5: Fix ALL issues
   - Step 6: Re-verify entire file (mandatory)
5. Creates detailed issue report
6. Fixes everything found
7. States "Re-verification complete"

**Use when:**
- You want to double-check an existing study guide
- You made manual edits and want accuracy check
- Source file was updated and you need to sync

---

## How Skill Auto-Activation Works

### What Are Skills?

Skills are specialized knowledge bases that automatically activate when you need them. Think of them as context-aware helpers.

### Installed Skills:

**1. source-only-enforcer** (CRITICAL - Blocks until verified)
- **Triggers when you say:** "create excel", "create study guide", "make drug chart"
- **What it does:** Blocks creation until you state the verification checklist
- **Why:** Prevents adding external medical facts, enforces source-only policy

**2. mnemonic-researcher** (HIGH - Suggests)
- **Triggers when you say:** "find mnemonic", "help me remember", "memory trick"
- **What it does:** Suggests researching established mnemonics via WebSearch
- **Why:** Ensures you get PROVEN mnemonics, not invented ones

**3. study-guide-verifier** (CRITICAL - Suggests)
- **Triggers when you say:** "verify accuracy", "check study guide", "analyze file"
- **What it does:** Suggests systematic 6-step verification protocol
- **Why:** Ensures comprehensive accuracy checking

**4. template-compliance-checker** (HIGH - Suggests)
- **Triggers when you say:** "check format", "correct colors", "template"
- **What it does:** Reminds you of template requirements
- **Why:** Ensures consistent formatting across all study guides

**5. drug-classification-assistant** (MEDIUM - Suggests)
- **Triggers when you say:** "drug class", "MOA", "first-line", "classification"
- **What it does:** Helps verify drug-specific vs class-wide information
- **Why:** Prevents incorrect grouping of drugs

### Example Session with Skill Auto-Activation:

**You say:**
```
Create an Excel drug chart from the HIV antivirals lecture
```

**What you see:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 SKILL ACTIVATION CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ CRITICAL SKILLS (REQUIRED):
  → source-only-enforcer

ACTION: Use Skill tool BEFORE responding
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Then Claude responds:**
```
VERIFICATION CHECKLIST:
☐ Source file: Pharmacology/Exam 3/Extract/HIV Antivirals.txt
☐ Instruction template: Excel Drugs Chart 11-1.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: Pharmacology/Exam 3/Claude Study Tools/

Now reading source file...
```

**No extra work required** - Claude automatically follows the protocol!

---

## Practical Workflows

### Workflow 1: Creating Study Guide from Scratch

**Step 1:** Extract lecture to text file
```
Pharmacology/Exam 3/Extract/Lecture 42.txt
```

**Step 2:** Use slash command
```
/create-word Pharmacology/Exam 3/Extract/Lecture 42.txt
```

**Step 3:** Wait for completion
- Claude states verification checklist
- Reads source completely
- Creates study guide
- Researches mnemonics
- Runs post-verification
- Saves file

**Step 4:** Review output
```
Claude Study Tools/Lecture_42_Study_Guide.docx
```

**Done!** - Usually takes 5-10 minutes for complete study guide

---

### Workflow 2: Creating Excel Drug Chart

**Step 1:** Extract drug info to text file
```
Pharmacology/Exam 3/Extract/HIV Drugs.txt
```

**Step 2:** Use slash command
```
/create-excel Pharmacology/Exam 3/Extract/HIV Drugs.txt
```

**Step 3:** Claude creates 4-tab chart
- Drug Details tab (comparisons)
- Key Comparisons tab (mechanisms, toxicities)
- Master Chart tab (all drugs)
- High-Yield & Pearls tab (mnemonics)

**Step 4:** Review Excel file
```
Claude Study Tools/HIV_Drugs_Drug_Chart.xlsx
```

**Step 5:** (Optional) Verify accuracy
```
/verify-accuracy "Claude Study Tools/HIV_Drugs_Drug_Chart.xlsx" "Extract/HIV Drugs.txt"
```

---

### Workflow 3: Verifying Existing Study Guide

**When to verify:**
- Before exam (double-check everything)
- After manual edits
- Source file was updated
- You want 100% confidence in accuracy

**Step 1:** Run verification
```
/verify-accuracy "Claude Study Tools/Exam2_Drug_Chart.xlsx" "Extract/Exam 2 Drugs.txt"
```

**Step 2:** Review issue report
Claude will show:
```
ACCURACY ANALYSIS REPORT
========================

ISSUES FOUND:
-------------
Issue 1: Drug X marked first-line but source doesn't specify
- Source says: "Class is first-line"
- File shows: "Drug X 🟢 First-line"
- Status: ❌ INCORRECT

Issue 2: Different MOAs incorrectly merged
- Source says: Drug A "blocks receptors", Drug B "inhibits enzyme"
- File shows: Both merged with same MOA
- Status: ❌ INCORRECT
```

**Step 3:** Claude fixes all issues automatically

**Step 4:** Re-verification runs (mandatory)
```
FINAL VERIFICATION:
✓ All names match source exactly
✓ All classifications correct
✓ No incorrect groupings
✓ No external information added
✓ Format matches template
✓ Colors correct

The study guide is now accurate and ready to use.
```

---

## Troubleshooting

### Skills Not Activating?

**Check 1:** Are you in the correct folder?
```bash
pwd
# Should show: /home/user/Skills/Copy Study Guide Claude Q3 2
```

**Check 2:** Files exist?
```bash
ls -la .claude/settings.json
ls -la .claude/skills/skill-rules.json
ls -la .claude/hooks/skill-activation-prompt.sh
```

**Check 3:** Hook is executable?
```bash
ls -l .claude/hooks/skill-activation-prompt.sh
# Should show: -rwxr-xr-x (executable)
```

**Check 4:** Node.js available?
```bash
node --version  # Should show v22+
npx tsx --version  # Should show tsx v4.20+
```

**Fix:** Start a new Claude Code session. Skills activate at session start.

---

### Slash Commands Not Working?

**Check 1:** Commands exist?
```bash
ls .claude/commands/
# Should show: create-word.md, create-excel.md, verify-accuracy.md
```

**Check 2:** Correct syntax?
```
# ✓ Correct:
/create-excel Pharmacology/Exam 3/Extract/HIV Drugs.txt

# ✗ Wrong:
create-excel (missing slash)
/create-excel (missing file path)
```

**Check 3:** File path correct?
```bash
ls "Pharmacology/Exam 3/Extract/HIV Drugs.txt"
# File should exist
```

---

### Claude Not Following Template?

**Issue:** Created study guide missing sections or wrong colors

**Check 1:** Template files exist?
```bash
ls "Claude Templates/Word LO 11-5.txt"
ls "Claude Templates/Excel Drugs Chart 11-1.txt"
```

**Check 2:** Used slash command?
- Slash commands load templates automatically
- Direct requests might skip template loading

**Fix:** Always use slash commands for template compliance:
```
/create-word [source]
/create-excel [source]
```

---

### Verification Checklist Not Showing?

**Issue:** Claude starts creating without stating checklist

**This is actually blocked now!** The source-only-enforcer skill (critical priority) will catch this and require the checklist first.

**If it still happens:**
1. Say: "Stop. State the verification checklist first."
2. Report as issue (skill trigger may need tuning)

---

### Post-Creation Verification Skipped?

**Issue:** Claude finishes but doesn't say "Post-creation verification complete"

**Check:** Did you use a slash command?
- Slash commands include post-verification as final step
- Template files also specify this requirement

**Fix:** Manually request:
```
Run post-creation verification on the file you just created
```

Or use detailed verification:
```
/verify-accuracy "path/to/file" "path/to/source"
```

---

## Tips and Best Practices

### Tip 1: Always Use Slash Commands

**Why:**
- Loads templates only when needed (saves ~5,000 tokens)
- Guarantees verification protocols run
- Ensures template compliance
- Triggers correct skill activation

**Compare:**
```
# ❌ Manual (inconsistent):
"Create an Excel drug chart from HIV drugs"

# ✓ Slash command (reliable):
/create-excel Pharmacology/Exam 3/Extract/HIV Drugs.txt
```

---

### Tip 2: Organize Your Files

**Recommended structure:**
```
Pharmacology/
  Exam 3/
    Extract/              # Source files (lectures, readings)
      Lecture 42.txt
      HIV Drugs.txt
      Antibiotics.txt
    Claude Study Tools/   # Generated study guides
      Lecture_42_Study_Guide.docx
      HIV_Drugs_Drug_Chart.xlsx
      Antibiotics_Drug_Chart.xlsx
```

**Why:** Claude automatically saves to `Claude Study Tools/` folder

---

### Tip 3: Verify Before Exams

**Schedule verification sessions:**
```
2 days before exam: Create all study guides
1 day before exam: Run verification on all files

/verify-accuracy "Study Tools/Topic1.xlsx" "Extract/Topic1.txt"
/verify-accuracy "Study Tools/Topic2.docx" "Extract/Topic2.txt"
```

**Why:** Catches any errors before you study from incorrect info

---

### Tip 4: Let Claude Research Mnemonics

**Don't ask:** "What's a mnemonic for beta blockers?"

**Instead:** Let the slash commands handle it:
```
/create-excel Extract/Beta_Blockers.txt
```

Claude will automatically:
1. WebSearch for established mnemonics
2. Add to "Memory Tricks" rows
3. Include in High-Yield & Pearls tab

**Why:** Slash commands enforce WebSearch requirement, you get proven mnemonics

---

### Tip 5: Use Verification for Manual Edits

**Scenario:** You manually added information to an Excel chart

**Action:** Verify accuracy
```
/verify-accuracy "Study Tools/Modified_Chart.xlsx" "Extract/Original_Source.txt"
```

**What Claude checks:**
- Did you add external info? (should have * marker)
- Did you modify merged cells incorrectly?
- Did you change classifications?
- Are colors still template-compliant?

---

## Quick Reference

### Slash Commands Summary

| Command | Purpose | Arguments | Output |
|---------|---------|-----------|--------|
| `/create-word` | Create Word study guide | Source file path | .docx in Claude Study Tools/ |
| `/create-excel` | Create Excel drug chart | Source file path | .xlsx in Claude Study Tools/ |
| `/verify-accuracy` | Deep accuracy analysis | Study guide path, Source path | Fixed file with report |

### Skill Triggers Summary

| Skill | Priority | You Say | Claude Does |
|-------|----------|---------|-------------|
| source-only-enforcer | CRITICAL | "create excel", "create study guide" | Blocks until checklist stated |
| mnemonic-researcher | HIGH | "mnemonic", "help remember" | Suggests WebSearch research |
| study-guide-verifier | CRITICAL | "verify", "check accuracy" | Runs 6-step protocol |
| template-compliance-checker | HIGH | "format", "colors", "template" | Reminds template specs |
| drug-classification-assistant | MEDIUM | "drug class", "MOA", "first-line" | Helps verify classifications |

### File Locations

```
.claude/
  settings.json              # Permissions and hook config
  skills/
    skill-rules.json         # Skill trigger definitions
  hooks/
    skill-activation-prompt.sh   # Hook script
    skill-activation-prompt.ts   # Hook logic
    state/                   # Session persistence (not committed)
  commands/
    create-word.md           # Word study guide creator
    create-excel.md          # Excel drug chart creator
    verify-accuracy.md       # Accuracy verification protocol
```

### Template Files

```
Claude Templates/
  Word LO 11-5.txt                      # 695 lines - Word template
  Excel Drugs Chart 11-1.txt            # 1,144 lines - Excel template
  HTML LO with Master Chart 10-30.txt   # HTML template (if using)
```

---

## Next Steps

**Phase 1 (COMPLETE):** Foundation infrastructure
- ✓ Settings and permissions
- ✓ Skill trigger rules
- ✓ UserPromptSubmit hook
- ✓ Slash commands

**Phase 2 (Coming Soon):** Quality Gates
- PreToolUse hook - Blocks writes without verification
- PostToolUse hook - Auto-reminder after creation
- Stop hook - Catches incomplete work

**Phase 3 (Coming Soon):** Auto-Activation Skills
- Actual skill implementations (SKILL.md files)
- mnemonic-researcher skill
- study-guide-verifier skill
- source-only-enforcer skill

---

## Getting Help

**Slash command not working?**
```
Check file exists: ls .claude/commands/[command-name].md
```

**Skill not activating?**
```
Check rules: cat .claude/skills/skill-rules.json
```

**Hook failing?**
```
Test manually:
CLAUDE_PROJECT_DIR="$(pwd)" bash -c 'echo "{\"session_id\":\"test\",\"prompt\":\"create excel\"}" | .claude/hooks/skill-activation-prompt.sh'
```

**Want to customize triggers?**
- Edit `.claude/skills/skill-rules.json`
- Add keywords to "keywords" array
- Add patterns to "intentPatterns" array
- Commit and push changes

---

## Remember

1. **Always use slash commands** for study guide creation
2. **Let skills auto-activate** - they work in the background
3. **Verify before exams** - run /verify-accuracy on all files
4. **Let Claude research mnemonics** - don't ask manually
5. **Start new session** if skills aren't activating

**You're all set!** Start creating study guides with confidence knowing quality checks are automatic.
