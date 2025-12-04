---
description: Create 3-tab Excel comparison chart for any medical topic (conditions, mechanisms, concepts)
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Excel comparison chart from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 comparison chart (inline processing)
- **BATCH SEPARATE**: N files → N comparison charts (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged comparison chart (orchestrator agent, intelligent merge)

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
☐ Instruction template: Excel_Comparison_Chart_REVISED.txt
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
☐ Homogeneity check: All files are medical content suitable for comparison
☐ Template: Excel_Comparison_Chart_REVISED.txt (per file)
☐ Output: N files → N comparison charts
☐ Agent: batch-separate-processor (launched N times)
☐ Architectural isolation: Each file processed in separate agent context
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-separate-processor agent:**

```
I'll use the batch-separate-processor agent to process your files with architectural isolation.

Launching agent [X] times:
- File 1: batch-separate-processor → [Output1.xlsx]
- File 2: batch-separate-processor → [Output2.xlsx]
...
- File N: batch-separate-processor → [OutputN.xlsx]

Each agent invocation is architecturally isolated (zero cross-contamination).
```

**STOP HERE - Do NOT continue with Steps 2-9. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ File validation: All files exist and are readable
☐ Files are related/compatible for merging
☐ Template: Excel_Comparison_Chart_REVISED.txt (unified)
☐ Output: N files → 1 merged comparison chart
☐ Agent: batch-merge-orchestrator (launched once)
☐ Merge features: Content matrix, overlap resolution, source traceability
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent:**

```
I'll use the batch-merge-orchestrator agent to intelligently merge your files.

Agent will:
1. Read all N files completely
2. Create content matrix (which topics in which files)
3. Identify overlaps and gaps
4. Resolve conflicts with source traceability
5. Merge into ONE comprehensive comparison chart
6. Create merge report with traceability map

Output:
- 1 merged comparison chart: [filename.xlsx]
- 1 merge report: [filename_merge_report.md]
```

**STOP HERE - Do NOT continue with Steps 2-9. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-9)
- Do NOT mix - if agent is launched, STOP and let agent complete the work

### Step 2: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/Excel_Comparison_Chart_REVISED.txt`
   - Main instructions and requirements

2. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Excel_Comparison_Example.py`
   - Complete 3-tab implementation with all helper functions
   - Shows Key Comparisons, Master Chart, Summary tabs

3. **Color Reference**: `study-guides/templates-and-examples/Excel_Color_Reference.txt`
   - Shared color palette and styling specifications

### Step 3: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL conditions/concepts/mechanisms mentioned (don't skip any)
- Note categories suitable for comparison tables
- Identify items that need side-by-side comparison
- Look for clinical presentation, diagnosis, treatment patterns
- Note any existing mnemonics or memory aids mentioned

### Step 4: Create 3-Tab Excel Chart

**Required Tabs:**

**Tab 1: Key Comparisons**
- Multiple side-by-side comparison tables
- ONE category per table (don't combine)
  - Example: Separate tables for Mechanism, Clinical Presentation, Treatment
- Columns = items being compared (e.g., Type I, Type II, Type III, Type IV)
- Rows = comparison categories within that topic
- Mnemonics placed directly BELOW relevant tables
- 2-3 blank rows between different comparison tables

**Tab 2: Master Chart**
- ALL items in one comprehensive table
- Rows = individual conditions/types
- Columns = key characteristics
- Frozen header row
- Color-coded by category

**Tab 3: Summary**
- Mnemonics (researched, with full breakdown)
- "If X Think Y" associations
- Critical values (if applicable)
- Key definitions
- High-yield pearls

**Critical Requirements:**
- Use ONLY source file information
- ALL data cells have soft pastel backgrounds
- Research mnemonics via WebSearch (mandatory)
- Multiple comparison tables (one category per table)
- Mnemonics directly below relevant tables (not on separate sheet)

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Excel Comparison Chart (3 tabs):

STRUCTURE:
- Tab 1 "Key Comparisons": MULTIPLE tables (one category per table)
  - NOT one giant table combining all categories
  - Columns = items compared, Rows = features
  - Mnemonics placed DIRECTLY BELOW relevant tables
  - 2-3 blank rows between different comparison tables
- Tab 2 "Master Chart": ALL items in ONE comprehensive table, header frozen
- Tab 3 "Summary": Mnemonics, "If X Think Y", critical values, key definitions

FORMATTING (MANDATORY):
- Header row: #4472C4 (dark blue), white bold text, size 12
- COLOR RULE: ONE color per table/category (NOT alternating rows)
  - Tab 1: Each comparison TABLE = one color (all rows same)
  - Tab 2: Each category/class = one color (all items in class same)
  - Change color only when starting NEW table or NEW category
- Pastel palette (use in order):
  1. #D9E2F3 (Ice Blue) - Table/Category 1
  2. #C8E6C9 (Seafoam) - Table/Category 2
  3. #D1C4E9 (Light Orchid) - Table/Category 3
  4. #F7E7CE (Champagne) - Table/Category 4
  5. #BDD7EE (Sky Blue) - Table/Category 5
  6. #F0F8FF (Pale Azure) - Table/Category 6
  7. #FCE4EC (Blush Pink) - Table/Category 7
  8. #EDE7F6 (Soft Lilac) - Table/Category 8
  9. #FFE8D6 (Soft Tangerine) - Table/Category 9
  10. #BBDEFB (Powder Blue) - Table/Category 10
- ALL data cells MUST have pastel background (NOT white)
- White borders (#FFFFFF) on all cells
- Text: Black (#000000), Calibri, size 11
- Column widths: 25-40 based on content
- Text wrapping enabled on all cells
</template-compliance>

### Step 5: WebSearch for Mnemonics

**MANDATORY - Research established mnemonics:**
- Search: "medical mnemonics [topic]"
- Search: "[concept] mnemonic USMLE"
- Find PROVEN mnemonics only - never invent
- Add mnemonic row after each comparison table
- Include full breakdown/explanation

### Step 6: Python Implementation

Use openpyxl to create the Excel file:
- Soft pastel color scheme (hex codes from template)
- ALL cells get background colors (not just first column)
- Expand row heights to fit content
- Set appropriate column widths
- Black text throughout (#000000)

### Step 7: Use TodoWrite

Track your progress:
- Create todo for each comparison table
- Create todo for each tab
- Mark completed as you finish
- Keep user informed

### Step 8: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 3 tabs present: Key Comparisons, Master Chart, Summary
☐ Tab names correct
☐ Tab 1: MULTIPLE comparison tables (one category per table)
☐ Tab 1: NOT one giant table combining all categories
☐ Tab 1: Mnemonics DIRECTLY BELOW relevant tables
☐ Tab 1: 2-3 blank rows between different comparison tables
☐ Tab 2: ALL items in ONE table, header frozen
☐ Tab 3: Mnemonics, "If X Think Y", critical values, key definitions

**Formatting Compliance:**
☐ Header row: Dark blue (#4472C4), white bold text, size 12
☐ ALL data cells have pastel background (NOT white/no fill)
☐ Each category uses ONE consistent color
☐ Colors rotate when category changes
☐ White borders (#FFFFFF) on all cells
☐ Text wrapping enabled on all cells
☐ Column widths appropriate (25-40)
☐ Row heights fit content
☐ Font: Calibri, size 11 (headers 12)

**Source Accuracy:**
☐ All information from source file only
☐ No external medical facts added
☐ Terminology matches source exactly

**Completeness:**
☐ ALL conditions/concepts from source included
☐ All comparison categories covered
☐ Master chart has all items
☐ Mnemonics researched via WebSearch (not invented)

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

### Step 9: Save File

- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Comparison_Chart.xlsx`
- Create Claude Study Tools folder if doesn't exist
- Confirm file saved successfully

