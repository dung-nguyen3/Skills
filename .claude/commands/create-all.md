---
description: Full workflow orchestrator - create ALL study guide formats in one command with automation
argument-hint: <source-file-or-directory> [--formats word,excel,anki,html] [--verify]
---

Create complete study guide workflow for: $ARGUMENTS

## Command Usage

**All formats (default):**
```
/create-all "HIV_Drugs.txt"
```

**Specific formats:**
```
/create-all "HIV_Drugs.txt" --formats word,excel-4tab,anki
```

**With post-verification:**
```
/create-all "HIV_Drugs.txt" --verify
```

**Directory (all files):**
```
/create-all "Pharmacology 3/Exam 2/Extract/"
```

---

## What This Command Does

**End-to-end automation:**

1. **Create study guides** (all formats or specified)
   - Word LO study guide
   - Excel 4-tab drug chart
   - Excel comparison chart
   - Excel master chart
   - Anki flashcards
   - HTML guides (LO or drugs)
   - Biography stories

2. **Auto-consolidation** (post-processing)
   - Merge master charts → reference file
   - Update QUICK_ACCESS index

3. **Verification** (if --verify flag)
   - Run accuracy verification
   - Generate analysis report

4. **Status report**
   - Show all created files
   - Token efficiency summary
   - Quick actions

---

## Instructions

### Step 1: Parse Arguments

**Extract components:**
```python
import re

args = "$ARGUMENTS"

# Extract source file/directory (first argument)
parts = args.split("--")
source = parts[0].strip()

# Extract format list (if --formats specified)
formats = []
if "--formats" in args:
    formats_match = re.search(r'--formats\s+([^\s]+)', args)
    if formats_match:
        formats = formats_match.group(1).split(',')

# Check for verification flag
verify = "--verify" in args

# If no formats specified, use course-specific defaults
if not formats:
    formats = get_default_formats_for_course(source)
```

### Step 2: Detect Course and Load Defaults

**Read format defaults:**

```python
import json
from pathlib import Path

def get_default_formats_for_course(source_path):
    """
    Detect course from path and load format defaults.

    Returns:
        list: Format names to generate
    """
    defaults_file = Path(".claude/format-defaults.json")

    with open(defaults_file) as f:
        defaults = json.load(f)

    # Detect course from path
    if "Pharmacology" in source_path or "pharmacology" in source_path.lower():
        return defaults["courses"]["Pharmacology"]["formats"]

    elif "Clinical" in source_path or "Pathophysiology" in source_path:
        return defaults["courses"]["Pathophysiology"]["formats"]

    else:
        # Default bundle
        return defaults["defaultBundle"]
```

**Display detected configuration:**

```
[FULL WORKFLOW ORCHESTRATOR]

Source: HIV_Drugs.txt
Course detected: Pharmacology
Formats: Word LO, Excel Comparison, Anki (default for Pharmacology)
Verification: No
Post-processing: Yes (auto)
```

---

### Step 2.5: Handle Directory Input with Tracking

**If source is a directory path:**

**Step 2.5.1: Scan directory for source files**
```bash
# Find all .txt and .pdf files in directory
source_dir="$source"
source_files=$(find "$source_dir" -maxdepth 1 -type f \( -name "*.txt" -o -name "*.pdf" \) | sort)
```

**Step 2.5.2: Check for processed files tracker**
```bash
# Read .processed_files.txt to get already-processed files
tracker_file="$source_dir/.processed_files.txt"

if [[ -f "$tracker_file" ]]; then
    mapfile -t processed_files < "$tracker_file"
else
    processed_files=()
fi
```

**Step 2.5.3: Filter to get NEW files only**
```bash
# Compare source files vs processed files
new_files=()

for file in $source_files; do
    basename=$(basename "$file")

    # Check if this file was already processed
    if ! printf '%s\n' "${processed_files[@]}" | grep -q "^$basename$"; then
        new_files+=("$basename")
    fi
done
```

