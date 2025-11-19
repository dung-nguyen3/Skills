---
description: Create interactive HTML drug reference chart (pharmacology)
---

# Create Drug Chart HTML

Create an **interactive single-page HTML drug reference chart** for pharmacology content.

## Usage

```
/create-drug-html [source_file.txt]
```

## What This Does

Creates a self-contained HTML file with:
- **3 main tabs**: Drug Classes & Comparisons, Master Drug Chart, Quick Reference
- **Sortable tables** for all drugs
- **Color-coded badges** (routes, contraindications, drug choice)
- **Highlight boxes** for mechanisms, warnings, side effects
- **Researched mnemonics** for drug lists
- **Works offline** - single HTML file, no external dependencies

## Example

```
/create-drug-html sources/24-HIV-drugs.txt
```

Output: `HIV_Drug_Reference_Chart.html`

## Template Location

The command uses the template at:
```
Example claude study guides/Drug Chart HTML/Drug Chart HTML.txt
```

## Best For

- Antiviral drugs, antibiotics, antifungals
- Comparing drugs within classes
- Quick reference during clinical rotations
- Mobile-friendly study on the go

## Pre-Creation Checklist

Before creating, Claude will verify:
- ☐ Source file identified
- ☐ Template loaded from correct location
- ☐ Source-only policy confirmed
- ☐ WebSearch for mnemonics/analogies (mandatory)
- ☐ Save location: `[Class]/[Exam]/Claude Study Tools/`

## Post-Creation

After creation, Claude automatically:
- ✓ Verifies all content from source only
- ✓ Confirms template compliance
- ✓ Checks all tabs present
- ✓ Reports "Post-creation verification complete"

## Related Commands

- `/create-excel` - Create comprehensive Excel drug chart (same content, different format)
- `/verify-accuracy` - Verify accuracy of created study guide
- `/create-lo-guide` - For non-drug medical topics with learning objectives
