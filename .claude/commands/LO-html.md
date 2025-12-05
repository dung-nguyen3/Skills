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

## Mode Detection & Directory Expansion

**Step 1: Check for --merge flag:**
- If arguments start with `--merge`: **BATCH MERGE MODE** (N files → 1 merged HTML)
- Strip `--merge` to get file list

**Step 2: Check for semicolons:**
- If arguments contain `;`: **BATCH SEPARATE MODE** (N files → N HTML files)

**Step 3: Handle Directory Input:**
If path is a directory, process all .txt/.pdf files within it.
If batch (semicolon-separated), process each path independently.

**Step 4: Update mode if needed:**
- If 1 file: SINGLE MODE
- If multiple files AND no --merge: BATCH SEPARATE MODE
- If multiple files AND --merge: BATCH MERGE MODE

**For BATCH SEPARATE:** Launch batch-separate-processor agent N times (architectural isolation)

**For BATCH MERGE:** Launch batch-merge-orchestrator agent once (intelligent merge with overlap resolution)

**For SINGLE:** Process inline (read Steps below)

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
/LO-html "Pharmacology/Exam 3/Extract/Cardiovascular_Disease.txt"
```
Creates: `Cardiovascular_Disease_LO_Guide.html`

### Batch Separate (N files → N outputs):
```
/LO-html "Cardio-Lec1.txt;Cardio-Lec2.txt;Cardio-Lec3.txt"
```
Creates 3 separate HTML files (architectural isolation via agent)

### Batch Merge (N files → 1 merged output):
```
/LO-html --merge "Cardio-Lec1.txt;Cardio-Lec2.txt;Cardio-Lec3.txt"
```
Creates 1 comprehensive HTML file with all content merged + merge report


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
- ☐ Save study guide to: `[Class]/[Exam]/Claude Study Tools/[SourceFileName].html` (e.g., `1 ANS.txt` → `1 ANS.html`)
- ☐ Save Python file to: `[Class]/[Exam]/Claude Study Tools/py/[SourceFileName].py`

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
- `/4-tab-excel` - For comprehensive drug charts (Excel format)
- `/clinical-assessment-html` - For history-taking and physical exam guides
- `/verify-accuracy` - Verify accuracy of created study guide

## Template Customization

To modify the HTML template:
1. Edit: `study-guides/templates-and-examples/HTML_LO_REVISED.txt`
2. Changes apply automatically to next `/LO-html` use
3. Update `HOW_TO_USE.md` if workflow changes