**Step 2.5.4: Display tracking status**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIRECTORY MODE - SMART TRACKING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Directory: [source_dir]
Total source files: [N total]
Formats per file: [M formats]
Total outputs planned: [N × M study guides]

Status:
  ✓ Already processed: [K files] (will skip)
  ⏳ New files to process: [L files]

[If K > 0]:
Previously processed files (skipping):
  1. [file1.txt]
  2. [file2.txt]
  ...

[If L > 0]:
New files to process:
  1. [new_file1.txt]
  2. [new_file2.txt]
  ...

[If L == 0]:
✅ All files already processed - nothing to do!
Run /batch-status to verify completion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**If no new files, exit early. Otherwise, continue with new files only.**

**Step 2.5.5: Update file list**
```python
# Replace source file list with NEW files only
source_files = new_files
file_count = len(new_files)
```

**If not directory mode, process single file and skip this step.**

---

### Step 3: Create Study Guides (Sequential)

**CRITICAL: Execute each format using its dedicated command with FULL instructions.**

Each format below must be executed completely, following ALL steps in that command's template.
Do NOT skip steps or summarize - execute as if user ran the command directly.

---

#### Format 1: Word LO Study Guide

**Execute /LO-word with source file:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT 1/N: WORD LO STUDY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing /LO-word "[source_file]"

[Follow ALL steps from /LO-word command]:
- Step 0: Mode detection
- Step 1: Pre-creation verification checklist
- Step 2: Load resources (Word_LO_11-5_REVISED.txt template)
- Step 3: Read source file, identify ALL learning objectives
- Step 4: Create study guide with 4 sections
- Step 5: Use TodoWrite to track each LO
- Step 6: Post-creation template compliance verification
- Step 7: Save files

CRITICAL REQUIREMENTS (from /LO-word):
- Learning objective STATEMENTS must be copied EXACTLY as written
- Use TodoWrite to create todo for EACH learning objective
- 4 sections: Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary
- Soft pastel colors, Calibri 12pt
- WebSearch for mnemonics (mandatory)
- Post-creation verification with ALL checks

Output: [Topic]_Study_Guide.docx
```

**Execute /LO-word completely before proceeding to next format.**

---

#### Format 2: Excel Comparison Chart (if in formats list)

**Execute /key-comparisons-excel with source file:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT 2/N: EXCEL COMPARISON CHART
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing /key-comparisons-excel "[source_file]"

[Follow ALL steps from /key-comparisons-excel command]:
- Step 0: Mode detection
- Step 1: Pre-creation verification checklist
- Step 2: Load resources (Excel_Comparison_Chart_REVISED.txt template)
- Step 3: Analyze source file (identify ALL conditions/concepts)
- Step 4: Create 3-tab Excel chart
- Step 5: WebSearch for mnemonics
- Step 6: Python implementation
- Step 7: Use TodoWrite to track progress
- Step 8: Post-creation template compliance verification
- Step 9: Save files

CRITICAL REQUIREMENTS (from /key-comparisons-excel):
- 3 tabs: Key Comparisons, Master Chart, Summary
- Tab 1: MULTIPLE comparison tables (one category per table)
- Mnemonics DIRECTLY BELOW relevant tables
- ONE color per table/category (not alternating rows)
- ALL data cells have pastel background (not white)
- Post-creation verification with ALL checks

Output: [Topic]_Comparison_Chart.xlsx
```

**Execute completely before proceeding to next format.**

---

#### Format 3: Anki Flashcards (if in formats list)

**Execute /anki with source file:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT 3/N: ANKI FLASHCARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing /anki "[source_file]"

[Follow ALL steps from /anki command]:
- Step 0: Mode detection
- Step 1: Pre-creation verification checklist
- Step 2: Load resources (Anki_APKG_Example.py)
- Step 3: Extract Learning Objectives (MANDATORY enumeration)
- Step 4: Analyze source file (LO-focused, create LO-Content Mapping)
- Step 5: Create flashcards (LO-filtered only)
- Step 6: Use TodoWrite to track progress
- Step 7: Generate APKG file
- Step 8: Post-creation verification
- Step 9: Save files

