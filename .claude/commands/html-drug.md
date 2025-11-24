---
description: Create interactive HTML drug reference chart (pharmacology)
argument-hint: Single file OR batch files separated by semicolon (e.g., "file1.txt" OR "file1.txt;file2.txt")
---

Create an HTML drug reference chart from source file: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single vs Batch)

**Parse arguments:** If $ARGUMENTS contains `;` → BATCH MODE (multiple files), otherwise SINGLE MODE.

**State mode:** MODE DETECTED: [SINGLE/BATCH], File count: [#], Files: [list]

---


### Step 1: Pre-Creation Verification

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Template: HTML_LO_REVISED.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

#### For BATCH MODE:

```
BATCH INITIAL VALIDATION:
☐ Source files: [list all files from $ARGUMENTS]
☐ File validation: All files exist and are readable
☐ Homogeneity check: All files are drug lectures (same template applies)
☐ Template: HTML_LO_REVISED.txt (applies to ALL)
☐ Output: ONE HTML file will be created per source file
☐ Save location: [Class]/[Exam]/Claude Study Tools/

BATCH PROCESSING RULES:
☐ Each file will get complete verification (not just once)
☐ Each file will be processed independently
☐ Context isolation: I will explicitly clear data between files
☐ Source-only policy applies per-file
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


---

### Batch Processing (BATCH MODE ONLY)

**If BATCH MODE, process each file independently:**

For each source file in the batch:
1. **Announce file**: "Processing file X of Y: [filename]"

2. **CRITICAL - Context Isolation Check**:
   ```
   CONTEXT ISOLATION VERIFICATION:
   ☐ I will FORGET all drugs from previous files
   ☐ I will ONLY extract information from THIS source file: [filename]
   ☐ I will verify drug list is ONLY from THIS file (not previous files)
   ☐ This HTML will contain ZERO drugs from previous files
   ```

3. **Per-File Verification** - Run complete verification checklist for THIS file

4. **Read source file** - Read THIS file completely, extract THIS file's drugs only

5. **MANDATORY - State drug list**: "Drugs found in [filename]: [list all drugs]"
   - This proves you're only using THIS file's drugs
   - If you see drugs from previous files, STOP and re-read source

6. **Create HTML file** - For THIS file only, using ONLY drugs from step 5

7. **Post-creation verification** - Verify THIS HTML contains ONLY THIS file's drugs

8. **MANDATORY - Isolation Confirmation**: "File [X] complete. Cleared all data. Ready for next file."

**Critical for Batch:**
- Each file gets complete verification (not once at start)
- Explicitly state drug list from each file before creating HTML
- Verify no drugs from previous files contaminated output
- Clear all data between files
- Each file gets its own HTML output

**Batch Summary**: After all files, provide summary of files created, drug counts, and any issues.

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

