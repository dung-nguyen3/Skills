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

### Step 4: Analyze Source File (Essential Facts + High-Yield)

**For EACH learning objective:**
- Identify the **minimum essential facts** needed to answer the LO
- Focus on what you'd need to **recall** to answer the question
- Skip background/context that doesn't require memorization
- Map essential content to LO number
- EXCLUDE content unrelated to any LO

**Create Essential Facts Mapping:**
```
LO 1: "Understand the mechanism of penicillin"
  - Essential: Penicillin inhibits transpeptidase enzyme
  - Essential: Prevents peptidoglycan cross-linking
  - Essential: Results in bacterial cell wall lysis

LO 2: [LO statement]
  - Essential: [minimum facts needed to answer LO]
...
```

**IDENTIFY HIGH-YIELD FACTS (even if not directly tied to LOs):**
```
HIGH-YIELD FACTS:
- Black box warnings
- Drug interactions (especially dangerous ones)
- First-line treatments
- Pathognomonic findings/"buzzwords"
- Common adverse effects (not exhaustive lists)
- Clinical pearls emphasized in lecture
- Board exam favorites
```

**ESSENTIAL + HIGH-YIELD FILTERING RULE:**
- Include facts that **directly answer** the LO (essential)
- Include **high-yield clinical facts** (black box warnings, dangerous interactions, first-line treatments)
- EXCLUDE background/context that doesn't require active recall
- EXCLUDE content unrelated to any LO or clinical practice
- **When in doubt about relevance, SKIP it** - focus on essential + high-yield only

### Step 5: Create Flashcards (LO-Filtered)

**CRITICAL: Only create flashcards for LO-mapped content from Step 4**

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

3. **Coverage (Essential + High-Yield)**
   - Create cards ONLY for essential facts and high-yield content from Step 4
   - **ONE fact per card** (Minimum Information Principle - atomic cards)
   - **Word limits:** Questions <20 words, Answers <30 words (ideally 3-15)
   - **No filler words** - be concise and precise
   - **Context connection:** Link each card to its LO or clinical significance
   - **Vary question structures:** Avoid repetitive phrasing (What/Which/How/Define/Describe)
   - No duplicate concepts
   - Do NOT create cards for content outside LO scope or low-yield facts

   **Essential vs Skip Decision Criteria:**
   ✓ Create cards for:
   - Facts that directly answer an LO
   - High-yield clinical facts (black box warnings, dangerous interactions)
   - Information you'd be tested on or need clinically

   ✗ Skip cards for:
   - Background physiology you already know
   - Low-yield trivia or historical facts
   - Over-detailed information not emphasized in lecture
   - Context that doesn't require active recall

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

### Step 6: Use TodoWrite

Track your progress:
- Create todo for analyzing source
- Create todo for each major topic section
- Create todo for APKG generation
- Mark completed as you finish

### Step 7: Generate APKG File

**Use genanki library to create .apkg:**

@study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py

### Step 8: Post-Creation Verification

**Verify the completed deck:**

1. **LO Coverage Check**
   - All LOs have at least one flashcard
   - Every flashcard maps to a specific LO or high-yield fact
   - No flashcards for non-LO or low-yield content

2. **Source Accuracy**
   - All facts come from source file only
   - Terminology matches source exactly
   - No external information added

3. **Question Quality**
   - Questions are clear and unambiguous
   - **Atomic cards:** Each card tests ONE fact only (no combined concepts)
   - **Word count:** Questions <20 words
   - **Variety:** Question structures vary (not repetitive)
   - **Precision:** Questions are specific and self-contained

4. **Answer Quality**
   - **Concise:** Answers <30 words (ideally 3-15 words)
   - **Atomic:** Single concept per answer
   - **Exact terminology:** Source wording preserved exactly
   - **Context:** Answers connect to LO or clinical significance

5. **Volume Check**
   - Typical range: 50-100 cards for standard lecture
   - If >150 cards: Review for over-inclusion (too many low-yield or background facts)
   - If <30 cards: Verify all LOs and high-yield facts covered
   - **Quality over quantity** - better fewer essential cards than exhaustive coverage

