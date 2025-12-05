---
description: Create comprehensive Word study guide from source material following template
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Word study guide from: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single / Batch Separate / Batch Merge)

**Parse arguments to detect mode:**

**Check for --merge flag:**
- If $ARGUMENTS starts with `--merge`: **BATCH MERGE MODE**
- Strip `--merge` from arguments to get file list

**Check for semicolons:**
- If $ARGUMENTS contains semicolons (`;`): **BATCH SEPARATE MODE**
- Split by semicolon to get file list

**Otherwise: SINGLE MODE**

**State which mode detected:**
```
MODE DETECTED: [SINGLE / BATCH SEPARATE / BATCH MERGE]
File count: [#]
Files: [list]
```

**Mode Descriptions:**
- **SINGLE**: 1 file → 1 Word guide (inline processing)
- **BATCH SEPARATE**: N files → N Word guides (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Word guide (orchestrator agent, intelligent merge)

---

### Step 0.5: Handle Directory Input

If $ARGUMENTS is a directory, process all .txt/.pdf files within it.
If batch (semicolon-separated), process each path independently.

---

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Instruction template: Word_LO_11-5_REVISED.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
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
☐ Template: Word_LO_11-5_REVISED.txt (per file)
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
☐ Template: Word_LO_11-5_REVISED.txt (unified)
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
   - Complete 4-section implementation with all helper functions
   - Shows Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary

### Step 3: Read Source File

- Read the complete source file: $ARGUMENTS
- Identify all learning objectives
- Note all topics, conditions, drugs mentioned
- Extract key information for each learning objective

### Step 4: Create Study Guide

Follow template instructions EXACTLY:

**Required Structure (4 sections):**
1. Learning Objectives - Each with summary, tables, boxes, mnemonics
2. Key Comparisons - Side-by-side comparison tables
3. Master Chart - Comprehensive table of all topics
4. High-Yield Summary - Color-coded boxes by category

**Key Requirements:**
- Use ONLY source file information (except mnemonics)
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
MANDATORY TEMPLATE REQUIREMENTS - Word Learning Objectives (4 sections):

STRUCTURE:
- Section 1 "Learning Objectives": Each LO with Summary + Tables + Pearls Box + Mnemonics Box + Analogy Box
  - Page break after each LO
- Section 2 "Key Comparisons": Comparison tables for 2+ similar items
- Section 3 "Master Chart": ALL conditions/topics from source, color-coded rows
- Section 4 "High-Yield Summary": Color-coded boxes grouped by category

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
  - Memory Tricks: Orange title (230, 81, 0), #FFF3E0 background
  - Normal Variants: Green title (27, 94, 32), #E8F5E9 background
</template-compliance>

**WebSearch Requirements (MANDATORY):**
- Research mnemonics for each learning objective
- Find analogies for drug mechanisms/complex concepts
- Look for "If X think Y" clinical associations
- Use PROVEN mnemonics only - never invent

### Step 5: Use TodoWrite

Track your progress:
- Create todo for each learning objective
- Mark in_progress as you work
- Mark completed when done
- Keep user informed

### Step 6: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 4 sections present: Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary
☐ Section names correct
☐ Section 1: Each LO has Summary + Tables + Pearls Box + Mnemonics Box + Analogy Box
☐ Section 1: Page break after each LO
☐ Section 2: Comparison tables for 2+ similar items
☐ Section 3: ALL conditions/topics from source in one table
☐ Section 3: Color-coded rows by category
☐ Section 4: Color-coded boxes grouped by category

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
  - Memory Tricks: Orange title (230, 81, 0), #FFF3E0 background
  - Normal Variants: Green title (27, 94, 32), #E8F5E9 background

**Source Accuracy:**
☐ All info from source only (except researched mnemonics)
☐ External additions marked with asterisk (*)
☐ No page references in Word docs
☐ Learning objective STATEMENTS verbatim (not paraphrased)

**Completeness:**
☐ ALL learning objectives from source included
☐ All LOs answered (all parts)
☐ All comparisons created for 2+ similar items
☐ Master chart complete with all conditions/topics
☐ Mnemonics researched via WebSearch (not invented)

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

### Step 7: Save Files

**Naming Convention:** Use source filename with new extension (e.g., `1 ANS.txt` → `1 ANS.docx`)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[SourceFileName].docx`
- Example: Source `1 ANS.txt` → Output `1 ANS.docx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[SourceFileName].py`
- Example: Source `1 ANS.txt` → Output `py/1 ANS.py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

---

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

❌ Paraphrasing learning objective statements (must be verbatim)
❌ Missing page breaks between learning objectives
❌ Using wrong box colors (e.g., using purple for Clinical Pearls)
❌ Inventing mnemonics instead of researching via WebSearch
❌ Missing sections (must have all 4 sections)
❌ Adding external medical information not in source

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 4 sections: Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary
✓ Each LO has Summary, Tables, Pearls Box, Mnemonics Box, Analogy Box
✓ Page break after each learning objective
✓ Comparison tables for similar conditions (Type I vs Type II diabetes)

**Formatting:**
✓ Clinical Pearls box: Teal title (0, 77, 64), #E0F2F1 background
✓ Memory Tricks box: Orange title (230, 81, 0), #FFF3E0 background
✓ High-Yield box: Purple title (118, 75, 162), #F3E5F5 background
✓ Section headings: Purple (118, 75, 162)
✓ Font: Calibri size 12

**Learning Objective Statements:**
✓ Source: "1. Describe the mechanism of action of beta-blockers"
✓ Guide:  "1. Describe the mechanism of action of beta-blockers"
✓ Status: VERBATIM - correct

### INCORRECT Implementation:

**Structure:**
✗ Only 3 sections (missing High-Yield Summary)
✗ No page breaks between learning objectives
✗ Missing Analogy boxes
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
/LO-word "Pharmacology/Exam 3/Extract/Lecture 42.txt"
```
Creates: `Lecture_42_LO_Guide.docx`

### Batch Separate (N files → N outputs):
```
/LO-word "Lecture42.txt;Lecture43.txt;Lecture44.txt"
```
Creates 3 separate Word files:
- `Lecture_42_LO_Guide.docx` (only Lecture 42 content)
- `Lecture_43_LO_Guide.docx` (only Lecture 43 content)
- `Lecture_44_LO_Guide.docx` (only Lecture 44 content)

Uses batch-separate-processor agent with architectural isolation.

### Batch Merge (N files → 1 merged output):
```
/LO-word --merge "Cardio-Lec1.txt;Cardio-Lec2.txt;Cardio-Lec3.txt"
```
Creates 1 merged Word file:
- `Cardiovascular_Comprehensive_LO_Guide.docx` (all 3 lectures merged)
- `Cardiovascular_Comprehensive_LO_Guide_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge and overlap resolution.
