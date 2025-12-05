---
description: Create multi-format study bundle (Word LO + Excel Comparison + Anki) from source
argument-hint: Single file, batch files separated by semicolon, or directory path (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir")
---

Create a multi-format study bundle from source file: $ARGUMENTS

This command generates 3 complementary formats by invoking individual commands:
1. Word LO Study Guide (.docx) - via /LO-word
2. Excel Comparison Chart (.xlsx) - via /key-comparisons-excel
3. Anki Flashcard Deck (.apkg) - via /anki

**Architecture:** Each format is created using its dedicated command with FULL instructions.
This ensures identical output quality whether you run this bundle or individual commands.

## Instructions

### Step 0: Detect Mode

**Parse arguments to detect mode:**

**Check for semicolons:**
- If $ARGUMENTS contains semicolons (`;`): **BATCH MODE**
- Split by semicolon to get file list

**Otherwise: SINGLE MODE**

**State which mode detected:**
```
MODE DETECTED: [SINGLE / BATCH]
File count: [#]
Files: [list]
```

---

### Step 0.5: Handle Directory Input

If $ARGUMENTS is a directory, process all .txt/.pdf files within it.
If batch (semicolon-separated), process each path independently.

---

### Step 1: Pre-Creation Verification

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file(s): $ARGUMENTS
☐ Formats: Word LO + Excel Comparison + Anki (3 formats)
☐ Method: Individual command invocation (full instructions per format)
☐ Commands to invoke:
   1. /LO-word - Full 376-line template with LO tracking
   2. /key-comparisons-excel - Full 408-line template with comparison tables
   3. /anki - Full 266-line template with LO extraction
☐ Source-only policy: Each command enforces source-only
☐ Learning objectives: Each command extracts LOs EXACTLY as written
☐ Exception: Memory tricks/mnemonics researched via WebSearch (per command)
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

---

### Step 2: Process Each Format Sequentially

**CRITICAL: Invoke each command with FULL execution, not abbreviated.**

Each command below must be executed completely, following ALL steps in that command's template.
Do NOT skip steps or summarize - execute as if user ran the command directly.

---

#### Format 1/3: Word LO Study Guide

**Invoke /LO-word with source file:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT 1/3: WORD LO STUDY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing /LO-word "$ARGUMENTS"

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

**Execute /LO-word completely before proceeding to Format 2.**

---

#### Format 2/3: Excel Comparison Chart

**Invoke /key-comparisons-excel with source file:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT 2/3: EXCEL COMPARISON CHART
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing /key-comparisons-excel "$ARGUMENTS"

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

**Execute /key-comparisons-excel completely before proceeding to Format 3.**

---

#### Format 3/3: Anki Flashcard Deck

**Invoke /anki with source file:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT 3/3: ANKI FLASHCARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing /anki "$ARGUMENTS"

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

**Execute /anki completely.**

---

### Step 3: Bundle Completion Report

**After all 3 formats complete:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ MULTI-FORMAT BUNDLE CREATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Source: [filename]
Formats generated: 3

Outputs:
1. [filename]_Study_Guide.docx (Word LO)
   - Learning objectives: [N]
   - Sections: 4 (LOs, Comparisons, Master Chart, High-Yield)

2. [filename]_Comparison_Chart.xlsx (Excel Comparison)
   - Comparison tables: [N]
   - Tabs: 3 (Key Comparisons, Master Chart, Summary)

3. [filename]_Flashcards.apkg (Anki)
   - Total cards: [N]
   - LOs covered: [N]

Location: [Class]/[Exam]/Claude Study Tools/

Quality Assurance:
✓ Each format used its dedicated command with full instructions
✓ Learning objectives extracted and tracked per format
✓ Source-only policy enforced per format
✓ Post-creation verification completed per format

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Batch Processing

**For batch mode (semicolon-separated files):**

Process each file independently:
1. File 1: Execute all 3 formats (Steps 2.1-2.3)
2. File 2: Execute all 3 formats (Steps 2.1-2.3)
3. ...continue for all files

**Each file gets complete processing with full command execution.**

---

## Why This Architecture

**Previous approach (multi-format-processor agent):**
- Sparse instructions delegated to agent
- Missing LO enumeration step
- Missing TodoWrite per LO tracking
- Skipped learning objectives

**Current approach (individual command invocation):**
- Each format uses its full dedicated command
- Identical output whether running bundle or individual commands
- All verification steps enforced
- All LO tracking in place

**Trade-off:** Slightly more tokens used, but guaranteed accuracy and completeness.

---

## Example Usage

**Single:**
```
/word-excel-anki "Pharmacology/Exam 3/Extract/HIV_Drugs.txt"
```

**Batch:**
```
/word-excel-anki "HIV.txt;Antibiotics.txt;Antivirals.txt"
```

**Directory:**
```
/word-excel-anki "Pharmacology/Exam 3/Extract/"
```

---

## Format Defaults

This command always creates: Word LO + Excel Comparison + Anki

For different format combinations, use:
- `/create-all` with --formats flag
- `/study-guides` for interactive format selection

---

**End of Command**
