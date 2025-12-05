---
description: Create multi-format study bundle (Word LO + Excel Comparison + Anki) from source
argument-hint: Single file, batch files separated by semicolon, or directory path (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir")
---

Create a multi-format study bundle from source file: $ARGUMENTS

This command generates 3 complementary formats:
1. Word LO Study Guide (.docx)
2. Excel Comparison Chart (.xlsx)
3. Anki Flashcard Deck (.apkg)

## Instructions

### Step 0: Detect Mode (Single vs Batch)

**Parse arguments:** If $ARGUMENTS contains `;` → BATCH MODE (multiple files), otherwise SINGLE MODE.

**State mode:** MODE DETECTED: [SINGLE/BATCH], File count: [#], Files: [list]

---

### Step 0.5: Handle Directory Input

If $ARGUMENTS is a directory, process all .txt/.pdf files within it.
If batch (semicolon-separated), process each path independently.

---

### Step 1: Pre-Creation Verification

**MANDATORY - State this checklist FIRST:**

```
MULTI-FORMAT BUNDLE VERIFICATION:
☐ Source file(s): $ARGUMENTS
☐ Formats to create: Word LO + Excel Comparison + Anki (3 formats)
☐ Source-only policy: I will ONLY use information from source file
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

---

## FORMAT 1: WORD LO STUDY GUIDE

### Word Step 1: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/Word_LO_11-5_REVISED.txt`
   - Main instructions and requirements (~450 lines)
   - Includes correct table formatting (black text on pastel backgrounds)

2. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Word_LO_Example.py`
   - Complete 4-section implementation with all helper functions
   - Shows Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary

### Word Step 2: Read Source File

- Read the complete source file: $ARGUMENTS
- Identify all learning objectives
- Note all topics, conditions, drugs mentioned
- Extract key information for each learning objective

### Word Step 3: Create Study Guide

Follow template instructions EXACTLY:

**Required Structure (4 sections):**
1. Learning Objectives - Each with summary, tables, boxes, mnemonics
2. Key Comparisons - Side-by-side comparison tables
3. Master Chart - Comprehensive table of all topics
4. High-Yield Summary - Color-coded boxes by category

**Key Requirements:**
- Use ONLY source file information (except mnemonics)
- Answer ALL parts of each learning objective
- Create comparison tables for 2+ similar items
- Use soft pastel color scheme from template
- NO page references in Word docs
- Font: Calibri size 12

<verbatim-requirement>
CRITICAL: Learning objective STATEMENTS must be copied EXACTLY as they appear in the source.
- Copy word-for-word, character-for-character
- Do NOT rephrase, summarize, or "improve" wording
- Preserve original numbering and sequence
- If an LO is long, still copy it completely
Note: Answers/explanations CAN be paraphrased from source content.
</verbatim-requirement>

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Word Learning Objectives (4 sections):

STRUCTURE:
- Section 1 "Learning Objectives": Each LO with Summary + Tables + Pearls Box + Mnemonics Box + Analogy Box
  - Page break after each LO
- Section 2 "Key Comparisons": Comparison tables for 2+ similar items
- Section 3 "Master Chart": ALL conditions/topics from source, color-coded rows
- Section 4 "High-Yield Summary": Color-coded boxes grouped by category

FORMATTING (MANDATORY):
- Font: Calibri size 12 (11 for dense tables)
- Table style: 'Table Grid'
- Margins: 0.8 inches all sides
- Headings: Purple (118, 75, 162)
- Table headers: Bold, colored background (pastel)
- Table data cells: Black text, white background
- Color-coded boxes:
  - High-Yield Box: Purple title (118, 75, 162), #F3E5F5 background
  - Clinical Pearls: Teal title (0, 77, 64), #E0F2F1 background
  - Critical/Emergency: Red title (183, 28, 28), #FFEBEE background
  - Memory Tricks: Orange title (230, 81, 0), #FFF3E0 background
  - Normal Variants: Green title (27, 94, 32), #E8F5E9 background
</template-compliance>

**WebSearch Requirements (MANDATORY):**
- Research mnemonics for each learning objective
- Find analogies for drug mechanisms/complex concepts
- Look for "If X think Y" clinical associations
- Use PROVEN mnemonics only - never invent

### Word Step 4: Use TodoWrite

Track your progress:
- Create todo for each learning objective
- Mark in_progress as you work
- Mark completed when done
- Keep user informed

### Word Step 5: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 4 sections present: Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary
☐ Section names correct
☐ Section 1: Each LO has Summary + Tables + Pearls Box + Mnemonics Box + Analogy Box
☐ Section 1: Page break after each LO
☐ Section 2: Comparison tables for 2+ similar items
☐ Section 3: ALL conditions/topics from source in one table
☐ Section 3: Color-coded rows by category
☐ Section 4: Color-coded boxes grouped by category

**Formatting Compliance:**
☐ Font: Calibri size 12 (11 for dense tables)
☐ Table style: 'Table Grid'
☐ Margins: 0.8 inches all sides
☐ Section headings: Purple (118, 75, 162)
☐ Table headers: Bold, colored background (pastel)
☐ Table data cells: Black text, white background
☐ Color-coded boxes use correct colors:
  - High-Yield: Purple title (118, 75, 162), #F3E5F5 background
  - Clinical Pearls: Teal title (0, 77, 64), #E0F2F1 background
  - Critical/Emergency: Red title (183, 28, 28), #FFEBEE background
  - Memory Tricks: Orange title (230, 81, 0), #FFF3E0 background
  - Normal Variants: Green title (27, 94, 32), #E8F5E9 background

**Source Accuracy:**
☐ All info from source only (except researched mnemonics)
☐ External additions marked with asterisk (*)
☐ No page references in Word docs
☐ Learning objective STATEMENTS verbatim (not paraphrased)

**Completeness:**
☐ ALL learning objectives from source included
☐ All LOs answered (all parts)
☐ All comparisons created for 2+ similar items
☐ Master chart complete with all conditions/topics
☐ Mnemonics researched via WebSearch (not invented)

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Word LO post-creation verification complete - all checks passed" or list issues found and fix them.**

### Word Step 6: Save Files

**Naming Convention:** Use source filename with new extension (e.g., `1 ANS.txt` → `1 ANS.docx`)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[SourceFileName].docx`
- Example: Source `1 ANS.txt` → Output `1 ANS.docx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[SourceFileName]_word.py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

---

## FORMAT 2: EXCEL COMPARISON CHART

### Excel Step 1: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/Excel_Comparison_Chart_REVISED.txt`
   - Main instructions and requirements

2. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Excel_Comparison_Example.py`
   - Complete 3-tab implementation with all helper functions
   - Shows Key Comparisons, Master Chart, Summary tabs

3. **Color Reference**: `study-guides/templates-and-examples/Excel_Color_Reference.txt`
   - Shared color palette and styling specifications

### Excel Step 2: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL conditions/concepts/mechanisms mentioned (don't skip any)
- Note categories suitable for comparison tables
- Identify items that need side-by-side comparison
- Look for clinical presentation, diagnosis, treatment patterns
- Note any existing mnemonics or memory aids mentioned

### Excel Step 3: Create 3-Tab Excel Chart

**Required Tabs:**

**Tab 1: Key Comparisons**
- Multiple side-by-side comparison tables
- ONE category per table (don't combine)
  - Example: Separate tables for Mechanism, Clinical Presentation, Treatment
- Columns = items being compared (e.g., Type I, Type II, Type III, Type IV)
- Rows = comparison categories within that topic
- Mnemonics placed directly BELOW relevant tables
- 2-3 blank rows between different comparison tables

**Tab 2: Master Chart**
- ALL items in one comprehensive table
- Rows = individual conditions/types
- Columns = key characteristics
- Frozen header row
- Color-coded by category

**Tab 3: Summary**
- Mnemonics (researched, with full breakdown)
- "If X Think Y" associations
- Critical values (if applicable)
- Key definitions
- High-yield pearls

**Critical Requirements:**
- Use ONLY source file information
- ALL data cells have soft pastel backgrounds
- Research mnemonics via WebSearch (mandatory)
- Multiple comparison tables (one category per table)
- Mnemonics directly below relevant tables (not on separate sheet)

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Excel Comparison Chart (3 tabs):

STRUCTURE:
- Tab 1 "Key Comparisons": MULTIPLE tables (one category per table)
  - NOT one giant table combining all categories
  - Columns = items compared, Rows = features
  - Mnemonics placed DIRECTLY BELOW relevant tables
  - 2-3 blank rows between different comparison tables
- Tab 2 "Master Chart": ALL items in ONE comprehensive table, header frozen
- Tab 3 "Summary": Mnemonics, "If X Think Y", critical values, key definitions

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

### Excel Step 4: WebSearch for Mnemonics

**MANDATORY - Research established mnemonics:**
- Search: "medical mnemonics [topic]"
- Search: "[concept] mnemonic USMLE"
- Find PROVEN mnemonics only - never invent
- Add mnemonic row after each comparison table
- Include full breakdown/explanation

### Excel Step 5: Python Implementation

Use openpyxl to create the Excel file:
- Soft pastel color scheme (hex codes from template)
- ALL cells get background colors (not just first column)
- Expand row heights to fit content
- Set appropriate column widths
- Black text throughout (#000000)

### Excel Step 6: Use TodoWrite

Track your progress:
- Create todo for each comparison table
- Create todo for each tab
- Mark completed as you finish
- Keep user informed

### Excel Step 7: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 3 tabs present: Key Comparisons, Master Chart, Summary
☐ Tab names correct
☐ Tab 1: MULTIPLE comparison tables (one category per table)
☐ Tab 1: NOT one giant table combining all categories
☐ Tab 1: Mnemonics DIRECTLY BELOW relevant tables
☐ Tab 1: 2-3 blank rows between different comparison tables
☐ Tab 2: ALL items in ONE table, header frozen
☐ Tab 3: Mnemonics, "If X Think Y", critical values, key definitions

**Formatting Compliance:**
☐ Header row: Dark blue (#4472C4), white bold text, size 12
☐ ALL data cells have pastel background (NOT white/no fill)
☐ Each category uses ONE consistent color
☐ Colors rotate when category changes
☐ White borders (#FFFFFF) on all cells
☐ Text wrapping enabled on all cells
☐ Column widths appropriate (25-40)
☐ Row heights fit content
☐ Font: Calibri, size 11 (headers 12)

**Source Accuracy:**
☐ All information from source file only
☐ No external medical facts added
☐ Terminology matches source exactly

**Completeness:**
☐ ALL conditions/concepts from source included
☐ All comparison categories covered
☐ Master chart has all items
☐ Mnemonics researched via WebSearch (not invented)

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Excel Comparison post-creation verification complete - all checks passed" or list issues found and fix them.**

### Excel Step 8: Save Files

**Naming Convention:** Use source filename with new extension (e.g., `1 ANS.txt` → `1 ANS.xlsx`)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[SourceFileName].xlsx`
- Example: Source `1 ANS.txt` → Output `1 ANS.xlsx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[SourceFileName]_excel.py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

---

## FORMAT 3: ANKI FLASHCARD DECK

### Anki Step 1: Load Resources

Read these files in order:
1. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py`
   - Complete implementation using genanki library
   - Shows model, deck, and note creation

2. **Source File**: Read the ENTIRE source file specified

### Anki Step 2: Extract Learning Objectives

**MANDATORY - Parse LOs from source file:**

1. Search for sections labeled:
   - "Learning Objectives"
   - "Learning Outcomes"
   - "LO:" or "LOs:"
   - Bullet points following these headers

2. Extract each LO statement verbatim
3. List all extracted LOs numbered

**If NO learning objectives found:**
- STOP and ask user: "No learning objectives found in source file. Options:
  A) Provide LO statements manually
  B) Proceed without filtering (create cards for all content)
  C) Cancel flashcard creation"
