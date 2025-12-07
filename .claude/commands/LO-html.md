---
description: Create HTML learning objectives guide (any medical topic)
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

# Create Learning Objectives Guide

Create an **interactive HTML study guide** for ANY medical topic with learning objectives.

## Usage

**Single Mode:**
```
/LO-html "source_file.txt"
```

**Directory Mode:**
```
/LO-html "/path/to/directory"
```

**Batch Separate Mode (N files → N outputs):**
```
/LO-html "file1.txt;file2.txt;file3.txt"
```

**Batch Merge Mode (N files → 1 merged output):**
```
/LO-html --merge "file1.txt;file2.txt;file3.txt"
```

**Batch Merge with Directories:**
```
/LO-html --merge "/path/to/dir1;/path/to/dir2"
```

## Step 0: Detect Mode (Single / Batch Separate / Batch Merge)

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
- **SINGLE**: 1 file → 1 HTML guide (inline processing)
- **BATCH SEPARATE**: N files → N HTML guides (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged HTML guide (orchestrator agent, intelligent merge)

**Agent Invocation:**
- **For BATCH SEPARATE:** Launch batch-separate-processor agent N times (architectural isolation)
- **For BATCH MERGE:** Launch batch-merge-orchestrator agent once (intelligent merge with overlap resolution)
- **For SINGLE:** Process inline (follow steps below)

---

## What This Creates

Comprehensive 4-tab HTML study guide:
- **Tab 1: Learning Objectives** - Q&A format answering each LO in detail
- **Tab 2: Key Comparisons** - Focused 2-3 way comparison tables
- **Tab 3: Master Comparison Tables** - Complete differential diagnosis tables
- **Tab 4: Summary** - High-yield pearls, mnemonics, "If X Think Y" associations

---

## Example Usage

### Single File:
```
/LO-html "Pharmacology/Exam 3/Extract/Pharm_11 Beta Blockers_text.txt"
```
Creates: `11 Beta Blockers.html`

### Batch Separate (N files → N outputs):
```
/LO-html "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt;Pharm_13 Diuretics_text.txt"
```
Creates 3 separate HTML files:
- `11 Beta Blockers.html`
- `12 ACE Inhibitors.html`
- `13 Diuretics.html`

(architectural isolation via agent)

### Batch Merge (N files → 1 merged output):
```
/LO-html --merge "Pharm_11 Beta Blockers_text.txt;Pharm_12 ACE Inhibitors_text.txt"
```
Creates 1 comprehensive HTML file:
- `Lecture 11-12.html`
- `Lecture 11-12_merge_report.md`


## Template Location

The command uses the template at:
```
study-guides/templates-and-examples/HTML_LO_REVISED.txt
```

Before starting, read the template to understand:
- 4-tab structure (Learning Objectives, Key Comparisons, Master Tables, Summary)
- Emergency color-coding system (red/orange/white)
- Clinical decision support formatting
- HTML-specific requirements

## Best For

**Works for ALL medical topics:**
- Cardiovascular disease
- Hematology conditions
- Immunology
- Rheumatology (RA, SLE, etc.)
- Respiratory physiology
- Gastrointestinal pathophysiology
- Endocrine disorders
- Infectious diseases (non-drug focus)
- Procedures and techniques
- ANY lecture with learning objectives

## Features

- **Content-agnostic**: Works for pathophysiology, procedures, physiology, clinical medicine
- **Source-only**: Uses only information from provided source files
- **Researched mnemonics**: WebSearch for established medical mnemonics
- **Comparison tables**: Helps differentiate similar conditions
- **Mobile-friendly**: Responsive design for studying on any device
- **Offline-ready**: Self-contained HTML file

## Pre-Creation Checklist

Before creating, Claude will verify:
- ☐ Source file identified
- ☐ Template loaded from correct location
- ☐ Source-only policy confirmed
- ☐ Learning objectives: Extract LO statements EXACTLY as written (NO paraphrasing)
- ☐ WebSearch for mnemonics/analogies (mandatory)
- ☐ Save study guide to: `[Class]/[Exam]/Claude Study Tools/`
- ☐ Save Python file to: `[Class]/[Exam]/Claude Study Tools/py/`

<verbatim-requirement>
CRITICAL: Learning objective STATEMENTS must be copied EXACTLY as they appear in the source.
- Copy word-for-word, character-for-character
- Do NOT rephrase, summarize, or "improve" wording
- Preserve original numbering and sequence
- If an LO is long, still copy it completely
Note: Answers/explanations CAN be paraphrased from source content.
</verbatim-requirement>

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - HTML Learning Objectives (4 tabs):

STRUCTURE:
- Tab 1 "Learning Objectives": Q&A format answering each LO in detail
  - LO statement verbatim from source
  - Comprehensive answer with tables, boxes, pearls
- Tab 2 "Key Comparisons": Focused 2-3 way comparison tables
  - One comparison table per category
  - Columns = items compared, Rows = features
- Tab 3 "Master Comparison Tables": Complete differential diagnosis tables
  - ALL conditions/topics in comprehensive tables
  - Color-coded by category
- Tab 4 "Summary": High-yield pearls, mnemonics, "If X Think Y" associations
  - Mnemonics (researched via WebSearch)
  - Clinical pearls boxes
  - Quick reference associations

FORMATTING (MANDATORY):
- Tab navigation: .nav-tabs with aria-selected states
- Tab content: .tab-content with proper show/hide
- Tables: table-bordered, header row with background color
- Color scheme:
  - Emergency/Critical: Red (#FFEBEE border, #FFCDD2 background)
  - Warning: Orange (#FFF3E0 border, #FFE0B2 background)
  - Normal/Info: Blue (#E3F2FD border, #BBDEFB background)
  - Clinical Pearls: Teal (#E0F2F1 background)
  - Memory Tricks: Orange (#FFF3E0 background)
  - High-Yield: Purple (#F3E5F5 background)
- Responsive design: Works on mobile and desktop
- Self-contained: No external dependencies (all CSS inline)
</template-compliance>

## Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ EXACTLY 4 tabs present: Learning Objectives, Key Comparisons, Master Comparison Tables, Summary
☐ Tab names correct
☐ Tab 1: Each LO has Q&A format with verbatim statement + comprehensive answer
☐ Tab 1: Answers include tables, boxes, and pearls where appropriate
☐ Tab 2: Focused 2-3 way comparison tables (one category per table)
☐ Tab 2: Columns = items compared, Rows = features
☐ Tab 3: ALL conditions/topics in comprehensive tables
☐ Tab 3: Color-coded by category
☐ Tab 4: Mnemonics, Clinical Pearls, "If X Think Y" sections

**Formatting Compliance:**
☐ Tab navigation uses .nav-tabs with proper aria states
☐ Tab content uses .tab-content with show/hide
☐ Tables: table-bordered with header row backgrounds
☐ Color scheme correct:
  - Emergency/Critical: Red (#FFEBEE border, #FFCDD2 background)
  - Warning: Orange (#FFF3E0 border, #FFE0B2 background)
  - Normal/Info: Blue (#E3F2FD border, #BBDEFB background)
  - Clinical Pearls: Teal (#E0F2F1 background)
  - Memory Tricks: Orange (#FFF3E0 background)
  - High-Yield: Purple (#F3E5F5 background)
☐ Responsive design (works on mobile)
☐ Self-contained (no external dependencies)

**Source Accuracy:**
☐ All info from source only (except researched mnemonics)
☐ External additions marked with asterisk (*)
☐ Learning objective STATEMENTS verbatim (not paraphrased)

**Completeness:**
☐ ALL learning objectives from source included
☐ All LOs answered (all parts)
☐ All comparison tables created for similar items
☐ Master tables complete with all topics
☐ Mnemonics researched via WebSearch (not invented)

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

---

## Save Files

**Output Filename Rule:**
1. Strip file extension and common suffixes (`_text.txt`, `_extracted.txt`, etc.)
2. Strip course prefixes (`Micro_`, `Pharm_`, `Clinical_`, `Patho_`, etc.)
3. Replace underscores with spaces for readability
4. Extract lecture number and topic: `[Number] [Topic]` or just `[Topic]`
5. Preserve capitalization as-is (after underscore→space conversion)
6. Add appropriate extension: `.html`
7. NO template suffixes, NO title case normalization

**Examples:**
- `Micro_4 Intro to Virology_text.txt` → `4 Intro to Virology.html`
- `Pharm_11 Beta Blockers_text.txt` → `11 Beta Blockers.html`
- `Micro_4_Intro_To_Virology_text.txt` → `4 Intro To Virology.html`
- `Micro_Basics Of Immunology_text.txt` → `Basics Of Immunology.html`

**Batch Merge Naming:**
- Input: `Micro_4 Intro to Virology_text.txt` + `Micro_5 Viral Replication_text.txt`
- Output: `Lecture 4-5.html`
- Format: `Lecture [min]-[max].html` (based on lecture numbers found)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[OutputFilename].html`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[OutputFilename].py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

---

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

❌ Paraphrasing learning objective statements (must be verbatim)
❌ Using wrong box colors (e.g., using red for normal info)
❌ Inventing mnemonics instead of researching via WebSearch
❌ Missing tabs (must have all 4 tabs)
❌ Adding external medical information not in source
❌ Using external CSS/JS dependencies (must be self-contained)
❌ Combining multiple categories in one comparison table

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 4 tabs: Learning Objectives, Key Comparisons, Master Comparison Tables, Summary
✓ Each LO has verbatim statement + comprehensive Q&A answer
✓ Separate comparison tables per category (one for Mechanism, one for Clinical)
✓ Master tables include ALL conditions from source

**Formatting:**
✓ Clinical Pearls box: Teal (#E0F2F1) background
✓ Memory Tricks box: Orange (#FFF3E0) background
✓ High-Yield box: Purple (#F3E5F5) background
✓ Emergency items: Red (#FFEBEE) border
✓ All CSS inline (self-contained HTML)

**Learning Objective Statements:**
✓ Source: "1. Compare and contrast the four types of hypersensitivity reactions"
✓ Guide:  "1. Compare and contrast the four types of hypersensitivity reactions"
✓ Status: VERBATIM - correct

### INCORRECT Implementation:

**Structure:**
✗ Only 3 tabs (missing Summary)
✗ LO statements paraphrased instead of verbatim
✗ All comparisons in ONE giant table instead of separate tables
✗ Missing conditions from master tables

**Formatting:**
✗ Clinical Pearls using purple instead of teal ← WRONG
✗ All boxes same color ← WRONG
✗ Emergency items not highlighted in red ← WRONG
✗ External Bootstrap CSS linked ← WRONG (must be self-contained)

**Learning Objective Statements:**
✗ Source: "1. Compare and contrast the four types of hypersensitivity reactions"
✗ Guide:  "1. Differentiate between hypersensitivity reaction types"
✗ Status: PARAPHRASED - must use exact wording from source

---

## Related Commands

- `/drugs-html` - For pharmacology topics (drug-focused template)
- `/drugs-3-tab-excel` - For comprehensive drug charts (Excel format)
- `/clinical-assessment-html` - For history-taking and physical exam guides
- `/verify-accuracy` - Verify accuracy of created study guide

## Template Customization

To modify the HTML template:
1. Edit: `study-guides/templates-and-examples/HTML_LO_REVISED.txt`
2. Changes apply automatically to next `/LO-html` use
3. Update `HOW_TO_USE.md` if workflow changes
