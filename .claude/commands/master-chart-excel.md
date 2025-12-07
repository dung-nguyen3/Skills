---
description: Create single-sheet Excel Master Chart for drugs, conditions, or any medical topic
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Excel Master Chart from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 Master Chart (inline processing)
- **BATCH SEPARATE**: N files → N Master Charts (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Master Chart (orchestrator agent, intelligent merge)

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
☐ Instruction template: Excel_Master_Chart_Only_REVISED.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ Columns: Will ASK user what columns to include (or use defaults)
☐ Single sheet: "Master Chart" only (no additional tabs)
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
☐ Template: Excel_Master_Chart_Only_REVISED.txt (per file)
☐ Output: N files → N Master Charts
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

**STOP HERE - Do NOT continue with Steps 2-8. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ File validation: All files exist and are readable
☐ Files are related/compatible for merging
☐ Template: Excel_Master_Chart_Only_REVISED.txt (unified)
☐ Output: N files → 1 merged Master Chart
☐ Agent: batch-merge-orchestrator (launched once)
☐ Merge features: Content matrix, overlap resolution, source traceability
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent:**

```
I'll use the batch-merge-orchestrator agent to intelligently merge your files.

Agent will:
1. Read all N files completely
2. Create content matrix (which items in which files)
3. Identify overlaps and gaps
4. Resolve conflicts with source traceability
5. Merge into ONE comprehensive Master Chart
6. Create merge report with traceability map

Output:
- 1 merged Master Chart: [filename.xlsx]
- 1 merge report: [filename_merge_report.md]
```

**STOP HERE - Do NOT continue with Steps 2-8. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-8)
- Do NOT mix - if agent is launched, STOP and let agent complete the work

### Step 2: Load Resources & Ask About Columns

**Read these files:**
1. **Template**: `study-guides/templates-and-examples/Excel_Master_Chart_Only_REVISED.txt`
2. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Excel_Master_Chart_Example.py`
3. **Color Reference**: `study-guides/templates-and-examples/Excel_Color_Reference.txt`

**CRITICAL - Ask user about columns:**

```
Before I create the Master Chart, what columns would you like me to include?

Common options:
- For Drug Charts: Drug Class, Drug Name (Brand), Route, Mechanism, Uses, Adverse Effects, Contraindications, Special Considerations
- For Condition Charts: Condition, Risk Factors, Clinical Presentation, Diagnosis, Treatment
- For Lab Charts: Test Name, Normal Range, Increased In, Decreased In, Significance

