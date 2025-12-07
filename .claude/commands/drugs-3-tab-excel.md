---
description: Create comprehensive Excel drug chart (3 main tabs + optional FYI) from pharmacology source material
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Excel drug chart from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 Excel chart (inline processing)
- **BATCH SEPARATE**: N files → N Excel charts (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Excel chart (orchestrator agent, intelligent merge)

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

**Edge Case Drugs - Tracking Ambiguous Classifications:**

During inventory, identify drugs that may not fit cleanly into the main drug class structure:

**What qualifies as an edge case drug:**
- Treatment/antidote agents (e.g., pralidoxime for organophosphate poisoning)
- Supportive therapy drugs mentioned alongside main therapeutic agents
- Drugs discussed with full details (MOA, route, uses, AEs, etc.) but not listed in main classification
- Adjunct agents that don't belong to a specific drug class

**Process for edge case drugs:**

1. **During Step 0.8 Inventory:** Flag any drugs that don't clearly fit into the main drug classes listed in source
   - Example: "2-PAM (Pralidoxime) - discussed as treatment for organophosphate poisoning, not listed in main 4 drug classes"

2. **Continue with main chart:** Do NOT block chart creation on edge cases
   - Create all 3 tabs using only the clearly classified drugs
   - Complete drug coverage report

3. **After chart completion (Step 9):** Report edge case drugs to user and ask for guidance

   **Output format:**
   ```
   ---
   EDGE CASE DRUGS IDENTIFIED
   The following drugs were discussed in source but don't fit into the main drug classification:

   1. [Drug Name] ([Brand]) - [Brief reason, e.g., "treatment for X poisoning"]
      Source pages: [page numbers]

   Should these be included in the chart? If yes, under which drug class?
   ---
   ```

4. **If user confirms inclusion:**
   - Add to appropriate tab/class as user specifies
   - Update drug coverage report to reflect inclusion
   - Regenerate affected sections

**Example - Cholinergic Agents source:**
```
Edge case identified:
- Pralidoxime (2-PAM) - Treatment for organophosphate poisoning
  Discussed: MOA, route, uses, AEs, contraindications, PK (pages 698-706)
  Not listed in main 4 classes: Direct acting agonists, AChE inhibitors,
  Cholinergic antagonists, Neuromuscular blockers

Ask user: "Should Pralidoxime (2-PAM) be included? If yes, under which class?"
```

**When NOT to flag as edge case:**
- Drugs clearly listed in one of the main drug classes
- FYI drugs (handled separately in Step 0.7)
- Brief mentions without detailed drug information

---

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Text template: Excel_Drugs_Chart_11-1_REVISED.txt (WHAT to create - structure/requirements)
☐ Python reference: Excel_Drug_Example.py (HOW to implement - styling/code)
☐ Resource hierarchy: Text=structure/requirements, Python=styling/implementation
☐ Source-only policy: I will ONLY use information from source file
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ 3-tab structure (+ optional FYI): Drug Details, Key Comparisons, Master Chart, FYI Drugs (if source has FYI section)
☐ 10 categories: MOA, Route, Uses (🟢 DOC), Combination, Adverse Effects (⚠️ toxicity), Contraindications, Interactions, PK, Special, [Other]
☐ FYI drugs: Check if source has FYI/Future Reference section (create 4th tab if present)
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
☐ Template: Excel Drugs Chart 11-1.txt (per file)
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
☐ Template: Excel Drugs Chart 11-1.txt (unified)
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
   - Complete 3-tab implementation with all helper functions
   - Shows Drug Details, Key Comparisons, Master Chart tabs

3. **Color Reference**: `study-guides/templates-and-examples/Excel_Color_Reference.txt`
   - Shared color palette and styling specifications

### Step 3: Analyze Source File

**CRITICAL - Extract Exact Drug Class Names:**

Before analyzing drug details, identify and extract the EXACT drug class names from the source:

1. **Find the drug classification structure** (usually near the beginning of lecture slides)
2. **Copy drug class names EXACTLY as written** - word-for-word, character-for-character
3. **Do NOT:**
   - Paraphrase or "improve" class names (e.g., "Direct acting agonists" → ❌ "Direct Muscarinic Agonists")
   - Add clarifying details not in source (e.g., "Neuromuscular blockers" → ❌ "Neuromuscular Blockers (Depolarizing)")
   - Create new classes not explicitly listed in source (e.g., ❌ "Nicotinic Agonists" if source doesn't list it as a main class)
   - Expand abbreviations unless source does (e.g., "AChE inhibitors" → ❌ "Acetylcholinesterase Inhibitors")
   - Combine or split classes differently than source presents them

4. **Use these EXACT class names** throughout all tabs, table headers, labels, and reports

**Example from Cholinergic Agents source (lines 14-18):**
```
✅ CORRECT (exact from source):
1. Direct acting agonists
2. AChE inhibitors
3. Cholinergic antagonists
4. Neuromuscular blockers

❌ INCORRECT (modified):
- "Direct Muscarinic Agonists" ← paraphrased/made more specific
- "Cholinesterase Inhibitors" ← expanded abbreviation AChE
- "Muscarinic Antagonists" ← paraphrased (source says "Cholinergic")
- "Neuromuscular Blockers (Depolarizing)" ← added clarifying detail
- "Nicotinic Agonists" ← created new class not in source's main list
```

**Same rule applies to drug names:**
- Use generic and brand names EXACTLY as written in source
- Preserve capitalization, spacing, abbreviations, punctuation, formatting
- Example: If source says "OnabotulinumtoxinA (Botox®)", use that exact spelling/capitalization

**Why this matters:**
- Ensures charts match source material exactly (students can cross-reference easily)
- Prevents confusion from inconsistent terminology
- Follows source-only policy strictly
- Mirrors verbatim-copy requirement for Learning Objectives

---

**CRITICAL - Read ENTIRE source file:**
- Identify ALL drugs mentioned (don't skip any)
- Note drug classes and classifications
- Extract drug-specific vs class-wide information
- Verify first-line designations
- Document combination therapies

### Step 4: Create 3-Tab Excel Chart (+ Optional FYI Tab)

**Required Tabs:**

**Tab 1: Drug Details**
- Drug class comparison tables
- Drugs as columns, properties as rows
- Merged cells for class-wide properties
- 10 categories in order: MOA, Route, Uses (🟢 DOC), Combination, Adverse Effects (⚠️ toxicity), Contraindications, Interactions, PK, Special, [Other]

**Tab 2: Key Comparisons**
- Side-by-side comparison tables
- Specific comparison tables: Combined Drug, Adverse Effects, First/Second-line, Toxicity, Mechanisms, Interactions, DOC
- Format rules: One category per comparison, group similar info together
- Example: Group drugs with same toxicity near each other for easy memorization

**Tab 3: Master Chart**
- ALL drugs in one table
- Rows = drugs, Columns = characteristics
- Column order: Drug Class, Drug Name, Mechanism, Route, Uses (🟢 DOC), Combination, Adverse Effects (⚠️ toxicity), Contraindications, Interactions, PK, Special, [Other]
- Frozen header row
- Color-coded by drug class

**Critical Requirements:**
- Use ONLY source file information
- ALL data cells have soft pastel backgrounds
- Mark first-line drugs only if source states it
- Verify before merging cells (identical info only)
- Use emoji notation: 🟢 DOC for [condition] in Uses, ⚠️ for serious/toxic effects in Adverse Effects

<verbatim-requirement>
CRITICAL: If source contains learning objectives, they must be copied EXACTLY.
- Copy word-for-word, character-for-character
- Do NOT rephrase, summarize, or "improve" wording
- Preserve original numbering and sequence
Note: Drug details/explanations CAN be paraphrased from source content.
</verbatim-requirement>

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Excel Drug Chart (3 main tabs + optional FYI tab):

STRUCTURE:
- Tab 1 "Drug Details": One table per drug class, columns=drugs, rows=properties
  - 10 categories in order: MOA, Route, Uses (🟢 DOC), Combination, Adverse Effects (⚠️ toxicity), Contraindications, Interactions, PK, Special, [Other]
  - Merged cells ONLY for class-wide info (not drug-specific)
- Tab 2 "Key Comparisons": Comparisons ACROSS drug classes
  - Specific comparison tables: Combined Drug, Adverse Effects, First/Second-line, Toxicity, Mechanisms, Interactions, DOC
  - Format rules: One category per comparison, group similar info together
- Tab 3 "Master Chart": ALL drugs in ONE table, header frozen
  - Column order: Drug Class, Drug Name, Mechanism, Route, Uses (🟢 DOC), Combination, Adverse Effects (⚠️ toxicity), Contraindications, Interactions, PK, Special, [Other]

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

### Step 5: Python Implementation

Use openpyxl to create the Excel file:
- Soft pastel color scheme (hex codes from template)
- ALL cells get background colors (not just first column)
- Expand row heights to fit content
- Set appropriate column widths
- Black text throughout (#000000)

### Step 6: Use TodoWrite

Track your progress:
- Create todo for each drug class
- Create todo for each tab
- Mark completed as you finish
- Keep user informed

### Step 7: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ 3 main tabs present (+ FYI tab if source has FYI section): Drug Details, Key Comparisons, Master Chart
☐ Tab names correct
☐ Tab 1: One table per drug class (NOT all classes in one table)
☐ Tab 1: 10 categories in correct order (MOA, Route, Uses, Combination, Adverse Effects, Contraindications, Interactions, PK, Special, [Other])
☐ Tab 1: Uses includes 🟢 DOC notation where applicable
☐ Tab 1: Adverse Effects includes ⚠️ for serious/toxic effects
☐ Tab 2: Specific comparison tables present (Combined Drug, Adverse Effects, First/Second-line, Toxicity, Mechanisms, Interactions, DOC)
☐ Tab 2: One category per comparison table
☐ Tab 2: Similar info grouped together
☐ Tab 3: ALL drugs in ONE table, header frozen
☐ Tab 3: Columns in correct order (Drug Class, Drug Name, Mechanism, Route, Uses, Combination, Adverse Effects, Contraindications, Interactions, PK, Special, [Other])
☐ Tab 4 (if applicable): FYI Drugs tab present if source contains FYI/Future Reference section
☐ Tab 4 (if applicable): Simple 2-column format (Drug Name | Page Number)
☐ Tab 4 (if applicable): FYI drugs NOT included in main drug inventory count

**Formatting Compliance:**
☐ Header row: Dark blue (#4472C4), white bold text, size 12
☐ ALL data cells have pastel background (NOT white/no fill)
☐ Each drug class uses ONE consistent color
☐ Colors rotate when drug class changes
☐ White borders (#FFFFFF) on all cells
☐ Merged cells have visible borders (no missing horizontal lines)
☐ Text wrapping enabled on all cells
☐ Column widths appropriate (25-40)
☐ Row heights fit content
☐ Font: Calibri, size 11 (headers 12)

**Python Pattern Compliance:**
☐ COLOR_SETS system used (3-shade: header, main, row_label)
☐ Colors match Excel_Drug_Example.py specifications
☐ Border pattern matches Python example (white thin borders)
☐ Merged cell pattern correct (styled ALL cells BEFORE merging)
☐ Font sizes match Python example per tab type

**Source Accuracy:**
☐ Drug-specific info NOT applied to entire class
☐ First-line designation only where source explicitly states
☐ No external info added
☐ Merged cells only for truly class-wide information

**Completeness:**
☐ ALL drugs from source included
☐ All drug classes covered
☐ Master chart has every drug
☐ All 10 categories present in Tab 1 and Tab 3

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

**Resource Compliance Note:**
Briefly confirm which resources were followed:
- Structure requirements: [Text template ✓]
- Styling implementation: [Python example ✓]
- Any conflicts resolved per hierarchy: [List if any]

### Step 8: Save Files

**Output Filename Rule:**
1. Strip file extension and common suffixes (`_text.txt`, `_extracted.txt`, etc.)
2. Strip course prefixes (`Micro_`, `Pharm_`, `Clinical_`, `Patho_`, etc.)
3. Replace underscores with spaces for readability
4. Extract lecture number and topic: `[Number] [Topic]` or just `[Topic]`
5. Preserve capitalization as-is (after underscore→space conversion)
6. Add appropriate extension: `.xlsx` for Excel, `.py` for Python
7. NO template suffixes, NO title case normalization

**Examples:**
- `Pharm_11 Beta Blockers_text.txt` → `11 Beta Blockers.xlsx`
- `Micro_4 Antibiotics_text.txt` → `4 Antibiotics.xlsx`
- `Pharm_HIV_Drugs_text.txt` → `HIV Drugs.xlsx`

**Batch Merge Naming:**
- Input: `Pharm_11 Beta Blockers_text.txt` + `Pharm_12 ACE Inhibitors_text.txt`
- Output: `Lecture 11-12.xlsx`
- Format: `Lecture [min]-[max].xlsx` (based on lecture numbers found)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[OutputFilename].xlsx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[OutputFilename].py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

### Step 9: Drug Coverage Report (SINGLE MODE ONLY)

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

Drugs included (by class):
- [Drug Class 1]: [Drug A, Drug B, Drug C]
- [Drug Class 2]: [Drug D, Drug E]
- [Drug Class 3]: [Drug F, Drug G, Drug H]
...

[If 100%]: All drugs from source included.
[If <100%]: MISSING: [list missing drug names]
---
```

**FORMAT EXAMPLES:**

✅ **CORRECT Format (Single-line per class):**
```
Drugs included (by class):
- Direct Muscarinic Agonists: Acetylcholine (Miochol®), Bethanechol (Urecholine®), Pilocarpine (IsoptoCarpine®)
- Nicotinic Agonists: Nicotine, Varenicline (Chantix®)
- Cholinesterase Inhibitors: Physostigmine (Eserine®), Neostigmine (Prostigmin®), Donepezil (Aricept®)
```

❌ **INCORRECT Format (Multi-line per class):**
```
**Direct Muscarinic Agonists (3):**
- Acetylcholine (Miochol®)
- Bethanechol (Urecholine®)
- Pilocarpine (IsoptoCarpine®)
```
**Why incorrect:** Each drug on separate line instead of comma-separated on single line; breaks scannability

❌ **INCORRECT Format (No class grouping):**
```
Drugs included:
- Acetylcholine (Miochol®)
- Bethanechol (Urecholine®)
- Physostigmine (Eserine®)
```
**Why incorrect:** Loses class context; drugs not grouped by class

---

**If coverage < 100%:** Fix immediately before completing. Add missing drugs to appropriate tabs.

### FYI Drugs Report (If Applicable)

**After reporting main drug coverage, if source contained FYI drugs, report them:**

**MANDATORY OUTPUT (if FYI drugs present):**
```
---
FYI DRUGS
FYI drugs found: [N]
FYI drugs: [Drug A, Drug B, Drug C]

Note: FYI drugs are NOT included in main drug inventory count. See Tab 4 for page numbers.
---
```

**If no FYI drugs in source:**
- Simply state: "No FYI drugs found in source."

---

## Common Mistakes to Avoid

❌ Marking all drugs as first-line when only specific ones are
❌ Merging cells without verifying identical information
❌ Applying drug-specific info to entire class
❌ White backgrounds on data cells (should be pastel)
❌ Forgetting to mark DOC with 🟢 in Uses category
❌ Forgetting to mark toxicity with ⚠️ in Adverse Effects category
❌ Wrong category order (must follow 10-category sequence)
❌ Creating 4 tabs instead of 3

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 3 main tabs: Drug Details, Key Comparisons, Master Chart (+ FYI tab if applicable)
✓ Tab 1 has separate table for each drug class (NRTIs, NNRTIs, PIs, etc.)
✓ Tab 1 has 10 categories in correct order
✓ Tab 2 has specific comparison tables (Combined Drug, Adverse Effects, First/Second-line, Toxicity, etc.)
✓ Tab 3 has all 11 columns in correct order

**Formatting:**
✓ "NRTIs" (5 drugs): All rows #D9E2F3 (Ice Blue)
✓ "NNRTIs" (3 drugs): All rows #C8E6C9 (Seafoam)
✓ "Protease Inhibitors" (4 drugs): All rows #D1C4E9 (Light Orchid)
✓ Header row: #4472C4 with white bold text
✓ All data cells have background color

### INCORRECT Implementation:

**Structure:**
✗ 4 tabs with wrong 4th tab (e.g., High-Yield & Pearls tab should NOT exist - only FYI Drugs tab is acceptable as 4th tab)
✗ Missing FYI tab when source has FYI section
✗ Including FYI drugs in main drug count
✗ All drug classes in ONE giant table instead of separate tables
✗ Wrong category order or missing categories
✗ Tab 2 missing specific comparison tables

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
/drugs-3-tab-excel "Pharmacology/Exam 3/Extract/Pharm_11 Beta Blockers_text.txt"
```
Creates: `11 Beta Blockers.xlsx`

### Single Directory (auto-finds all files):
```
/drugs-3-tab-excel "/Users/name/Documents/Pharmacology/Exam 2/Extract"
```
Finds all readable files in directory, processes in batch separate mode.

### Batch Separate (N files → N outputs):
```
/drugs-3-tab-excel "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt;Pharm_13 Diuretics_text.txt"
```
Creates 3 separate Excel files:
- `11 Beta Blockers.xlsx` (only Beta Blockers)
- `12 ACE Inhibitors.xlsx` (only ACE Inhibitors)
- `13 Diuretics.xlsx` (only Diuretics)

Uses batch-separate-processor agent with architectural isolation (zero contamination).

### Batch Merge (N files → 1 merged output):
```
/drugs-3-tab-excel --merge "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt;Pharm_13 Diuretics_text.txt"
```
Creates 1 merged Excel file:
- `Lecture 11-13.xlsx` (all drug classes merged)
- `Lecture 11-13_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge, overlap resolution, and source traceability.

### Batch Merge with Directories (N directories → 1 merged output):
```
/drugs-3-tab-excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```
Finds all files from both directories, merges into 1 comprehensive Excel chart.

### Mixed Files and Directories:
```
/drugs-3-tab-excel --merge "/path/to/Extract;specific-file.txt;/path/to/Txt"
```
Expands directories, keeps specific files, merges all into 1 Excel chart.
