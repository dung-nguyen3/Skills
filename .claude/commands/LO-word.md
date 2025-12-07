---
description: Create comprehensive Word study guide from source material following template
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Word study guide from: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single / Batch Separate / Batch Merge)

**Parse arguments to detect mode:**

**Step 0.1: Check if input is a directory**
- If $ARGUMENTS is a directory path:
  - List all .txt/.pdf files in directory (non-recursive)
  - Count files found
  - Store file list for later use
  - **Important**: Continue to Step 0.2 with file count information

**Step 0.2: Check for --merge flag**
- If $ARGUMENTS starts with `--merge`: **BATCH MERGE MODE**
- Strip `--merge` from arguments to get file list

**Step 0.3: Check for semicolons**
- If $ARGUMENTS contains semicolons (`;`): **BATCH SEPARATE MODE**
- Split by semicolon to get file list

**Step 0.4: Check directory file count (from Step 0.1)**
- If directory with 0 files: **ERROR** - "No .txt/.pdf files found in directory"
- If directory with 1 file: **SINGLE MODE** - Process that one file
- If directory with 2+ files: **BATCH SEPARATE MODE** - Process all files independently

**Step 0.5: Otherwise SINGLE MODE**
- Single file path with no special flags

**State which mode detected:**
```
MODE DETECTED: [SINGLE / BATCH SEPARATE / BATCH MERGE]
File count: [#]
Files: [list]
Source: [directory (auto-detected batch) / semicolon-separated / single file]
```

