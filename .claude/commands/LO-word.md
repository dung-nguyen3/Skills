---
description: Create comprehensive Word study guide from source material following template
argument-hint: Single file, batch files separated by semicolon, or directory paths. Use --merge for combined output (e.g., "file.txt" OR "f1.txt;f2.txt" OR "/path/to/dir" OR "--merge /dir1;/dir2")
---

Create Word study guide from: $ARGUMENTS

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
- **SINGLE**: 1 file → 1 Word guide (inline processing)
- **BATCH SEPARATE**: N files → N Word guides (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged Word guide (orchestrator agent, intelligent merge)

---

### Step 0.8: Learning Objective Inventory (SINGLE MODE ONLY)

**Skip this step for BATCH modes** (agents handle their own counting).

**Before creating content, extract ALL LO statements from source:**

1. Scan source file for Learning Objectives section
2. Extract each LO statement verbatim
3. Number them sequentially
4. Document the count

**Output format:**
```
LEARNING OBJECTIVE INVENTORY
Source: [filename]
Total LOs found: [N]

1. [LO statement 1]
2. [LO statement 2]
3. [LO statement 3]
...
N. [LO statement N]
```

**Keep this list for verification at end (Step 10).**

---

### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: $ARGUMENTS
☐ Instruction template: Word LO 11-5.txt
☐ Source-only policy: I will ONLY use information from source file
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
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
   - Complete 2-section implementation with all helper functions
   - Shows Learning Objectives and Key Comparisons

### Step 3: Read and Extract Source Content COMPLETELY

**Read entire source file:** $ARGUMENTS

Use Read tool to load complete file (no limits):
- For 200-line files: Read fully
- For 800+ line files: Read fully (Read tool handles large files)
- Do NOT skip sections due to length

**Extract ALL content in order:**

1. **Learning Objectives** (Step 0.8 already created inventory):
   - Extract each LO statement VERBATIM (no paraphrasing)
   - Number sequentially
   - Store for Python generation

2. **Content for Each LO:**
   - Scan source for content relevant to each LO
   - Look for:
     - Section headings matching LO keywords
     - Slide titles corresponding to LOs
     - Content blocks between LO mentions
   - Extract facts, mechanisms, definitions, processes

3. **Comparison Opportunities:**
   - Identify any 2+ similar items (conditions, mechanisms, processes)
   - Note categories (presentation, mechanism, treatment, etc.)
   - Extract comparison data for tables

4. **Clinical Context:**
   - Note clinical significance statements
   - Identify diagnostic tips or common mistakes
   - Extract warnings or red flags
   - Look for "Important:" or "Note:" markers

**Large file strategy (800+ lines, 14+ LOs):**
- Process sequentially: LO 1 → LO 14
- Map content sections to specific LOs
- Track which content belongs to which LO
- Use Read tool (handles complete file in single read)

### Step 3.5: Analyze Summary Format Needs

**MANDATORY - Analyze EACH learning objective answer to determine correct summary format:**

For each LO you extracted in Step 3, analyze the answer structure:

**Decision workflow:**
1. Count the main components/layers/functions/mechanisms in the answer
2. Determine if answer has hierarchy (main points with sub-details)
3. Choose format based on criteria below

**Format Decision Criteria:**

Use `add_summary_structured()` if ANY of these apply:
- ✅ Answer lists 3+ distinct components/layers/functions/mechanisms
- ✅ Answer has hierarchical structure (main points with sub-details)
- ✅ Answer describes sequential processes with 3+ steps
- ✅ Answer enumerates 3+ categories/types/classifications

Use `add_summary_simple()` if:
- ✅ Answer explains 1-2 concepts only
- ✅ Answer is cohesive paragraph without enumeration
- ✅ Answer describes a single mechanism or process

**Output format:**
```
SUMMARY FORMAT ANALYSIS
-----------------------
LO 1: [LO statement]
Answer components: [count]
Format: [STRUCTURED / SIMPLE]
Reason: [Lists 4 functions / Simple mechanism explanation / etc.]

LO 2: [LO statement]
Answer components: [count]
Format: [STRUCTURED / SIMPLE]
Reason: [Lists 4 layers / etc.]

... for all LOs
```

**Keep this analysis for Step 4 (Python generation).**

---

### Step 4: Generate Python Script with Extracted Content

**CRITICAL - You will generate a COMPLETE Python script with ALL extracted content hardcoded.**

This is NOT about modifying the example file. You will create a NEW Python script with your extracted data.

**Python Script Structure:**

```python
#!/usr/bin/env python3
"""
WORD LEARNING OBJECTIVE STUDY GUIDE
Source: [filename]
Course: [course name]
Topic: [topic]
LO Count: [N]
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# =============================================================================
# HELPER FUNCTIONS (Copy from Word_LO_Example.py)
# =============================================================================

def set_cell_background(cell, color):
    """Set cell background color using hex"""
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), color)
    cell._element.get_or_add_tcPr().append(shading_elm)

def set_cell_text(cell, text, bold=False, size=11):
    """
    Set cell text - always black for readability
    Supports line breaks: text with \n renders on multiple lines
    """
    cell.text = text
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(size)
            run.font.name = 'Calibri'
            run.bold = bold

def add_plain_bullets(doc, items, bold_title=None):
    """Add plain bulleted list without colored box (for Clinical Pearls)"""
    if bold_title:
        para = doc.add_paragraph()
        run = para.add_run(bold_title)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(12)

    for item in items:
        para = doc.add_paragraph(item, style='List Bullet')
        # Word default: bullet at 0.25", text at 0.5"
        para.paragraph_format.left_indent = Inches(0.5)
        para.paragraph_format.first_line_indent = Inches(-0.25)  # Hanging indent
        # Universal formatting: 1.5 spacing
        para.paragraph_format.space_before = Pt(0)
        para.paragraph_format.space_after = Pt(0)
        para.paragraph_format.line_spacing = 1.5
        for run in para.runs:
            run.font.name = 'Calibri'
            run.font.size = Pt(12)

def add_summary_simple(doc, summary_text):
    """Add simple paragraph-style summary (1-2 concepts) - NO 'Summary:' label"""
    summary_para = doc.add_paragraph(summary_text)
    # Universal formatting: 1.5 spacing
    summary_para.paragraph_format.space_before = Pt(0)
    summary_para.paragraph_format.space_after = Pt(0)
    summary_para.paragraph_format.line_spacing = 1.5
    summary_para.runs[0].font.name = 'Calibri'
    summary_para.runs[0].font.size = Pt(12)
    return summary_para

def add_summary_structured(doc, intro_text, items):
    """
    Add structured numbered summary with sub-bullets (3+ components) - NO 'Summary:' label
    Uses manual numbering to ensure numbering restarts at 1 for each LO
    Uses Word multilevel list defaults with hanging indents

    Args:
        doc: Document object
        intro_text: Introduction text (no label)
        items: List of dicts: [{'main': 'Point 1', 'subs': ['Sub A', 'Sub B']}, ...]
    """
    # Intro paragraph (no label)
    summary_intro = doc.add_paragraph(intro_text)
    summary_intro.paragraph_format.space_before = Pt(0)
    summary_intro.paragraph_format.space_after = Pt(0)
    summary_intro.paragraph_format.line_spacing = 1.5
    summary_intro.runs[0].font.name = 'Calibri'
    summary_intro.runs[0].font.size = Pt(12)

    # Numbered items with manual numbering
    for idx, item in enumerate(items, start=1):
        p = doc.add_paragraph()
        num_run = p.add_run(f'{idx}. ')
        num_run.bold = True
        num_run.font.size = Pt(12)
        num_run.font.name = 'Calibri'
        text_run = p.add_run(item['main'])
        text_run.font.size = Pt(12)
        text_run.font.name = 'Calibri'
        # Word default: number at 0", text at 0.25"
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.first_line_indent = Inches(-0.25)  # Hanging indent
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.5

        # Sub-bullets (if any)
        if 'subs' in item and item['subs']:
            for sub in item['subs']:
                sub_p = doc.add_paragraph(sub, style='List Bullet')
                # Word default: bullet at 0.25", text at 0.5"
                sub_p.paragraph_format.left_indent = Inches(0.5)
                sub_p.paragraph_format.first_line_indent = Inches(-0.25)  # Hanging indent
                sub_p.paragraph_format.space_before = Pt(0)
                sub_p.paragraph_format.space_after = Pt(0)
                sub_p.paragraph_format.line_spacing = 1.5
                sub_p.runs[0].font.name = 'Calibri'
                sub_p.runs[0].font.size = Pt(12)

def add_bookmark(paragraph, bookmark_name):
    """Add a bookmark anchor to a paragraph for hyperlinking"""
    bookmark_id = str(abs(hash(bookmark_name)) % 1000000)
    bookmark_start = OxmlElement('w:bookmarkStart')
    bookmark_start.set(qn('w:id'), bookmark_id)
    bookmark_start.set(qn('w:name'), bookmark_name)
    bookmark_end = OxmlElement('w:bookmarkEnd')
    bookmark_end.set(qn('w:id'), bookmark_id)
    paragraph._element.insert(0, bookmark_start)
    paragraph._element.append(bookmark_end)

def add_hyperlink_to_bookmark(paragraph, display_text, bookmark_name, color='0563C1'):
    """Add clickable hyperlink to a bookmark within paragraph"""
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('w:anchor'), bookmark_name)
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    c = OxmlElement('w:color')
    c.set(qn('w:val'), color)
    rPr.append(c)
    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    rPr.append(u)
    font = OxmlElement('w:rFonts')
    font.set(qn('w:ascii'), 'Calibri')
    rPr.append(font)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), '24')
    rPr.append(sz)
    new_run.append(rPr)
    text_elem = OxmlElement('w:t')
    text_elem.text = display_text
    new_run.append(text_elem)
    hyperlink.append(new_run)
    paragraph._element.append(hyperlink)

# =============================================================================
# EXTRACTED DATA (Hardcoded from source)
# =============================================================================

# Learning objectives (verbatim from source)
learning_objectives = [
    "1. [Exact LO 1 text from source]",
    "2. [Exact LO 2 text from source]",
    # ... all LOs from source
]

# Content for each LO
lo1_summary = "[Concise paragraph answering LO 1 from source content]"
lo1_table_data = [
    ['Category 1', 'Value 1A', 'Value 1B'],
    ['Category 2', 'Value 2A', 'Value 2B'],
    # ... all rows extracted from source
]
lo1_clinical_pearls = [
    "[Clinical reasoning pearl 1]",
    "[High-yield point 2]",
    "[If X think Y association 3]"
]

lo2_summary = "[Answer to LO 2...]"
lo2_table_data = [...]
lo2_clinical_pearls = [...]

# ... data for all LOs

# Key comparisons data
comparison1_title = "[e.g., Segmentation vs Peristalsis]"
comparison1_data = [
    ['Feature', 'Item A', 'Item B'],
    ['Definition', '[From source]', '[From source]'],
    ['Function', '[From source]', '[From source]'],
    # ... all comparison rows
]

# =============================================================================
# DOCUMENT CREATION
# =============================================================================

def create_word_study_guide(output_path):
    """Create complete Word LO study guide"""

    doc = Document()

    # Set margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Title page with Table of Contents
    title = doc.add_heading('[Topic from source]', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.runs[0].font.color.rgb = RGBColor(118, 75, 162)
    title.runs[0].font.size = Pt(20)

    doc.add_paragraph()  # Spacing

    # Table of Contents heading
    toc_heading = doc.add_heading('Table of Contents', 2)
    toc_heading.runs[0].font.color.rgb = RGBColor(118, 75, 162)

    # TOC entries (clickable)
    for idx, lo_text in enumerate(learning_objectives, start=1):
        toc_para = doc.add_paragraph()
        toc_para.paragraph_format.left_indent = Inches(0.25)

        # Number (not hyperlinked)
        num_run = toc_para.add_run(f'{idx}. ')
        num_run.font.name = 'Calibri'
        num_run.font.size = Pt(12)

        # LO text (hyperlinked to bookmark)
        bookmark_name = f'LO_{idx}'
        add_hyperlink_to_bookmark(toc_para, lo_text, bookmark_name, color='0563C1')

    doc.add_page_break()

    # Learning Objectives (no section heading - starts directly with LO 1)
    # LO 1 (with bookmark for TOC and back-links from tables)
    # Format: "1. [Learning objective statement]" - statement is IN heading, no separate paragraph
    obj1 = doc.add_heading(f'1. {learning_objectives[0]}', 2)
    obj1.runs[0].font.color.rgb = RGBColor(118, 75, 162)
    obj1.runs[0].font.size = Pt(14)  # Font size 14pt for LO headings
    add_bookmark(obj1, 'LO_1')  # Add bookmark

    # CRITICAL - Use the format analysis from Step 3.5
    # Check your Step 3.5 analysis to determine which format to use:
    # - If format is STRUCTURED: Use add_summary_structured(doc, intro_text, items)
    # - If format is SIMPLE: Use add_summary_simple(doc, summary_text)

    # Example for STRUCTURED format (3+ components):
    # LO 1 - Format: STRUCTURED (4 components)
    add_summary_structured(doc,
        'The GI system performs four primary functions:',
        [
            {'main': 'Motility - muscular contractions moving contents through the tract'},
            {'main': 'Secretion - release of enzymes, acid, mucus, and bile'},
            {'main': 'Digestion - breakdown of macronutrients into absorbable units'},
            {'main': 'Absorption - uptake of nutrients, water, and electrolytes'}
        ]
    )
    # Note: Indentation is handled by add_summary_structured:
    #   - Numbers: 0.25 inches left indent
    #   - Sub-bullets: 0.5 inches left indent

    # Example for SIMPLE format (1-2 concepts):
    # LO 2 - Format: SIMPLE (1 concept)
    # add_summary_simple(doc,
    #     'Beta blockers competitively antagonize β-adrenergic receptors, reducing heart rate, '
    #     'contractility, and blood pressure through blockade of sympathetic stimulation.')

    # Clinical Pearls (plain bullets, NO colored box)
    # NOTE: Only 1 line space between sections (natural paragraph spacing - NO doc.add_paragraph())
    add_plain_bullets(doc, lo1_clinical_pearls,
                      bold_title='Clinical Pearls & High-Yield Points:')

    # Tables (clickable links to Reference Tables section)
    # NOTE: Only 1 line space between sections (natural paragraph spacing)
    tables_heading = doc.add_paragraph()
    run = tables_heading.add_run('Tables:')
    run.bold = True
    run.font.name = 'Calibri'
    run.font.size = Pt(12)

    # Add clickable link for each table (bookmark names: LO_1_Table_1, LO_1_Table_2, etc.)
    for table_idx, table_title in enumerate(['[Table 1 Title]', '[Table 2 Title]'], start=1):
        link_para = doc.add_paragraph()
        link_para.paragraph_format.left_indent = Inches(0.25)
        arrow_run = link_para.add_run('→ ')
        arrow_run.font.name = 'Calibri'
        arrow_run.font.size = Pt(12)
        bookmark_name = f'LO_1_Table_{table_idx}'
        add_hyperlink_to_bookmark(link_para, table_title, bookmark_name, color='0563C1')

    # 1 line space between Learning Objectives (NO page break)
    doc.add_paragraph()

    # LO 2, LO 3, ... repeat pattern for all LOs (each with bookmark, related tables, spacing)

    # Reference Tables section (NEW - tables grouped by LO)
    ref_tables_heading = doc.add_heading('Reference Tables', 1)
    ref_tables_heading.runs[0].font.color.rgb = RGBColor(118, 75, 162)

    doc.add_paragraph()

    # Tables for Learning Objective 1
    # (No subsection heading - tables listed directly)

    # Table 1 for LO 1 (with bookmark and back-link)
    table_heading_para = doc.add_paragraph()
    title_run = table_heading_para.add_run('[Table 1 Title]')
    title_run.bold = True
    title_run.font.name = 'Calibri'
    title_run.font.size = Pt(14)
    title_run.font.color.rgb = RGBColor(118, 75, 162)
    add_bookmark(table_heading_para, 'LO_1_Table_1')
    table_heading_para.add_run('    ')  # Spacing
    add_hyperlink_to_bookmark(table_heading_para, 'LO 1', 'LO_1', color='0563C1')

    # Create the table
    table1 = doc.add_table(rows=len(lo1_table_data)+1, cols=3)
    table1.style = 'Table Grid'

    # Headers
    headers = ['Feature', 'Category A', 'Category B']
    for i, header_text in enumerate(headers):
        set_cell_background(table1.rows[0].cells[i], 'B3E5FC')
        set_cell_text(table1.rows[0].cells[i], header_text, bold=True, size=12)

    # Data rows (supports line breaks and bullet points)
    for row_idx, row_content in enumerate(lo1_table_data, start=1):
        cells = table1.rows[row_idx].cells
        set_cell_background(cells[0], 'E1F5FE')
        set_cell_text(cells[0], row_content[0], bold=True)
        for col_idx in range(1, 3):
            set_cell_background(cells[col_idx], 'FFFFFF')
            # If cell_data is a list, format as bullets
            if isinstance(row_content[col_idx], list):
                cells[col_idx].text = ''
                for item in row_content[col_idx]:
                    para = cells[col_idx].add_paragraph(item, style='List Bullet')
                    para.runs[0].font.name = 'Calibri'
                    para.runs[0].font.size = Pt(11)
            else:
                # Single text (may contain \n for line breaks)
                set_cell_text(cells[col_idx], row_content[col_idx])

    doc.add_paragraph()

    # Repeat for all tables for LO 1, then all tables for LO 2, etc.

    # Key Comparisons section (section heading kept)
    heading2 = doc.add_heading('Key Comparisons', 1)
    heading2.runs[0].font.color.rgb = RGBColor(118, 75, 162)

    # Comparison table (no "Comparison 1:" prefix - descriptive title only)
    doc.add_heading(comparison1_title, 2)
    comp_table = doc.add_table(rows=len(comparison1_data), cols=3)
    comp_table.style = 'Table Grid'

    # [Create comparison table using comparison1_data...]

    # Save document
    doc.save(output_path)
    print(f"✅ Word LO study guide created: {output_path}")

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    output_path = '[Full absolute path to output.docx]'
    create_word_study_guide(output_path)
```

**Content Extraction Guidelines:**

**Learning Objective Statements:**
- Copy EXACTLY as written (verbatim, character-for-character)
- Do NOT rephrase, summarize, or "improve"
- Preserve original numbering
- If source has 14 LOs, create data for all 14

**Summary Formatting - Choose Based on Complexity:**

**Simple Summaries (1-2 concepts):**
- Use paragraph format
- Concise, cohesive explanation (2-4 sentences)
- Example: "Beta blockers competitively antagonize β-adrenergic receptors..."

**Complex Summaries (3+ components with hierarchy):**
- Use numbered list with sub-bullets for readability
- Main points: Manual numbering (1. 2. 3.)
- Sub-details: `style='List Bullet 2'`
- NO "Summary:" label
- Example:
  ```python
  summary_intro = doc.add_paragraph('Regulation involves multiple mechanisms:')
  summary_intro.paragraph_format.space_before = Pt(0)
  summary_intro.paragraph_format.space_after = Pt(0)
  summary_intro.paragraph_format.line_spacing = 1.5
  summary_intro.runs[0].font.name = 'Calibri'
  summary_intro.runs[0].font.size = Pt(12)

  # Item 1 with manual numbering
  p1 = doc.add_paragraph()
  p1.add_run('1. ').bold = True
  p1.add_run('Neural regulation')
  # Word default: number at 0", text at 0.25"
  p1.paragraph_format.left_indent = Inches(0.25)
  p1.paragraph_format.first_line_indent = Inches(-0.25)  # Hanging indent
  p1.paragraph_format.space_before = Pt(0)
  p1.paragraph_format.space_after = Pt(0)
  p1.paragraph_format.line_spacing = 1.5

  sub1 = doc.add_paragraph('Parasympathetic increases motility', style='List Bullet')
  # Word default: bullet at 0.25", text at 0.5"
  sub1.paragraph_format.left_indent = Inches(0.5)
  sub1.paragraph_format.first_line_indent = Inches(-0.25)  # Hanging indent
  sub1.paragraph_format.space_before = Pt(0)
  sub1.paragraph_format.space_after = Pt(0)
  sub1.paragraph_format.line_spacing = 1.5

  sub2 = doc.add_paragraph('Sympathetic decreases motility', style='List Bullet')
  sub2.paragraph_format.left_indent = Inches(0.5)
  sub2.paragraph_format.first_line_indent = Inches(-0.25)  # Hanging indent
  sub2.paragraph_format.space_before = Pt(0)
  sub2.paragraph_format.space_after = Pt(0)
  sub2.paragraph_format.line_spacing = 1.5
  ```

**Decision Criteria (USE THIS FOR EVERY LO):**

**Numbered List Format Required When:**
- 3+ distinct components (e.g., "four primary functions", "three regulatory mechanisms")
- 3+ steps/stages (e.g., "three phases of digestion")
- 3+ layers/structures (e.g., "four layers of the GI tract wall")
- Hierarchical structure (main points with sub-details)

**Paragraph Format Required When:**
- 1-2 concepts explained cohesively
- Single mechanism or process
- Definition or simple explanation

**Critical:** DO NOT default to paragraph format. Analyze each LO answer and count components BEFORE choosing format.

**Examples:**

❌ **WRONG** - Should be numbered (4 functions listed):
```python
add_summary_simple(doc, 'The GI system performs motility, secretion, digestion, and absorption.')
```

✅ **CORRECT** - Numbered list (4 functions):
```python
add_summary_structured(doc,
    'The GI system performs four primary functions:',
    [
        {'main': 'Motility - muscular contractions moving contents'},
        {'main': 'Secretion - release of enzymes and fluids'},
        {'main': 'Digestion - breakdown of macronutrients'},
        {'main': 'Absorption - uptake of nutrients'}
    ]
)
```

✅ **CORRECT** - Paragraph (1 concept):
```python
add_summary_simple(doc,
    'Beta blockers reduce heart rate and blood pressure by blocking β-adrenergic receptors.')
```

**General Requirements:**
- Answer ALL parts of the learning objective
- Use source information only (no external facts)
- Synthesize source content into coherent answer

**Table Data:**
- Create comparison tables for 2+ similar items
- Use categories from template (Mechanism, Presentation, Treatment, Function, etc.)
- All data extracted from source only
- Include all rows/columns needed to answer LO

**Clinical Pearls:**
- Use medical reasoning (not just restating facts)
- "If X think Y" clinical associations
- Diagnostic tips, common mistakes, red flags
- Transform source facts into clinical insights

**Example transformation:**
- Source fact: "PNS increases intestinal contraction"
- Clinical pearl: "Vagal stimulation during eating initiates intestinal motility. Think parasympathetic = 'rest and digest'"

**Table Cell Formatting for Multiple Items:**

When a cell contains 3+ distinct items, use bullets with line breaks for readability:

```python
# Instead of: 'Metoprolol, Atenolol, Bisoprolol, Esmolol'
# Use bullets with line breaks:
cell_text = "• Metoprolol\n• Atenolol\n• Bisoprolol\n• Esmolol"
set_cell_text(cells[1], cell_text)
```

**Guidelines:**
- 1-2 items: Comma-separated acceptable (e.g., "Metoprolol, Atenolol")
- 3+ items: Use bullets with line breaks for scannability
- Example with arrows: `"• ↑ Motility\n• ↑ Secretion\n• ↑ Blood flow"`

**Key Comparisons Section:**
- Extract side-by-side comparison data for commonly confused items
- Focus on differential diagnosis points
- Use appropriate color scheme (rotate through color sets)
- **Heading format:** Use descriptive title ONLY (e.g., `'Segmentation vs Peristalsis'`)
- **DO NOT** add "Comparison 1:", "Comparison 2:" prefixes to headings
- Example: `doc.add_heading('Cardioselective vs Non-Selective Beta Blockers', 2)` ✅
- NOT: `doc.add_heading('Comparison 1: Cardioselective vs Non-Selective Beta Blockers', 2)` ❌

**Save and Execute Python:**

1. Save the generated Python script:
   - Path: `[Class]/[Exam]/Claude Study Tools/py/[OutputFilename].py`
   - Use Write tool to save complete generated script

2. Execute the Python script:
   ```bash
   python3 "[full absolute path to saved script]"
   ```

3. Verify:
   - Python executes without errors
   - Word document created at expected location
   - Document has all sections populated with content

<template-compliance>
MANDATORY TEMPLATE REQUIREMENTS - Word Learning Objectives:

STRUCTURE:
- Page 1: Title + Table of Contents (clickable links to LOs, no subtitle)
- Page 2+: Learning Objectives (NO section heading - starts with LO 1)
  - Each LO with: Summary (NO "Summary:" label) + Clinical Pearls (plain bullets) + Tables links
  - NO page break between LOs (continuous flow with spacing)
  - Each LO has bookmark for TOC linking and back-links from tables
- Reference Tables section (NEW): All tables grouped by LO
  - Section heading "Reference Tables"
  - Subsection headings "Learning Objective X"
  - Each table has title with "LO X" hyperlink
  - Tables support line breaks (\n) and bullet points in cells
- Key Comparisons section: Comparison tables for 2+ similar items
  - Section heading "Key Comparisons" (stays after Reference Tables)

FORMATTING (MANDATORY):
- Font: Calibri size 12 (11 for dense tables)
- Table style: 'Table Grid'
- Margins: 0.8 inches all sides
- Headings: Purple (118, 75, 162)
- Table headings: NO "TABLE 1:", "TABLE 2:" prefixes (descriptive titles only)
- Table headers: Bold, colored background (pastel)
- Table data cells: Black text, white background
- TOC links: Blue (0563C1), underlined
- Clinical Pearls: Plain bullets (NO colored box)
- NO "Summary:" label before summaries
- Summaries: Use numbered list format when answer lists 3+ components/layers/functions/mechanisms
- Spacing: 1 line space within LO sections (natural paragraph spacing), 2 line spaces between LOs
- Bidirectional linking: Forward to tables (→), back to LOs (←)
</template-compliance>

### Step 5: Use TodoWrite

Track your progress:
- Create todo for each learning objective
- Mark in_progress as you work
- Mark completed when done
- Keep user informed

### Step 6: Post-Creation Template Compliance Verification

**MANDATORY - Verify EACH requirement before reporting complete:**

**Structure Compliance:**
☐ Page 1: Title + clickable Table of Contents (no subtitle)
☐ Page 2+: Learning Objectives (NO "Learning Objectives" section heading)
☐ Each LO has: Bookmark + Summary (NO "Summary:" label) + Clinical Pearls (plain bullets) + Tables links
☐ NO page break between LOs (continuous flow with spacing)
☐ Reference Tables section: "Reference Tables" heading + grouping headings "Learning Objective X"
☐ Each table has: Bookmark + Title + "LO X" hyperlink
☐ Key Comparisons section: Heading present + comparison tables (after Reference Tables)

**Formatting Compliance:**
☐ Font: Calibri size 12 (11 for dense tables)
☐ Table style: 'Table Grid'
☐ Margins: 0.8 inches all sides
☐ NO subtitle on page 1
☐ NO "Learning Objectives" section heading on page 2
☐ NO "Summary:" label before summaries
☐ Summaries use correct format based on answer structure:
  - 3+ components/layers/functions → numbered list (add_summary_structured)
  - 1-2 concepts → paragraph format (add_summary_simple)
☐ Structured summaries have proper indentation:
  - Numbered items: 0.25 inches left indent
  - Sub-bullets: 0.5 inches left indent
☐ Spacing: 1 line space within LO sections (NO extra doc.add_paragraph() calls), 2 line spaces between LOs
☐ NO "TABLE 1:", "TABLE 2:" prefixes on table headings
☐ TOC links: Blue (0563C1), underlined, clickable
☐ LO headings: Purple (118, 75, 162) with bookmarks
☐ Table headers: Bold, colored background (pastel)
☐ Table data cells: Black text, white background
☐ Clinical Pearls: Plain bullets (NO colored box)
☐ Table cells support line breaks (\n) and bullet points (lists)
☐ Bidirectional linking: Forward links (→ table titles) and back links (LO X) work

**Source Accuracy:**
☐ All info from source only
☐ External additions marked with asterisk (*)
☐ No page references in Word docs
☐ Learning objective STATEMENTS verbatim (not paraphrased)

**Completeness:**
☐ ALL learning objectives from source included
☐ All LOs answered (all parts)
☐ All comparisons created for 2+ similar items

**CRITICAL: If ANY check fails, FIX BEFORE reporting complete.**

**State: "Post-creation verification complete - all checks passed" or list issues found and fix them.**

### Step 7: Save Files

**Output Filename Rule:**
1. Strip file extension and common suffixes (`_text.txt`, `_extracted.txt`, etc.)
2. Strip course prefixes (`Micro_`, `Pharm_`, `Clinical_`, `Patho_`, etc.)
3. Replace underscores with spaces for readability
4. Extract lecture number and topic: `[Number] [Topic]` or just `[Topic]`
5. Preserve capitalization as-is (after underscore→space conversion)
6. Add appropriate extension: `.docx` for Word, `.py` for Python
7. NO template suffixes, NO title case normalization

**Examples:**
- `Micro_4 Intro to Virology_text.txt` → `4 Intro to Virology.docx`
- `Pharm_11 Beta Blockers_text.txt` → `11 Beta Blockers.docx`
- `Micro_4_Intro_To_Virology_text.txt` → `4 Intro To Virology.docx`
- `Micro_Basics Of Immunology_text.txt` → `Basics Of Immunology.docx`

**Batch Merge Naming:**
- Input: `Micro_4 Intro to Virology_text.txt` + `Micro_5 Viral Replication_text.txt`
- Output: `Lecture 4-5.docx`
- Format: `Lecture [min]-[max].docx` (based on lecture numbers found)

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[OutputFilename].docx`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[OutputFilename].py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully

### Step 8: LO Coverage Report (SINGLE MODE ONLY)

**Compare LOs included vs LO Inventory from Step 0.8:**

1. Count LOs actually included in the Word guide
2. Compare against inventory list from Step 0.8
3. Calculate coverage percentage
4. Identify any missing LOs

**MANDATORY OUTPUT:**
```
---
LO COVERAGE REPORT
Source LOs: [N] (from inventory)
Included LOs: [M]
Coverage: [M/N] ([percentage]%)

[If 100%]: ✓ All learning objectives from source included.
[If <100%]: ⚠️ MISSING LOs: [list missing LO numbers and statements]
---
```

**If coverage < 100%:** Fix immediately before completing. Add missing LOs to document.

---

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

---

## Common Mistakes to Avoid

❌ Paraphrasing learning objective statements (must be verbatim)
❌ Missing page breaks between learning objectives
❌ Using wrong box colors (e.g., using purple for Clinical Pearls)
❌ Missing sections (must have all 3 sections)
❌ Adding external medical information not in source

---

## Template Compliance Examples

### CORRECT Implementation:

**Structure:**
✓ 2 sections: Learning Objectives, Key Comparisons
✓ Each LO has Summary, Tables, Pearls Box
✓ Page break after each learning objective
✓ Comparison tables for similar conditions (Type I vs Type II diabetes)

**Formatting:**
✓ Clinical Pearls box: Teal title (0, 77, 64), #E0F2F1 background
✓ High-Yield box: Purple title (118, 75, 162), #F3E5F5 background
✓ Section headings: Purple (118, 75, 162)
✓ Font: Calibri size 12

**Learning Objective Statements:**
✓ Source: "1. Describe the mechanism of action of beta-blockers"
✓ Guide:  "1. Describe the mechanism of action of beta-blockers"
✓ Status: VERBATIM - correct

### INCORRECT Implementation:

**Structure:**
✗ Only 1 section (missing Key Comparisons)
✗ No page breaks between learning objectives
✗ No comparison tables for similar items

**Formatting:**
✗ Clinical Pearls box using purple instead of teal ← WRONG
✗ All boxes same color ← WRONG
✗ Random colors not matching template ← WRONG
✗ Section headings in black instead of purple ← WRONG
✗ Font: Arial instead of Calibri ← WRONG

**Learning Objective Statements:**
✗ Source: "1. Describe the mechanism of action of beta-blockers"
✗ Guide:  "1. Explain how beta-blockers work"
✗ Status: PARAPHRASED - must use exact wording from source

---

## Example Usage

### Single File:
```
/LO-word "Pharmacology/Exam 3/Extract/Pharm_42 Beta Blockers_text.txt"
```
Creates: `42 Beta Blockers.docx`

### Batch Separate (N files → N outputs):
```
/LO-word "Micro_4 Intro to Virology_text.txt;Micro_5 Viral Replication_text.txt;Micro_6 Viral Pathogenesis_text.txt"
```
Creates 3 separate Word files:
- `4 Intro to Virology.docx` (only Lecture 4 content)
- `5 Viral Replication.docx` (only Lecture 5 content)
- `6 Viral Pathogenesis.docx` (only Lecture 6 content)

Uses batch-separate-processor agent with architectural isolation.

### Batch Merge (N files → 1 merged output):
```
/LO-word --merge "Micro_4 Intro to Virology_text.txt;Micro_5 Viral Replication_text.txt;Micro_6 Viral Pathogenesis_text.txt"
```
Creates 1 merged Word file:
- `Lecture 4-6.docx` (all 3 lectures merged)
- `Lecture 4-6_merge_report.md` (source traceability)

Uses batch-merge-orchestrator agent with intelligent merge and overlap resolution.