CRITICAL REQUIREMENTS (from /anki):
- Step 3: Extract and LIST all LOs verbatim before creating cards
- LO-filtering: ONLY create cards for LO-mapped content
- EXACT wording from source (no paraphrasing medical terms)
- 3-15 words per answer
- One concept per card
- Post-creation verification: All LOs have at least one flashcard

Output: [Topic]_Flashcards.apkg
```

**Execute completely before proceeding to next format.**

---

#### Other Formats (as specified by --formats flag)

**For each additional format, execute its dedicated command with FULL instructions:**

| Format | Command | Key Requirements |
|--------|---------|------------------|
| `excel-4tab` | /4-tab-excel | 4 tabs, drug inventory, coverage report |
| `excel-master` | /master-chart-excel | Single comprehensive table |
| `html-lo` | /LO-html | 4 tabs, interactive, source-only |
| `html-drugs` | /drugs-html | Drug reference chart |
| `biography` | /autobiography-trick | Personified drug stories |

**Each format must follow its command's FULL template with all steps.**

---

### Step 4: Post-Processing Automation

**Auto-triggered by hook:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-PROCESSING AUTOMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Running post-processing tasks...

[Post-processing-automation agent runs automatically]

✓ Master chart consolidated
  → Pharmacology_Master_Reference.xlsx
  → Added 15 drugs (total: 102 drugs)

✓ QUICK_ACCESS index updated
  → QUICK_ACCESS_Pharmacology.md
  → Indexed 15 new entities

Token cost: ~1,400 tokens
```

---

### Step 4.5: Update Tracker (Directory Mode Only)

**If in directory mode, update `.processed_files.txt` after each file completes:**

```bash
# Append successfully processed file to tracker
tracker_file="$source_dir/.processed_files.txt"

# After each file completes successfully (all formats created):
echo "$filename" >> "$tracker_file"
```

**Tracker file format:**
```
HIV_Drugs.txt
COVID_Drugs.txt
Antibiotics.txt
Beta_Blockers.txt
```

**Benefits:**
- If workflow fails mid-processing, restart will skip completed files
- Run `/batch-status` to see processed vs pending
- Run `/error-recovery-resume` to retry failed files only
- Token savings: ~108k tokens per skipped file (all formats)

**If NOT directory mode, skip this step.**

---

### Step 5: Verification (if --verify flag)

**Only if user specified --verify:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-CREATION VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Running accuracy verification...

[Launches study-guide-analyzer agent for each format]

Verification Results:

✓ Word LO Study Guide: PASS
  - Source accuracy: 100%
  - Template compliance: 100%
  - Completeness: 100%
  - LO text fidelity: 100%

✓ Excel Comparison Chart: PASS
  - Source accuracy: 100%
  - Template compliance: 100%
  - Drug coverage: 15/15 (100%)

✓ Anki Flashcards: PASS
  - Source accuracy: 100%
  - LO coverage: 8/8 (100%)
  - Card count: 127

Analysis reports saved:
  HIV_Drugs_Study_Guide-analysis-report.md
  HIV_Drugs_Comparison_Chart-analysis-report.md
  HIV_Drugs_Flashcards-analysis-report.md

