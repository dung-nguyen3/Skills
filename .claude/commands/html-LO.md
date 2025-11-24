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