- Wait for user response before proceeding

**State extracted LOs:**
```
LEARNING OBJECTIVES EXTRACTED:
1. [LO statement 1]
2. [LO statement 2]
3. [LO statement 3]
...
```

### Anki Step 3: Analyze Source File (LO-Focused)

**For EACH learning objective:**
- Identify facts that DIRECTLY answer the LO
- Identify foundational facts needed to understand the answer
- Include supporting context that leads to the answer
- Map all related content to LO number
- EXCLUDE content unrelated to any LO

**Create LO-Content Mapping:**
```
LO 1: "Understand the mechanism of penicillin"
  - Foundation: Peptidoglycan structure and function
  - Foundation: Why peptidoglycan is essential for bacteria
  - Direct: Penicillin inhibits transpeptidase enzyme
  - Direct: Prevents cross-linking of peptidoglycan
  - Result: Bacterial cell wall weakens and lyses

LO 2: [LO statement]
  - Foundation: [prerequisite knowledge]
  - Direct: [facts that answer the LO]
...
```

**LO-RELEVANT FILTERING RULE:**
- Include facts that directly answer the LO
- Include foundational knowledge needed to understand the answer
- Include context that leads to or supports the answer
- EXCLUDE content that has no relationship to any LO
- When in doubt about relevance, include if it helps understanding

