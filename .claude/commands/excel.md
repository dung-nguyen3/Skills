---
description: Create comprehensive 4-tab Excel drug chart from pharmacology source material
argument-hint: Single file OR batch files separated by semicolon. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "--merge f1.txt;f2.txt")
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

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Instruction template: Excel Drugs Chart 11-1.txt
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

### Step 8: Post-Creation Verification

**Automatically verify the completed file:**

1. **Source Accuracy**
   - Drug-specific info NOT applied to all drugs in class
   - First-line designation only for drugs explicitly stated
   - No external info (except researched mnemonics)
   - Verify before merging cells

2. **Template Compliance**
   - EXACTLY 4 tabs (Drug Details, Key Comparisons, Master Chart, High-Yield)
   - Soft pastel colors on ALL data cells
   - Memory tricks row after EACH drug class
   - Correct structure per template

3. **Completeness**
   - ALL drugs from source included
   - All drug classes covered
   - Master chart has all drugs
   - Mnemonics researched (not invented)

4. **Quality**
   - No incorrect groupings or merged cells
   - Row heights fit content
   - Proper formatting throughout

**CRITICAL: State "Post-creation verification complete" and report any issues. Fix immediately.**

### Step 9: Save File

- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Drug_Chart.xlsx`
- Create Claude Study Tools folder if doesn't exist
- Confirm file saved successfully

---

## Common Mistakes to Avoid

❌ Marking all drugs as first-line when only specific ones are
❌ Merging cells without verifying identical information
❌ Applying drug-specific info to entire class
❌ Inventing mnemonics instead of researching
❌ White backgrounds on data cells (should be pastel)
❌ Missing memory tricks row after drug classes

## Example Usage

### Single File:
```
/excel "Pharmacology/Exam 3/Extract/HIV Antivirals.txt"
```
Creates: `HIV_Antivirals_Drug_Chart.xlsx`

### Batch Separate (N files → N outputs):
```
/excel "HIV.txt;COVID.txt;Antibiotics.txt"
```
Creates 3 separate Excel files:
- `HIV_Drug_Chart.xlsx` (only HIV drugs)
- `COVID_Drug_Chart.xlsx` (only COVID drugs)
- `Antibiotics_Drug_Chart.xlsx` (only antibiotic drugs)

Uses batch-separate-processor agent with architectural isolation (zero contamination).

### Batch Merge (N files → 1 merged output):
```
/excel --merge "HIV-PIs.txt;HIV-NRTIs.txt;HIV-NNRTIs.txt"
```
Creates 1 merged Excel file:
- `HIV_Comprehensive_Drug_Chart.xlsx` (all HIV drug classes merged)
- `HIV_Comprehensive_Drug_Chart_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge, overlap resolution, and source traceability.