**Mode Descriptions:**
- **SINGLE**: 1 file → 1 Word guide (inline processing)
- **BATCH SEPARATE**: N files → N Word guides (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Word guide (orchestrator agent, intelligent merge)

---

### Step 0.8: Learning Objective Inventory (SINGLE MODE ONLY)

**Skip this step for BATCH modes** (agents handle their own counting).

**Before creating content, extract ALL LO statements from source:**

1. Scan source file for Learning Objectives section
2. Extract each LO statement verbatim
3. Number them sequentially
4. Document the count

**Output format:**
```
LEARNING OBJECTIVE INVENTORY
Source: [filename]
Total LOs found: [N]

1. [LO statement 1]
2. [LO statement 2]
3. [LO statement 3]
...
N. [LO statement N]
```

**Keep this list for verification at end (Step 10).**

---

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Instruction template: Word LO 11-5.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then proceed with Step 2 (inline processing).**

---

#### For BATCH SEPARATE MODE:

**MANDATORY - State this checklist:**

```
BATCH SEPARATE VALIDATION:
☐ Source files: [list all files]
☐ File validation: All files exist and are readable
☐ Homogeneity check: All files are learning objective lectures
☐ Template: Word LO 11-5.txt (per file)
☐ Output: N files → N Word guides
☐ Agent: batch-separate-processor (launched N times)
☐ Architectural isolation: Each file processed in separate agent context
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-separate-processor agent:**

```
I'll use the batch-separate-processor agent to process your files with architectural isolation.

Launching agent [X] times:
- File 1: batch-separate-processor → [Output1.docx]
- File 2: batch-separate-processor → [Output2.docx]
...
- File N: batch-separate-processor → [OutputN.docx]

Each agent invocation is architecturally isolated (zero cross-contamination).
```

**STOP HERE - Do NOT continue with Steps 2-7. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ File validation: All files exist and are readable
☐ Files are related/compatible for merging
☐ Template: Word LO 11-5.txt (unified)
☐ Output: N files → 1 merged Word guide
☐ Agent: batch-merge-orchestrator (launched once)
☐ Merge features: Content matrix, overlap resolution, source traceability
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent:**

```
I'll use the batch-merge-orchestrator agent to intelligently merge your files.

Agent will:
1. Read all N files completely
2. Create content matrix (which topics/LOs in which files)
3. Identify overlaps and gaps
4. Resolve conflicts with source traceability
5. Merge into ONE comprehensive Word guide
6. Create merge report with traceability map

Output:
- 1 merged Word guide: [filename.docx]
- 1 merge report: [filename_merge_report.md]
```

**STOP HERE - Do NOT continue with Steps 2-7. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-7)
- Do NOT mix - if agent is launched, STOP and let agent complete the work

### Step 2: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/Word_LO_11-5_REVISED.txt`
   - Main instructions and requirements (~450 lines)
   - Includes correct table formatting (black text on pastel backgrounds)

2. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Word_LO_Example.py`
   - Complete 2-section implementation with all helper functions
   - Shows Learning Objectives and Key Comparisons

### Step 3: Read Source File

- Read the complete source file: $ARGUMENTS
- Identify all learning objectives
- Note all topics, conditions, drugs mentioned
- Extract key information for each learning objective

### Step 4: Create Study Guide

Follow template instructions EXACTLY:

**Required Structure (2 sections):**
1. Learning Objectives - Each with summary, tables, boxes
2. Key Comparisons - Side-by-side comparison tables

**Key Requirements:**
- Use ONLY source file information
- Answer ALL parts of each learning objective
- Create comparison tables for 2+ similar items
- Use soft pastel color scheme from template
- NO page references in Word docs
- Font: Calibri size 12

<verbatim-requirement>
CRITICAL: Learning objective STATEMENTS must be copied EXACTLY as they appear in the source.
- Copy word-for-word, character-for-character
- Do NOT rephrase, summarize, or "improve" wording
- Preserve original numbering and sequence
- If an LO is long, still copy it completely
Note: Answers/explanations CAN be paraphrased from source content.
</verbatim-requirement>

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Word Learning Objectives (2 sections):

STRUCTURE:
- Section 1 "Learning Objectives": Each LO with Summary + Tables + Pearls Box
  - Page break after each LO
- Section 2 "Key Comparisons": Comparison tables for 2+ similar items

FORMATTING (MANDATORY):
- Font: Calibri size 12 (11 for dense tables)
- Table style: 'Table Grid'
- Margins: 0.8 inches all sides
- Headings: Purple (118, 75, 162)
- Table headers: Bold, colored background (pastel)
- Table data cells: Black text, white background
- Color-coded boxes:
  - High-Yield Box: Purple title (118, 75, 162), #F3E5F5 background
  - Clinical Pearls: Teal title (0, 77, 64), #E0F2F1 background
  - Critical/Emergency: Red title (183, 28, 28), #FFEBEE background
  - Normal Variants: Green title (27, 94, 32), #E8F5E9 background
</template-compliance>

### Step 5: Use TodoWrite

Track your progress:
- Create todo for each learning objective
- Mark in_progress as you work
- Mark completed when done
- Keep user informed

### Step 6: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 2 sections present: Learning Objectives, Key Comparisons
☐ Section names correct
☐ Section 1: Each LO has Summary + Tables + Pearls Box
☐ Section 1: Page break after each LO
☐ Section 2: Comparison tables for 2+ similar items

**Formatting Compliance:**
☐ Font: Calibri size 12 (11 for dense tables)
☐ Table style: 'Table Grid'
☐ Margins: 0.8 inches all sides
☐ Section headings: Purple (118, 75, 162)
☐ Table headers: Bold, colored background (pastel)
☐ Table data cells: Black text, white background
☐ Color-coded boxes use correct colors:
  - High-Yield: Purple title (118, 75, 162), #F3E5F5 background
  - Clinical Pearls: Teal title (0, 77, 64), #E0F2F1 background
  - Critical/Emergency: Red title (183, 28, 28), #FFEBEE background
  - Normal Variants: Green title (27, 94, 32), #E8F5E9 background

**Source Accuracy:**
☐ All info from source only
☐ External additions marked with asterisk (*)
☐ No page references in Word docs
☐ Learning objective STATEMENTS verbatim (not paraphrased)

**Completeness:**
☐ ALL learning objectives from source included
☐ All LOs answered (all parts)
☐ All comparisons created for 2+ similar items

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

### Step 7: Save Files

**Output Filename Rule:**
1. Strip file extension and common suffixes (`_text.txt`, `_extracted.txt`, etc.)
2. Strip course prefixes (`Micro_`, `Pharm_`, `Clinical_`, `Patho_`, etc.)
3. Replace underscores with spaces for readability
4. Extract lecture number and topic: `[Number] [Topic]` or just `[Topic]`
5. Preserve capitalization as-is (after underscore→space conversion)
6. Add appropriate extension: `.docx` for Word, `.py` for Python
7. NO template suffixes, NO title case normalization

**Examples:**
- `Micro_4 Intro to Virology_text.txt` → `4 Intro to Virology.docx`
- `Pharm_11 Beta Blockers_text.txt` → `11 Beta Blockers.docx`
- `Micro_4_Intro_To_Virology_text.txt` → `4 Intro To Virology.docx`
- `Micro_Basics Of Immunology_text.txt` → `Basics Of Immunology.docx`

**Batch Merge Naming:**
- Input: `Micro_4 Intro to Virology_text.txt` + `Micro_5 Viral Replication_text.txt`
- Output: `Lecture 4-5.docx`
- Format: `Lecture [min]-[max].docx` (based on lecture numbers found)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[OutputFilename].docx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[OutputFilename].py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

### Step 8: LO Coverage Report (SINGLE MODE ONLY)

**Compare LOs included vs LO Inventory from Step 0.8:**

1. Count LOs actually included in the Word guide
2. Compare against inventory list from Step 0.8
3. Calculate coverage percentage
4. Identify any missing LOs

**MANDATORY OUTPUT:**
```
---
LO COVERAGE REPORT
Source LOs: [N] (from inventory)
Included LOs: [M]
Coverage: [M/N] ([percentage]%)

[If 100%]: ✓ All learning objectives from source included.
[If <100%]: ⚠️ MISSING LOs: [list missing LO numbers and statements]
---
```

**If coverage < 100%:** Fix immediately before completing. Add missing LOs to document.

---

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

❌ Paraphrasing learning objective statements (must be verbatim)
❌ Missing page breaks between learning objectives
❌ Using wrong box colors (e.g., using purple for Clinical Pearls)
❌ Missing sections (must have all 3 sections)
❌ Adding external medical information not in source

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 2 sections: Learning Objectives, Key Comparisons
✓ Each LO has Summary, Tables, Pearls Box
✓ Page break after each learning objective
✓ Comparison tables for similar conditions (Type I vs Type II diabetes)

**Formatting:**
✓ Clinical Pearls box: Teal title (0, 77, 64), #E0F2F1 background
✓ High-Yield box: Purple title (118, 75, 162), #F3E5F5 background
✓ Section headings: Purple (118, 75, 162)
✓ Font: Calibri size 12

**Learning Objective Statements:**
✓ Source: "1. Describe the mechanism of action of beta-blockers"
✓ Guide:  "1. Describe the mechanism of action of beta-blockers"
✓ Status: VERBATIM - correct

### INCORRECT Implementation:

**Structure:**
✗ Only 1 section (missing Key Comparisons)
✗ No page breaks between learning objectives
✗ No comparison tables for similar items

**Formatting:**
✗ Clinical Pearls box using purple instead of teal ← WRONG
✗ All boxes same color ← WRONG
✗ Random colors not matching template ← WRONG
✗ Section headings in black instead of purple ← WRONG
✗ Font: Arial instead of Calibri ← WRONG

**Learning Objective Statements:**
✗ Source: "1. Describe the mechanism of action of beta-blockers"
✗ Guide:  "1. Explain how beta-blockers work"
✗ Status: PARAPHRASED - must use exact wording from source

---

## Example Usage

### Single File:
```
/LO-word "Pharmacology/Exam 3/Extract/Pharm_42 Beta Blockers_text.txt"
```
Creates: `42 Beta Blockers.docx`

### Batch Separate (N files → N outputs):
```
/LO-word "Micro_4 Intro to Virology_text.txt;Micro_5 Viral Replication_text.txt;Micro_6 Viral Pathogenesis_text.txt"
```
Creates 3 separate Word files:
- `4 Intro to Virology.docx` (only Lecture 4 content)
- `5 Viral Replication.docx` (only Lecture 5 content)
- `6 Viral Pathogenesis.docx` (only Lecture 6 content)

Uses batch-separate-processor agent with architectural isolation.

### Batch Merge (N files → 1 merged output):
```
/LO-word --merge "Micro_4 Intro to Virology_text.txt;Micro_5 Viral Replication_text.txt;Micro_6 Viral Pathogenesis_text.txt"
```
Creates 1 merged Word file:
- `Lecture 4-6.docx` (all 3 lectures merged)
- `Lecture 4-6_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge and overlap resolution.
