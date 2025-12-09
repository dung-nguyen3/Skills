---
description: Create comprehensive Anki flashcard deck (.apkg) from source material
argument-hint: Single file, batch files separated by semicolon, or directory path. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create an Anki flashcard deck from source file: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single / Batch Separate / Batch Merge)

**Parse arguments to detect mode:**

**Step 0.1: Check if input is a directory**
- If $ARGUMENTS is a directory path:
  - List all .txt/.pdf files in directory (non-recursive)
  - Count files found
  - Store file list for later use
  - **Important**: Continue to Step 0.2 with file count information

**Step 0.2: Check for --merge flag**
- If $ARGUMENTS starts with `--merge`: **BATCH MERGE MODE**
- Strip `--merge` from arguments to get file list

**Step 0.3: Check for semicolons**
- If $ARGUMENTS contains semicolons (`;`): **BATCH SEPARATE MODE**
- Split by semicolon to get file list

**Step 0.4: Check directory file count (from Step 0.1)**
- If directory with 0 files: **ERROR** - "No .txt/.pdf files found in directory"
- If directory with 1 file: **SINGLE MODE** - Process that one file
- If directory with 2+ files: **BATCH SEPARATE MODE** - Process all files independently

**Step 0.5: Otherwise SINGLE MODE**
- Single file path with no special flags

**State which mode detected:**
```
MODE DETECTED: [SINGLE / BATCH SEPARATE / BATCH MERGE]
File count: [#]
Files: [list]
Source: [directory (auto-detected batch) / semicolon-separated / single file]
```

**Mode Descriptions:**
- **SINGLE**: 1 file → 1 Anki deck (inline processing)
- **BATCH SEPARATE**: N files → N Anki decks (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Anki deck (orchestrator agent, intelligent merge)

---


### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Source-only policy: I will ONLY use information from source file
☐ Source-driven: I will create cards for ALL content from source
☐ Comprehensive coverage: No content will be excluded from source material
☐ LO verification: All learning objectives will be covered (but cards not limited to LOs)
☐ Exact wording: I will use exact words from source - NO paraphrasing
☐ No external facts will be added
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
☐ Homogeneity check: All files use same source-only policy
☐ Source-driven: Each file will have comprehensive content extraction
☐ Exact wording: Use exact words from source - NO paraphrasing
☐ Output: N files → N Anki decks
☐ Agent: batch-separate-processor (launched N times)
☐ Architectural isolation: Each file processed in separate agent context
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-separate-processor agent:**

```
I'll use the batch-separate-processor agent to process your files with architectural isolation.

Launching agent [X] times:
- File 1: batch-separate-processor → [Output1.apkg]
- File 2: batch-separate-processor → [Output2.apkg]
...
- File N: batch-separate-processor → [OutputN.apkg]

Each agent invocation is architecturally isolated (zero cross-contamination).
```

**STOP HERE - Do NOT continue with Steps 2-9. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ File validation: All files exist and are readable
☐ Files are related/compatible for merging
☐ Source-driven: Comprehensive content extraction from all files
☐ Exact wording: Use exact words from sources - NO paraphrasing
☐ Output: N files → 1 merged Anki deck
☐ Agent: batch-merge-orchestrator (launched once)
☐ Merge features: Content matrix, overlap resolution, source traceability
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent:**

```
I'll use the batch-merge-orchestrator agent to intelligently merge your files.

Agent will:
1. Read all N files completely
2. Create content matrix (which LOs/concepts in which files)
3. Identify overlaps and gaps
4. Resolve conflicts with source traceability
5. Merge into ONE comprehensive Anki deck
6. Create merge report with traceability map

Output:
- 1 merged Anki deck: [filename.apkg]
- 1 merge report: [filename_merge_report.md]
```

**STOP HERE - Do NOT continue with Steps 2-9. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-9)
- Do NOT mix - if agent is launched, STOP and let agent complete the work

### Step 2: Load Resources

Read these files in order:
1. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py`
   - Complete implementation using genanki library
   - Shows model, deck, and note creation

2. **Source File**: Read the ENTIRE source file specified

### Step 3: Extract Learning Objectives (For Coverage Verification Only)

**IMPORTANT: LOs will be used to verify coverage in Step 8, NOT to filter content.**

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

### Step 4: Analyze Source File (Comprehensive Extraction)

**COMPREHENSIVE SOURCE ANALYSIS:**

Extract ALL content from source material including:
- Key concepts, definitions, and terminology
- Mechanisms and processes
- Characteristics and features
- Effects, outcomes, and consequences
- Diagnostic/identifying criteria
- Facts and details from source
- Comparisons and contrasts presented

**Completeness Check:**
- Re-read source after analysis to verify nothing missed
- Include supporting context and explanatory details
- Do NOT exclude content - extract everything from the source
- Use EXACT wording from source - NO paraphrasing

**Content Organization:**
Organize extracted content by topic/concept for card creation in Step 5.

```
TOPIC 1: [Concept name]
  - Fact 1 (exact wording from source)
  - Fact 2 (exact wording from source)
  - Fact 3 (exact wording from source)