6. **Essential vs Exhaustive**
   - Are these essential facts or exhaustive coverage?
   - Did you skip low-yield background information?
   - Are cards focused on what you'd be tested on?

**CRITICAL: State "Post-creation verification complete" and report:**
- Total LOs: [#]
- Total flashcards: [#]
- Cards per LO: [breakdown]
- Volume assessment: [within/above/below typical range]

### Step 9: Save Files

**Output Filename Rule:**
1. Strip file extension and common suffixes (`_text.txt`, `_extracted.txt`, etc.)
2. Strip course prefixes (`Micro_`, `Pharm_`, `Clinical_`, `Patho_`, etc.)
3. Replace underscores with spaces for readability
4. Extract lecture number and topic: `[Number] [Topic]` or just `[Topic]`
5. Preserve capitalization as-is (after underscore→space conversion)
6. Add appropriate extension: `.apkg`
7. NO template suffixes, NO title case normalization

**Examples:**
- `Micro_4 Intro to Virology_text.txt` → `4 Intro to Virology.apkg`
- `Pharm_11 Beta Blockers_text.txt` → `11 Beta Blockers.apkg`
- `Micro_4_Intro_To_Virology_text.txt` → `4 Intro To Virology.apkg`
- `Micro_Basics Of Immunology_text.txt` → `Basics Of Immunology.apkg`

**Batch Merge Naming:**
- Input: `Micro_4 Intro to Virology_text.txt` + `Micro_5 Viral Replication_text.txt`
- Output: `Lecture 4-5.apkg`
- Format: `Lecture [min]-[max].apkg` (based on lecture numbers found)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/anki/[OutputFilename].apkg`
- Create `Claude Study Tools/anki/` folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[OutputFilename].py`
- Create `Claude Study Tools/py/` subfolder if doesn't exist

**Directory Structure:**
```
Claude Study Tools/
├── anki/
│   └── [OutputFilename].apkg
├── py/
│   └── [OutputFilename].py
```

- Confirm both files saved successfully

### Step 10: Auto-Import (Optional)

**Auto-import uses AnkiConnect to automatically import .apkg files into Anki.**

**Status messages:**

✅ **Success:**
```
🔄 Importing deck into Anki via AnkiConnect...
✅ Successfully imported into Anki!
```

⚠️ **AnkiConnect not available:**
```
⚠️  Auto-import skipped: AnkiConnect not available
    → Make sure Anki is running
    → Install AnkiConnect add-on (code: 2055492159)
    → Restart Anki after installing
```

⚠️ **Auto-import disabled (default):**
```
💡 To import: Open Anki → File → Import
   Or enable auto-import in .claude/settings.json
```

**To enable auto-import:**

Create or edit `.claude/settings.local.json`:
```json
{
  "anki_auto_import": {
    "enabled": true
  }
}
```

**Requirements:**
- Anki must be running
- AnkiConnect add-on installed (code: 2055492159)
- Run: `pip install requests`

**Setup AnkiConnect:**
1. Open Anki
2. Tools → Add-ons → Get Add-ons
3. Enter code: `2055492159`
4. Restart Anki

**Batch mode:** All decks are imported in a single session with success/failure summary.

---

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

- Creating vague or ambiguous questions
- **Putting multiple concepts in one card** (violates Minimum Information Principle)
- **Creating too many cards** - Focus on essential + high-yield, not exhaustive coverage
- **Including low-yield facts** that don't appear in LOs or clinical practice
- Adding information not in the source
- **Paraphrasing medical terms** instead of using exact source wording
- Using pronouns without clear referents
- Making answers too long (should be 3-15 words, max 30)
- **Skipping essential or high-yield facts** from source
- **Repetitive question phrasing** - vary structures (What/Which/How/Define)
- Not escaping special characters in data properly

## Example Usage

**Single:** Command with one file

**Batch:** Command with semicolon-separated files → Creates separate output files