---

## Common Mistakes to Avoid

❌ Combining multiple categories in one comparison table
❌ Putting mnemonics only in Summary (should be below relevant tables too)
❌ Inventing mnemonics instead of researching
❌ White backgrounds on data cells (should be pastel)
❌ Using 4 tabs instead of 3
❌ Adding external medical information not in source

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 3 tabs: Key Comparisons, Master Chart, Summary
✓ Tab 1 has MULTIPLE tables (one for Mechanism, one for Clinical, one for Treatment)
✓ Mnemonic directly below each comparison table
✓ 2-3 blank rows between comparison tables

**Formatting:**
✓ "Type I Hypersensitivity" rows: All #D9E2F3 (Ice Blue)
✓ "Type II Hypersensitivity" rows: All #C8E6C9 (Seafoam)
✓ "Type III Hypersensitivity" rows: All #D1C4E9 (Light Orchid)
✓ "Type IV Hypersensitivity" rows: All #F7E7CE (Champagne)
✓ Header row: #4472C4 with white bold text
✓ All data cells have background color

### INCORRECT Implementation:

**Structure:**
✗ Only 2 tabs (missing Summary)
✗ ONE giant comparison table combining Mechanism, Clinical, and Treatment
✗ Mnemonics only in Summary tab (should be below relevant tables)
✗ No spacing between different comparison sections

**Formatting:**
✗ "Type I": Some rows colored, others white/no fill ← WRONG
✗ All hypersensitivity types same color ← WRONG
✗ Random colors per row instead of per category ← WRONG
✗ Gray borders instead of white ← WRONG
✗ Data cells with no background color ← WRONG

---

## Example Usage

### Single File:
```
/key-comparisons-excel "Clinical Medicine/Exam 2/Extract/Hypersensitivity.txt"
```
Creates: `Hypersensitivity_Comparison_Chart.xlsx`

### Single Directory (auto-finds all files):
```
/key-comparisons-excel "/Users/name/Documents/ClinMed/Exam 2/Extract"
```
Finds all readable files in directory, processes in batch separate mode.

### Batch Separate (N files → N outputs):
```
/key-comparisons-excel "TypeI.txt;TypeII.txt;TypeIII.txt;TypeIV.txt"
```
Creates 4 separate comparison charts:
- `TypeI_Comparison_Chart.xlsx`
- `TypeII_Comparison_Chart.xlsx`
- `TypeIII_Comparison_Chart.xlsx`
- `TypeIV_Comparison_Chart.xlsx`

Uses batch-separate-processor agent with architectural isolation (zero contamination).

### Batch Merge (N files → 1 merged output):
```
/key-comparisons-excel --merge "Hypersensitivity-Mechanisms.txt;Hypersensitivity-Clinical.txt;Hypersensitivity-Treatment.txt"
```
Creates 1 merged comparison chart:
- `Hypersensitivity_Comprehensive_Comparison_Chart.xlsx` (all content merged)
- `Hypersensitivity_Comprehensive_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge, overlap resolution, and source traceability.

### Batch Merge with Directories (N directories → 1 merged output):
```
/key-comparisons-excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```
Finds all files from both directories, merges into 1 comprehensive comparison chart.

### Mixed Files and Directories:
```
/key-comparisons-excel --merge "/path/to/Extract;specific-file.txt;/path/to/Txt"
```
Expands directories, keeps specific files, merges all into 1 comparison chart.
