---
description: Create engaging drug autobiography stories with personified characters
argument-hint: Single file OR batch files separated by semicolon (e.g., "file1.txt" OR "file1.txt;file2.txt")
---

Create drug autobiography stories from source file: $ARGUMENTS

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

**File naming:**
```
[Topic]_Drug_Biographies.docx
```

**Example:**
```
Cardiovascular_Drug_Biographies.docx
HIV_Antiretroviral_Drug_Biographies.docx
Antibiotic_Drug_Biographies.docx
```


---

### Batch Processing (BATCH MODE ONLY)

**If BATCH MODE, process each file independently:**

For each source file in the batch:
1. **Announce file**: "Processing file X of Y: [filename]"

2. **CRITICAL - Context Isolation Check**:
   ```
   CONTEXT ISOLATION VERIFICATION:
   ☐ I will FORGET all drugs/characters from previous files
   ☐ I will ONLY extract information from THIS source file: [filename]
   ☐ I will verify drug list is ONLY from THIS file (not previous files)
   ☐ This biography will contain ZERO drugs from previous files
   ```

3. **Per-File Verification** - Run complete verification checklist for THIS file

4. **Read source file** - Read THIS file completely, extract THIS file's drugs only

5. **MANDATORY - State drug list**: "Drugs in [filename]: [list all drugs]"
   - This proves you're only using THIS file's drugs
   - If you see drugs from previous files, STOP and re-read source

6. **Create drug biographies** - For THIS file only, using ONLY drugs from step 5

7. **Post-creation verification** - Verify THIS document contains ONLY THIS file's drugs

8. **MANDATORY - Isolation Confirmation**: "File [X] complete. Cleared all data. Ready for next file."

**Critical for Batch:**
- Each file gets complete verification (not once at start)
- Explicitly state drug list from each file before creating biographies
- Verify no drugs from previous files contaminated output
- Clear all data between files
- Each file gets its own Word output

**Batch Summary**: After all files, provide summary of files created, drug counts, and any issues.

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
2. Changes apply automatically to next `/biography` use
3. Update this command file if workflow changes
