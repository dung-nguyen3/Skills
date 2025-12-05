---
description: Create engaging drug autobiography stories with personified characters
argument-hint: Single file, batch files separated by semicolon, or directory path (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir")
---

Create drug autobiography stories from source file: $ARGUMENTS

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
☐ Template: Autobiography_Drug_Stories_REVISED.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Exception: Creative analogies/metaphors WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for storytelling devices and memory techniques
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

#### For BATCH MODE:

```
BATCH INITIAL VALIDATION:
☐ Source files: [list all files from $ARGUMENTS]
☐ File validation: All files exist and are readable
☐ Homogeneity check: All files are drug-related content
☐ Template: Autobiography_Drug_Stories_REVISED.txt (applies to ALL)
☐ Output: ONE biography document will be created per source file
☐ Save location: [Class]/[Exam]/Claude Study Tools/

BATCH PROCESSING RULES:
☐ Each file will get complete verification (not just once)
☐ Each file will be processed independently
☐ Context isolation: I will explicitly clear data between files
☐ Source-only policy applies per-file
☐ Creative analogies researched per-file via WebSearch
```

**IMPORTANT**: Full verification checklist will run for EACH file (Step 1 repeated in Batch Processing).

### Step 2: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/Autobiography_Drug_Stories_REVISED.txt`
   - Storytelling guidelines and character development
   - Narrative structure requirements
   - Creative metaphor examples

2. **Source File**: $ARGUMENTS
   - Extract all drug information
   - Note mechanisms, uses, side effects
   - Identify drug classes and relationships

### Step 3: Create Drug Biography Stories

Follow template instructions EXACTLY:

**Required Structure:**

**For Each Drug:**
1. **Introduction** - Drug introduces themselves (generic + brand name, main role)
2. **Mechanism of Action** - As a creative story with analogies
3. **Therapeutic Uses** - Described as "missions" or "adventures"
4. **Side Effects** - As "challenges," "secrets," or "weaknesses"
5. **Interactions** - As relationships with other characters
6. **Clinical Pearls** - As "wisdom" or "advice"

**Character Development Requirements:**
- Personify drugs with personality traits matching properties
- Use titles (Mr., Ms., Dr., Professor, Captain, etc.)
- Create family relationships for same-class drugs
- Match personalities to characteristics:
  - Selective drugs = "focused" or "precise"
  - Non-selective = "broad" or "indiscriminate"
  - Toxic = "dangerous" or "dark secrets"
  - Newer = "young" or "modern"
  - Older = "veterans" or "old-timers"

**WebSearch Requirements (MANDATORY):**
- Research creative analogies and metaphors for mechanisms
- Find character traits and storytelling devices
- Look for established medical education analogies
- Search for proven memory techniques

**Key Rules:**
- Use ONLY source file information (except creative analogies)
- Keep stories medically accurate
- Make mechanisms memorable through narrative
- Connect related drugs through character relationships
- Output format: Word document (.docx)

### Step 4: Use TodoWrite

Track your progress:
- Create todo for each drug biography
- Mark in_progress as you work
- Mark completed when done
- Keep user informed

### Step 5: Post-Creation Verification

**Automatically verify the completed document:**

1. **Source Accuracy**
   - All medical info from source only
   - Creative elements (analogies) marked if external
   - No invented medical facts

2. **Story Completeness**
   - Each drug has: intro, mechanism story, uses, side effects, interactions, pearls
   - All drugs from source file included
   - Family relationships established for drug classes

3. **Character Development**
   - Each drug personified with appropriate personality
   - Titles and relationships consistent
   - Personalities match pharmacological properties

4. **Narrative Quality**
   - Mechanisms explained through creative analogies
   - Stories are engaging and memorable
   - Medical accuracy maintained

5. **WebSearch Verification**
   - Confirm mnemonics/analogies were researched
   - No invented memory devices

**CRITICAL: State "Post-creation verification complete" when done.**

### Step 6: Summary

Provide:
- Number of drug biographies created
- Drug classes covered
- Character relationships established
- File location and name
- Any notes on creative analogies used

## Output Format

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Drug_Biographies.docx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[Topic]_Drug_Biographies.py`
- Create `py/` subfolder if doesn't exist

**Example filenames:**
```
Cardiovascular_Drug_Biographies.docx
HIV_Antiretroviral_Drug_Biographies.docx
Antibiotic_Drug_Biographies.docx
```


---

## Batch Processing

For batch operations (semicolon-separated files):
@.claude/skills/batch-coordinator/SKILL.md

---

## Example Usage

**Single:** Command with one file

**Batch:** Command with semicolon-separated files → Creates separate output files


## Best For

- **Pharmacology courses** - Make drug mechanisms memorable
- **Drug classes** - Show family relationships through characters
- **Complex mechanisms** - Explain through creative stories
- **Exam preparation** - Engaging review material
- **Visual/creative learners** - Story-based memory

## Important Notes

- **Medical accuracy first**: Stories must be medically accurate, not just entertaining
- **Use established analogies**: Research proven teaching analogies via WebSearch
- **Source-only policy**: All medical facts from source file only
- **Character consistency**: Keep personalities/relationships consistent throughout
- **Format**: Word document with sections for each drug

## Template Customization

To modify the drug biography template:
1. Edit: `study-guides/templates-and-examples/Autobiography_Drug_Stories_REVISED.txt`
2. Changes apply automatically to next `/autobiography-trick` use
3. Update this command file if workflow changes
