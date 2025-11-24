---
description: Create HTML learning objectives guide (any medical topic)
argument-hint: Single file OR batch files separated by semicolon (e.g., "file1.txt" OR "file1.txt;file2.txt")
---

# Create Learning Objectives Guide

Create an **interactive HTML study guide** for ANY medical topic with learning objectives.

## Usage

```
/html-LO [source_file.txt]
```

## What This Does

Creates a comprehensive 4-tab HTML study guide:
- **Tab 1: Learning Objectives** - Q&A format answering each LO in detail
- **Tab 2: Key Comparisons** - Focused 2-3 way comparison tables
- **Tab 3: Master Comparison Tables** - Complete differential diagnosis tables
- **Tab 4: Summary** - High-yield pearls, mnemonics, "If X Think Y" associations

## Example Usage

**Single:** Command with one file

**Batch:** Command with semicolon-separated files → Creates separate output files


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
- ☐ WebSearch for mnemonics/analogies (mandatory)
- ☐ All learning objectives extracted verbatim
- ☐ Save location: `[Class]/[Exam]/Claude Study Tools/`

## Post-Creation

After creation, Claude automatically:
- ✓ Verifies all learning objectives answered (all parts)
- ✓ Confirms all comparison tables present
- ✓ Checks master tables include ALL topics
- ✓ Reports "Post-creation verification complete"

## Batch Processing (BATCH MODE ONLY)

**If BATCH MODE, process each file independently:**

For each source file in the batch:
1. **Announce file**: "Processing file X of Y: [filename]"

2. **CRITICAL - Context Isolation Check**:
   ```
   CONTEXT ISOLATION VERIFICATION:
   ☐ I will FORGET all content from previous files
   ☐ I will ONLY extract information from THIS source file: [filename]
   ☐ I will verify content is ONLY from THIS file (not previous files)
   ☐ This HTML will contain ZERO content from previous files
   ```

3. **Per-File Verification** - Run complete verification checklist for THIS file

4. **Read source file** - Read THIS file completely, extract THIS file's content only

5. **MANDATORY - State content scope**: "Learning objectives in [filename]: [list main topics]"
   - This proves you're only using THIS file's content
   - If you see content from previous files, STOP and re-read source

6. **Create HTML file** - For THIS file only, using ONLY content from step 5

7. **Post-creation verification** - Verify THIS HTML contains ONLY THIS file's content

8. **MANDATORY - Isolation Confirmation**: "File [X] complete. Cleared all data. Ready for next file."

**Critical for Batch:**
- Each file gets complete verification (not once at start)
- Explicitly state learning objectives from each file before creating HTML
- Verify no content from previous files contaminated output
- Clear all data between files
- Each file gets its own HTML output

**Batch Summary**: After all files, provide summary of files created, topics covered, and any issues.

## Related Commands

- `/html-drug` - For pharmacology topics (drug-focused template)
- `/excel` - For comprehensive drug charts (Excel format)
- `/clinical` - For history-taking and physical exam guides
- `/verify-accuracy` - Verify accuracy of created study guide

## Template Customization

To modify the HTML template:
1. Edit: `study-guides/templates-and-examples/HTML_LO_REVISED.txt`
2. Changes apply automatically to next `/html-LO` use
3. Update `HOW_TO_USE.md` if workflow changes
