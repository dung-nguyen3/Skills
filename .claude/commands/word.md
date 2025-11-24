---
description: Create comprehensive Word study guide from source material following template
argument-hint: Single file OR batch files separated by semicolon. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "--merge f1.txt;f2.txt")
---

Create Word study guide from: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single / Batch Separate / Batch Merge)

**Parse arguments to detect mode:**

**Check for --merge flag:**
- If $ARGUMENTS starts with `--merge`: **BATCH MERGE MODE**
- Strip `--merge` from arguments to get file list

**Check for semicolons:**
- If $ARGUMENTS contains semicolons (`;`): **BATCH SEPARATE MODE**
- Split by semicolon to get file list

**Otherwise: SINGLE MODE**

**State which mode detected:**
```
MODE DETECTED: [SINGLE / BATCH SEPARATE / BATCH MERGE]
File count: [#]
Files: [list]
```

**Mode Descriptions:**
- **SINGLE**: 1 file → 1 Word guide (inline processing)
- **BATCH SEPARATE**: N files → N Word guides (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Word guide (orchestrator agent, intelligent merge)

---

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Instruction template: Word LO 11-5.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
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
☐ Homogeneity check: All files are learning objective lectures
☐ Template: Word LO 11-5.txt (per file)
☐ Output: N files → N Word guides
☐ Agent: batch-separate-processor (launched N times)
☐ Architectural isolation: Each file processed in separate agent context
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-separate-processor agent:**

```
I'll use the batch-separate-processor agent to process your files with architectural isolation.

Launching agent [X] times:
- File 1: batch-separate-processor → [Output1.docx]
- File 2: batch-separate-processor → [Output2.docx]
...
- File N: batch-separate-processor → [OutputN.docx]

Each agent invocation is architecturally isolated (zero cross-contamination).
```

**STOP HERE - Do NOT continue with Steps 2-7. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ File validation: All files exist and are readable
☐ Files are related/compatible for merging
☐ Template: Word LO 11-5.txt (unified)
☐ Output: N files → 1 merged Word guide
☐ Agent: batch-merge-orchestrator (launched once)
☐ Merge features: Content matrix, overlap resolution, source traceability
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent:**

```
I'll use the batch-merge-orchestrator agent to intelligently merge your files.

Agent will:
1. Read all N files completely
2. Create content matrix (which topics/LOs in which files)
3. Identify overlaps and gaps
4. Resolve conflicts with source traceability
5. Merge into ONE comprehensive Word guide
6. Create merge report with traceability map

Output:
- 1 merged Word guide: [filename.docx]
- 1 merge report: [filename_merge_report.md]
```

**STOP HERE - Do NOT continue with Steps 2-7. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-7)
- Do NOT mix - if agent is launched, STOP and let agent complete the work

### Step 2: Load Resources

Read these files in order:
1. **Template**: `study-guides/templates-and-examples/Word_LO_11-5_REVISED.txt`
   - Main instructions and requirements (~450 lines)
   - Includes correct table formatting (black text on pastel backgrounds)

2. **Example Code**: `study-guides/templates-and-examples/Python_Examples/Word_LO_Example.py`
   - Complete 4-section implementation with all helper functions
   - Shows Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary

### Step 3: Read Source File

- Read the complete source file: $ARGUMENTS
- Identify all learning objectives
- Note all topics, conditions, drugs mentioned
- Extract key information for each learning objective

### Step 4: Create Study Guide

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

**WebSearch Requirements (MANDATORY):**
- Research mnemonics for each learning objective
- Find analogies for drug mechanisms/complex concepts
- Look for "If X think Y" clinical associations
- Use PROVEN mnemonics only - never invent

### Step 5: Use TodoWrite

Track your progress:
- Create todo for each learning objective
- Mark in_progress as you work
- Mark completed when done
- Keep user informed

### Step 6: Post-Creation Verification

**Automatically verify the completed document:**

1. **Source Accuracy**
   - All info from source only (except mnemonics)
   - External additions marked with *
   - No page references

2. **Template Compliance**
   - All 4 sections present
   - Correct colors (soft pastels)
   - All required elements included

3. **Completeness**
   - All LOs answered (all parts)
   - All comparisons created
   - Master chart complete

4. **Quality**
   - No incorrect groupings
   - No spelling errors
   - Proper formatting

**CRITICAL: State "Post-creation verification complete" and report any issues. Fix immediately.**

### Step 7: Save File

- Save to: `[Class]/[Exam]/Claude Study Tools/[Topic]_Study_Guide.docx`
- Create Claude Study Tools folder if doesn't exist
- Confirm file saved successfully

---

### Step 8: Batch Processing (BATCH MODE ONLY)

**If BATCH MODE, repeat Steps 1-7 for EACH file:**

For each source file in the batch:
1. **Announce file**: "Processing file X of Y: [filename]"

2. **CRITICAL - Context Isolation Check**:
   ```
   CONTEXT ISOLATION VERIFICATION:
   ☐ I will FORGET all content from previous files
   ☐ I will ONLY extract information from THIS source file: [filename]
   ☐ I will verify content is ONLY from THIS file (not previous files)
   ☐ This Word doc will contain ZERO content from previous files
   ```

3. **Per-File Verification** (Step 1) - Run complete verification checklist for THIS file

4. **Load resources** (Step 2) - templates already loaded, reuse

5. **Read source file** (Step 3) - read THIS file completely, extract THIS file's content only

6. **MANDATORY - State content summary**: "Content found in [filename]: [brief summary]"
   - This proves you're only using THIS file's content
   - If you see content from previous files, STOP and re-read source

7. **Create Word doc** (Step 4-5) - for THIS file only, using ONLY content from step 6

8. **Post-creation verification** (Step 6) - verify THIS file contains ONLY THIS file's content

9. **Save file** (Step 7) - with unique filename based on source

10. **MANDATORY - Isolation Confirmation**: "File [X] complete. Cleared all data. Ready for next file."

**Critical for Batch:**
- Each file gets complete verification (not once at start)
- Explicitly state content summary from each file before creating Word doc
- Verify no content from previous files contaminated output
- Clear all data between files
- Each file gets its own Word output

**Batch Summary**: After all files, provide summary of files created, statistics, and any issues.

## Example Usage

### Single File:
```
/word "Pharmacology/Exam 3/Extract/Lecture 42.txt"
```
Creates: `Lecture_42_LO_Guide.docx`

### Batch Separate (N files → N outputs):
```
/word "Lecture42.txt;Lecture43.txt;Lecture44.txt"
```
Creates 3 separate Word files:
- `Lecture_42_LO_Guide.docx` (only Lecture 42 content)
- `Lecture_43_LO_Guide.docx` (only Lecture 43 content)
- `Lecture_44_LO_Guide.docx` (only Lecture 44 content)

Uses batch-separate-processor agent with architectural isolation.

### Batch Merge (N files → 1 merged output):
```
/word --merge "Cardio-Lec1.txt;Cardio-Lec2.txt;Cardio-Lec3.txt"
```
Creates 1 merged Word file:
- `Cardiovascular_Comprehensive_LO_Guide.docx` (all 3 lectures merged)
- `Cardiovascular_Comprehensive_LO_Guide_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge and overlap resolution.
