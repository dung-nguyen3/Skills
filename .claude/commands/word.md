---
description: Create comprehensive Word study guide from source material following template
argument-hint: Single file OR batch files separated by semicolon (e.g., "file1.txt" OR "file1.txt;file2.txt")
---

Create Word study guide from: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single vs Batch)

**Parse arguments:** If $ARGUMENTS contains `;` → BATCH MODE (multiple files), otherwise SINGLE MODE.

**State mode:** MODE DETECTED: [SINGLE/BATCH], File count: [#], Files: [list]

---

### Step 1: Pre-Creation Verification

#### For SINGLE MODE:
```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Instruction template: Word LO 11-5.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

#### For BATCH MODE:
```
BATCH VERIFICATION CHECKLIST:
☐ Source files: [list all]
☐ File validation: All exist and readable
☐ Homogeneity: All are learning objective-based lectures
☐ Template: Word LO 11-5.txt (applies to ALL)
☐ Source-only policy confirmed
☐ WebSearch for mnemonics (mandatory)
☐ Output: ONE Word file per source
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

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

### Step 6: Post-Creation Verification

**Automatically verify the completed document:**

1. **Source Accuracy**
   - All info from source only (except mnemonics)
   - External additions marked with *
   - No page references

2. **Template Compliance**
   - All 4 sections present
   - Correct colors (soft pastels)
   - All required elements included

3. **Completeness**
   - All LOs answered (all parts)
   - All comparisons created
   - Master chart complete

4. **Quality**
   - No incorrect groupings
   - No spelling errors
   - Proper formatting

**CRITICAL: State "Post-creation verification complete" and report any issues. Fix immediately.**

### Step 7: Save File

- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Study_Guide.docx`
- Create Claude Study Tools folder if doesn't exist
- Confirm file saved successfully

---

### Step 8: Batch Processing (BATCH MODE ONLY)

If BATCH MODE, repeat Steps 2-7 for EACH file with progress tracking and batch summary at end.

## Example Usage

**Single:** `/word "Pharmacology/Exam 3/Extract/Lecture 42.txt"`

**Batch:** `/word "Lecture42.txt;Lecture43.txt;Lecture44.txt"` → Creates 3 separate Word files.
