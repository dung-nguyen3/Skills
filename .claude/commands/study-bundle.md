# Study Bundle Command - Word LO + Excel Comparison + Anki Cards

**Purpose:** Generate 3 complementary study formats from source file(s) in one pass:
1. Word LO Study Guide (detailed learning objectives with tables)
2. Excel Comparison Chart (side-by-side comparisons)
3. Anki Flashcard Deck (.apkg file)

**Token Efficiency:** Reads source once, generates all 3 formats (~40k tokens saved vs. 3 separate commands)

---

## Usage

### Single File
```bash
/study-bundle "source-file.txt"
```

### Batch Separate (N files → N bundles)
```bash
/study-bundle "file1.txt;file2.txt;file3.txt"
```

### Batch Merge (N files → 1 merged bundle)
```bash
/study-bundle --merge "file1.txt;file2.txt;file3.txt"
```

### Directory Input
```bash
/study-bundle "path/to/folder/"
```

---

## What This Creates

For a source file named "HIV_Drugs.txt":

```
Claude Study Tools/
├── HIV_Drugs_Study_Guide.docx          (Word LO format)
├── HIV_Drugs_Comparison_Chart.xlsx     (Excel comparison tables)
└── HIV_Drugs_Flashcards.apkg           (Anki deck)
```

**Output location:** `[Class]/[Exam]/Claude Study Tools/`

---

## Command Execution

When you run `/study-bundle [source-file]`:

### Step 1: Pre-Creation Verification

**MANDATORY CHECKLIST** (source-only-enforcer):
```
VERIFICATION CHECKLIST:
☐ Source file: [exact path]
☐ Templates: Word LO 11-5, Excel Comparison, Anki
☐ Source-only policy: I will ONLY use information from source file
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

### Step 2: Batch Validation (batch-coordinator)

If multiple files detected:
```
BATCH VALIDATION:
☐ All files exist and are readable
☐ Files are compatible for chosen mode (separate vs merge)
☐ Template compatible with ALL files
☐ Total content size manageable
```

### Step 3: Read Source File(s)

**Read ENTIRE source file(s)** - No partial reads

**Extract key information:**
- Learning objectives (verbatim)
- All conditions/drugs mentioned
- Comparison categories (mechanisms, uses, adverse effects, etc.)
- Clinical pearls
- Key facts for flashcards

### Step 4: Generate Formats in Parallel

**Format 1: Word LO Study Guide**
- Template: `study-guides/templates-and-examples/Word_LO_11-5_REVISED.txt`
- 4 sections: Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary
- Soft pastel color scheme (Calibri 12pt)
- **Comparison Item Inventory Protocol:** Mandatory before creating comparison tables
- Output: `[Topic]_Study_Guide.docx`

**Format 2: Excel Comparison Chart**
- Template: `study-guides/templates-and-examples/Excel_Comparison_REVISED.txt`
- Side-by-side comparison tables
- Font: Calibri size 10 (data), size 12 (headers)
- Colors: Soft pastels from ROW_COLORS palette
- White borders (#FFFFFF)
- Output: `[Topic]_Comparison_Chart.xlsx`

**Format 3: Anki Flashcard Deck**
- Template: `study-guides/templates-and-examples/Anki_REVISED.txt`
- Card types: Basic, Cloze, Clinical Scenario
- Front/back from source only
- Researched mnemonics included
- Output: `[Topic]_Flashcards.apkg`

### Step 5: Create Verification Marker

```bash
mkdir -p "$CLAUDE_PROJECT_DIR/.claude/study-guide-cache/${session_id}"
echo '{"verified":true,"timestamp":"'$(date -Iseconds)'","formats":["word","excel-comparison","anki"]}' > \
  "$CLAUDE_PROJECT_DIR/.claude/study-guide-cache/${session_id}/verification.json"
