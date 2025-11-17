# Claude Memory - HTML Learning Objects Workspace

This file stores key learnings and rules for creating educational materials in this workspace.

## Last Updated
2025-11-01

---

## Recent Updates (2025-11-01)

### New Protocols Added to CLAUDE.md

1. **Pre-Creation Verification Checklist** (MANDATORY)
   - Must complete verification checklist BEFORE creating any study guide
   - Checklist includes: Source file, Instruction template, Source-only policy, Save location
   - Applies to EACH new study guide creation (not just first one)
   - If user says "do this for file 35", must complete full verification again

2. **Post-Creation Verification Protocol** (MANDATORY)
   - After creating ANY study guide, automatically re-analyze the document
   - Check 4 areas:
     - Source Accuracy (source-only, asterisks for external info, page references)
     - Template Compliance (structure, formatting, all required elements)
     - Completeness (all LOs answered, all comparisons, master chart complete)
     - Quality Checks (no incorrect groupings/merged cells, spelling, formatting, TodoWrite used)
   - Must state: "Post-creation verification complete" and report issues
   - Fix issues immediately if found

3. **Key Learnings from Gas Transport Study Guide (Lecture 37) - WORD DOCUMENT**
   - **Format**: Word document (.docx) using python-docx library
   - Successfully implemented all 4 tabs (Learning Objectives, Key Comparisons, Master Chart, High-Yield Summary)
   - Created 9 learning objectives with summaries, comparison tables, clinical pearls, mnemonics, and analogies
   - Included 30 topics in master chart with page references
   - Used soft pastel color scheme consistently (hex codes from template)
   - Added external critical information marked with asterisks (*)
   - Researched mnemonics for each learning objective
   - Template used: Word LO new.md

