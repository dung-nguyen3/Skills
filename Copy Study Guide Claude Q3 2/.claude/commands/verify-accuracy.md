---
description: Perform comprehensive accuracy analysis of existing study guide against source file
argument-hint: Study guide file path and source file path (e.g., "study_guide.xlsx source.txt")
---

Analyze study guide accuracy: $ARGUMENTS

## Purpose

Systematically verify an existing study guide (Word/Excel/HTML) against its source file to ensure:
- All information from source only
- Correct classifications and groupings
- No incorrect merged cells
- Template compliance
- Complete coverage of source material

---

## 6-Step Verification Protocol

### Step 1: Read Source File Completely

**Read the ENTIRE source file thoroughly:**
- Identify ALL drugs/topics/conditions mentioned
- Note all learning objectives
- Document specific information for each item
- Extract key details: MOA, uses, adverse effects, etc.

**Create notes:**
- Drug 1: [specific info from source]
- Drug 2: [specific info from source]
- Condition 1: [specific info from source]

---

### Step 2: Load and Examine Existing File

**Load the study guide file:**
- Open Excel/Word/HTML file
- List all sheets/sections/tabs
- Print drug/topic lists
- Note their classifications
- Identify all merged cells and groupings

**Initial assessment:**
- How many items total?
- How are they organized?
- What sections/tabs exist?

---

### Step 3: Systematic Verification Checks

**Check 1: Names & Spelling**
- Verify ALL names match source EXACTLY
- Check spelling, capitalization, brand names
- Identify any names NOT in source (external additions)
- Create list: ✓ Present or ✗ Missing

**Check 2: Classifications**
- Verify each item assigned to correct class/category
- Check source for class assignments
- Confirm: All classifications accurate ✓

**Check 3: Merged Cells & Groupings (CRITICAL)**
- Identify ALL merged cells in Excel
- For EACH merged cell, verify in source:
  - Do these items truly share IDENTICAL information?
  - Are they grouped together in source?
  - Is this class-wide or drug-specific?

**Common issues:**
- Different drugs merged but have different MOAs
- Different adverse effects incorrectly grouped
- Items with different info merged together
- Drug-specific info applied to entire class

**Check 4: Information Accuracy (Item-Specific)**

For EACH drug/item, verify:
- **Mechanism:** Is this MOA for THIS specific drug or class-wide?
- **Adverse effects:** Are these for THIS drug specifically?
- **First-line:** Is THIS drug marked first-line (or just its class)?
- **Contraindications:** Are these specific to THIS drug?
- **Combinations:** Is THIS drug in this combination (source confirms)?

**Check for external information:**
- Anything NOT in source should have asterisk (*)
- Critical external info marked properly

**Check 5: Format & Colors (Excel/Word)**

**For Excel files:**
- Correct color scheme (soft pastels, black text)
- Correct hex codes from template
- Proper tab structure (4 tabs for Drug Chart, 5 for Complete)
- Column widths appropriate
- Row heights fit content
- ALL data cells have pastel backgrounds (not white)
- Text wrapping enabled
- Frozen headers where specified
- Memory tricks/mnemonics row after EACH drug class:
  - Merged across all columns
  - Light blue background (#E6F3FF)
  - Label: "💡 MEMORY TRICKS & MNEMONICS"
  - Contains researched mnemonics
  - 2 blank rows after before next class

**For Word files:**
- Soft pastel color scheme
- Calibri font size 12
- All 4 sections present
- Proper table formatting
- Color-coded boxes correct

**Check 6: Emojis & Visual Indicators**
- Verify ONLY template emojis used
- Check: 🟢 (first-line), ⚠️ (warnings), 🚫 (contraindications)
- No extra emojis added

---

### Step 4: Document All Issues Found

**Create comprehensive issue report:**

```
ACCURACY ANALYSIS REPORT
========================

FILE: [filename]
SOURCE: [source file]
DATE: [date]

ISSUES FOUND:
-------------

Issue 1: [Description]
- Source says: [what source actually says]
- File shows: [what file incorrectly shows]
- Status: ❌ INCORRECT

Issue 2: [Description]
- Source says: [actual info]
- File shows: [incorrect info]
- Status: ❌ INCORRECT

CORRECT ITEMS:
--------------
✅ [What's accurate]
✅ [What's correct]

SUMMARY:
--------
Total issues: [number]
Critical issues: [number]
Minor issues: [number]
```

---

### Step 5: Fix ALL Issues

**For each issue identified:**
1. Locate the incorrect cell/section
2. Verify correct information from source
3. Update with source-only information
4. Correct spelling to match source EXACTLY
5. Un-merge cells if grouped incorrectly
6. Re-verify the fix

**Use TodoWrite:**
- Create todo for each issue
- Mark in_progress as you fix
- Mark completed when verified

---

### Step 6: Re-Verify After Fixes (MANDATORY)

**CRITICAL - Never skip this step!**

**Re-analyze the ENTIRE file:**
- Verify all drug/topic groupings correct
- Confirm all information matches source
- Check format/colors match template
- Verify no new errors introduced

**Create final verification checklist:**
```
FINAL VERIFICATION:
☐ All names match source exactly
☐ All classifications correct
☐ No incorrect groupings or merged cells
☐ No external information (except * marked)
☐ Format matches instruction template
☐ Colors correct per template specifications
☐ All issues from Step 4 resolved
☐ No new errors introduced
```

**State:** "Re-verification complete. All issues resolved."

---

### Step 7: Use TodoWrite Throughout

Track verification progress:
- [ ] Step 1: Read source file
- [ ] Step 2: Load existing file
- [ ] Step 3: Run systematic checks
- [ ] Step 4: Document all issues
- [ ] Step 5: Fix all issues
- [ ] Step 6: Re-verify entire file
- [ ] Step 7: Final report

---

## Common Issues to Look For

### Drug-Specific Issues:
- ❌ Class-wide MOA incorrectly applied to specific drug
- ❌ Drug marked first-line when only class is
- ❌ Specific adverse effect merged with entire class
- ❌ Pregnancy safety assumed for all drugs in class
- ❌ Contraindications applied to wrong drug

### Grouping Issues:
- ❌ Drugs merged that have different information
- ❌ Conditions grouped that aren't similar
- ❌ Clinical findings merged incorrectly

### Source Accuracy Issues:
- ❌ External medical facts added without asterisk
- ❌ Information not in source included
- ❌ Interpretations instead of source facts

### Format Issues:
- ❌ Wrong color scheme used
- ❌ Missing required sections/tabs
- ❌ Memory tricks row missing or incorrect
- ❌ White backgrounds instead of pastels

---

## Example Usage

```
/verify-accuracy "Pharmacology/Exam 3/Claude Study Tools/HIV_Drug_Chart.xlsx" "Pharmacology/Exam 3/Extract/HIV Drugs.txt"
```

This will perform comprehensive 6-step accuracy analysis and fix all issues found.

---

## Final Report Format

After completing all 6 steps, provide:

```
VERIFICATION COMPLETE
=====================

File analyzed: [filename]
Source file: [source]

RESULTS:
--------
Issues found: [number]
Issues fixed: [number]
Re-verification: ✓ PASSED

SUMMARY OF CHANGES:
-------------------
1. [Change made]
2. [Change made]
3. [Change made]

FINAL STATUS:
-------------
✅ All names match source exactly
✅ All classifications correct
✅ No incorrect groupings
✅ No external information added
✅ Format matches template
✅ Colors correct

The study guide is now accurate and ready to use.
```