```

### Step 6: Batch Mode Execution

**For Single File:**
- Process directly
- Create all 3 outputs

**For Batch Separate (N→N):**
- Invoke `batch-separate-processor` agent per file
- Each file creates its own bundle (3 outputs per file)
- Architectural isolation guarantees zero cross-contamination

**For Batch Merge (N→1):**
- Invoke `batch-merge-orchestrator` agent once
- Read all N files
- Merge content intelligently
- Create ONE unified bundle (3 merged outputs)
- Generate merge_report.md with source traceability

### Step 7: Post-Creation Verification

After creating all 3 formats:

```
POST-CREATION VERIFICATION:
☐ Source Accuracy: All information from source only
☐ Template Compliance:
  - Word: 4 sections, soft pastels, Calibri 12pt
  - Excel: Font size 10, white borders, pastel colors
  - Anki: Source-only cards, researched mnemonics
☐ Completeness: All topics from source included
☐ Quality: Comparison Item Inventory Protocol followed
```

### Step 8: Summary Output

```
✅ STUDY BUNDLE CREATED

Source: HIV_Drugs.txt

Outputs:
1. HIV_Drugs_Study_Guide.docx (Word LO - 12 pages)
2. HIV_Drugs_Comparison_Chart.xlsx (Excel - 8 comparisons)
3. HIV_Drugs_Flashcards.apkg (Anki - 47 cards)

Location: Pharmacology/Exam 3/Claude Study Tools/

Token Efficiency: ~42,000 tokens saved vs. 3 separate commands
```

---

## Template Integration

### Word LO Template Requirements

**Source:** `study-guides/templates-and-examples/Word_LO_11-5_REVISED.txt`

**Key Requirements:**
- 4 sections: Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary
- Soft pastel colors: Purple #D1C4E9, Green #C8E6C9, Blue #B3E5FC, Teal #B2DFDB
- Calibri font, size 12pt
- Learning objectives VERBATIM (no paraphrasing)
- Comparison Item Inventory Protocol before creating tables
- WebSearch for mnemonics

**Python Implementation:**
```python
from docx import Document
from docx.shared import Pt, RGBColor, Inches

def set_cell_text(cell, text, bold=False, color=None, size=11):
    cell.text = text
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(size)
            run.font.name = 'Calibri'
            run.bold = bold
            if color:
                run.font.color.rgb = RGBColor(*color)
```

### Excel Comparison Template Requirements

**Source:** `study-guides/templates-and-examples/Excel_Comparison_REVISED.txt`

**Key Requirements:**
- Side-by-side comparison tables
- Font: Calibri size 10 (data), size 12 (headers)
- Color scheme: ROW_COLORS palette
- White borders: #FFFFFF
- Frozen header rows
- Comparison Item Inventory Protocol mandatory

**Python Implementation:**
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

HEADER_BG = '4472C4'
ROW_COLORS = ['D9E2F3', 'C8E6C9', 'D1C4E9', 'F7E7CE', 'BDD7EE',
              'F0F8FF', 'FCE4EC', 'EDE7F6', 'FFE8D6', 'BBDEFB']

def apply_cell_style(cell, text='', bold=False, font_size=10, bg_color=None):
    cell.value = text
    cell.font = Font(name='Calibri', size=font_size, bold=bold, color='000000')
    cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    if bg_color:
        cell.fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type='solid')
    cell.border = Border(
        left=Side(style='thin', color='FFFFFF'),
        right=Side(style='thin', color='FFFFFF'),
        top=Side(style='thin', color='FFFFFF'),
        bottom=Side(style='thin', color='FFFFFF')
    )
```

### Anki Template Requirements

**Source:** `study-guides/templates-and-examples/Anki_REVISED.txt`

**Key Requirements:**
- Card types: Basic (front/back), Cloze (fill-in-blank), Clinical Scenario
- Source-only content
- Researched mnemonics via WebSearch
- No external medical facts

---

## Comparison Item Inventory Protocol (MANDATORY)

