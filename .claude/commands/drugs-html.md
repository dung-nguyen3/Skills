---
description: Create interactive HTML drug reference chart (pharmacology)
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create an HTML drug reference chart from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 HTML drug reference (inline processing)
- **BATCH SEPARATE**: N files → N HTML drug references (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged HTML drug reference (orchestrator agent, intelligent merge)

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
☐ Template: HTML_LO_REVISED.txt (adapted for drugs)
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
☐ Template: HTML_LO_REVISED.txt (adapted for drugs, per file)
☐ Output: N files → N HTML drug references
☐ Agent: batch-separate-processor (launched N times)
☐ Architectural isolation: Each file processed in separate agent context
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-separate-processor agent:**

```
I'll use the batch-separate-processor agent to process your files with architectural isolation.

Launching agent [X] times:
- File 1: batch-separate-processor → [Output1.html]
- File 2: batch-separate-processor → [Output2.html]
...
- File N: batch-separate-processor → [OutputN.html]

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
☐ Template: HTML_LO_REVISED.txt (adapted for drugs, unified)
☐ Output: N files → 1 merged HTML drug reference
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
5. Merge into ONE comprehensive HTML drug reference
6. Create merge report with traceability map

Output:
- 1 merged HTML drug reference: [filename.html]
- 1 merge report: [filename_merge_report.md]
```

**STOP HERE - Do NOT continue with Steps 2-7. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-7)
- Do NOT mix - if agent is launched, STOP and let agent complete the work
☐ Mnemonics researched per-file via WebSearch
```

**IMPORTANT**: Full verification checklist will run for EACH file (Step 1 repeated in Batch Processing).

### Step 2: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/HTML_LO_REVISED.txt`
   - HTML structure and formatting guide
   - Tab organization requirements
   - Color-coding specifications

2. **Source File**: $ARGUMENTS
   - Extract all drugs mentioned
   - Note drug classes and classifications
   - Identify mechanisms, uses, adverse effects

### Step 3: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL drugs mentioned (don't skip any)
- Note drug classes and classifications
- Extract drug-specific vs class-wide information
- Verify first-line designations
- Document combination therapies

### Step 4: Create 3-Tab HTML Chart

**Required Tabs:**

**Tab 1: Drug Classes & Comparisons**
- Drug class comparison tables
- Drugs as columns, properties as rows
- Mechanism of action with analogies
- Key differences highlighted
- Memory tricks after each drug class

**Tab 2: Master Drug Chart**
- ALL drugs in one comprehensive table
- Sortable columns
- Color-coded badges for:
  - Routes (PO, IV, IM, etc.)
  - Contraindications
  - First-line drugs (green badge)
- Includes: Drug name, Class, Mechanism, Uses, Adverse Effects, Interactions

**Tab 3: Quick Reference**
- High-yield pearls
- "If X Think Y" associations
- Clinical decision support
- Researched mnemonics
- Must-know facts

### Step 5: WebSearch for Mnemonics

**MANDATORY - Research established mnemonics:**
- Search: "medical mnemonics [drug class]"
- Search: "[drug name] mnemonic USMLE"
- Find PROVEN mnemonics only - never invent
- Add mnemonic sections after drug classes
- Include full breakdown/explanation

### Step 6: HTML Formatting Requirements

**Required:**
- Inline CSS styles (no external stylesheets)
- Interactive tabs with onclick navigation
- Sortable tables (JavaScript included)
- Responsive grid layouts
- Color-coded badges:
  - Green: First-line drugs
  - Red: Serious warnings/contraindications
  - Blue: IV route
  - Orange: Special populations caution

**Structure:**
- Self-contained single HTML file
- Works offline
- Mobile-friendly responsive design

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
   - Terminology matches source exactly

2. **Template Compliance**
   - All 3 tabs present (Drug Classes, Master Chart, Quick Reference)
   - Color-coded badges correctly applied
   - Sortable tables functional
   - Responsive design working

3. **Completeness**
   - ALL drugs from source included
   - All drug classes covered
   - Master chart has all drugs
   - Mnemonics researched (not invented)

4. **Quality**
   - No incorrect groupings
   - Proper HTML structure
   - All tabs clickable and functional
   - Mobile-friendly layout

**CRITICAL: State "Post-creation verification complete" and report any issues. Fix immediately.**

### Step 9: Save File

- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Drug_Reference_Chart.html`
- Create Claude Study Tools folder if doesn't exist
- Confirm file saved successfully

### Step 10: Drug Coverage Report (SINGLE MODE ONLY)

**Compare drugs included vs Drug Inventory from Step 0.8:**

1. Count drugs actually included in the HTML chart
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

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

❌ Marking all drugs as first-line when only specific ones are
❌ Applying drug-specific info to entire class
❌ Inventing mnemonics instead of researching
❌ Missing drugs from source file
❌ Non-functional tabs or sorting
❌ External stylesheet references (should be inline)

## Example Usage

**Single:** Command with one file

**Batch:** Command with semicolon-separated files → Creates separate output files