TOPIC 2: [Concept name]
  - Fact 1 (exact wording from source)
  - Fact 2 (exact wording from source)
...
```

### Step 5: Create Flashcards (Comprehensive)

**Create flashcards for ALL content from Step 4**

**Card Creation Principles:**
- Atomic cards as default (one fact per card - proven superior)
- Focused comparison cards when testing differentiation
- Comprehensive coverage of source material
- No artificial restrictions on card creation
- Use EXACT wording from source - NO paraphrasing

**COMPARISON CARDS - Use When Testing Differentiation:**

Create focused comparison cards when source content involves:
- Explicit comparisons ("X vs Y", "compared to", "differentiate")
- Contrasting related items with different characteristics
- Distinguishing between similar concepts

**Comparison Card Format** (focused per category):
```
Q: "Item A vs Item B: [Category]"
A: "Item A:
- Characteristic 1
- Characteristic 2
- Characteristic 3

Item B:
- Characteristic 1
- Characteristic 2
- Characteristic 3"
```

**Default to atomic cards** - Only use comparison format when differentiation/contrast is being tested.

**Card Direction Logic (CRITICAL):**

Determine card direction based on content type:

**REVERSE CARDS (Definition/Features → Term):**
Use when asking "What is the NAME of..." or "Which TERM has..."

Examples:
- Diagnostic tools: Features → Tool name
- Drug names: MOA/indications → Drug name
- Anatomical structures: Location/function → Structure name
- Disease names: Presentation/features → Disease name
- Receptor/enzyme names: Function/location → Name

Question templates:
- "What diagnostic tool [has/uses/measures] [characteristics]?"
- "Which drug [mechanism/indication]?"
- "What structure [location/function]?"
- "Which disease presents with [symptoms]?"

**FORWARD CARDS (Term/Context → Mechanism/Process):**
Use when asking "HOW/WHY/WHEN/WHERE does..." or "What happens when..."

Examples:
- Mechanisms: "How does [drug] affect [target]?" → Mechanism
- Treatments: "How is [condition] treated?" → Treatment protocol
- Side effects: "What are adverse effects of [drug]?" → Side effects
- Pathophysiology: "What causes [condition]?" → Pathophysiology
- Clinical presentation: "What are symptoms of [condition]?" → Symptoms
- **Procedures/Protocols: ALL STEPS IN ONE CARD** → Complete step-by-step protocol

Question templates:
- "How does [term] affect [target]?"
- "What are the [effects/symptoms/causes] of [term]?"
- "When is [drug/test] used?"
- "Where does [structure/drug] act?"
- "What is the protocol/procedure for [test/intervention]?"

**IMPORTANT EXCEPTION - Procedure/Protocol Cards:**
When the content is a multi-step procedure or protocol, keep ALL steps in ONE card.
Do NOT split into separate cards per step - the sequence is the concept being tested.

Example:
✓ CORRECT:
Q: "What is the protocol for Ankle-Brachial Index?"
A: "1. Patient supine x10 min
    2. Doppler measure brachial pressures (both arms, use highest)
    3. Doppler measure ankle pressures (both legs, use highest per foot)
    4. Calculate ABI"

✗ WRONG (do not split):
- Q: "What is step 1 of ABI?" A: "Patient supine"
- Q: "What is step 2 of ABI?" A: "Measure brachial..."
[Splitting loses procedural flow and context]

**Answer Formatting - Line Breaks for Multiple Items:**
When the answer contains multiple items (steps, symptoms, treatments, side effects, etc.), use line breaks to improve scannability.

✓ CORRECT (line breaks for multiple items):
Q: "What are the symptoms of heart failure?"
A: "Dyspnea
Orthopnea
Paroxysmal nocturnal dyspnea
Peripheral edema
Fatigue"

Q: "How is acute hyperkalemia treated?"
A: "1. IV Calcium (membrane stabilization)
2. Insulin + D50W (shift K+ intracellularly)
3. Albuterol nebulizer (shift K+ intracellularly)
4. Sodium bicarbonate (if acidotic)
5. Dialysis (if refractory)"

✗ WRONG (comma-separated, hard to scan):
Q: "What are the symptoms of heart failure?"
A: "Dyspnea, orthopnea, paroxysmal nocturnal dyspnea, peripheral edema, fatigue"

Q: "How is acute hyperkalemia treated?"
A: "IV Calcium, insulin + D50W, albuterol, sodium bicarbonate, dialysis if refractory"

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

3. **Coverage (Comprehensive)**
   - Create cards for ALL content from Step 4
   - **ONE fact per card** (Minimum Information Principle - atomic cards)
   - **Word limits:** Questions <20 words, Answers <30 words (ideally 3-15)
   - **No filler words** - be concise and precise
   - **Vary question structures:** Avoid repetitive phrasing (What/Which/How/Define/Describe)
   - No duplicate concepts
   - Comprehensive coverage of source material

4. **Source-Only Policy**
   - Use ONLY information from the source file
   - **Preserve exact terminology from source** - Copy word-for-word, do NOT paraphrase
   - Do NOT add external medical knowledge

**Question Type Examples:**

REVERSE CARDS (Features → Term):
- "What diagnostic tool measures duration, phase, frequency of heart sounds?" → "Phonocardiography"
- "Which drug inhibits transpeptidase and prevents peptidoglycan cross-linking?" → "Penicillin"
- "What structure connects the right atrium to right ventricle?" → "Tricuspid valve"

FORWARD CARDS (Term → Mechanism/Process):
- "How does atropine affect presynaptic M2 receptors?" → "Blocked → ↑NE release → ↑β1 stimulation"
- "What are the adverse effects of penicillin?" → "Hypersensitivity reactions, GI upset, rash"
- "How is hyperkalemia treated emergently?" → "IV Calcium, insulin + D50W, albuterol"

### Step 6: Use TodoWrite

Track your progress:
- Create todo for analyzing source
- Create todo for each major topic section
- Create todo for APKG generation
- Mark completed as you finish

### Step 7: Generate APKG File

**Use genanki library to create .apkg:**

@study-guides/templates-and-examples/Python_Examples/Anki_APKG_Example.py

**Deck Naming Convention:**

Determine the deck name based on the file path:
1. Extract course name from file path
2. Apply course name mapping if needed
3. Use format: `[Course Name]::[Topic]`

**Course Name Mapping:**
- Path contains "Clinical Medicine 3" → Use "Clinical Medicine II"
- Path contains "Clinical Medicine I" → Use "Clinical Medicine I"
- Path contains "Clinical Medicine II" → Use "Clinical Medicine II"
- Path contains "Pharmacology" → Use "Pharmacology"
- Path contains "Microbiology" → Use "Microbiology"
- Other courses: Use exact name from path

**Example:**
- File path: `.../Clinical Medicine 3/Exam 1/...`
- Topic: "Diagnostics in Cardiology"
- Deck name: `'Clinical Medicine II::Diagnostics in Cardiology'`

### Step 8: Post-Creation Verification

**Verify the completed deck:**

1. **LO Coverage Verification**
   - Verify all LOs are adequately covered (multiple cards per LO as needed for different components)
   - This ensures all objectives are covered
   - BUT cards are not limited to only LO-mapped content

2. **Source Completeness Check**
   - Compare cards against source material
   - Verify no content was excluded
   - Check: key concepts, mechanisms, characteristics, effects, details from source
   - Comprehensive coverage of ALL source content

3. **Source Accuracy & Exact Wording**
   - All facts come from source file only
   - **CRITICAL: Terminology matches source EXACTLY - word-for-word**
   - No paraphrasing of medical terms, drug names, or technical language
   - No external information added

4. **Question Quality**
   - Questions are clear and unambiguous
   - **Atomic cards:** Each card tests ONE fact only (no combined concepts)
   - **Word count:** Questions <20 words
   - **Variety:** Question structures vary (not repetitive)
   - **Precision:** Questions are specific and self-contained

5. **Answer Quality**
   - **Concise:** Answers <30 words (ideally 3-15 words)
   - **Atomic:** Single concept per answer
   - **Exact terminology:** Source wording preserved exactly - NO paraphrasing

6. **Volume Check**
   - Comprehensive coverage of source material
   - Typical range: 50-100 cards for standard lecture (may vary based on source density)
   - If unusually high/low: Verify completeness and accuracy

7. **Card Direction Check**
   - Reverse cards used for terms/tools/structures/diseases?
   - Forward cards used for mechanisms/treatments/processes?
   - No repetitive "What is [term]?" → "[definition]" patterns
   - Variety in question stems for both card types

8. **Comparison Card Check**
   - Comparison cards used appropriately (only when testing differentiation)?
   - Focused per category (not mega-cards with all aspects)?
   - Atomic cards used as default?

9. **Answer Formatting Check**
   - Multi-item answers use line breaks (not comma-separated)?
   - Procedure steps displayed with line breaks for readability?
   - Symptoms/treatments/side effects listed with line breaks?
   - Answers are scannable and easy to review quickly?

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
- **Excluding content from source** - Create comprehensive coverage
- Adding information not in the source
- **CRITICAL: Paraphrasing medical terms** instead of using exact source wording word-for-word
- Using pronouns without clear referents
- Making answers too long (should be 3-15 words, max 30)
- **Skipping content from source material**
- **Repetitive question phrasing** - vary structures (What/Which/How/Define)
- Not escaping special characters in data properly
- Using comparison cards when atomic cards are more appropriate

## Example Usage

**Single:** Command with one file

**Batch:** Command with semicolon-separated files → Creates separate output files

