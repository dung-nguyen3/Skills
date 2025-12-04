# How to Use Claude Study Guide Automation

## What's Installed

Your study guide folder now has automated quality controls and shortcuts:

### 1. Slash Commands (Quick Actions)
- `/LO-word` - Create Word study guide from source file
- `/4-tab-excel` - Create 4-tab Excel drug chart (pharmacology)
- `/drugs-html` - Create interactive HTML drug reference (pharmacology)
- `/LO-html` - Create HTML learning objectives guide (ANY medical topic)
- `/clinical-assessment-html` - Create clinical assessment guide (history & physical exam)
- `/verify-accuracy` - Deep accuracy analysis of existing study guide

### 2. Skill Auto-Activation System
- Automatically suggests relevant guidance when you work on study guides
- Enforces quality checks (source-only policy, verification)
- Runs in the background - no manual activation needed

### 3. Hook System (Background Quality Gates) ✅ ACTIVE
- **UserPromptSubmit** - Analyzes your prompts and suggests skills
- **PreToolUse** - Blocks writes without verification ⛔
- **PostToolUse** - Reminds to verify after creation 📋
- **Stop** - Catches incomplete work at session end ⚠️

---

## Using Slash Commands

### Basic Syntax

```
/command-name path/to/source/file.txt
```

### Example 1: Create Excel Drug Chart

**You say:**
```
/4-tab-excel Pharmacology/Exam 3/Extract/HIV Antivirals.txt
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
/LO-word Pharmacology/Exam 3/Extract/Lecture 42.txt
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

### Example 4: Create Interactive HTML Drug Chart

**You say:**
```
/drugs-html Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

**What happens:**
1. Claude loads the Drug Chart HTML template
2. States the verification checklist
3. Reads your source file completely
4. Creates single-page interactive HTML with:
   - Drug Classes & Comparisons (with key similarities/differences)
   - Master Drug Chart (sortable by clicking headers)
   - Quick Reference (first-line treatments, mnemonics)
5. Researches mnemonics via WebSearch
6. Runs post-creation verification
7. Saves to: `Pharmacology/Exam 3/Claude Study Tools/HIV_Antivirals_Reference_Chart.html`

**Best for:**
- Quick mobile reference during rotations
- Offline study (works without internet)
- Comparing drugs within classes visually

---

### Example 5: Create Learning Objectives Guide (Any Medical Topic)

**You say:**
```
/LO-html Clinical Medicine/Exam 2/Extract/Cardiovascular-Disease.txt
```

**What happens:**
1. Claude loads the HTML LO template
2. States the verification checklist
3. Reads your source file completely
4. Creates 4-tab HTML study guide with:
   - Tab 1: Learning Objectives (Q&A format for each LO)
   - Tab 2: Key Comparisons (focused 2-3 way comparison tables)
   - Tab 3: Master Comparison Tables (complete differential diagnosis)
   - Tab 4: Summary (high-yield pearls, mnemonics, "If X Think Y")
5. Researches mnemonics via WebSearch
6. Runs post-creation verification
7. Saves to: `Clinical Medicine/Exam 2/Claude Study Tools/Cardiovascular_Disease_Study_Guide.html`

**Works for ALL medical topics:**
- Pathophysiology (cardiovascular, hematology, immunology)
- Clinical medicine (rheumatology, endocrinology)
- Physiology (respiratory, renal)
- Procedures and techniques
- ANY lecture with learning objectives

---

### Example 6: Create Clinical Assessment Guide

**You say:**
```
/clinical-assessment-html "Clinical Medicine/Exam 1/Extract/Lower-Extremity.txt" "Leg Pain"
```

**What happens:**
1. Claude loads the Clinical Assessment template
2. States the verification checklist
3. Reads your source file completely
4. Creates interactive HTML organized by onset (Acute/Subacute/Chronic) with:
   - Complete HPI (OLDCAARTS) - exact patient questions to ask
   - Essential PMH, FH, SH - relevant history elements
   - Focused ROS - checkbox format for all systems
   - Detailed Physical Exam - inspection, palpation, specialized tests
   - Differential diagnosis by presentation pattern
   - Clinical decision trees
5. Follows Medical History Card format exactly
6. Runs post-creation verification
7. Saves to: `Clinical Medicine/Exam 1/Claude Study Tools/Leg_Pain_Clinical_Assessment_Guide.html`