### Anki Step 4: Create Flashcards (LO-Filtered)

**CRITICAL: Only create flashcards for LO-mapped content from Step 3**

**LO-Aligned Flashcard Creation:**

For each LO:
- Create flashcards that test knowledge required by that LO
- Questions should align with the verb in the LO (describe, understand, define, etc.)
- Each LO should have at least 1 flashcard
- All flashcards must map to an LO

**Flashcard-LO Alignment Examples:**
- LO: "Describe bacterial shapes" → Cards asking about each shape
- LO: "Understand peptidoglycan structure" → Cards about components, function
- LO: "Define virulence factors" → Definition and example cards

**Flashcard Guidelines:**

1. **Question Quality**
   - Keep questions simple, specific, and unambiguous
   - One concept per question
   - Vary question types: What/Where/Which/How/Define/Describe
   - Avoid yes/no questions
   - Make questions self-contained (no "it" or "this")

2. **Answer Quality**
   - Single key concept per answer (typically 3-15 words)
   - **CRITICAL: Use EXACT wording from source** - Do NOT paraphrase medical terms
     - Example: Source says "beta-1 adrenergic receptors" → Answer: "beta-1 adrenergic receptors" (NOT "heart beta receptors")
     - Example: Source says "ACE inhibitor" → Answer: "ACE inhibitor" (NOT "angiotensin-converting enzyme inhibitor" unless source uses full form)
   - Preserve exact drug names, receptor names, classifications
   - No lengthy explanations - just the core fact