**Before creating ANY comparison table:**

### Step 1: Extract ALL Comparable Items
```
COMPARISON INVENTORY for [Category]:
Items to compare: [list all items from source]
Total count: [N items]
```

### Step 2: Create Comparison Table
- Include ALL items from inventory
- No skipping items
- Each item gets complete row/column

### Step 3: Post-Table Verification
```
POST-TABLE VERIFICATION:
☑ All [N] items from inventory appear in table
☑ No items from inventory were skipped
☑ Items match source names exactly
☑ Each item has all relevant properties filled in
```

**Purpose:** Prevents common error where less prominent items are skipped in comparison tables.

---

## Batch Processing Modes

### Mode 1: Single File (Default)
```bash
/study-bundle "HIV_Drugs.txt"
```

**Output:** 3 files
- HIV_Drugs_Study_Guide.docx
- HIV_Drugs_Comparison_Chart.xlsx
- HIV_Drugs_Flashcards.apkg

---

### Mode 2: Batch Separate (N files → N bundles)
```bash
/study-bundle "HIV_Drugs.txt;Antibiotics.txt;Antivirals.txt"
```

**Output:** 9 files (3 per source)
```
HIV_Drugs_Study_Guide.docx
HIV_Drugs_Comparison_Chart.xlsx
HIV_Drugs_Flashcards.apkg

Antibiotics_Study_Guide.docx
Antibiotics_Comparison_Chart.xlsx
Antibiotics_Flashcards.apkg

Antivirals_Study_Guide.docx
Antivirals_Comparison_Chart.xlsx
Antivirals_Flashcards.apkg
```

**Agent:** batch-separate-processor (invoked 3 times, architectural isolation)

---

### Mode 3: Batch Merge (N files → 1 merged bundle)
```bash
/study-bundle --merge "HIV-NRTIs.txt;HIV-NNRTIs.txt;HIV-PIs.txt"
```

**Output:** 3 merged files
```
HIV_Comprehensive_Study_Guide.docx      (all 3 lectures merged)
HIV_Comprehensive_Comparison_Chart.xlsx (all drug classes merged)
HIV_Comprehensive_Flashcards.apkg       (all cards merged)
HIV_Comprehensive_merge_report.md       (traceability map)
```

**Agent:** batch-merge-orchestrator (invoked once, intelligent merging)

**Merge Report Includes:**
- Content matrix (which files covered which topics)
- Overlap resolution (how conflicts were handled)
- Source traceability (which file contributed which content)
- Gaps identified (topics mentioned but not detailed)

---

## Directory Input Support

```bash
/study-bundle "Pharmacology/Exam 3/Extract/"
```

**Behavior:**
1. Scans directory for `.txt` source files
2. Reads `.processed_files.txt` to skip already-processed files
3. Creates study bundles for NEW files only
4. Updates `.processed_files.txt` with timestamps

**Example `.processed_files.txt`:**
```
HIV_Drugs.txt|2025-12-04T10:30:00|processed
Antibiotics.txt|2025-12-04T10:35:00|processed
Antivirals.txt|2025-12-04T10:40:00|processed
```

**Next run:** Only processes files NOT in `.processed_files.txt`

**Force reprocess:** Delete `.processed_files.txt` or specific lines

---

## Error Handling

### Missing Source File
```
❌ ERROR: Source file not found
File: HIV_Drugs.txt
Action: Verify file path and try again
```

### Incompatible Files (Batch Merge)
```
❌ ERROR: Files incompatible for merging
File1: HIV_Drugs.txt (drug lecture)
File2: Pneumonia.txt (condition lecture)
Reason: Different content types require different templates
Action: Use batch separate mode OR process separately
```