Which columns would you like, or should I analyze the source and suggest appropriate ones?
```

**If user specifies columns:** Use those exactly
**If user says "analyze" or doesn't specify:** Analyze source and suggest appropriate columns, then confirm

### Step 3: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL items mentioned (drugs, conditions, etc.)
- Group items by class/category
- Note what information is available for each column
- Do NOT skip any items

### Step 4: Create Master Chart

**Single Sheet Structure:**
- Sheet name: "Master Chart"
- Frozen header row
- Color-coded rows by class/group

**Header Row:**
- Dark blue background (#4472C4)
- White, bold text, size 12
- Center aligned, word wrap
- Row height: 25

**Data Rows:**
- Calibri, size 11, black text
- Column A (class/group): Bold
- Left aligned, top vertical, word wrap
- Row colors rotate by class (10-color palette)
- White borders (#FFFFFF)

**Critical Requirements:**
- Use ONLY source file information
- ALL data cells have pastel backgrounds
- First column (class/group) always bold
- Complete coverage - ALL items from source

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Excel Master Chart (1 tab):

STRUCTURE:
- Single sheet named "Master Chart"
- ALL items from source in ONE table
- Header row frozen
- User-specified columns (or defaults)
- First column (class/group) bold

FORMATTING (MANDATORY):
- Header row: #4472C4 (dark blue), white bold text, size 12
- Data rows: Rotate through pastel palette BY CLASS/GROUP:
  1. #D9E2F3 (Ice Blue)
  2. #C8E6C9 (Seafoam)
  3. #D1C4E9 (Light Orchid)
  4. #F7E7CE (Champagne)
  5. #BDD7EE (Sky Blue)
  6. #F0F8FF (Pale Azure)
  7. #FCE4EC (Blush Pink)
  8. #EDE7F6 (Soft Lilac)
  9. #FFE8D6 (Soft Tangerine)
  10. #BBDEFB (Powder Blue)
- ALL data cells MUST have pastel background (NOT white)
- Same class/group = same color throughout
- White borders (#FFFFFF) on all cells
- Text: Black (#000000), Calibri, size 11
- Column widths: 25-40 based on content
- Text wrapping enabled on all cells
</template-compliance>

### Step 5: Apply Color Coding

**Assign colors by class/group:**
```python
ROW_COLORS = [
    'D9E2F3',  # Ice Blue
    'C8E6C9',  # Seafoam
    'D1C4E9',  # Light Orchid
    'F7E7CE',  # Champagne
    'BDD7EE',  # Sky Blue
    'F0F8FF',  # Pale Azure
    'FCE4EC',  # Blush Pink
    'EDE7F6',  # Soft Lilac
    'FFE8D6',  # Soft Tangerine
    'BBDEFB',  # Powder Blue
]
```

- One color per class - all items in same class get same color
- Rotate through colors as classes change

### Step 6: Use TodoWrite

Track your progress:
- Create todo for each class/group
- Mark completed as you finish each group
- Keep user informed

### Step 7: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ Single sheet named "Master Chart"
☐ ALL items from source in ONE table
☐ Header row frozen
☐ User-specified columns present
☐ First column (class/group) bold

**Formatting Compliance:**
☐ Header row: Dark blue (#4472C4), white bold text, size 12
☐ ALL data cells have pastel background (NOT white/no fill)
☐ Each class/group uses ONE consistent color
☐ Colors rotate when class/group changes
☐ White borders (#FFFFFF) on all cells
☐ Text wrapping enabled on all cells
☐ Column widths appropriate (25-40)
☐ Row heights fit content
☐ Font: Calibri, size 11 (headers 12)

**Completeness:**
☐ ALL items from source included
☐ All user-specified columns filled
☐ No items missed

**Accuracy:**
☐ Information matches source exactly
☐ No external knowledge added
☐ Names spelled correctly

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

### Step 8: Save Files

**Output Filename Rule:**
1. Strip file extension and common suffixes (`_text.txt`, `_extracted.txt`, etc.)
2. Strip course prefixes (`Micro_`, `Pharm_`, `Clinical_`, `Patho_`, etc.)
3. Replace underscores with spaces for readability
4. Extract lecture number and topic: `[Number] [Topic]` or just `[Topic]`
5. Preserve capitalization as-is (after underscore→space conversion)
6. Add appropriate extension: `.xlsx`
7. NO template suffixes, NO title case normalization

**Examples:**
- `Micro_4 Intro to Virology_text.txt` → `4 Intro to Virology.xlsx`
- `Pharm_11 Beta Blockers_text.txt` → `11 Beta Blockers.xlsx`
- `Micro_4_Intro_To_Virology_text.txt` → `4 Intro To Virology.xlsx`
- `Micro_Basics Of Immunology_text.txt` → `Basics Of Immunology.xlsx`

**Batch Merge Naming:**
- Input: `Micro_4 Intro to Virology_text.txt` + `Micro_5 Viral Replication_text.txt`
- Output: `Lecture 4-5.xlsx`
- Format: `Lecture [min]-[max].xlsx` (based on lecture numbers found)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[OutputFilename].xlsx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[OutputFilename].py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

---

## Common Mistakes to Avoid

❌ Not asking user about columns - ALWAYS ask or suggest
❌ Missing items from source file
❌ Using different colors for same class
❌ Adding external medical information
❌ Forgetting to freeze header row
❌ Using gray/black borders instead of white
❌ Creating multiple tabs (should be single sheet)

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ Single sheet: "Master Chart"
✓ ALL items from source in one table
✓ Header row frozen
✓ First column (Drug Class) bold

**Formatting:**
✓ "NRTIs" (5 drugs): All rows #D9E2F3 (Ice Blue)
✓ "NNRTIs" (3 drugs): All rows #C8E6C9 (Seafoam)
✓ "Protease Inhibitors" (4 drugs): All rows #D1C4E9 (Light Orchid)
✓ Header row: #4472C4 with white bold text
✓ All data cells have background color

### INCORRECT Implementation:

**Structure:**
✗ Multiple tabs instead of single sheet
✗ Missing items from source
✗ Header row not frozen

**Formatting:**
✗ "NRTIs": Some rows colored, others white/no fill ← WRONG
✗ All drug classes same color ← WRONG
✗ Random colors per row instead of per class ← WRONG
✗ Gray/black borders instead of white ← WRONG
✗ Data cells with no background color ← WRONG

---

## Example Usage

### Single File:
```
/master-chart-excel "Pharmacology/Exam 2/Extract/Pharm_11 Beta Blockers_text.txt"
```
Creates: `11 Beta Blockers.xlsx`

### Single Directory (auto-finds all files):
```
/master-chart-excel "/Users/name/Documents/ClinMed/Exam 2/Extract"
```
Finds all readable files in directory, processes in batch separate mode.

### Batch Separate (N files → N outputs):
```
/master-chart-excel "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt;Pharm_13 Diuretics_text.txt"
```
Creates 3 separate Master Charts:
- `11 Beta Blockers.xlsx`
- `12 ACE Inhibitors.xlsx`
- `13 Diuretics.xlsx`

Uses batch-separate-processor agent with architectural isolation (zero contamination).

### Batch Merge (N files → 1 merged output):
```
/master-chart-excel --merge "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt"
```
Creates 1 merged Master Chart:
- `Lecture 11-12.xlsx` (all drug classes merged)
- `Lecture 11-12_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge, overlap resolution, and source traceability.

### Batch Merge with Directories (N directories → 1 merged output):
```
/master-chart-excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```
Finds all files from both directories, merges into 1 comprehensive Master Chart.

### Mixed Files and Directories:
```
/master-chart-excel --merge "/path/to/Extract;specific-file.txt;/path/to/Txt"
```
Expands directories, keeps specific files, merges all into 1 Master Chart.

---

## Key Difference from Other Excel Commands

| Command | Tabs | Purpose |
|---------|------|---------|
| `/drugs-3-tab-excel` | 3 tabs | Drug pharmacology (detailed) |
| `/key-comparisons-excel` | 3 tabs | Side-by-side comparisons |
| `/master-chart-excel` | 1 tab | Quick reference chart (flexible columns) |

**Use `/master-chart-excel` when:**
- You want a simple, single-sheet reference
- You need flexible columns (not drug-specific)
- Content is conditions, labs, or mixed topics
- You want to define custom columns