**Best for:**
- OSCE preparation
- Physical diagnosis courses
- Clinical rotations
- Patient encounter practice
- Chief complaint workups

---

## Template Selection Guide

### Which Command Should I Use?

| Content Type | Recommended Command | Output Format |
|--------------|---------------------|---------------|
| **Pharmacology (drugs)** | `/4-tab-excel` OR `/drugs-html` | Excel or HTML |
| **Any medical topic with learning objectives** | `/LO-html` | HTML |
| **Clinical history & physical exam** | `/clinical-assessment-html` | HTML |
| **Word document needed** | `/LO-word` | Word (any topic) |

### Detailed Selection Guide

**Use `/4-tab-excel` when:**
- Creating comprehensive drug charts
- Need 4-tab format (Details, Comparisons, Master Chart, Pearls)
- Want print-friendly Excel for exam prep
- Studying pharmacology: antibiotics, antivirals, antineoplastics, cardiovascular drugs

**Use `/drugs-html` when:**
- Creating quick drug reference for mobile
- Need offline-ready HTML file
- Want sortable drug tables
- Same content as Excel but more portable

**Use `/LO-html` when:**
- Source has learning objectives
- ANY medical topic: pathophysiology, diseases, procedures, physiology
- Examples: Cardiovascular disease, Hematology II, Immunology, Rheumatology, Respiratory physiology
- Want 4-tab HTML with Q&A, comparisons, master tables, summary

**Use `/clinical-assessment-html` when:**
- Learning history-taking and physical examination
- Need chief complaint workup (e.g., "Leg Pain", "Headache", "Chest Pain")
- Want OLDCAARTS format with exact patient questions
- Preparing for OSCE or clinical rotations
- Need differential diagnosis by onset (acute/subacute/chronic)

**Use `/LO-word` when:**
- School requires Word document submission
- Need print-friendly document
- Works for any medical topic

### Can I Use Multiple Templates?

**Yes!** For pharmacology, consider creating BOTH:
- `/4-tab-excel` - Comprehensive study (detailed tables, comparisons)
- `/drugs-html` - Quick mobile reference (same content, different format)

---

## Using Specialized Agents (Phase 4 - NEW!)

The infrastructure now includes **two specialized agents** that provide deep automation for complex tasks:

### Agent 1: medical-mnemonic-researcher

**Purpose:** Finds PROVEN, ESTABLISHED medical mnemonics from medical education sources

**When it activates:**
- Automatically during study guide creation (when mnemonics are needed)
- When you ask: "Find mnemonics for [topic]"
- When creating any study guide with memory aids

**What it does:**
1. Generates 5-10 search query variations
2. Searches medical education sources (Reddit r/medicalschool, SDN, USMLE forums, First Aid, Sketchy, Pathoma)
3. Finds top 3 mnemonics with reliability scores (1-5 stars)
4. Provides source links for each mnemonic
5. Includes user feedback from medical students
6. Recommends best mnemonics for different use cases

**Output:** Comprehensive research report with established mnemonics, sources, and recommendations

**Example:**
```
You: "Find mnemonics for cranial nerves"
Claude: "I'll use the medical-mnemonic-researcher agent to find established mnemonics."
Agent: Returns top 3 mnemonics with 5-star reliability, source links, user feedback
Result: Add to study guide with attribution
```

**Performance:** 30-60 seconds (vs. 5-10 minutes manual research)

---

### Agent 2: study-guide-analyzer

**Purpose:** Comprehensive 6-step verification of study guides against source files

**When it activates:**
- Automatically after study guide creation (post-creation verification)
- When you ask: "Verify accuracy of [filename]"
- When using `/verify-accuracy` command
- When checking completeness or quality

**What it does:**
1. **Step 1:** Reads source file completely
2. **Step 2:** Reads study guide completely
3. **Step 3:** Systematic verification (source accuracy, names, merged cells, format, completeness)
4. **Step 4:** Documents all issues (Critical/Important/Minor)
5. **Step 5:** Saves detailed analysis report to file
6. **Step 6:** Returns summary and requests approval before fixes

**Output:** Comprehensive analysis report saved to `[filename]-analysis-report.md`

**Report includes:**
- Executive summary with overall assessment
- Critical/Important/Minor issues categorized
- Statistics (coverage %, issue counts)
- Specific fix recommendations
- Approval request before changes

