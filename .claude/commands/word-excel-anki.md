---
description: Create multi-format study bundle (Word LO + Excel Comparison + Anki) from source
argument-hint: Single file, batch files separated by semicolon, or directory path. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create a multi-format study bundle from source file: $ARGUMENTS

This command generates 3 complementary formats in ONE efficient pass:
1. Word LO Study Guide (.docx)
2. Excel Comparison Chart (.xlsx)
3. Anki Flashcard Deck (.apkg)

**Token Efficiency:** Reads source ONCE → generates all 3 formats (~35-40k tokens saved vs separate commands)

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
- **SINGLE**: 1 file → 1 multi-format bundle (inline processing)
- **BATCH SEPARATE**: N files → N multi-format bundles (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged multi-format bundle (orchestrator agent, intelligent merge)

---

### Step 1: Pre-Creation Verification

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file(s): $ARGUMENTS
☐ Templates: Word LO 11-5, Excel Comparison, Anki
☐ Source-only policy: I will ONLY use information from source file(s)
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Formats: Word LO + Excel Comparison + Anki (3 formats per file)
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

---

### Step 2: Launch Multi-Format Processor Agent

**Use the Task tool to invoke multi-format-processor agent:**

```python
Task(
    subagent_type="multi-format-processor",
    prompt=f"""
Process source file to generate 3 study guide formats:

Source file: {source_file_path}
Formats: ["word", "excel-comparison", "anki"]
Output directory: {output_directory}

Instructions:
1. Read source file ONCE completely
2. Extract all information (LOs, drugs/conditions, comparisons, pearls)
3. Generate Word LO study guide following Word_LO_11-5_REVISED.txt
4. Generate Excel comparison chart following Excel_Comparison_Chart_REVISED.txt
5. Generate Anki flashcards following anki.md instructions
6. Use EXACT terminology from source in all formats
7. WebSearch for mnemonics ONCE, use in all formats
8. Save all 3 outputs to output directory

Token efficiency: Read source once, generate all formats sequentially.
    """
)
```

**For BATCH mode:** Launch agent once per file (each in isolated context)

**For DIRECTORY mode:**
1. Scan directory for `.txt` files
2. Read `.processed_files.txt` to skip already-processed
3. Launch agent for each NEW file
4. Update `.processed_files.txt`

---

### Step 3: Agent Processing

The multi-format-processor agent will:

1. **Read source ONCE** - Extract comprehensive data structure
2. **Load all 3 templates** - Word, Excel, Anki
3. **Generate Word LO Study Guide:**
   - 4 sections (LOs, Key Comparisons, Master Chart, High-Yield)
   - Soft pastel colors, Calibri 12pt
   - Comparison Item Inventory Protocol mandatory
   - Output: `[Topic]_Study_Guide.docx`

4. **Generate Excel Comparison Chart:**
   - Side-by-side comparison tables
   - Font: Calibri size 10 (data), size 12 (headers)
   - Colors: ROW_COLORS palette
   - White borders (#FFFFFF)
   - Output: `[Topic]_Comparison_Chart.xlsx`

5. **Generate Anki Flashcards:**
   - **CRITICAL: EXACT wording from source** (no paraphrasing)
   - 3-15 words per answer
   - One concept per card
   - LO-filtering mandatory
   - Output: `[Topic]_Flashcards.apkg`

6. **WebSearch for mnemonics ONCE** - Reuse across all 3 formats

7. **Verify exact terminology consistency** across all outputs

---

### Step 4: Post-Creation Actions

**After agent completes:**

1. **Verify outputs created:**
   ```
   ✓ [Topic]_Study_Guide.docx created
   ✓ [Topic]_Comparison_Chart.xlsx created
   ✓ [Topic]_Flashcards.apkg created
   ```

2. **Report token efficiency:**
   ```
   Token Efficiency Report:
   - Source read: 1x (not 3x)
   - Estimated savings: ~[calculate]k tokens
   - Formats: 3 outputs from single source read
   ```

3. **Optional: Auto-consolidate master charts**
   If Excel comparison includes master chart data:
   ```bash
   python study-guides/templates-and-examples/Python_Examples/Auto_Consolidate_Master_Charts.py \
     "[Topic]_Comparison_Chart.xlsx" \
     "Pharmacology_Master_Reference.xlsx"
   ```

4. **Optional: Update QUICK_ACCESS index**
   ```bash
   python study-guides/templates-and-examples/Python_Examples/Generate_Quick_Access_Index.py \
     "[Class]/[Exam]/Claude Study Tools/"
   ```

5. **Update batch tracker** (for weekly reminder):
   ```bash
   bash .claude/hooks/helpers/update-batch-date.sh
   ```

---

### Step 5: Completion Report

```
✅ MULTI-FORMAT BUNDLE CREATED

Source: [filename]
Formats generated: 3

Outputs:
1. [filename]_Study_Guide.docx ([N] pages, [M] LOs)
2. [filename]_Comparison_Chart.xlsx ([N] comparison tables)
3. [filename]_Flashcards.apkg ([N] cards)

Location: [Class]/[Exam]/Claude Study Tools/

Token Efficiency: Saved ~[N]k tokens vs separate commands
Exact Terminology: ✓ Consistent across all formats
```

---

## Batch Processing

**For batch separate (N files → N×3 outputs):**
- Launch multi-format-processor agent N times
- Each invocation: 1 source → 3 outputs
- Architectural isolation per file

**For batch merge (N files → 3 merged outputs):**
- Use batch-merge-orchestrator instead
- Merge content from N files → 1 Word + 1 Excel + 1 Anki

@.claude/agents/multi-format-processor.md
@.claude/agents/batch-merge-orchestrator.md

---

## Format Defaults

**Course-specific bundles** (from `.claude/format-defaults.json`):
- Pharmacology: Word + Excel Comparison + Anki (default)
- Pathophysiology: Word + Excel Comparison (no Anki)
- Clinical Medicine: Word + HTML-LO (quick reference)

**Override with --formats flag:**
```bash
/word-excel-anki --formats word,anki "source.txt"
```

---

## Error Handling

**If source file not found:**
```
❌ ERROR: Source file not found
File: [filename]
Action: Verify file path and try again
```

**If agent fails:**
```
❌ ERROR: Multi-format processing failed
Reason: [error message]
Action: Check source file format and try again
```

**If partial success:**
```
⚠️  PARTIAL SUCCESS
Created: [list successful formats]
Failed: [list failed formats]
Action: Review error messages and retry failed formats
```

---

## Quality Assurance

Before completing, agent verifies:
- [ ] Source read completely (ONCE)
- [ ] All 3 formats created successfully
- [ ] **EXACT terminology from source** in all formats (no paraphrasing)
- [ ] Learning objectives verbatim in Word
- [ ] Comparison Item Inventory Protocol followed
- [ ] WebSearch mnemonics shared across formats
- [ ] All outputs source-only compliant

---

## Example Usage

**Single:**
```
/word-excel-anki "Pharmacology/Exam 3/Extract/Pharm_11 Beta Blockers_text.txt"
```
Creates:
- `11 Beta Blockers.docx` (Word)
- `11 Beta Blockers.xlsx` (Excel)
- `11 Beta Blockers.apkg` (Anki)

**Batch:**
```
/word-excel-anki "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt;Pharm_13 Diuretics_text.txt"
```
Creates 9 files (3 formats × 3 sources):
- `11 Beta Blockers.docx`, `11 Beta Blockers.xlsx`, `11 Beta Blockers.apkg`
- `12 ACE Inhibitors.docx`, `12 ACE Inhibitors.xlsx`, `12 ACE Inhibitors.apkg`
- `13 Diuretics.docx`, `13 Diuretics.xlsx`, `13 Diuretics.apkg`

**Directory:**
```
/word-excel-anki "Pharmacology/Exam 3/Extract/"
```
Processes all .txt files in directory

---

**End of Command**
