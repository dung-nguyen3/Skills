---
description: Create comprehensive 4-tab Excel drug chart from pharmacology source material
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Excel drug chart from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 Excel chart (inline processing)
- **BATCH SEPARATE**: N files → N Excel charts (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Excel chart (orchestrator agent, intelligent merge)

---

### Step 0.5: Handle Directory Input

If $ARGUMENTS is a directory, process all .txt/.pdf files within it.
If batch (semicolon-separated), process each path independently.

---

### Step 0.8: Drug Inventory (SINGLE MODE ONLY)

**Skip this step for BATCH modes** (agents handle their own counting).

**Before creating content, extract ALL drug names from source:**

1. Scan source file for all drug names (generic and brand names)
2. Create internal inventory list
3. Document the count

**Output format:**
```
DRUG INVENTORY
Source: [filename]
Total drugs found: [N]
Drug list: [Drug A, Drug B, Drug C, ...]
```

**Keep this list for verification at end (Step 10).**

---

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Instruction template: Excel_Drugs_Chart_11-1_REVISED.txt
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
☐ Homogeneity check: All files are drug lectures
☐ Template: Excel_Drugs_Chart_11-1_REVISED.txt (per file)
☐ Output: N files → N Excel charts
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

**STOP HERE - Do NOT continue with Steps 2-10. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ File validation: All files exist and are readable
☐ Files are related/compatible for merging
☐ Template: Excel_Drugs_Chart_11-1_REVISED.txt (unified)
☐ Output: N files → 1 merged Excel chart
☐ Agent: batch-merge-orchestrator (launched once)
☐ Merge features: Content matrix, overlap resolution, source traceability
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent:**

```
I'll use the batch-merge-orchestrator agent to intelligently merge your files.

Agent will:
1. Read all N files completely
2. Create content matrix (which drugs in which files)
3. Identify overlaps and gaps
4. Resolve conflicts with source traceability
5. Merge into ONE comprehensive Excel chart
6. Create merge report with traceability map

Output:
- 1 merged Excel chart: [filename.xlsx]
- 1 merge report: [filename_merge_report.md]
```

**STOP HERE - Do NOT continue with Steps 2-10. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-10)
- Do NOT mix - if agent is launched, STOP and let agent complete the work

### Step 2: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/Excel_Drugs_Chart_11-1_REVISED.txt`
   - Main instructions and requirements (~550 lines)

2. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Excel_Drug_Example.py`
   - Complete 4-tab implementation with all helper functions
   - Shows Drug Details, Key Comparisons, Master Chart, High-Yield tabs

3. **Color Reference**: `study-guides/templates-and-examples/Excel_Color_Reference.txt`
   - Shared color palette and styling specifications

### Step 3: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL drugs mentioned (don't skip any)
- Note drug classes and classifications
- Extract drug-specific vs class-wide information
- Verify first-line designations
- Document combination therapies

### Step 4: Create 4-Tab Excel Chart

**Required Tabs:**

**Tab 1: Drug Details**
- Drug class comparison tables
- Drugs as columns, properties as rows
- Merged cells for class-wide properties
- Memory tricks row after EACH drug class
- Analogy boxes for mechanisms

**Tab 2: Key Comparisons**
- Side-by-side comparison tables
- Mechanisms, toxicities, uses, interactions
- Analogies for drug mechanisms (researched)
- One category per comparison

**Tab 3: Master Chart**
- ALL drugs in one table
- Rows = drugs, Columns = characteristics
- Frozen header row
- Color-coded by drug class

**Tab 4: High-Yield & Pearls**
- Clinical pearls
- Mnemonics (researched)
- "If X Think Y" associations
- Must-know facts

**Critical Requirements:**
- Use ONLY source file information
- ALL data cells have soft pastel backgrounds
- Mark first-line drugs only if source states it
- Verify before merging cells (identical info only)
- Research mnemonics via WebSearch (mandatory)
- Use emojis sparingly: 🟢 (DOC), ⚠️ (critical warnings)

<verbatim-requirement>
CRITICAL: If source contains learning objectives, they must be copied EXACTLY.
- Copy word-for-word, character-for-character
- Do NOT rephrase, summarize, or "improve" wording
- Preserve original numbering and sequence
Note: Drug details/explanations CAN be paraphrased from source content.
</verbatim-requirement>

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Excel Drug Chart (4 tabs):

STRUCTURE:
- Tab 1 "Drug Details": One table per drug class, columns=drugs, rows=properties
  - Analogy column (Column G) with 2-4 sentence analogies
  - Memory tricks row after EACH drug class table
  - Merged cells ONLY for class-wide info (not drug-specific)
- Tab 2 "Key Comparisons": Comparisons ACROSS drug classes
- Tab 3 "Master Chart": ALL drugs in ONE table, header frozen
- Tab 4 "High-Yield & Pearls": Clinical pearls, mnemonics, must-know facts

FORMATTING (MANDATORY):
- Header row: #4472C4 (dark blue), white bold text, size 12
- Data rows: Rotate through pastel palette BY DRUG CLASS:
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
- Same drug class = same color throughout
- White borders (#FFFFFF) on all cells
- Text: Black (#000000), Calibri, size 10
- Column widths: 25-40 based on content
- Text wrapping enabled on all cells
</template-compliance>

### Step 5: WebSearch for Mnemonics

**MANDATORY - Research established mnemonics:**
- Search: "medical mnemonics [drug class]"
- Search: "[drug name] mnemonic USMLE"
- Find PROVEN mnemonics only - never invent
- Add mnemonic row after each drug class table
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
- Create todo for each drug class
- Create todo for each tab
- Mark completed as you finish
- Keep user informed

### Step 8: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 4 tabs present: Drug Details, Key Comparisons, Master Chart, High-Yield & Pearls
☐ Tab names correct
☐ Tab 1: One table per drug class (NOT all classes in one table)
☐ Tab 1: Analogy column present with 2-4 sentence analogies
☐ Tab 1: Memory tricks row after EACH drug class table
☐ Tab 2: Comparisons ACROSS drug classes
☐ Tab 3: ALL drugs in ONE table, header frozen
☐ Tab 4: Clinical pearls, mnemonics, must-know facts sections

**Formatting Compliance:**
☐ Header row: Dark blue (#4472C4), white bold text, size 12
☐ ALL data cells have pastel background (NOT white/no fill)
☐ Each drug class uses ONE consistent color
☐ Colors rotate when drug class changes
☐ White borders (#FFFFFF) on all cells
☐ Text wrapping enabled on all cells
☐ Column widths appropriate (25-40)
☐ Row heights fit content
☐ Font: Calibri, size 11 (headers 12)

**Source Accuracy:**
☐ Drug-specific info NOT applied to entire class
☐ First-line designation only where source explicitly states
☐ No external info (except researched mnemonics)
☐ Merged cells only for truly class-wide information

**Completeness:**
☐ ALL drugs from source included
☐ All drug classes covered
☐ Master chart has every drug
☐ Mnemonics researched via WebSearch (not invented)

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

### Step 9: Save Files

**Naming Convention:** Use source filename with new extension (e.g., `1 ANS.txt` → `1 ANS.xlsx`)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[SourceFileName].xlsx`
- Example: Source `1 ANS.txt` → Output `1 ANS.xlsx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[SourceFileName].py`
- Example: Source `1 ANS.txt` → Output `py/1 ANS.py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

### Step 10: Drug Coverage Report (SINGLE MODE ONLY)

**Compare drugs included vs Drug Inventory from Step 0.8:**

1. Count drugs actually included in the Excel chart
2. Compare against inventory list from Step 0.8
3. Calculate coverage percentage
4. Identify any missing drugs

**MANDATORY OUTPUT:**
```
---
DRUG COVERAGE REPORT
Source drugs: [N] (from inventory)
Included drugs: [M]
Coverage: [M/N] ([percentage]%)

