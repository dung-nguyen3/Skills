# Study Guides System

Automated pharmacy study guide generation using Claude Code.

## What This Does

Creates comprehensive study guides in multiple formats from source lecture notes:
- **Word (.docx)** - Learning objectives with tables, comparisons, and summaries
- **Excel (.xlsx)** - Drug charts with 4-tab structure (Details, Comparisons, Master Chart, High-Yield)
- **HTML** - Interactive web-based study guides with tabs and search

## Quick Start

### Create a Study Guide

```bash
# Word study guide from lecture notes
/LO-word "source-files/Lecture_42.txt"

# Excel drug chart
/4-tab-excel "source-files/HIV_Antivirals.txt"

# HTML interactive guide
/LO-html "source-files/Cardiovascular_Disease.txt"
```

## Folder Structure

```
study-guides/
├── .claude/
│   └── commands/          # Slash commands (/LO-word, /4-tab-excel, etc.)
├── CLAUDE.md              # Study guide specific settings
├── templates-and-examples/
│   ├── *_REVISED.txt      # Cleaned instruction templates
│   ├── Python_Examples/   # Complete working code examples
│   └── Excel_Color_Reference.txt
├── source-files/          # Your lecture notes go here
├── example-guides/        # Sample output for reference
└── generated-guides/      # Your created study guides appear here
```

## Available Commands

### /LO-word
Creates 4-section Word document:
1. Learning Objectives (with tables and clinical pearls)
2. Key Comparisons (side-by-side tables)
3. Master Chart (comprehensive overview)
4. High-Yield Summary (color-coded boxes)

### /4-tab-excel
Creates 4-tab Excel drug chart:
1. Drug Details (by class with comparison tables)
2. Key Comparisons (mechanisms, toxicities, uses)
3. Master Chart (all drugs in one table)
4. High-Yield & Pearls (mnemonics and clinical tips)

### /LO-html
Creates interactive HTML with tabs:
- Learning Objectives Q&A
- Comparison tables
- Master differential diagnosis
- Summary with mnemonics

## Key Features

- **Source-only policy**: Uses ONLY information from your source files
- **WebSearch for mnemonics**: Automatically researches established medical mnemonics
- **Consistent formatting**: Soft pastel colors, black text, professional layout
- **Verification built-in**: Each command includes pre/post-creation checklists

## Templates

### Current (REVISED)
- `Word_LO_11-5_REVISED.txt` (~450 lines, 35% reduction from original)
- `Excel_Drugs_Chart_11-1_REVISED.txt` (~550 lines, 52% reduction)
- `Excel_Master_Chart_Only_REVISED.txt` (~280 lines, 43% reduction)
- `HTML_LO_REVISED.txt` (~125 lines, 9% reduction)

All revised templates:
- Reference parent CLAUDE.md for shared policies (no duplication)
- Link to Python_Examples/ for complete working code
- Fixed table text color bug (black text, not white)
- Removed redundant verification checklists

### Python Examples
Complete working implementations you can reference:
- `Excel_Drug_Example.py` - Full 4-tab drug chart (365 lines)
- `Excel_Master_Chart_Example.py` - Single-sheet examples (238 lines)
- `Word_LO_Example.py` - Full 4-section Word doc (304 lines)

## Source File Requirements

Your lecture notes should include:
- Clear learning objectives
- Drug information (names, mechanisms, side effects, uses)
- Clinical context and comparisons
- Any relevant diagrams or tables (will be converted to text descriptions)

The system extracts information and creates structured study materials automatically.

## Output Location

Generated files save to:
```
[Class]/[Exam]/Claude Study Tools/[Topic]_Study_Guide.{docx|xlsx|html}
```

Example:
```
Pharmacology/Exam 3/Claude Study Tools/HIV_Antivirals_Drug_Chart.xlsx
```

## Customization

To modify templates:
1. Edit files in `templates-and-examples/`
2. Reference `Python_Examples/` for code patterns
3. Changes apply immediately to next command use
4. Keep templates under 500 lines for optimal performance

## Related Folders

- **`.claude/`** - Claude infrastructure (commands, skills, hooks, agents)
- **`templates-and-examples/`** - All templates and Python examples

## Best Practices

1. **One topic per file**: Don't combine multiple lectures in one source file
2. **Clear learning objectives**: Start source files with explicit LOs
3. **Verify output**: Always review generated guides for accuracy
4. **Iterative improvement**: If output isn't perfect, refine source file and regenerate

## Requirements

- Python 3.x with libraries:
  - `python-docx` (for Word documents)
  - `openpyxl` (for Excel files)
- Claude Code extension in VS Code

Install missing libraries:
```bash
pip3 install python-docx openpyxl
```
