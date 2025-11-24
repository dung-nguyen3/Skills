---
description: Create comprehensive 4-tab Excel drug chart from pharmacology source material
argument-hint: Single file OR batch files separated by semicolon (e.g., "file1.txt" OR "file1.txt;file2.txt;file3.txt")
---

Create Excel drug chart from: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single vs Batch)

**Parse arguments to detect batch mode:**

If $ARGUMENTS contains semicolons (`;`):
- **BATCH MODE**: Multiple source files
- Split by semicolon to get file list
- Each file will create a separate Excel chart
- Example: `"HIV.txt;COVID.txt;Antibiotics.txt"` → 3 Excel files

If $ARGUMENTS does NOT contain semicolons:
- **SINGLE MODE**: One source file (existing behavior)
- Example: `"HIV.txt"` → 1 Excel file

**State which mode detected:**
```
MODE DETECTED: [SINGLE or BATCH]
File count: [#]
Files: [list]
```

---

### Step 1: Pre-Creation Verification

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

#### For BATCH MODE:

**MANDATORY - State this checklist FIRST:**

```
BATCH INITIAL VALIDATION:
☐ Source files: [list all files from $ARGUMENTS]
☐ File validation: All files exist and are readable
☐ Homogeneity check: All files are drug lectures (same template applies)
☐ Instruction template: Excel Drugs Chart 11-1.txt (applies to ALL files)
☐ Output: ONE Excel file will be created per source file
☐ Save location: [Class]/[Exam]/Claude Study Tools/

BATCH PROCESSING RULES:
☐ Each file will get complete verification (not just once)
☐ Each file will be processed independently
☐ Context isolation: I will explicitly clear data between files
☐ Source-only policy applies per-file
☐ Mnemonics researched per-file via WebSearch
```

**IMPORTANT**: Full verification checklist will run for EACH file (Step 1 repeated in Step 10).

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

### Step 10: Batch Processing (BATCH MODE ONLY)

**If BATCH MODE, repeat Steps 1-9 for EACH file:**

For each source file in the batch:
1. **Announce file**: "Processing file X of Y: [filename]"

2. **CRITICAL - Context Isolation Check**:
   ```
   CONTEXT ISOLATION VERIFICATION:
   ☐ I will FORGET all drugs from previous files
   ☐ I will ONLY extract information from THIS source file: [filename]
   ☐ I will verify drug list is ONLY from THIS file (not previous files)
   ☐ This Excel will contain ZERO drugs from previous files
   ```

3. **Per-File Verification** (Step 1) - Run complete verification checklist for THIS file

4. **Load resources** (Step 2) - templates already loaded, reuse

5. **Analyze source file** (Step 3) - read THIS file completely, extract THIS file's drugs only

6. **MANDATORY - State drug list**: "Drugs found in [filename]: [list all drugs]"
   - This proves you're only using THIS file's drugs
   - If you see drugs from previous files, STOP and re-read source

7. **Create 4-tab Excel** (Step 4-6) - for THIS file only, using ONLY drugs from step 6

8. **WebSearch mnemonics** (Step 5) - for THIS file's drugs only

9. **Use TodoWrite** (Step 7) - track THIS file's progress

10. **Post-creation verification** (Step 8) - verify THIS file contains ONLY THIS file's drugs

11. **Save file** (Step 9) - with unique filename based on source

12. **MANDATORY - Isolation Confirmation**: "File [X] complete. Cleared all data. Ready for next file."

**Critical for Batch:**
- Each file gets complete verification (not once at start)
- Explicitly state drug list from each file before creating Excel
- Verify no drugs from previous files contaminated output
- Clear all drug data between files
- Each file gets its own Excel output
- Track which source created which Excel file

**Progress Tracking:**
```
[BATCH PROGRESS]
✅ File 1/3: HIV_Drug_Chart.xlsx (45 drugs)
✅ File 2/3: COVID_Drug_Chart.xlsx (28 drugs)
🔄 File 3/3: Antibiotics_Drug_Chart.xlsx (in progress...)
```

---

### Step 11: Batch Summary (BATCH MODE ONLY)

**After all files processed, provide summary:**

```
BATCH CREATION COMPLETE
═══════════════════════════════════════

Files Created Successfully:
✅ [filename1]_Drug_Chart.xlsx ([#] drugs from [source1])
✅ [filename2]_Drug_Chart.xlsx ([#] drugs from [source2])
✅ [filename3]_Drug_Chart.xlsx ([#] drugs from [source3])

Failed Files (if any):
❌ [filename]: [error reason]

Statistics:
- Total files processed: [#]
- Successful: [#]
- Failed: [#]
- Total drugs across all files: [#]
- All verifications: [PASS/NEEDS WORK]

Location: [Class]/[Exam]/Claude Study Tools/

Next Steps:
- Review each file for accuracy
- Use /verify-accuracy for deep analysis if needed
```

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

### Batch Files:
```
/excel "Pharmacology/Exam 3/Extract/HIV.txt;Pharmacology/Exam 3/Extract/COVID.txt;Pharmacology/Exam 3/Extract/Antibiotics.txt"
```
Creates 3 separate Excel files:
- `HIV_Drug_Chart.xlsx`
- `COVID_Drug_Chart.xlsx`
- `Antibiotics_Drug_Chart.xlsx`

Each file will be comprehensive 4-tab Excel drug chart with all drugs, comparisons, and researched mnemonics.
