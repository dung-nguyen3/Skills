---
description: Create HTML learning objectives guide (any medical topic)
---

# Create Learning Objectives Guide

Create an **interactive HTML study guide** for ANY medical topic with learning objectives.

## Usage

```
/create-lo-guide [source_file.txt]
```

## What This Does

Creates a comprehensive 4-tab HTML study guide:
- **Tab 1: Learning Objectives** - Q&A format answering each LO in detail
- **Tab 2: Key Comparisons** - Focused 2-3 way comparison tables
- **Tab 3: Master Comparison Tables** - Complete differential diagnosis tables
- **Tab 4: Summary** - High-yield pearls, mnemonics, "If X Think Y" associations

## Example

```
/create-lo-guide sources/Cardiovascular-Disease.txt
/create-lo-guide sources/Hematology-II.txt
/create-lo-guide sources/Respiratory-Physiology.txt
```

Output: `[Topic]_Study_Guide.html`

## Template Location

The command uses the template at:
```
Example claude study guides/HTML LO/HTML LO with Master Chart 10-30.txt
```

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

- `/create-drug-html` - For pharmacology topics (drug-focused template)
- `/create-excel` - For comprehensive drug charts (Excel format)
- `/create-clinical-guide` - For history-taking and physical exam guides
- `/verify-accuracy` - Verify accuracy of created study guide

## Template Customization

To modify the HTML template:
1. Edit: `Example claude study guides/HTML LO/HTML LO with Master Chart 10-30.txt`
2. Changes apply automatically to next `/create-lo-guide` use
3. Update `HOW_TO_USE.md` if workflow changes