[If 100%]: All drugs from source included.
[If <100%]: MISSING: [list missing drug names]
---
```

**If coverage < 100%:** Fix immediately before completing. Add missing drugs to appropriate tabs.

---

## Common Mistakes to Avoid

❌ Marking all drugs as first-line when only specific ones are
❌ Merging cells without verifying identical information
❌ Applying drug-specific info to entire class
❌ Inventing mnemonics instead of researching
❌ White backgrounds on data cells (should be pastel)
❌ Missing memory tricks row after drug classes

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 4 tabs: Drug Details, Key Comparisons, Master Chart, High-Yield & Pearls
✓ Tab 1 has separate table for each drug class (NRTIs, NNRTIs, PIs, etc.)
✓ Memory tricks row after each drug class table
✓ Analogy column (Column G) explaining mechanisms

**Formatting:**
✓ "NRTIs" (5 drugs): All rows #D9E2F3 (Ice Blue)
✓ "NNRTIs" (3 drugs): All rows #C8E6C9 (Seafoam)
✓ "Protease Inhibitors" (4 drugs): All rows #D1C4E9 (Light Orchid)
✓ Header row: #4472C4 with white bold text
✓ All data cells have background color

### INCORRECT Implementation:

**Structure:**
✗ Only 3 tabs (missing High-Yield & Pearls)
✗ All drug classes in ONE giant table instead of separate tables
✗ No memory tricks row after drug classes
✗ Missing analogy column

**Formatting:**
✗ "NRTIs": Some rows #D9E2F3, others white/no fill ← WRONG
✗ All drug classes same color ← WRONG
✗ Random colors per row instead of per class ← WRONG
✗ Gray borders instead of white ← WRONG
✗ Data cells with no background color ← WRONG

---

## Example Usage

### Single File:
```
/4-tab-excel "Pharmacology/Exam 3/Extract/HIV Antivirals.txt"
```
Creates: `HIV_Antivirals_Drug_Chart.xlsx`

### Single Directory (auto-finds all files):
```
/4-tab-excel "/Users/name/Documents/Pharmacology/Exam 2/Extract"
```
Finds all readable files in directory, processes in batch separate mode.

### Batch Separate (N files → N outputs):
```
/4-tab-excel "HIV.txt;COVID.txt;Antibiotics.txt"
```
Creates 3 separate Excel files:
- `HIV_Drug_Chart.xlsx` (only HIV drugs)
- `COVID_Drug_Chart.xlsx` (only COVID drugs)
- `Antibiotics_Drug_Chart.xlsx` (only antibiotic drugs)

Uses batch-separate-processor agent with architectural isolation (zero contamination).

### Batch Merge (N files → 1 merged output):
```
/4-tab-excel --merge "HIV-PIs.txt;HIV-NRTIs.txt;HIV-NNRTIs.txt"
```
Creates 1 merged Excel file:
- `HIV_Comprehensive_Drug_Chart.xlsx` (all HIV drug classes merged)
- `HIV_Comprehensive_Drug_Chart_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge, overlap resolution, and source traceability.

### Batch Merge with Directories (N directories → 1 merged output):
```
/4-tab-excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```
Finds all files from both directories, merges into 1 comprehensive Excel chart.

### Mixed Files and Directories:
```
/4-tab-excel --merge "/path/to/Extract;specific-file.txt;/path/to/Txt"
```
Expands directories, keeps specific files, merges all into 1 Excel chart.