Token cost: ~120k tokens (3 formats × ~40k each)
```

**Note:** Verification is expensive (~40k tokens per format). Only use when needed.

---

### Step 6: Final Summary

**Completion report:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ FULL WORKFLOW COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Source: HIV_Drugs.txt
Course: Pharmacology 3

Study Guides Created (3 formats):
  ✓ HIV_Drugs_Study_Guide.docx (Word LO)
  ✓ HIV_Drugs_Comparison_Chart.xlsx (Excel Comparison)
  ✓ HIV_Drugs_Flashcards.apkg (Anki)

Post-Processing:
  ✓ Master chart consolidated → Pharmacology_Master_Reference.xlsx
  ✓ QUICK_ACCESS updated → QUICK_ACCESS_Pharmacology.md

Verification:
  [If --verify]: ✓ All formats passed accuracy verification
  [If not --verify]: Skipped (use --verify flag to enable)

Token Efficiency:
  Study guides: ~108k tokens
  Post-processing: ~1.4k tokens
  [If --verify]: Verification: ~120k tokens
  ─────────────────────────────
  Total: ~[109.4k or 229.4k] tokens

  vs. Manual Workflow:
  - Separate commands: ~135k tokens
  - Savings: ~26k tokens (19%)

Location: Pharmacology 3/Exam 2/Claude Study Tools/

Reference Files:
  Pharmacology_Master_Reference.xlsx (102 drugs total)
  QUICK_ACCESS_Pharmacology.md (147 entities indexed)

Next Steps:
  ✓ Review study guides
  ✓ Import Anki deck to Anki app
  ✓ Use QUICK_ACCESS.md for fast lookups (Ctrl+F)
  ✓ Study from Word guide, test with Anki

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Format Options

### Available Formats

| Format Name | Output | Command Used |
|-------------|--------|--------------|
| `word` | Word LO study guide | `/LO-word` |
| `excel-4tab` | 4-tab Excel drug chart | `/4-tab-excel` |
| `excel-comparison` | Excel comparison chart | `/key-comparisons-excel` |
| `excel-master` | Excel master chart only | `/master-chart-excel` |
| `anki` | Anki flashcard deck | `/anki` |
| `html-lo` | HTML LO guide | `/LO-html` |
| `html-drugs` | HTML drug reference | `/drugs-html` |
| `biography` | Drug autobiography stories | `/autobiography-trick` |

### Format Presets

**Pharmacology (default):**
```
word, excel-comparison, anki
```
Rationale: Needs memorization (Anki), comparison tables, LO-based study

**Pathophysiology:**
```
word, excel-comparison
```
Rationale: Understanding-focused, less memorization needed

**Clinical Medicine:**
```
word, html-lo
```
Rationale: Quick reference (HTML), comprehensive LO coverage

---

## Example Usage

### Pharmacology (Default Formats)

**Input:**
```
/create-all "HIV_Antivirals.txt"
```

**Creates:**
- HIV_Antivirals_Study_Guide.docx
- HIV_Antivirals_Comparison_Chart.xlsx
- HIV_Antivirals_Flashcards.apkg

**Auto-processing:**
- Updates Pharmacology_Master_Reference.xlsx
- Updates QUICK_ACCESS_Pharmacology.md

---

### Custom Formats

**Input:**
```
/create-all "Beta_Blockers.txt" --formats word,excel-4tab,anki,biography
```

**Creates:**
- Beta_Blockers_Study_Guide.docx
- Beta_Blockers_Drug_Chart.xlsx (4-tab)
- Beta_Blockers_Flashcards.apkg
- Beta_Blockers_Biography.docx

---

### With Verification

**Input:**
```
/create-all "ACE_Inhibitors.txt" --verify
```

**Creates study guides + runs verification:**
- 3 study guides created
- 3 accuracy analysis reports
- Total cost: ~230k tokens (includes verification)

---

### Directory Processing

**Input:**
```
/create-all "Pharmacology 3/Exam 2/Extract/"
```

**Creates:**
- Processes all .txt files in directory
- 3 formats per file
- Auto-consolidation after all files
- Batch status tracking

---

## Token Efficiency

### Workflow Comparison

**Manual workflow (separate commands):**
```
/LO-word "HIV.txt"           → ~48k tokens
/key-comparisons-excel "HIV.txt" → ~38k tokens
/anki "HIV.txt"              → ~22k tokens
Manual consolidation         → ~5k tokens
Manual QUICK_ACCESS update   → ~5k tokens
─────────────────────────────────────────
Total: ~118k tokens
```

**Orchestrated workflow (/create-all):**
```
Integrated processing        → ~108k tokens
Auto post-processing         → ~1.4k tokens
─────────────────────────────────────────
Total: ~109.4k tokens

