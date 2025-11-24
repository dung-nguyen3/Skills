---
description: Create comprehensive Anki flashcard deck (.apkg) from source material
argument-hint: Single file OR batch files separated by semicolon (e.g., "file1.txt" OR "file1.txt;file2.txt")
---

Create an Anki flashcard deck from source file: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single vs Batch)

**Parse arguments:** If $ARGUMENTS contains `;` → BATCH MODE (multiple files), otherwise SINGLE MODE.

**State mode:** MODE DETECTED: [SINGLE/BATCH], File count: [#], Files: [list]

---


### Step 1: Pre-Creation Verification

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Source-only policy: I will ONLY use information from source file
☐ No external facts will be added
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

### Step 2: Load Resources

Read these files in order:
1. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py`
   - Complete implementation using genanki library
   - Shows model, deck, and note creation

2. **Source File**: Read the ENTIRE source file specified

### Step 3: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL major topics and subtopics
- Note key facts, definitions, mechanisms
- Extract drug names, receptor names, medical terminology exactly
- Document relationships and comparisons
- Identify "must-know" facts

### Step 4: Create Flashcards

**CSV Format:**
- First line: `Question,Answer`
- One Q&A pair per line
- Save intermediate as: `[topic]_Flashcards.csv`

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

3. **Coverage**
   - Create as many cards as needed for comprehensive coverage
   - One clear question-answer pair per fact
   - No duplicate concepts
   - Cover all major topics from source

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

### Step 5: Use TodoWrite

Track your progress:
- Create todo for analyzing source
- Create todo for each major topic section
- Create todo for CSV generation
- Create todo for APKG conversion
- Mark completed as you finish

### Step 6: Generate APKG File

**Use genanki library to create .apkg:**

```python
import genanki
import csv

# Create model (use consistent IDs for updates)
model = genanki.Model(
    1607392319,  # Unique model ID
    'Study Guide Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[{
        'name': 'Card 1',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    }],
    css='''
    .card {
        font-family: arial;
        font-size: 20px;
        text-align: center;
        color: black;
        background-color: white;
    }
    '''
)

# Create deck
deck = genanki.Deck(
    2059400110,  # Unique deck ID
    'Topic Name')

# Add notes from CSV
with open('flashcards.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        note = genanki.Note(
            model=model,
            fields=[row[0], row[1]])
        deck.add_note(note)

# Export
genanki.Package(deck).write_to_file('output.apkg')
```

### Step 7: Post-Creation Verification

**Verify the completed deck:**

1. **Source Accuracy**
   - All facts come from source file only
   - Terminology matches source exactly
   - No external information added

2. **Question Quality**
   - Questions are clear and unambiguous
   - One concept per card
   - Variety of question types used

3. **Answer Quality**
   - Answers are concise (3-15 words typical)
   - Single concept per answer
   - Exact terminology preserved

4. **Completeness**
   - All major topics covered
   - No duplicate cards
   - Comprehensive coverage of source material

**CRITICAL: State "Post-creation verification complete" and report card count.**

### Step 8: Save Files

- CSV: `[Class]/[Exam]/Claude Study Tools/[Topic]_Flashcards.csv`
- APKG: `[Class]/[Exam]/Claude Study Tools/[Topic]_Flashcards.apkg`
- Create Claude Study Tools folder if doesn't exist
- Confirm files saved successfully


---

### Batch Processing (BATCH MODE ONLY)

If BATCH MODE, repeat previous steps for EACH file with progress tracking and batch summary at end.

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