4. **Workflow Improvements**
   - TodoWrite tool must be used throughout creation process to track progress
   - Each file = new verification process (don't assume settings from previous file)
   - CLAUDE_MEMORY.md is reference file, updated only when user requests
   - Template instructions are comprehensive enough; memory file is supplementary

---

## HTML Learning Object Structure Rules

### 1. Learning Objective Format
- **Structure**: Learning objective → Summary answer → Comparison table charts directly below
- Each learning objective should have:
  1. The verbatim learning objective text
  2. A summary answer paragraph
  3. Comparison tables immediately following the summary
  4. Clinical pearls/high-yield boxes
  5. **Memory tricks/mnemonics** below each learning objective answer

### 2. Source Material Rules

#### STRICT SOURCE-ONLY for Medical Content:
- Use **ONLY** information from the source file for:
  - Medical facts and definitions
  - Clinical findings and exam techniques
  - Diagnostic criteria
  - Condition descriptions
  - Exam procedures
- **Always include page references** from source file

#### EXTERNAL KNOWLEDGE ALLOWED for Learning Aids:
- **Memory tricks and mnemonics** - Can use external knowledge even if not in source
- **Clinical pearls** - Can add practical tips related to source material
- **Must-know facts** - Can add high-yield educational tips if related to source
- **Study strategies** - Can add learning techniques to help memorization

### 3. Comparison Tables
- Create comparison tables when there are **2 or more** similar:
  - Conditions
  - Drugs
  - Categories
  - Exam findings
- Common comparison categories:
  - Age/Epidemiology
  - Risk Factors
  - Presentation
  - Diagnosis
  - Management
  - Complications
  - Laboratory values
  - Treatment

### 4. Color-Coded Boxes (for both HTML and Word docs)

**Box Types:**
1. **HIGH-YIELD BOXES** (`.high-yield-box`):
   - Testable facts
   - Exam questions
   - Must-memorize values
   - Distinguishing features
   - Key thresholds

2. **CLINICAL PEARLS** (`.clinical-pearl`):
   - Practical tips
   - Pitfalls to avoid
   - "If X think Y" associations
   - Clinical reasoning shortcuts

3. **CRITICAL/EMERGENCY** (`.critical-box`):
   - Emergencies
   - Never-miss diagnoses
   - Red flags
   - Urgent criteria

### 5. Highlighting Rules
- **Highlight SPARINGLY**
- Use highlights to make important details stand out from other text
- Focus on: buzz words, key distinguishing features, critical values

### 6. Memory Tricks/Mnemonics
- **MUST include** mnemonics and memory tricks below each learning objective answer
- These help with memorization and retention
- Can use external knowledge for these (not restricted to source file)

---

## Word Document Specifications

### Color Scheme - Soft Pastels
Use soft pastel colors for all tables and boxes (similar to Excel chart design):

**Table Header Colors:**
- Purple: `#D1C4E9` (RGB: 209, 196, 233)
- Green: `#C8E6C9` (RGB: 200, 230, 201)
- Blue: `#B3E5FC` (RGB: 179, 229, 252)
- Teal: `#B2DFDB` (RGB: 178, 223, 219)
- Orange: `#FFE0B2` (RGB: 255, 224, 178)
- Red: `#FFCDD2` (RGB: 255, 205, 210)
- Pink: `#F8BBD0` (RGB: 248, 187, 208)
- Light Purple: `#EDE7F6` (RGB: 237, 231, 246)

**Background Colors (lighter versions):**
- Light Purple: `#F3E5F5`
- Light Green: `#E8F5E9`
- Light Blue: `#E1F5FE`
- Light Teal: `#E0F2F1`
- Light Orange: `#FFF3E0`
- Light Red: `#FFEBEE`
- Light Pink: `#FCE4EC`

### When to Create Comparison Tables
Create comparison tables when there are **2 or more** similar:
- Conditions with overlapping presentations
- Drugs in the same class
- Categories or classifications
- Exam findings or techniques

### Table Formatting
- **Headers**: Bold white text on colored background
- **Row labels** (first column): Bold text on light colored background
- **Data cells**: Regular text on white background
- Font: Calibri, size 12pt (11pt for dense tables)
- Table style: 'Table Grid'

### Document Structure
1. **Tab 1: Learning Objectives**
   - Each objective with summary + comparison tables + clinical boxes + mnemonics

2. **Tab 2: Key Comparisons**
   - Side-by-side comparison tables for similar conditions

3. **Tab 3: Master Chart**
   - Comprehensive table of all conditions with key features

4. **Tab 4: High-Yield Summary**
   - Color-coded boxes with must-know information
   - Grouped by category (Anatomy, Emergency, Pearls, etc.)
   - Memory aids and mnemonics section

---

## HTML Specifications

### File Format
- Single HTML file
- All CSS inline in `<style>` block
- All JavaScript inline in `<script>` block
- Self-contained (works offline)
- Mobile-responsive

### Tab Structure
Use tabbed interface with:
- Learning Objectives tab
- Key Comparisons tab
- Master Chart tab
- High-Yield Summary tab

---

## Project-Specific Notes

### GU & Rectal Exam Study Guide
- Source file: `Physical Diagnosis/Exam 3/Extract/GU, Rectal.txt`
- Created both HTML and Word versions
- Key error learned: **Do NOT add external medical knowledge** (treatments, time windows, BPH, etc.)
- **DO add**: Memory tricks, mnemonics, clinical pearls for learning

### Important Violations to Avoid
From GU/Rectal project, these were **incorrectly added** (not in source):
- Treatment details (medications, dosages)
- Time windows (e.g., "6 hour window" for torsion)
- Disease classifications not mentioned (e.g., "primary syphilis")
- Specific lab values (e.g., "elevated PSA")
- Detailed pathophysiology beyond source images
- Risk factors not detailed in source

### Critical Error to Avoid
**INCOMPLETE COVERAGE OF CONDITIONS**: In the GU/Rectal study guide, many medical conditions/abnormalities from the source file were NOT included in the learning objectives section.

**Rule**: When creating learning objectives for medical exams:
1. **READ THE ENTIRE SOURCE FILE** to identify ALL conditions, abnormalities, and findings mentioned
2. **CREATE COMPREHENSIVE COMPARISON TABLES** that include EVERY condition from the source
3. **Don't just include the "main" conditions** - include ALL abnormalities, variants, and findings
4. **Cross-reference** the Master Chart with Learning Objectives to ensure completeness
5. **Include tables for**:
   - All abnormal findings (even if brief in source)
   - Normal variants vs pathology
   - Benign vs malignant conditions
   - Acute vs chronic presentations
   - All anatomical variants

---

## File Naming Conventions
- HTML: `[Topic]_Study_Guide.html`
- Word: `[Topic]_Study_Guide.docx`
- Source-verified: `[Topic]_SOURCE_ONLY.docx`
- Python scripts: `create_[description].py`

---

## Tools Used
- **Python libraries**: python-docx for Word document creation
- **HTML/CSS/JS**: Vanilla JavaScript, no frameworks
- **Colors**: Soft pastels for educational materials

---

## Summary Checklist

When creating educational materials:
- [ ] Use source file ONLY for medical facts
- [ ] Include page references for all source information
- [ ] Create comparison tables for 2+ similar items
- [ ] Add memory tricks/mnemonics (external knowledge OK)
- [ ] Add clinical pearls (external knowledge OK if related)
- [ ] Use soft pastel color scheme for Word docs
- [ ] Include all 4 tabs: Learning Objectives, Key Comparisons, Master Chart, High-Yield
- [ ] Highlight sparingly (buzz words only)
- [ ] Single-file HTML with inline CSS/JS
- [ ] Summary answer THEN comparison table within each learning objective

---

**End of Memory File**