**Example:**
```
You: "Verify accuracy of HIV_Drug_Chart.xlsx"
Claude: "I'll use the study-guide-analyzer agent to perform 6-step verification."
Agent: Analyzes completely, finds 0 critical issues, 2 minor suggestions
Result: Analysis report saved, study guide approved for use
```

**Performance:** 1-2 minutes (vs. 10-15 minutes manual verification)

---

### How Agents Work

**Agents are autonomous:**
- Run as separate sub-tasks
- Work independently with specialized instructions
- Return comprehensive reports when complete
- Save results to files

**You don't launch agents manually:**
- Skills automatically invoke agents when needed
- Just request the task (create study guide, verify accuracy)
- Claude handles agent invocation automatically

**Agent workflow:**
1. Skill activates (e.g., mnemonic-researcher skill)
2. Skill launches agent (e.g., medical-mnemonic-researcher agent)
3. Agent performs specialized task autonomously
4. Agent returns comprehensive report
5. Claude uses agent results to complete your request

---

### Benefits of Phase 4 Agents

**Time savings:**
- Mnemonic research: 5-10 minutes → 30-60 seconds
- Study guide verification: 10-15 minutes → 1-2 minutes

**Quality improvements:**
- Only established mnemonics (not invented)
- Systematic 6-step verification (catches issues)
- Source validation and reliability scores
- Statistical analysis of coverage

**Consistency:**
- Same verification protocol every time
- Reproducible analysis
- Documented findings in reports

---

## How Skill Auto-Activation Works

### What Are Skills?

Skills are specialized knowledge bases that automatically activate when you need them. Think of them as context-aware helpers.

### Installed Skills:

**IMPORTANT:** Claude AUTOMATICALLY does pre-creation and post-creation verification for all study guides. Skills are safety nets that enforce this if Claude somehow skips a step.

**1. source-only-enforcer** (CRITICAL - Safety Net)
- **Triggers when you say:** "create excel", "create study guide", "make drug chart"
- **What it does:** Ensures Claude states the pre-creation verification checklist automatically before starting
- **Why:** Safety net that prevents Claude from skipping verification or adding external medical facts
- **You don't do anything:** Claude handles this automatically - you just request the study guide

**2. mnemonic-researcher** (HIGH - Suggests)
- **Triggers when you say:** "find mnemonic", "help me remember", "memory trick"
- **What it does:** Reminds Claude to research established mnemonics via WebSearch (already required)
- **Why:** Ensures you get PROVEN mnemonics, not invented ones
- **You don't do anything:** Claude automatically researches mnemonics during study guide creation

**3. study-guide-verifier** (CRITICAL - Suggests)
- **Triggers when you say:** "verify accuracy", "check study guide", "analyze file"
- **What it does:** Activates the systematic 6-step verification protocol
- **Why:** Ensures comprehensive accuracy checking of existing study guides
- **When to use:** When you want to verify an already-created study guide

**4. template-compliance-checker** (HIGH - Suggests)
- **Triggers when you say:** "check format", "correct colors", "template"
- **What it does:** Reminds Claude of template requirements during creation
- **Why:** Ensures consistent formatting across all study guides
- **You don't do anything:** Claude follows templates automatically

**5. drug-classification-assistant** (MEDIUM - Suggests)
- **Triggers when you say:** "drug class", "MOA", "first-line", "classification"
- **What it does:** Helps Claude verify drug-specific vs class-wide information
- **Why:** Prevents incorrect grouping of drugs
- **You don't do anything:** Claude checks this automatically during creation

### Example Session with Skill Auto-Activation:

**You say:**
```
Create an Excel drug chart from the HIV antivirals lecture
```

**What happens behind the scenes (you see this in output):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 SKILL ACTIVATION CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ CRITICAL SKILLS (REQUIRED):
  → source-only-enforcer