Savings: ~8.6k tokens (7.3%)
```

**Why savings?**
- Single source read shared across formats
- Mnemonic cache hits (2nd+ format reuses)
- Post-processing runs locally (Python scripts)

---

## Integration with Other Features

**Works seamlessly with:**

1. **Mnemonic Cache**
   - First format: WebSearch mnemonics (~5k tokens)
   - Subsequent formats: Cache hit (~50 tokens)
   - Savings: ~5k tokens per format after first

2. **Post-Processing Automation**
   - Auto-triggered by hook
   - No manual consolidation needed
   - QUICK_ACCESS auto-updates

3. **Error Recovery**
   - If workflow fails mid-processing
   - Run `/error-recovery-resume`
   - Preserves completed formats

4. **Batch Status**
   - Check completion: `/batch-status`
   - See which files processed
   - Identify pending work

---

## Advanced Options

### Format Combinations

**Comprehensive (all formats):**
```
/create-all "source.txt" --formats word,excel-4tab,excel-comparison,excel-master,anki,html-lo,biography
```

Creates 7 different study guide formats.

**Quick reference only:**
```
/create-all "source.txt" --formats excel-master,html-lo
```

Fast to create, good for quick lookups.

**Deep study:**
```
/create-all "source.txt" --formats word,excel-4tab,anki --verify
```

Comprehensive + verification for critical exams.

---

## Error Handling

### Invalid Format Name

```
❌ Error: Unknown format "excel-tabs"

Valid formats:
  word, excel-4tab, excel-comparison, excel-master,
  anki, html-lo, html-drugs, biography

Example:
  /create-all "source.txt" --formats word,excel-4tab,anki
```

---

### Source File Not Found

```
❌ Error: Source file not found
Path: HIV_Drugs.txt

Check:
  1. File path is correct
  2. File exists in specified location
  3. File has .txt or .pdf extension
```

---

### Workflow Interrupted

```
⚠️  Workflow interrupted after format 2/3

Completed formats:
  ✓ HIV_Drugs_Study_Guide.docx
  ✓ HIV_Drugs_Comparison_Chart.xlsx

Pending formats:
  ⏳ Anki flashcards

To resume:
  /error-recovery-resume
```

---

## Best Practices

1. **Use course defaults** - Don't specify --formats unless you need custom bundle
2. **Skip verification normally** - Only use --verify for critical exams (expensive)
3. **Directory mode for batches** - Process entire exam folder at once
4. **Check /batch-status** - Verify completion after directory processing
5. **Let post-processing run** - Don't interrupt consolidation/indexing

---

## Performance

**Single file (3 formats):**
- Time: 3-5 minutes
- Token cost: ~109k tokens
- Approval clicks: ~8-10 (with optimization)

**Directory (10 files, 3 formats each):**
- Time: 30-40 minutes
- Token cost: ~1,090k tokens
- Creates: 30 study guides
- Approval clicks: ~10-15 total (batched)

---

## When to Use This Command

**Use /create-all when:**
- ✓ Want multiple formats from same source
- ✓ Need comprehensive study materials
- ✓ Processing entire exam folder
- ✓ Want automation (consolidation, indexing)

**Use individual commands when:**
- ✗ Only need one specific format
- ✗ Want granular control over each format
- ✗ Testing/debugging format creation

---

## Notes

- Post-processing runs automatically (hook-triggered)
- Verification optional but expensive (~40k tokens per format)
- Format defaults per course (Pharmacology vs Clinical Medicine)
- Directory mode uses batch tracking (`.processed_files.txt`)
- Mnemonic cache reduces redundant WebSearch
- Error recovery available if workflow fails