3. **Coverage (LO-Based)**
   - Create cards ONLY for content mapped to LOs in Step 3
   - One clear question-answer pair per LO-mapped fact
   - No duplicate concepts
   - Do NOT create cards for content outside LO scope

4. **Source-Only Policy**
   - Use ONLY information from the source file
   - **Preserve exact terminology from source** - Copy word-for-word, do NOT paraphrase
   - Do NOT add external medical knowledge

**Question Type Examples:**
- "What is the mechanism of action of [drug]?" → "[MOA]"
- "Which drug class inhibits [target]?" → "[Drug class]"
- "What are the adverse effects of [drug]?" → "[Side effects]"
- "Define [term]" → "[Definition]"
- "Where does [drug] act?" → "[Site of action]"

### Anki Step 5: Use TodoWrite

Track your progress:
- Create todo for analyzing source
- Create todo for each major topic section
- Create todo for APKG generation
- Mark completed as you finish

### Anki Step 6: Generate APKG File

**Use genanki library to create .apkg:**

@study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py

### Anki Step 7: Post-Creation Verification

**Verify the completed deck:**

1. **LO Coverage Check**
   - All LOs have at least one flashcard
   - Every flashcard maps to a specific LO
   - No flashcards for non-LO content

2. **Source Accuracy**
   - All facts come from source file only
   - Terminology matches source exactly
   - No external information added

