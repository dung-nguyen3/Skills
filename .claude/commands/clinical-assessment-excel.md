---
description: Create 4-tab Excel clinical assessment chart with onset-based categorization
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Excel clinical assessment chart from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 clinical assessment chart (inline processing)
- **BATCH SEPARATE**: N files → N clinical assessment charts (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged clinical assessment chart (orchestrator agent, intelligent merge)

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
☐ Physical Assessment Template: WILL AUTO-INCLUDE (H&P reference)
☐ Instruction template: Excel_Clinical_Assessment_Chart_REVISED.txt
☐ Source-only policy: I will ONLY use information from source file
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
☐ Physical Assessment Template: WILL AUTO-INCLUDE for each
☐ File validation: All files exist and are readable
☐ Template: Excel_Clinical_Assessment_Chart_REVISED.txt (per file)
☐ Output: N files → N clinical assessment charts
☐ Agent: batch-separate-processor (launched N times)
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-separate-processor agent.**

**STOP HERE - Do NOT continue with Steps 2-9. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ Physical Assessment Template: WILL AUTO-INCLUDE once
☐ File validation: All files exist and are readable
☐ Files are related/compatible for merging (same clinical topic)
☐ Template: Excel_Clinical_Assessment_Chart_REVISED.txt (unified)
☐ Output: N files → 1 merged clinical assessment chart
☐ Agent: batch-merge-orchestrator (launched once)
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent.**

**STOP HERE - Do NOT continue with Steps 2-9. The agent handles all processing.**

---

### Step 2: Load Resources

Read these files in order:

1. **Physical Assessment Template** (AUTO-INCLUDE - always read first):
   `/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Claude instructions/Templates claude/Physical Assessment Template/Complete Medical History Card.txt`
   - Provides H&P structure: OLD CAARTS, PMH, FH, SH, ROS
   - Use as reference for clinical exam categories

2. **Template**: `study-guides/templates-and-examples/Excel_Clinical_Assessment_Chart_REVISED.txt`
   - Main instructions and requirements for clinical charts

3. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Excel_Clinical_Assessment_Example.py`
   - Complete 3-tab implementation with onset-based categorization
   - Shows Key Comparisons, Master Chart (7 columns), Summary tabs

4. **Color Reference**: `study-guides/templates-and-examples/Excel_Color_Reference.txt`
   - Shared color palette and styling specifications

### Step 3: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL clinical conditions mentioned (don't skip any)
- Categorize each by ONSET pattern:
  - Acute (emergencies, immediate)
  - Acute/Subacute (days to weeks)
  - Subacute (weeks)
  - Chronic (months to years)
  - Chronic Inflammatory (chronic with inflammatory component)
- Note clinical presentations, PE findings, diagnosis, treatment
- Identify conditions that need side-by-side comparison
- Look for red flags and emergency conditions

### Step 4: Create 4-Tab Excel Chart

**Required Tabs:**

**Tab 1: Key Comparisons**
- Multiple side-by-side comparison tables for clinical differentials
- ONE comparison per table (don't combine)
  - Example: Inflammatory vs Mechanical, LMN vs UMN, Condition A vs B
- Columns = conditions being compared
- Rows = clinical comparison categories
- Mnemonics placed directly BELOW relevant tables
- 2-3 blank rows between different comparison tables

**Tab 2: Master Chart (7 Clinical Columns)**
- ALL conditions in one comprehensive table
- **REQUIRED COLUMNS:**
  1. Condition (bold)
  2. Category/Onset
  3. Clinical Presentation
  4. Physical Exam Findings
  5. Diagnosis/Imaging
  6. Treatment
  7. Patient Education
- Conditions grouped by onset (Acute first, then Chronic)
- Color-coded by onset category (NOT random)
- Frozen header row AND condition column

**Tab 3: H&P Guide (Comprehensive Clinical Encounter Guide)**
- **HISTORY: OLDCAARTS** - Chief complaint focused questions
- **PMH/FH/SH** - Past Medical, Family, Social History
- **ROS** - Review of Systems (relevant systems)
- **PHYSICAL EXAM** - Inspection, Palpation, ROM, Neuro, Special Tests (with verbalizations)
- **PATIENT EDUCATION** - Disease process, management, lifestyle, medication risks
- **RED FLAGS / WHEN TO RETURN** - Emergency signs, when to seek care

**Tab 4: Summary**
- Mnemonics (researched, with full breakdown)
- "If X Think Y" clinical associations
- **RED FLAGS section (REQUIRED)** - urgent evaluation criteria
- High-yield pearls

**Critical Requirements:**
- Use ONLY source file information (plus Physical Assessment Template for structure)
- ALL data cells have soft pastel backgrounds
- Research mnemonics via WebSearch (mandatory)
- Onset-based color coding (not generic category)

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Excel Clinical Assessment Chart (4 tabs):

STRUCTURE:
- Tab 1 "Key Comparisons": MULTIPLE tables (one comparison per table)
  - Clinical differentials for exam preparation
  - Mnemonics placed DIRECTLY BELOW relevant tables
- Tab 2 "Master Chart": 7 REQUIRED COLUMNS, onset-based grouping
  - Condition, Category, Presentation, PE, Dx, Tx, Education
  - Header frozen, conditions grouped by onset
- Tab 3 "H&P Guide": Comprehensive clinical encounter guide
  - OLDCAARTS history, PMH/FH/SH, ROS, Physical Exam (with verbalizations), Patient Education, Red Flags
- Tab 4 "Summary": MUST INCLUDE RED FLAGS SECTION
  - Mnemonics, "If X Think Y", Red Flags, High-Yield Pearls

ONSET-BASED COLORS (Master Chart):
- Acute: #FCE4EC (Blush Pink) - emergencies
- Acute/Subacute: #FFE8D6 (Soft Tangerine)
- Subacute: #F7E7CE (Champagne)
- Chronic: #C8E6C9 (Seafoam)
- Chronic Inflammatory: #BDD7EE (Sky Blue)

FORMATTING (MANDATORY):
- Header row: #4472C4 (dark blue), white bold text, size 12
- Data rows: Pastel colors based on ONSET category
- All conditions with same onset = same color
- White borders (#FFFFFF) on all cells
- Text wrapping enabled
- Column widths: A=28, B=18, C-G=38-45
</template-compliance>

### Step 5: WebSearch for Mnemonics

**MANDATORY - Research established mnemonics:**
- Search: "medical mnemonics [topic]"
- Search: "[condition] mnemonic USMLE"
- Find PROVEN mnemonics only - never invent
- Add mnemonic row after each comparison table
- Include full breakdown/explanation

### Step 6: Python Implementation

Use openpyxl to create the Excel file:
- Onset-based color scheme (hex codes from template)
- ALL cells get background colors (not just first column)
- Expand row heights to fit content
- Set appropriate column widths (7 columns)
- Black text throughout (#000000)
- Use emojis: ⭐ (hallmark), ⚠️ (warning), 🟢 (first-line), ❗ (critical), ✅ (positive)

### Step 7: Use TodoWrite

Track your progress:
- Create todo for each comparison table
- Create todo for Master Chart (all onset categories)
- Create todo for Summary sections (including Red Flags)
- Mark completed as you finish

### Step 8: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 4 tabs present: Key Comparisons, Master Chart, H&P Guide, Summary
☐ Tab names correct
☐ Tab 1: MULTIPLE comparison tables (one per comparison)
☐ Tab 1: Mnemonics DIRECTLY BELOW relevant tables
☐ Tab 2: ALL 7 columns present (Condition, Category, Presentation, PE, Dx, Tx, Education)
☐ Tab 2: Conditions grouped by ONSET category
☐ Tab 2: Header frozen
☐ Tab 3: H&P Guide with OLDCAARTS, PMH/FH/SH, ROS, Physical Exam, Patient Education, Red Flags
☐ Tab 4: RED FLAGS section present (REQUIRED)
☐ Tab 4: Mnemonics, "If X Think Y", High-yield pearls present

**Formatting Compliance:**
☐ Header row: Dark blue (#4472C4), white bold text, size 12
☐ ALL data cells have pastel background (NOT white/no fill)
☐ Onset-based color coding (Acute=pink, Chronic=seafoam, etc.)
☐ Same onset = same color throughout
☐ White borders (#FFFFFF) on all cells
☐ Text wrapping enabled
☐ Column widths appropriate (28-45)

**Source Accuracy:**
☐ All information from source file only
☐ Physical Assessment Template used for H&P structure reference
☐ No external medical facts added
☐ Terminology matches source exactly

**Completeness:**
☐ ALL conditions from source included
☐ All onset categories represented
☐ Red Flags section complete
☐ Mnemonics researched via WebSearch (not invented)

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

### Step 9: Save Files

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Clinical_Assessment_Chart.xlsx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[Topic]_Clinical_Assessment_Chart.py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

---

## Common Mistakes to Avoid

❌ Missing H&P Guide tab (Tab 3)
❌ Missing Red Flags section in Summary tab
❌ Using generic category colors instead of onset-based colors
❌ Not grouping conditions by onset in Master Chart
❌ Missing the 7 required columns (especially Patient Education)
❌ Inventing mnemonics instead of researching
❌ Not reading Physical Assessment Template first
❌ White backgrounds on data cells (should be pastel)
❌ H&P Guide missing OLDCAARTS, PMH/FH/SH, ROS, or Patient Education sections

---

## Example Usage

### Single File:
```
/excel-clinical "Clinical Medicine/Exam 2/Extract/Back_Pain.txt"
```
Creates: `Back_Pain_Clinical_Assessment_Chart.xlsx`

### Single Directory:
```
/excel-clinical "/Users/name/Documents/ClinMed/Exam 2/Extract"
```
Finds all readable files, processes in batch separate mode.

### Batch Separate (N files → N outputs):
```
/excel-clinical "BackPain.txt;HeadachePain.txt;ChestPain.txt"
```
Creates 3 separate clinical assessment charts.

### Batch Merge (N files → 1 merged output):
```
/excel-clinical --merge "Rheumatology.txt;Orthopedics.txt;Neurology.txt"
```
Creates 1 merged clinical assessment chart with all conditions.