ACTION: Use Skill tool BEFORE responding
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Then Claude AUTOMATICALLY states the verification checklist (you don't do this):**
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

**What you do:** Nothing! Just request the study guide and Claude handles all verification automatically.

**The skill system ensures:** Claude doesn't skip the verification steps, even if it gets distracted or makes a mistake.

---

## How Quality Gate Hooks Work

Quality gate hooks are automatic enforcement mechanisms that run at different lifecycle events to ensure study guide quality.

### The Three Quality Gates:

**1. Pre-Creation Gate (verification-guard.sh)** ⛔

**When it runs:** BEFORE Claude creates/edits study guide files

**What it does:**
- Detects if Claude is about to write to a study guide file (`Claude Study Tools/*.xlsx|.docx|.html`)
- Checks if pre-creation verification checklist was completed
- BLOCKS the write operation if verification not done
- Shows error message explaining what's needed

**Example scenario:**
```
You say: "Create study guide from lecture 42"
Claude tries to write file
↓
Hook detects: Writing to "Claude Study Tools/Lecture_42.docx"
Hook checks: Is verification file present? NO
↓
⛔ BLOCKED - Shows error message
Claude sees: Must state verification checklist first
Claude states checklist, creates verification marker
Hook checks again: Verification file present? YES
↓
✅ ALLOWED - Write proceeds
```

**Why this matters:** Prevents Claude from creating study guides without reading the source file completely and confirming the source-only policy.

---

**2. Post-Creation Reminder (post-verification-trigger.sh)** 📋

**When it runs:** AFTER Claude creates/edits study guide files

**What it does:**
- Detects that a study guide file was just created/modified
- Shows reminder about post-creation verification
- Lists all 4 verification checks required
- Suggests using `/verify-accuracy` for deep analysis

**Example output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 POST-CREATION VERIFICATION REMINDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Study guide file created/modified:
📁 HIV_Drug_Chart.xlsx

⚠️  MANDATORY NEXT STEP: Run post-creation verification

Verify the completed file for:
1. ✓ Source Accuracy
2. ✓ Template Compliance
3. ✓ Completeness
4. ✓ Quality Checks

🎯 ACTION REQUIRED:
State: "Post-creation verification complete"
```

**Why this matters:** Reminds Claude to verify the study guide was created correctly before moving on to other tasks.

---

**3. Session End Check (verification-completion-check.sh)** ⚠️

**When it runs:** When Claude Code session STOPS

**What it does:**
- Checks if pre-verification was done but post-verification was skipped
- Checks if study guide files were created but not verified
- Warns about incomplete work
- Lists files that need verification
- Suggests actions for next session

**Example scenario:**
```
Session ending...
↓
Hook checks: Files created this session? YES (2 files)
Hook checks: Post-verification done? NO
↓
⚠️  WARNING - Incomplete verification detected

Files needing verification:
📄 HIV_Drug_Chart.xlsx
📄 Antibiotics_Study_Guide.docx

Recommended actions for next session:
1. Run /verify-accuracy on each file
2. Complete all 4 quality checks
```

**Why this matters:** Catches situations where you might have created study guides but forgot to verify them before the session ended.

---

### How They Work Together:

**Normal workflow:**
1. 📝 You: `/excel source.txt`
2. ✅ Claude states verification checklist (automatic)
3. ⛔ PreToolUse hook: Checks verification → ALLOWS
4. 📝 Claude creates Excel file
5. 📋 PostToolUse hook: Shows reminder
6. ✅ Claude runs post-verification (automatic)
7. ✅ Claude states "Post-creation verification complete"
8. ⚠️  Stop hook: Checks complete → No warning

**If Claude skips verification:**
1. 📝 You: "Make study guide"
2. 📝 Claude tries to write file
3. ⛔ PreToolUse hook: No verification → **BLOCKS**
4. ❌ Claude sees error, realizes must verify first
5. ✅ Claude states verification checklist
6. ✅ Creates verification marker
7. ⛔ PreToolUse hook: Verification present → ALLOWS
8. 📝 Claude creates file
9. 📋 PostToolUse hook: Shows reminder
10. ✅ Claude completes post-verification

### What You Do:

**NOTHING!** The hooks work automatically in the background. You just:
- Request study guides normally
- Use slash commands (recommended)
- Claude handles all verification automatically

The hooks ensure Claude doesn't skip steps even if it gets confused or makes a mistake.

---

## Advanced Accuracy Features

Based on comprehensive analysis of production Claude Code infrastructure patterns, your system includes 5 critical accuracy improvements that work automatically in the background.

### 1. Session-Based State Tracking ⭐⭐⭐⭐⭐

**What it is:** Persistent session cache that tracks all verification activity

**Location:** `.claude/study-guide-cache/[session_id]/`

**What gets tracked:**
```
.claude/study-guide-cache/abc123/
├── verification.json           # Pre-creation verification status
├── post-verification.json      # Post-creation verification status
├── created-files.log          # All study guides created (timestamped)
├── operations.log             # All file operations with timestamps
└── files-needing-verification.txt  # Files requiring verification
```

**Why this matters:**
- Verification state persists across all hook executions
- No more lost validation between hooks
- Session-level analytics available
- Supports multi-file tracking

**What you do:** Nothing! The cache is created and managed automatically.

---

### 2. Content Pattern Detection ⭐⭐⭐⭐⭐

**What it is:** Automatic detection of accuracy red flags

**What it catches:**
- Filenames with "Draft", "Temp", "Test", "WIP" → Flags incomplete work
- Future: Vague language patterns ("maybe", "probably", "might")
- Future: Missing source references
- Future: Inconsistent medical terminology

**Example warning:**
```
POTENTIAL ACCURACY ISSUES:
📄 HIV_Draft_Chart.xlsx - Filename suggests incomplete work (draft)
📄 Test_Guide.docx - Filename suggests incomplete work (test)
```

**Why this matters:** Catches potential issues BEFORE you study from them!

**When it runs:** At session end (Stop hook)

---

### 3. Error Threshold Automation ⭐⭐⭐⭐

**What it is:** Smart recommendations based on issue count

**How it works:**
```
1-2 issues → Shows manual verification steps

3-5 issues → Detailed report with specific fixes

6+ issues → Recommends automated agent:
🤖 RECOMMENDED: Use accuracy verification agent
   Multiple issues detected - automated verification recommended

   Next session, run:
   /verify-accuracy [file-path] [source-path]
```

**Why this matters:** Saves you from manually fixing 10+ accuracy issues!

**Example:**
- Created 1 study guide, 1 issue → "Run post-verification manually"
- Created 5 study guides, 4 issues → "Use /verify-accuracy agent"

---

### 4. Session-Aware Guardrails ⭐⭐⭐⭐

**What it is:** Blocks verification bypass without nagging repeatedly

**How it works:**

**First study guide in session:**
```
⛔ BLOCKED - Pre-Creation Verification Required
(Shows full error message with requirements)
```

**Second study guide in same session:**
```
✅ ALLOWED - Verification marker from first guide applies
(No blocking, no nagging)
```

**File markers supported:**
- Add `@verified` comment to source files → Skip enforcement
- Set `SKIP_SOURCE_ONLY_ENFORCEMENT=1` → Temporary bypass

**Why this matters:** Prevents bypass without being annoying!

**Benefit:** Create multiple study guides in one session without repeated verification prompts.

---

### 5. Enhanced Stop Hook Validation ⭐⭐⭐⭐

**What it is:** Comprehensive accuracy checks at session end

**What it checks:**
```
✅ Was pre-verification done?
✅ Was post-verification done?
✅ Were files created but not verified?
✅ Any problematic filenames?
✅ How many total issues?
```

**Example output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  STUDY GUIDE QUALITY CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INCOMPLETE VERIFICATION DETECTED:
⚠️  Created 2 study guide file(s) but did not run post-verification

POTENTIAL ACCURACY ISSUES:
📄 Draft_Chart.xlsx - Filename suggests incomplete work

FILES REQUIRING VERIFICATION:
   📄 HIV_Drug_Chart.xlsx
   📄 Antibiotics_Study_Guide.docx

🎯 RECOMMENDED ACTIONS FOR NEXT SESSION:
   1. Run post-creation verification on all files
   2. Use /verify-accuracy for deep analysis
   3. Verify source-only policy followed

Session cache: .claude/study-guide-cache/abc123
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Automatic cleanup:** Keeps last 5 session caches, deletes older ones

**Why this matters:** Safety net that catches incomplete work before you close Claude!

---

### How All 5 Work Together

**Complete workflow with all improvements:**

```
1. Session starts
   └─ Cache directory created automatically

2. You: /excel source.txt
   └─ UserPromptSubmit: Skill activation check

3. Claude: States verification checklist
   └─ Creates verification.json marker (Feature 1: State Tracking)

4. PreToolUse hook: Checks marker
   └─ Marker exists → ALLOWS write (Feature 4: Session-Aware)
   └─ Logs operation to operations.log

5. Claude: Creates Excel file
   └─ File written successfully

6. PostToolUse hook: Runs after creation
   └─ Logs to created-files.log (Feature 1: State Tracking)
   └─ Shows post-verification reminder

7. Claude: Runs post-verification
   └─ Creates post-verification.json marker

8. You: Create second study guide
   └─ PreToolUse: Same session marker → ALLOWS (Feature 4: No nag)

9. Session ends → Stop hook validates
   └─ Checks filenames (Feature 2: Pattern Detection)
   └─ Counts issues (Feature 3: Threshold Automation)
   └─ Shows smart recommendations (Feature 5: Enhanced Validation)
   └─ Cleans up old caches
```

---

### Benefits Summary

**Accuracy:**
- ✅ Automatic issue detection
- ✅ Content pattern analysis
- ✅ Persistent verification tracking
- ✅ Multi-file consistency checks

**Automation:**
- ✅ Smart agent triggering (3+ issues)
- ✅ Session-aware enforcement (less nagging)
- ✅ Automatic cache management
- ✅ Intelligent recommendations

**Confidence:**
- ✅ Multiple safety nets
- ✅ Clear warnings at session end
- ✅ Actionable recommendations
- ✅ Nothing falls through the cracks

**User Experience:**
- ✅ Only blocks ONCE per session
- ✅ File marker support
- ✅ Environment overrides available
- ✅ Works completely automatically

---

## Practical Workflows

### Workflow 1: Creating Study Guide from Scratch

**Step 1:** Extract lecture to text file
```
Pharmacology/Exam 3/Extract/Lecture 42.txt
```

**Step 2:** Use slash command
```
/LO-word Pharmacology/Exam 3/Extract/Lecture 42.txt
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
/4-tab-excel Pharmacology/Exam 3/Extract/HIV Drugs.txt
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
/4-tab-excel Pharmacology/Exam 3/Extract/HIV Drugs.txt

# ✗ Wrong:
4-tab-excel (missing slash)
/4-tab-excel (missing file path)
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
/LO-word [source]
/4-tab-excel [source]
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
/4-tab-excel Pharmacology/Exam 3/Extract/HIV Drugs.txt
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
/4-tab-excel Extract/Beta_Blockers.txt
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
| `/LO-word` | Create Word study guide | Source file path | .docx in Claude Study Tools/ |
| `/4-tab-excel` | Create Excel drug chart | Source file path | .xlsx in Claude Study Tools/ |
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

## Infrastructure Status

**Phase 1 (COMPLETE):** Foundation
- ✓ Settings and permissions
- ✓ Skill trigger rules
- ✓ UserPromptSubmit hook
- ✓ Slash commands

**Phase 2 (COMPLETE):** Quality Gates
- ✓ PreToolUse hook - Blocks writes without verification
- ✓ PostToolUse hook - Auto-reminder after creation
- ✓ Stop hook - Catches incomplete work
- ✓ SessionStart hook - Shows requirements at session start

**Phase 3 (PARTIAL):** Native Skills
- ✓ source-only-enforcer (SKILL.md created - 80%+ activation)
- ✓ study-guide-verifier (SKILL.md created - 80%+ activation)
- ⏳ mnemonic-researcher (using skill-rules.json - 50% activation)
- ⏳ template-compliance-checker (using skill-rules.json - 50% activation)
- ⏳ drug-classification-assistant (using skill-rules.json - 50% activation)

**Reliability Improvements (COMPLETE):**
- ✓ Error resilience in all hooks (jq failures, fallback session IDs)
- ✓ Environment override support (`SKIP_STUDY_GUIDE_VERIFICATION=1`)
- ✓ Separate SessionStart script (maintainable)
- ✓ TypeScript hook dependencies (package.json, tsconfig.json)

---

## Emergency Override

If hooks malfunction or block legitimate operations, you can temporarily disable them:

**Method 1: Environment Variable (Recommended)**
```bash
export SKIP_STUDY_GUIDE_VERIFICATION=1
# Your study guide creation command
unset SKIP_STUDY_GUIDE_VERIFICATION
```

**Method 2: File Marker**
Add `@verified` comment to your source files to skip enforcement.

**Method 3: Session-Based**
Once verification is completed in a session, subsequent study guides are allowed automatically (no repeated blocking).

**When to use:**
- Hooks are malfunctioning
- Emergency study guide creation needed
- Testing or debugging

**Important:** Re-enable verification after emergency use!

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
