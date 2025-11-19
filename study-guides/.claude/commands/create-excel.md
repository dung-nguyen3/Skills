---
description: Create comprehensive 4-tab Excel drug chart from pharmacology source material
argument-hint: Source file path (e.g., "Pharmacology/Exam 3/Extract/HIV Drugs.txt")
---

Create an Excel drug chart from source file: $ARGUMENTS

## Instructions

### Step 1: Pre-Creation Verification

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

### Step 2: Load Resources

Read these files in order:
1. **Template**: `templates-and-examples/Excel_Drugs_Chart_11-1_REVISED.txt`
   - Main instructions and requirements (~550 lines)

2. **Example Code**: `templates-and-examples/Python_Examples/Excel_Drug_Example.py`
   - Complete 4-tab implementation with all helper functions
   - Shows Drug Details, Key Comparisons, Master Chart, High-Yield tabs

3. **Color Reference**: `templates-and-examples/Excel_Color_Reference.txt`
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

## Common Mistakes to Avoid

❌ Marking all drugs as first-line when only specific ones are
❌ Merging cells without verifying identical information
❌ Applying drug-specific info to entire class
❌ Inventing mnemonics instead of researching
❌ White backgrounds on data cells (should be pastel)
❌ Missing memory tricks row after drug classes

## Example Usage

```
/create-excel Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

This will create a comprehensive 4-tab Excel drug chart with all drugs, comparisons, and researched mnemonics.
