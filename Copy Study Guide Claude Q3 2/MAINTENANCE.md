# Maintenance & Customization Guide

This guide covers how to customize, modify, and maintain your Claude Code study guide automation system.

---

## Table of Contents

1. [Renaming or Moving Files](#renaming-or-moving-files)
2. [Creating New Slash Commands](#creating-new-slash-commands)
3. [Modifying Skill Triggers](#modifying-skill-triggers)
4. [Adding New Skills](#adding-new-skills)
5. [Customizing Hooks](#customizing-hooks)
6. [File Structure Reference](#file-structure-reference)
7. [Common Customizations](#common-customizations)
8. [Troubleshooting](#troubleshooting)

---

## Renaming or Moving Files

### Renaming Template Files

**Scenario:** You want to rename `Excel Drugs Chart 11-1.txt` to `Excel Drugs Chart v2.txt`

**Steps:**

1. **Rename the template file:**
   ```bash
   cd "Claude Templates"
   mv "Excel Drugs Chart 11-1.txt" "Excel Drugs Chart v2.txt"
   ```

2. **Update slash command reference:**
   ```bash
   # Edit the slash command file
   open .claude/commands/create-excel.md
   ```

   Find line ~26:
   ```markdown
   - **File**: `Copy Study Guide Claude Q3 2/Claude Templates/Excel Drugs Chart 11-1.txt`
   ```

   Change to:
   ```markdown
   - **File**: `Copy Study Guide Claude Q3 2/Claude Templates/Excel Drugs Chart v2.txt`
   ```

3. **Update CLAUDE.md reference:**
   ```bash
   open CLAUDE.md
   ```

   Find line ~8:
   ```markdown
   - **Excel**: `Claude Templates/Excel Drugs Chart 11-1.txt` - 4-tab drug charts
   ```

   Change to:
   ```markdown
   - **Excel**: `Claude Templates/Excel Drugs Chart v2.txt` - 4-tab drug charts
   ```

4. **Update HOW_TO_USE.md:**
   - Update any references to the old filename
   - Check "File Locations" and "Template Files" sections

5. **Test the slash command:**
   ```
   /create-excel path/to/test/file.txt
   ```

---

### Moving Template Files

**Scenario:** You want to move templates from `Claude Templates/` to `Study Templates/`

**Steps:**

1. **Create new directory and move files:**
   ```bash
   mkdir "Study Templates"
   mv "Claude Templates"/* "Study Templates/"
   ```

2. **Update ALL slash command files:**

   **`.claude/commands/create-excel.md` (line ~26):**
   ```markdown
   - **File**: `Copy Study Guide Claude Q3 2/Study Templates/Excel Drugs Chart 11-1.txt`
   ```

   **`.claude/commands/create-word.md` (line ~24):**
   ```markdown
   - **File**: `Copy Study Guide Claude Q3 2/Study Templates/Word LO 11-5.txt`
   ```

3. **Update CLAUDE.md (lines 6-9):**
   ```markdown
   ## Templates Available
   - **Word**: `Study Templates/Word LO 11-5.txt` - Learning objectives with tables
   - **Excel**: `Study Templates/Excel Drugs Chart 11-1.txt` - 4-tab drug charts
   - **HTML**: `Study Templates/HTML LO with Master Chart 10-30.txt` - Interactive lessons
   ```

4. **Update HOW_TO_USE.md:**
   - Search and replace all instances of `Claude Templates/` with `Study Templates/`
   - Check "Template Files" section specifically

5. **Test all slash commands:**
   ```
   /create-excel test.txt
   /create-word test.txt
   ```

---

### Renaming Slash Commands

**Scenario:** You want to rename `/create-excel` to `/make-drugchart`

**Steps:**

1. **Rename the command file:**
   ```bash
   cd .claude/commands
   mv create-excel.md make-drugchart.md
   ```

2. **Update the command file header:**
   ```bash
   open .claude/commands/make-drugchart.md
   ```

   Change line 6:
   ```markdown
   Create an Excel drug chart from source file: $ARGUMENTS
   ```

   Update any internal references to the command name.

3. **Update HOW_TO_USE.md:**
   - Replace all `/create-excel` with `/make-drugchart`
   - Update Quick Reference tables
   - Update usage examples

4. **Update skill triggers (optional):**
   If you want skills to suggest the new command name:
   ```bash
   open .claude/skills/skill-rules.json
   ```

   In `source-only-enforcer` skill, add to keywords:
   ```json
   "keywords": [
     "make drugchart",
     "/make-drugchart"
   ]
   ```

5. **Test the renamed command:**
   ```
   /make-drugchart path/to/test.txt
   ```

---

## Creating New Slash Commands

### Step-by-Step: Create `/create-flashcards` Command

**Goal:** Create a new slash command that generates flashcards from a source file.

**Step 1: Create the command file**

```bash
touch .claude/commands/create-flashcards.md
```

**Step 2: Write the command structure**

```markdown
---
description: Create interactive flashcards from source material
argument-hint: Source file path (e.g., "Pharmacology/Exam 3/Extract/Lecture 42.txt")
---

Create flashcards from source file: $ARGUMENTS

## Instructions

### Step 1: Pre-Creation Verification

**MANDATORY - State this checklist FIRST:**

\`\`\`
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Output format: HTML flashcards
☐ Source-only policy: I will ONLY use information from source file
☐ Save location: [Class]/[Exam]/Claude Study Tools/
\`\`\`

### Step 2: Read Source File

- Read the complete source file: $ARGUMENTS
- Identify key concepts, definitions, drug names
- Extract Q&A pairs from learning objectives

### Step 3: Create Flashcard HTML

**Required Features:**
- Interactive flip animations
- Keyboard navigation (arrow keys)
- Progress tracking
- Shuffle mode
- Mobile responsive
- Print-friendly

### Step 4: Save File

- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Flashcards.html`
- Confirm file saved successfully

### Step 5: Post-Creation Verification

**Verify the completed file:**
1. All information from source only
2. All key concepts covered
3. Q&A pairs accurate
4. HTML works in browser
5. Mobile responsive

**CRITICAL: State "Post-creation verification complete"**

## Example Usage

\`\`\`
/create-flashcards Pharmacology/Exam 3/Extract/HIV Drugs.txt
\`\`\`

This creates interactive flashcards with all HIV drugs, mechanisms, and key facts.
```

**Step 3: Add skill trigger for auto-activation**

```bash
open .claude/skills/skill-rules.json
```

Add new skill entry:

```json
"flashcard-creator": {
  "type": "domain",
  "enforcement": "suggest",
  "priority": "high",
  "description": "Creates interactive flashcards from source material",
  "promptTriggers": {
    "keywords": [
      "flashcard",
      "flashcards",
      "create flashcards",
      "/create-flashcards",
      "flash cards",
      "study cards"
    ],
    "intentPatterns": [
      "(create|make|generate|build).*?(flashcard|flash card)",
      "flashcard.*?(from|using|with)",
      "turn.*?into flashcard"
    ]
  },
  "fileTriggers": {
    "pathPatterns": [
      "**/Extract/**/*.txt",
      "**/Claude Study Tools/**/*_Flashcards.html"
    ]
  }
}
```

**Step 4: Update HOW_TO_USE.md**

Add new section under "Slash Commands Summary":

```markdown
### Example 4: Create Flashcards

**You say:**
\`\`\`
/create-flashcards Pharmacology/Exam 3/Extract/Lecture 42.txt
\`\`\`

**What happens:**
1. Claude reads your source file
2. Extracts key concepts and Q&A pairs
3. Creates interactive HTML flashcards
4. Saves to: `Pharmacology/Exam 3/Claude Study Tools/Lecture_42_Flashcards.html`

**Features:**
- Flip animations
- Keyboard navigation
- Progress tracking
- Shuffle mode
- Works offline
```

Update Quick Reference table:

```markdown
| `/create-flashcards` | Create interactive flashcards | Source file path | .html in Claude Study Tools/ |
```

**Step 5: Test the command**

```
/create-flashcards path/to/test/file.txt
```

**Step 6: Commit and push**

```bash
git add .claude/commands/create-flashcards.md
git add .claude/skills/skill-rules.json
git add HOW_TO_USE.md
git commit -m "Add /create-flashcards slash command with skill trigger"
git push
```

---

## Modifying Skill Triggers

### Understanding Skill Triggers

Skills auto-activate based on:
- **keywords** - Exact word matches (case-insensitive)
- **intentPatterns** - Regex patterns matching user intent
- **fileTriggers** - File paths and content patterns

### Example: Add More Keywords to source-only-enforcer

**Goal:** Trigger source-only-enforcer when user says "build study guide"

**Steps:**

1. **Open skill rules:**
   ```bash
   open .claude/skills/skill-rules.json
   ```

2. **Find the skill (line ~13):**
   ```json
   "source-only-enforcer": {
     "promptTriggers": {
       "keywords": [
         "create excel",
         "create word",
         ...
       ]
     }
   }
   ```

3. **Add new keywords:**
   ```json
   "keywords": [
     "create excel",
     "create word",
     "create study guide",
     "build study guide",      ← ADD
     "generate study guide",   ← ADD
     "make study guide"        ← ADD
   ]
   ```

4. **Test the trigger:**
   Ask Claude: "build study guide from my lecture notes"

   Should see:
   ```
   ⚠️ CRITICAL SKILLS (REQUIRED):
     → source-only-enforcer
   ```

5. **Commit the change:**
   ```bash
   git add .claude/skills/skill-rules.json
   git commit -m "Add more keywords to source-only-enforcer trigger"
   git push
   ```

---

### Example: Add Intent Pattern

**Goal:** Trigger mnemonic-researcher when user says "how do I memorize this"

**Steps:**

1. **Open skill rules:**
   ```bash
   open .claude/skills/skill-rules.json
   ```

2. **Find mnemonic-researcher skill (line ~26):**
   ```json
   "mnemonic-researcher": {
     "promptTriggers": {
       "intentPatterns": [
         "(find|search|research|look up).*?(mnemonic|memory trick|analogy)",
         ...
       ]
     }
   }
   ```

3. **Add new pattern:**
   ```json
   "intentPatterns": [
     "(find|search|research|look up).*?(mnemonic|memory trick|analogy)",
     "(how to|how do I).*?(memorize|remember|recall)",  ← ADD
     "help.*?(memorize|remember) this"                 ← ADD
   ]
   ```

4. **Test:**
   Ask: "how do I memorize all these drug names"

   Should trigger mnemonic-researcher.

---

### Changing Skill Priority

**Priorities:**
- `critical` - Always trigger (blocks or requires immediate attention)
- `high` - Important, trigger for most matches
- `medium` - Moderate, trigger for clear matches
- `low` - Optional, trigger only for explicit matches

**Example: Change template-compliance-checker to critical**

```json
"template-compliance-checker": {
  "type": "domain",
  "enforcement": "suggest",
  "priority": "critical",  ← CHANGED from "high"
  "description": "..."
}
```

**Effect:** Will show under "⚠️ CRITICAL SKILLS" instead of "📚 RECOMMENDED SKILLS"

---

### Changing Enforcement Level

**Enforcement types:**
- `suggest` - Shows suggestion, doesn't block
- `block` - Requires action before proceeding (guardrail)
- `warn` - Shows warning, allows proceeding

**Example: Make mnemonic-researcher blocking**

```json
"mnemonic-researcher": {
  "type": "guardrail",           ← CHANGED from "domain"
  "enforcement": "block",         ← CHANGED from "suggest"
  "priority": "critical",         ← CHANGED from "high"
  "blockMessage": "⚠️ BLOCKED - Mnemonic Research Required\n\n📋 REQUIRED ACTION:\n1. Use WebSearch to find established mnemonics\n2. Do NOT invent mnemonics\n3. Add researched mnemonics to study guide\n\nReason: Enforce proven mnemonic usage",
  ...
}
```

**Effect:** Claude will be BLOCKED from creating study guides until mnemonics are researched.

---

## Adding New Skills

### What Are Skills?

Skills are specialized knowledge bases stored as SKILL.md files that auto-activate when triggered.

### Step-by-Step: Create `pharmacy-calculator` Skill

**Goal:** Create a skill that helps with pharmacy calculations.

**Step 1: Create skill directory**

```bash
mkdir -p .claude/skills/pharmacy-calculator
```

**Step 2: Create SKILL.md file**

```bash
touch .claude/skills/pharmacy-calculator/SKILL.md
```

**Step 3: Write the skill content**

```markdown
# Pharmacy Calculator Skill

## Purpose
Assists with common pharmacy calculations including:
- Dose calculations
- IV drip rates
- Concentration conversions
- Pediatric dosing
- Creatinine clearance

## When to Use This Skill

Use when the user needs help with:
- "calculate dose for..."
- "what's the drip rate for..."
- "convert mg to mcg..."
- "pediatric dose for..."

## Calculation Formulas

### Dose Calculations

**Basic Dose:**
\`\`\`
Dose = Weight (kg) × Dose per kg
\`\`\`

**IV Drip Rate:**
\`\`\`
Rate (mL/hr) = (Volume (mL) × Drip Factor) / Time (minutes)
\`\`\`

**Creatinine Clearance (Cockcroft-Gault):**
\`\`\`
CrCl (male) = [(140 - Age) × Weight (kg)] / (72 × SCr)
CrCl (female) = CrCl (male) × 0.85
\`\`\`

### Concentration Conversions

- 1 gram (g) = 1000 milligrams (mg)
- 1 milligram (mg) = 1000 micrograms (mcg)
- 1 liter (L) = 1000 milliliters (mL)

## Step-by-Step Process

1. Identify what needs to be calculated
2. List known values
3. Identify missing values (ask user if needed)
4. Select appropriate formula
5. Show calculation with units
6. Verify result makes clinical sense

## Important Notes

- Always include units in calculations
- Double-check decimal placement
- Verify pediatric doses against references
- Flag calculations that seem clinically unusual
- Never guess missing values - ask user

## Example Calculations

### Example 1: Basic Dose
**Question:** Patient weighs 70 kg. Dose is 5 mg/kg. What's the total dose?

**Calculation:**
\`\`\`
Dose = 70 kg × 5 mg/kg
Dose = 350 mg
\`\`\`

### Example 2: IV Drip Rate
**Question:** Infuse 1000 mL over 8 hours. What rate in mL/hr?

**Calculation:**
\`\`\`
Rate = 1000 mL / 8 hours
Rate = 125 mL/hr
\`\`\`
```

**Step 4: Add skill trigger to skill-rules.json**

```bash
open .claude/skills/skill-rules.json
```

Add new entry:

```json
"pharmacy-calculator": {
  "type": "domain",
  "enforcement": "suggest",
  "priority": "high",
  "description": "Assists with pharmacy dose calculations and conversions",
  "promptTriggers": {
    "keywords": [
      "calculate",
      "calculation",
      "dose",
      "dosing",
      "drip rate",
      "convert",
      "conversion",
      "creatinine clearance",
      "CrCl"
    ],
    "intentPatterns": [
      "(calculate|compute|determine).*?(dose|dosing|rate)",
      "(convert|change).*?(mg|mcg|mL|units)",
      "(what|what's).*?(dose|rate|conversion)",
      "how (much|many).*?(give|administer)"
    ]
  }
}
```

**Step 5: Update HOW_TO_USE.md**

Add to "Installed Skills" section:

```markdown
**6. pharmacy-calculator** (HIGH - Suggests)
- **Triggers when you say:** "calculate dose", "convert mg to mcg", "drip rate"
- **What it does:** Provides pharmacy calculation formulas and step-by-step guidance
- **Why:** Ensures accurate calculations with proper units and verification
```

**Step 6: Test the skill**

Ask: "calculate dose for 80 kg patient at 10 mg/kg"

Should see skill activation and calculation help.

**Step 7: Commit**

```bash
git add .claude/skills/pharmacy-calculator/
git add .claude/skills/skill-rules.json
git add HOW_TO_USE.md
git commit -m "Add pharmacy-calculator skill for dose calculations"
git push
```

---

## Customizing Hooks

### Understanding Hook Files

Hooks are shell scripts or TypeScript files that run at specific lifecycle events:

- **UserPromptSubmit** - Before Claude processes your prompt
- **PreToolUse** - Before Claude uses a tool (Edit, Write, etc.)
- **PostToolUse** - After Claude uses a tool
- **Stop** - When you stop Claude or session ends

### Example: Modify skill-activation-prompt.sh Output

**Goal:** Change the visual format of skill activation messages.

**Steps:**

1. **Open the TypeScript hook:**
   ```bash
   open .claude/hooks/skill-activation-prompt.ts
   ```

2. **Find the output generation (lines 82-117):**
   ```typescript
   let output = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n';
   output += '🎯 SKILL ACTIVATION CHECK\n';
   output += '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n';
   ```

3. **Customize the format:**
   ```typescript
   let output = '═══════════════════════════════════════\n';
   output += '📚 SKILLS READY TO HELP\n';
   output += '═══════════════════════════════════════\n\n';
   ```

4. **Change priority labels:**
   ```typescript
   if (critical.length > 0) {
     output += '🚨 MUST USE (Critical):\n';  // Changed from "CRITICAL SKILLS"
     critical.forEach(s => output += `  • ${s.name}\n`);  // Changed arrow
     output += '\n';
   }
   ```

5. **Test the hook:**
   ```bash
   cd "/home/user/Skills/Copy Study Guide Claude Q3 2"
   CLAUDE_PROJECT_DIR="$(pwd)" bash -c 'echo "{\"prompt\":\"create excel\"}" | .claude/hooks/skill-activation-prompt.sh'
   ```

6. **Commit:**
   ```bash
   git add .claude/hooks/skill-activation-prompt.ts
   git commit -m "Customize skill activation output format"
   git push
   ```

---

## File Structure Reference

```
Copy Study Guide Claude Q3 2/
├── .claude/
│   ├── settings.json              # Permissions and hook configuration
│   ├── commands/                  # Slash commands
│   │   ├── create-word.md         # /create-word command
│   │   ├── create-excel.md        # /create-excel command
│   │   └── verify-accuracy.md     # /verify-accuracy command
│   ├── skills/
│   │   ├── skill-rules.json       # Skill trigger definitions
│   │   └── [skill-name]/          # Individual skills (if created)
│   │       └── SKILL.md           # Skill knowledge base
│   └── hooks/
│       ├── skill-activation-prompt.sh   # UserPromptSubmit hook script
│       ├── skill-activation-prompt.ts   # UserPromptSubmit hook logic
│       └── state/                 # Session persistence storage
├── Claude Templates/              # Study guide templates
│   ├── Word LO 11-5.txt          # Word template (695 lines)
│   ├── Excel Drugs Chart 11-1.txt # Excel template (1144 lines)
│   └── HTML LO with Master Chart 10-30.txt
├── CLAUDE.md                      # Project-specific rules and protocols
├── HOW_TO_USE.md                  # User guide for features
├── MAINTENANCE.md                 # This file
└── .gitignore                     # Exclude state files from git
```

### Key File Relationships

```
Slash Command → Template File
/create-word → Claude Templates/Word LO 11-5.txt
/create-excel → Claude Templates/Excel Drugs Chart 11-1.txt

Skill Trigger → Skill Implementation
skill-rules.json → .claude/skills/[skill-name]/SKILL.md

Hook Registration → Hook Script
settings.json → .claude/hooks/skill-activation-prompt.sh
```

---

## Common Customizations

### 1. Change Save Location for Study Guides

**Current:** `[Class]/[Exam]/Claude Study Tools/`
**Want:** `[Class]/[Exam]/My Study Files/`

**Files to update:**
- CLAUDE.md (line 65)
- All slash command files (.claude/commands/*.md)
- HOW_TO_USE.md (search "Claude Study Tools")

**Find and replace:**
```bash
# In each file
Claude Study Tools → My Study Files
```

---

### 2. Add New Template Format (PDF)

**Goal:** Add /create-pdf command

**Steps:**

1. Create template file:
   ```bash
   touch "Claude Templates/PDF Study Guide Template.txt"
   ```

2. Write template specifications in that file

3. Create slash command:
   ```bash
   touch .claude/commands/create-pdf.md
   ```

4. Follow "Creating New Slash Commands" section above

5. Add skill trigger in skill-rules.json

6. Update HOW_TO_USE.md

---

### 3. Change Color Scheme in Excel Templates

**Goal:** Use different pastel colors

**Steps:**

1. Open Excel template:
   ```bash
   open "Claude Templates/Excel Drugs Chart 11-1.txt"
   ```

2. Find color specifications (search for hex codes like #E6F3FF)

3. Replace with new colors:
   ```
   Old: #E6F3FF (light blue)
   New: #F0E6FF (light purple)
   ```

4. Changes automatically apply to future study guides

5. No configuration updates needed!

---

### 4. Add Pre-Commit Hook for Validation

**Goal:** Validate study guides before committing

**Steps:**

1. Create pre-commit hook:
   ```bash
   touch .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

2. Add validation script:
   ```bash
   #!/bin/bash

   # Check if CLAUDE.md was updated but not HOW_TO_USE.md
   if git diff --cached --name-only | grep -q "CLAUDE.md"; then
     if ! git diff --cached --name-only | grep -q "HOW_TO_USE.md"; then
       echo "⚠️  Warning: CLAUDE.md changed but HOW_TO_USE.md not updated"
       echo "Consider updating HOW_TO_USE.md to reflect changes"
       # Don't block, just warn
     fi
   fi

   exit 0
   ```

---

## Troubleshooting

### Skills Not Triggering After Changes

**Problem:** Modified skill-rules.json but skills don't activate

**Solutions:**

1. **Check JSON syntax:**
   ```bash
   cat .claude/skills/skill-rules.json | python3 -m json.tool
   ```

   Should not show errors. If errors, fix JSON syntax.

2. **Verify hook is executable:**
   ```bash
   ls -l .claude/hooks/skill-activation-prompt.sh
   # Should show: -rwxr-xr-x
   ```

   If not:
   ```bash
   chmod +x .claude/hooks/skill-activation-prompt.sh
   ```

3. **Test hook manually:**
   ```bash
   CLAUDE_PROJECT_DIR="$(pwd)" bash -c 'echo "{\"prompt\":\"create excel\"}" | .claude/hooks/skill-activation-prompt.sh'
   ```

   Should show skill activation output.

4. **Restart Claude Code session:**
   - End current session
   - Start new session in study guide folder
   - Hooks load at session start

---

### Slash Command Not Found

**Problem:** `/create-excel` returns "command not found"

**Solutions:**

1. **Check file exists:**
   ```bash
   ls .claude/commands/create-excel.md
   ```

2. **Check file extension:**
   Must be `.md` not `.txt` or `.markdown`

3. **Check file has description:**
   ```bash
   head -3 .claude/commands/create-excel.md
   ```

   Should show:
   ```markdown
   ---
   description: Create comprehensive 4-tab Excel drug chart from pharmacology source material
   ---
   ```

4. **Restart Claude Code session**

---

### Template Changes Not Applying

**Problem:** Edited template but study guides still use old format

**Solutions:**

1. **Verify you edited correct file:**
   ```bash
   ls -l "Claude Templates/Excel Drugs Chart 11-1.txt"
   # Check modification time
   ```

2. **Check slash command references correct path:**
   ```bash
   grep -n "Claude Templates" .claude/commands/create-excel.md
   ```

   Should match your edited file.

3. **Clear any cached files:**
   Templates are read at runtime, no cache. If issue persists, restart session.

4. **Test with new source file:**
   Changes only apply to NEW study guides, not existing ones.

---

### Hook Errors

**Problem:** Hook shows error message

**Check 1: Node.js available**
```bash
which node
which npx
```

Both should return paths. If not, install Node.js.

**Check 2: TypeScript executor (tsx)**
```bash
npx tsx --version
```

Should show version. If not, tsx will auto-install on first run.

**Check 3: Hook script syntax**
```bash
bash -n .claude/hooks/skill-activation-prompt.sh
```

Should not show errors.

**Check 4: TypeScript syntax**
```bash
npx tsx .claude/hooks/skill-activation-prompt.ts
```

Shows any TypeScript errors.

---

### Git Commit Issues

**Problem:** Can't commit changes to hooks/state/ files

**Reason:** .gitignore excludes state files (intentional)

**Solution:**
```bash
# State files SHOULD NOT be committed
# If you need to commit hook scripts:
git add .claude/hooks/skill-activation-prompt.sh
git add .claude/hooks/skill-activation-prompt.ts

# But NOT state files:
# .claude/hooks/state/*.json should remain excluded
```

---

## Quick Reference

### Files That Require Updates Together

| Change | Files to Update |
|--------|----------------|
| Rename template | Slash command, CLAUDE.md, HOW_TO_USE.md |
| Move template location | All slash commands, CLAUDE.md, HOW_TO_USE.md |
| Rename slash command | Command file, HOW_TO_USE.md, skill-rules.json (optional) |
| Add new slash command | Create command file, skill-rules.json, HOW_TO_USE.md |
| Modify skill trigger | skill-rules.json, HOW_TO_USE.md (if behavior changes) |
| Add new skill | Create skill directory/SKILL.md, skill-rules.json, HOW_TO_USE.md |
| Change save location | CLAUDE.md, all slash commands, HOW_TO_USE.md |

### Testing Checklist

After making changes:

- [ ] JSON syntax valid (`python3 -m json.tool`)
- [ ] Hooks executable (`chmod +x`)
- [ ] Test slash commands (`/command-name test-file.txt`)
- [ ] Test skill triggers (ask Claude test prompts)
- [ ] Updated HOW_TO_USE.md
- [ ] Committed changes to git
- [ ] Pushed to remote

---

## Getting Help

**Before asking for help:**

1. Check this MAINTENANCE.md file
2. Check HOW_TO_USE.md for usage questions
3. Check CLAUDE.md for protocol questions
4. Test manually using command line

**Common issues:**
- JSON syntax errors → Validate JSON
- Hooks not running → Check executable permissions
- Slash commands not found → Check file extension (.md)
- Templates not loading → Verify file paths

**Still stuck?**
- Check git history for working versions
- Test with backup files
- Ask Claude: "Debug my slash command setup"

---

Remember: **Always update HOW_TO_USE.md when you make changes!**
