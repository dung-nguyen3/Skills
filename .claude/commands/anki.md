---
description: Create comprehensive Anki flashcard deck (.apkg) from source material
argument-hint: Single file, batch files separated by semicolon, or directory path (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir")
---

Create an Anki flashcard deck from source file: $ARGUMENTS

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

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Source-only policy: I will ONLY use information from source file
☐ LO-filtering: I will ONLY create cards for content that directly answers Learning Objectives
☐ No non-LO content will be included
☐ No external facts will be added
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

#### For BATCH MODE:

```
BATCH INITIAL VALIDATION:
☐ Source files: [list all files from $ARGUMENTS]
☐ File validation: All files exist and are readable
☐ Homogeneity check: All files use same source-only policy
☐ LO-filtering: Each file will be filtered by its Learning Objectives
☐ Output: ONE Anki deck will be created per source file
☐ Save location: [Class]/[Exam]/Claude Study Tools/

BATCH PROCESSING RULES:
☐ Each file will get complete verification (not just once)
☐ Each file will be processed independently
☐ Context isolation: I will explicitly clear data between files
☐ Source-only policy applies per-file
☐ LO-filtering applies per-file
☐ No external facts will be added to any deck
```

**IMPORTANT**: Full verification checklist will run for EACH file (Step 1 repeated in Batch Processing).

### Step 2: Load Resources

Read these files in order:
1. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py`
   - Complete implementation using genanki library
   - Shows model, deck, and note creation

2. **Source File**: Read the ENTIRE source file specified

### Step 3: Extract Learning Objectives

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

### Step 4: Analyze Source File (LO-Focused)

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

### Step 5: Create Flashcards (LO-Filtered)

**CRITICAL: Only create flashcards for LO-mapped content from Step 4**

**CSV Format:**
- First line: `Question,Answer`
- One Q&A pair per line
- Save intermediate as: `[topic]_Flashcards.csv`

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
   - Preserve exact medical/technical terminology
   - Preserve exact drug names, receptor names, classifications
   - No lengthy explanations - just the core fact

3. **Coverage (LO-Based)**
   - Create cards ONLY for content mapped to LOs in Step 4
   - One clear question-answer pair per LO-mapped fact
   - No duplicate concepts
   - Do NOT create cards for content outside LO scope

4. **Source-Only Policy**
   - Use ONLY information from the source file
   - Preserve exact terminology from source
   - Do NOT add external medical knowledge

**Question Type Examples:**
- "What is the mechanism of action of [drug]?" → "[MOA]"
- "Which drug class inhibits [target]?" → "[Drug class]"
- "What are the adverse effects of [drug]?" → "[Side effects]"
- "Define [term]" → "[Definition]"
- "Where does [drug] act?" → "[Site of action]"

### Step 6: Use TodoWrite

Track your progress:
- Create todo for analyzing source
- Create todo for each major topic section
- Create todo for CSV generation
- Create todo for APKG conversion
- Mark completed as you finish

### Step 7: Generate APKG File

**Use genanki library to create .apkg:**

@study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py

### Step 8: Post-Creation Verification

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

**CRITICAL: State "Post-creation verification complete" and report:**
- Total LOs: [#]
- Total flashcards: [#]
- Cards per LO: [breakdown]

### Step 9: Save Files

- CSV: `[Class]/[Exam]/Claude Study Tools/[Topic]_Flashcards.csv`
- APKG: `[Class]/[Exam]/Claude Study Tools/[Topic]_Flashcards.apkg`
- Create Claude Study Tools folder if doesn't exist
- Confirm files saved successfully


---

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

- Creating vague or ambiguous questions
- Putting multiple concepts in one answer
- Adding information not in the source
- Using pronouns without clear referents
- Making answers too long (should be 3-15 words)
- Skipping important facts from source
- Not escaping commas/quotes in CSV properly

## Example Usage

**Single:** Command with one file

**Batch:** Command with semicolon-separated files → Creates separate output files

