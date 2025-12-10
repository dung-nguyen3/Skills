---
description: Create 3-tab Excel comparison chart for any medical topic (conditions, mechanisms, concepts)
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Excel comparison chart from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 comparison chart (inline processing)
- **BATCH SEPARATE**: N files → N comparison charts (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged comparison chart (orchestrator agent, intelligent merge)

---

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Text template: Excel_Comparison_Chart_REVISED.txt (WHAT to create - structure/requirements)
☐ Python reference: Excel_Comparison_Example.py (HOW to implement - styling/code)
☐ Resource hierarchy: Text=structure/requirements, Python=styling/implementation
☐ Source-only policy: I will ONLY use information from source file
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
- Identify ALL conditions/concepts/mechanisms, diagnostic tools mentioned (don't skip any)
- Identify topic type (diagnostic tools, medical conditions, drugs, mechanisms, etc.)
- Identify all subtypes if any.
- Search for and include all items found in "Lecture Outline", "Outline", or "Overview"
- Note items that need side-by-side comparison


### Step 3.5: Select Comparison Categories from Menus

<category_selection_step>

**Using the comprehensive category menus from template as examples or other relevant categories not listed, select relevant categories:**

**Checklist:**
☐ Analyzed all content in source file (lecture outline, topics, subtypes)
☐ Identified which menu(s) apply (A-M from template)
☐ Selected categories from menu that relate to source content
☐ Documented category list for comparison tables

**Process:**

1. **Example Match Source to Menu(s):**
   - Diagnostic tools/tests → Menu A
   - Medical conditions (any specialty) → Menu B
   - Drugs/pharmacology → Menu C
   - Mechanisms/pathophysiology → Menu D
   - Physical exam/assessment → Menu E
   - Treatments/interventions → Menu F
   - Risk factors → Menu G
   - Classifications/staging → Menu H
   - Labs/biomarkers → Menu I
   - Anatomy/structures → Menu J
   - Procedures/techniques → Menu K
   - Differential diagnosis → Menu L
   - Systems/physiology → Menu M

2. **Select Relevant Categories:**
   From the matched menu(s) or other categories, select categories that:
   - Are explicitly compared or emphasized in source content
   - Help differentiate items students frequently confuse
   - Enable actionable clinical decisions
   - Contain hallmark/pathognomonic/distinguishing findings
   - Include any other shared categories mentioned throughout source file

3. **Exclude Irrelevant Categories:**
   Skip categories that contain:
   - Tangential information not central to the main topics
   - No comparable data (only one item has information)

4. **Document Category List:**
   ```
   CATEGORY SELECTION:
   Source topic: [topic type]
   Menu used: [Menu letter(s)]
   Categories selected: [list of categories from menu]
   Number of comparison tables: [N]
   ```

**Example:**
```
CATEGORY SELECTION:
Source topic: Pulmonary embolism diagnostic tests
Menu used: Menu A (Diagnostic Tools & Tests)
Categories selected:
  1. Test Characteristics (Sensitivity, Specificity, PPV, NPV)
  2. Indications (When to Order)
  3. Interpretation (How to Read Results)
  4. Advantages & Disadvantages
Number of comparison tables: 4
```

</category_selection_step>

**IMPORTANT:** The number of comparison tables = number of categories. Do NOT limit to 3 tables.

### Step 4: Create 3-Tab Excel Chart

**Required Tabs:**

**Tab 1: Key Comparisons**
- **DYNAMIC number of comparison tables** - create as many as needed based on source content
- Each table compares 1-2 categories at a time to help break it down and differentiate
- ONE category per table (don't combine)
  - Example: If comparing Clinical Presentation, Diagnosis, and Treatment for Conditions A, B, C:
    - Table 1: Clinical Presentation comparing Conditions A, B, and C
    - Table 2: Diagnosis comparing Conditions A, B, and C
    - Table 3: Treatment comparing Conditions A, B, and C
- Columns = items being compared (e.g., Condition A, Condition B, Condition C)
- Rows = features within that category
- 2-3 blank rows between different comparison tables
- **Do NOT limit to 3 tables** - create N tables where N = comparison categories in source content

**Tab 2: Master Chart**
- ALL items in one comprehensive table
- Rows = individual conditions/types
- Columns = key characteristics
- Frozen header row
- Color-coded by category

**Example Column Categories by Topic Type:**

**For Diagnostic Tools/Tests:**
- Test Name, Category/Type, Technology/How It Works, Indications, Contraindications, Protocol/Procedure, Interpretation, Key Characteristics

**For Procedures:**
- Procedure Name, Procedure Type & Approach, Indications, Contraindications, Patient Preparation & Consent, Equipment & Setup, Step-by-Step Technique, Expected Findings/Results, Complications, Management, Post-Procedure Care, Alternatives & When to Choose, Patient Education, Considerations

**For Medical Conditions:**
- Condition/Disease, Definition, Etiology/Causes, Clinical Presentation/Symptoms, Pathophysiology/Mechanism, Diagnosis/Labs, Treatment (First-line), Treatment (Alternatives), Complications, Key Differentiators

**For Drugs:**
- Drug Name, Drug Class, Mechanism of Action, Indications, Contraindications, Dosing, Adverse Effects, Drug Interactions, Monitoring, Special Populations

**IMPORTANT:** These are EXAMPLES only. Adapt columns based on what categories are actually mentioned and shared throughout the source file. Use source-driven column selection.

**Tab 3: Summary (for clinical medicine sources)**
- "If you see X, Think Y" associations
- Critical values
- Key definitions
- Final high-yield exam pearls

**Critical Requirements:**
- Use ONLY source file information
- ALL data cells have soft pastel backgrounds
- Multiple comparison tables (one category per table)
- If unsure, ask user. 

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Excel Comparison Chart (3 tabs):

STRUCTURE:
- Tab 1 "Key Comparisons": MULTIPLE tables (one category per table)
  - NOT one giant table combining all categories
  - Columns = items compared, Rows = features
  - 2-3 blank rows between different comparison tables
- Tab 2 "Master Chart": ALL items in ONE comprehensive table, header frozen
- Tab 3 "Summary": "If X Think Y", critical values, key definitions

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

### Step 5: Python Implementation

Use openpyxl to create the Excel file:
- Soft pastel color scheme (hex codes from template)
- ALL cells get background colors (not just first column)
- Expand row heights to fit content
- Set appropriate column widths
- Black text throughout (#000000)

### Step 6: Use TodoWrite

Track your progress:
- Create todo for each comparison table
- Create todo for each tab
- Mark completed as you finish
- Keep user informed

### Step 7: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 3 tabs present: Key Comparisons, Master Chart, Summary
☐ Tab names correct
☐ Tab 1: MULTIPLE comparison tables (one category per table)
☐ Tab 1: NOT one giant table combining all categories
☐ Tab 1: 2-3 blank rows between different comparison tables
☐ Tab 2: ALL items in ONE table, header frozen
☐ Tab 3: "If X Think Y", critical values, key definitions

**Formatting Compliance:**
☐ Header row: Dark blue (#4472C4), white bold text, size 12
☐ ALL data cells have pastel background (NOT white/no fill)
☐ Each category uses ONE consistent color
☐ Colors rotate when category changes
☐ White borders (#FFFFFF) on all cells
☐ Merged cells have visible borders (no missing horizontal lines)
☐ Text wrapping enabled on all cells
☐ Column widths appropriate (25-40)
☐ Row heights fit content
☐ Font: Calibri, size 11 (headers 12)

**Python Pattern Compliance:**
☐ COLOR_SETS system used (3-shade: header, main, row_label)
☐ Colors match Excel_Comparison_Example.py specifications
☐ Border pattern matches Python example (white thin borders)
☐ Merged cell pattern correct (styled ALL cells BEFORE merging)
☐ Font sizes match Python example per tab type

**Source Accuracy:**
☐ All information from source file only
☐ No external medical facts added
☐ Terminology matches source exactly

**Completeness:**
☐ ALL conditions/concepts from source included
☐ All comparison categories covered
☐ Master chart has all items

**Resource Compliance Note:**
Briefly confirm which resources were followed:
- Structure requirements: [Text template ✓]
- Styling implementation: [Python example ✓]
- Any conflicts resolved per hierarchy: [List if any]

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

❌ **Limiting to only 3 comparison tables** - create as many as needed based on source content
❌ Combining multiple categories in one comparison table
❌ White backgrounds on data cells (should be pastel)
❌ Using 4 tabs instead of 3
❌ Adding external medical information not in source

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 3 tabs: Key Comparisons, Master Chart, Summary
✓ Tab 1 has MULTIPLE tables (one for Mechanism, one for Clinical, one for Treatment, etc.)
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
/key-comparisons-excel "Clinical Medicine/Exam 2/Extract/Pharm_11 Beta Blockers_text.txt"
```
Creates: `11 Beta Blockers.xlsx`

### Single Directory (auto-finds all files):
```
/key-comparisons-excel "/Users/name/Documents/ClinMed/Exam 2/Extract"
```
Finds all readable files in directory, processes in batch separate mode.

### Batch Separate (N files → N outputs):
```
/key-comparisons-excel "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt;Pharm_13 Diuretics_text.txt"
```
Creates 3 separate comparison charts:
- `11 Beta Blockers.xlsx`
- `12 ACE Inhibitors.xlsx`
- `13 Diuretics.xlsx`

Uses batch-separate-processor agent with architectural isolation (zero contamination).

### Batch Merge (N files → 1 merged output):
```
/key-comparisons-excel --merge "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt"
```
Creates 1 merged comparison chart:
- `Lecture 11-12.xlsx` (all content merged)
- `Lecture 11-12_merge_report.md` (source traceability)

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