### Verification Checklist Missing
```
⛔ BLOCKED - Pre-Creation Verification Required

You must state the verification checklist before proceeding.

VERIFICATION CHECKLIST:
☐ Source file: [exact path]
☐ Templates: Word LO, Excel Comparison, Anki
☐ Source-only policy: I will ONLY use information from source file
☐ Exception: Mnemonics WILL be researched via WebSearch
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

---

## Quality Checklist

Before finalizing, verify:

### Content Accuracy
- [ ] ALL information from source only (except researched mnemonics)
- [ ] Learning objectives extracted VERBATIM (no paraphrasing)
- [ ] No external medical facts added
- [ ] Mnemonics researched via WebSearch (not invented)

### Format Compliance
- [ ] **Word:** 4 sections, soft pastels, Calibri 12pt
- [ ] **Excel:** Font size 10, white borders, ROW_COLORS palette
- [ ] **Anki:** Source-only cards, proper card types

### Completeness
- [ ] All topics from source included in all 3 formats
- [ ] Comparison Item Inventory Protocol followed
- [ ] No items skipped in comparison tables

### Verification
- [ ] Verification marker created
- [ ] Post-creation verification completed
- [ ] All 3 formats created successfully

---

## Token Efficiency

**Traditional Approach (3 separate commands):**
- /word: Read source (20k) + generate Word (15k) = 35k
- /excel-comparison: Read source (20k) + generate Excel (12k) = 32k
- /anki: Read source (20k) + generate Anki (10k) = 30k
- **Total: ~97k tokens**

**Study Bundle Approach:**
- Read source ONCE (20k)
- Generate Word (15k) + Excel (12k) + Anki (10k) = 37k
- **Total: ~57k tokens**

**Savings: ~40k tokens per source file**

---

## Integration with Other Commands

**Complementary Commands:**
- `/excel` - Full 4-tab drug chart (more comprehensive than comparison chart)
- `/html-drug` - Interactive HTML drug reference
- `/clinical` - Clinical assessment guide for H&P
- `/biography` - Drug autobiography stories
- `/verify-accuracy` - Comprehensive accuracy verification

**When to use /study-bundle:**
- You want Word LO + Excel comparisons + Anki cards
- You're studying for exams (need multiple formats)
- You want token-efficient multi-format generation

**When to use separate commands:**
- You only need one format
- You need specialized formats (HTML, clinical, biography)
- You need full 4-tab Excel drug chart

---

## Tips

💡 **Batch processing:** Process multiple files at once to save time

💡 **Directory mode:** Point to your Extract folder and process all new files automatically

💡 **Merge mode:** Use `--merge` flag when multiple lectures cover the same topic

💡 **Verification:** Checklist ensures source-only policy and quality standards

💡 **Token efficiency:** Study bundle saves ~40k tokens vs. 3 separate commands

---

## Examples

### Example 1: Single File
```bash
/study-bundle "Pharmacology/Exam 3/Extract/HIV_Drugs.txt"
```

Creates:
- HIV_Drugs_Study_Guide.docx
- HIV_Drugs_Comparison_Chart.xlsx
- HIV_Drugs_Flashcards.apkg

---

### Example 2: Batch Separate
```bash
/study-bundle "HIV_Drugs.txt;Antibiotics.txt;Antivirals.txt"
```

Creates 9 files (3 per topic):
- 3 Word study guides
- 3 Excel comparison charts
- 3 Anki decks

---

### Example 3: Batch Merge
```bash
/study-bundle --merge "HIV-Lecture1.txt;HIV-Lecture2.txt;HIV-Lecture3.txt"
```

Creates 3 merged files + merge report:
- HIV_Comprehensive_Study_Guide.docx
- HIV_Comprehensive_Comparison_Chart.xlsx
- HIV_Comprehensive_Flashcards.apkg
- HIV_Comprehensive_merge_report.md

---

### Example 4: Directory Processing
```bash
/study-bundle "Pharmacology/Exam 3/Extract/"
```

Processes all NEW `.txt` files in directory, creates bundles for each.

---

**End of Command Documentation**