3. **Question Quality**
   - Questions are clear and unambiguous
   - One concept per card
   - Variety of question types used

4. **Answer Quality**
   - Answers are concise (3-15 words typical)
   - Single concept per answer
   - Exact terminology preserved

**CRITICAL: State "Anki post-creation verification complete" and report:**
- Total LOs: [#]
- Total flashcards: [#]
- Cards per LO: [breakdown]

### Anki Step 8: Save Files

**Naming Convention:** Use source filename with new extension (e.g., `1 ANS.txt` → `1 ANS.apkg`)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[SourceFileName].apkg`
- Example: Source `1 ANS.txt` → Output `1 ANS.apkg`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[SourceFileName]_anki.py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

---

## Bundle Completion Report

**After all 3 formats complete:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MULTI-FORMAT BUNDLE CREATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Source: [filename]
Formats generated: 3

Outputs:
1. [filename]_Study_Guide.docx (Word LO)
   - Learning objectives: [N]
   - Sections: 4 (LOs, Comparisons, Master Chart, High-Yield)

2. [filename]_Comparison_Chart.xlsx (Excel Comparison)
   - Comparison tables: [N]
   - Tabs: 3 (Key Comparisons, Master Chart, Summary)

3. [filename]_Flashcards.apkg (Anki)
   - Total cards: [N]
   - LOs covered: [N]

Location: [Class]/[Exam]/Claude Study Tools/

Quality Assurance:
✓ Word LO post-creation verification complete
✓ Excel Comparison post-creation verification complete
✓ Anki post-creation verification complete
✓ All source-only policies enforced
✓ All LO tracking completed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Batch Processing

For batch operations (semicolon-separated files):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

### Word LO Mistakes
- Paraphrasing learning objective statements (must be verbatim)
- Missing page breaks between learning objectives
- Using wrong box colors (e.g., using purple for Clinical Pearls)
- Inventing mnemonics instead of researching via WebSearch
- Missing sections (must have all 4 sections)

### Excel Comparison Mistakes
- Combining multiple categories in one comparison table
- Putting mnemonics only in Summary (should be below relevant tables too)
- Inventing mnemonics instead of researching
- White backgrounds on data cells (should be pastel)
- Using 4 tabs instead of 3

### Anki Mistakes
- Creating vague or ambiguous questions
- Putting multiple concepts in one answer
- Adding information not in the source
- Using pronouns without clear referents
- Making answers too long (should be 3-15 words)
- Skipping important facts from source
- Creating cards for non-LO content

### General Mistakes
- Adding external medical information not in source
- Not using TodoWrite to track progress
- Skipping post-creation verification

---

## Example Usage

**Single:**
```
/word-excel-anki "Pharmacology/Exam 3/Extract/HIV_Drugs.txt"
```

**Batch:**
```
/word-excel-anki "HIV.txt;Antibiotics.txt;Antivirals.txt"
```

**Directory:**
```
/word-excel-anki "Pharmacology/Exam 3/Extract/"
```

---

## Format Defaults

This command always creates: Word LO + Excel Comparison + Anki

For different format combinations, use:
- `/create-all` with --formats flag
- `/study-guides` for interactive format selection

---

**End of Command**
