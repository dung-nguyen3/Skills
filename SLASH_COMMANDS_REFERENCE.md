# Slash Commands Reference

Complete list of all available slash commands in the Skills repository.

---

## Study Guide Commands

Location: `.claude/commands/`

### /word
**Purpose:** Create comprehensive Word study guide from source material
**Arguments:** Source file path (e.g., `Pharmacology/Exam 3/Extract/Lecture 42.txt`)
**Output:** `.docx` file in `[Class]/[Exam]/Claude Study Tools/`
**Best For:** Any medical topic with learning objectives

**What it creates:**
- Section 1: Learning Objectives (with tables, clinical pearls, mnemonics)
- Section 2: Key Comparisons (side-by-side comparison tables)
- Section 3: Master Chart (comprehensive overview table)
- Section 4: High-Yield Summary (color-coded boxes by category)

**Example:**
```
/word Pharmacology/Exam 3/Extract/Lecture 42.txt
```

---

### /excel
**Purpose:** Create comprehensive 4-tab Excel drug chart from pharmacology source material
**Arguments:** Source file path (e.g., `Pharmacology/Exam 3/Extract/HIV Drugs.txt`)
**Output:** `.xlsx` file in `[Class]/[Exam]/Claude Study Tools/`
**Best For:** Pharmacology drug charts (antibiotics, antivirals, cardiovascular drugs, etc.)

**What it creates:**
- Tab 1: Drug Details (drug class comparison tables)
- Tab 2: Key Comparisons (mechanisms, toxicities, uses, interactions)
- Tab 3: Master Chart (all drugs in one table)
- Tab 4: High-Yield & Pearls (clinical pearls, mnemonics, "If X Think Y")

**Example:**
```
/excel Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

---

### /html-LO
**Purpose:** Create interactive HTML learning objectives guide (works for ANY medical topic)
**Arguments:** Source file path (e.g., `Clinical Medicine/Exam 2/Extract/Cardiovascular-Disease.txt`)
**Output:** `.html` file in `[Class]/[Exam]/Claude Study Tools/`
**Best For:** ANY medical topic - pathophysiology, clinical medicine, physiology, procedures

**What it creates:**
- Tab 1: Learning Objectives (Q&A format answering each LO)
- Tab 2: Key Comparisons (focused 2-3 way comparison tables)
- Tab 3: Master Comparison Tables (complete differential diagnosis)
- Tab 4: Summary (high-yield pearls, mnemonics, "If X Think Y")

**Works for:**
- Cardiovascular disease
- Hematology conditions
- Immunology, Rheumatology
- Respiratory physiology
- Gastrointestinal pathophysiology
- ANY lecture with learning objectives

**Example:**
```
/html-LO Clinical Medicine/Exam 2/Extract/Cardiovascular-Disease.txt
```

---

### /html-drug
**Purpose:** Create interactive single-page HTML drug reference chart (pharmacology)
**Arguments:** Source file path (e.g., `Pharmacology/Exam 3/Extract/HIV Antivirals.txt`)
**Output:** `.html` file in `[Class]/[Exam]/Claude Study Tools/`
**Best For:** Quick mobile drug reference, offline study during rotations

**What it creates:**
- Tab 1: Drug Classes & Comparisons (key similarities/differences)
- Tab 2: Master Drug Chart (sortable by clicking headers)
- Tab 3: Quick Reference (first-line treatments, mnemonics)

**Features:**
- Offline-ready (single HTML file, no internet needed)
- Mobile-friendly responsive design
- Sortable tables
- Color-coded badges for routes, contraindications, drug choice

**Example:**
```
/html-drug Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

---

### /clinical
**Purpose:** Create clinical assessment guide for history-taking and physical examination
**Arguments:** Source file path and chief complaint (e.g., `"Clinical Medicine/Exam 1/Extract/Lower-Extremity.txt" "Leg Pain"`)
**Output:** `.html` file in `[Class]/[Exam]/Claude Study Tools/`
**Best For:** OSCE preparation, physical diagnosis courses, clinical rotations

**What it creates:**
- Complete HPI (OLDCAARTS) - exact patient questions in quotes
- Essential PMH, FH, SH - relevant history elements
- Focused ROS - checkbox format for all systems
- Detailed Physical Exam - inspection, palpation, specialized tests
- Differential diagnosis by onset pattern (Acute/Subacute/Chronic)
- Clinical decision trees ("If X, Think Y")

**Follows Medical History Card format exactly**

**Example:**
```
/clinical "Clinical Medicine/Exam 1/Extract/Lower-Extremity.txt" "Leg Pain"
```

---

### /biography
**Purpose:** Create memorable drug biography stories for easier memorization
**Arguments:** Source file path (e.g., `Pharmacology/Exam 3/Extract/HIV Drugs.txt`)
**Output:** Creative narrative study material
**Best For:** Making drug information memorable through storytelling

**Example:**
```
/biography Pharmacology/Exam 3/Extract/HIV Drugs.txt
```

---

### /anki
**Purpose:** Create comprehensive Anki flashcard deck (.apkg) from source material
**Arguments:** Source file path (e.g., `Pharmacology/Exam 3/Extract/HIV Drugs.txt`)
**Output:** `.csv` and `.apkg` files in `[Class]/[Exam]/Claude Study Tools/`
**Best For:** Spaced repetition study, active recall practice, exam preparation

**What it creates:**
- CSV file with Question,Answer format
- APKG file ready to import into Anki

**Flashcard Guidelines:**
- Simple, specific, unambiguous questions
- Single concept answers (3-15 words)
- Varied question types (What/Where/Which/How/Define/Describe)
- Comprehensive coverage of all source material
- Source-only content (no external information)

**Features:**
- Uses genanki library for native .apkg generation
- Preserves exact medical/technical terminology
- One fact per card for optimal learning
- Import directly into Anki via File -> Import

**Example:**
```
/anki Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

---

### /study-bundle
**Purpose:** Create multiple study guide formats from source in ONE efficient pass (Word LO + Excel Comparison + Anki)
**Arguments:** Source file path or directory (e.g., `Pharmacology/Exam 3/Extract/HIV Drugs.txt`)
**Output:** 3 files per source: `.docx`, `.xlsx`, `.apkg` in `[Class]/[Exam]/Claude Study Tools/`
**Best For:** Comprehensive study preparation, token-efficient multi-format generation

**What it creates:**
1. **Word LO Study Guide** - 4 sections with learning objectives, comparisons, master chart
2. **Excel Comparison Chart** - Side-by-side comparison tables with soft pastel colors
3. **Anki Flashcards** - Q&A cards with LO-filtering and exact terminology

**Token Efficiency:**
- Traditional: `/word` + `/excel-comparison` + `/anki` = ~97k tokens (reads source 3 times)
- Study Bundle: Reads source ONCE = ~62k tokens
- **Savings: ~35-40k tokens per source file**

**Features:**
- Uses multi-format-processor agent for true token efficiency
- Maintains exact terminology consistency across all formats
- Researches mnemonics once, uses in all formats
- Source-only policy enforced across all outputs
- Auto-consolidate master charts (optional)
- QUICK_ACCESS.md index generation (optional)

**Modes:**
```bash
# Single file (creates 3 outputs)
/study-bundle "HIV_Drugs.txt"

# Batch separate (N files → N×3 outputs)
/study-bundle "HIV.txt;Antibiotics.txt;Antivirals.txt"

# Batch merge (N files → 3 merged outputs)
/study-bundle --merge "HIV-Lec1.txt;HIV-Lec2.txt;HIV-Lec3.txt"

# Directory input (processes all .txt files)
/study-bundle "Pharmacology/Exam 3/Extract/"
```

**When to use:**
- ✅ Want Word + Excel + Anki from same source
- ✅ Need comprehensive study materials for exams
- ✅ Want to maximize token efficiency
- ✅ Studying pharmacology (memorization + understanding + comparisons)

**When NOT to use:**
- ❌ Only need ONE format (use individual commands)
- ❌ Need specialized formats (HTML, clinical guide, biography)
- ❌ Need full 4-tab Excel drug chart (use `/excel` instead of comparison chart)

**Course-Specific Defaults:**
- Pharmacology: Word + Excel Comparison + Anki (default)
- Pathophysiology: Word + Excel Comparison (no Anki)
- Clinical Medicine: Word + HTML-LO (quick reference)
- See `.claude/format-defaults.json` for all course mappings

**Example:**
```
/study-bundle Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

**Output:**
```
Claude Study Tools/
├── HIV_Antivirals_Study_Guide.docx     (12 pages, 8 LOs)
├── HIV_Antivirals_Comparison_Chart.xlsx (5 comparison tables)
└── HIV_Antivirals_Flashcards.apkg       (47 cards)
```

---

### /verify-accuracy
**Purpose:** Deep accuracy analysis of existing study guide against source file
**Arguments:** Study guide file path, Source file path
**Output:** Fixed study guide + analysis report
**Best For:** Double-checking before exams, verifying after manual edits, checking source synchronization

**What it does:**
1. Reads entire source file
2. Reads entire study guide
3. Runs systematic 6-step verification (names, classifications, merged cells, info accuracy, format, emojis)
4. Documents all issues found (Critical/Important/Minor)
5. Fixes ALL issues automatically
6. Re-verifies entire file (mandatory)
7. States "Re-verification complete"

**Use when:**
- Before exam (verify everything is accurate)
- After manual edits
- Source file was updated
- Want 100% confidence in accuracy

**Example:**
```
/verify-accuracy "Claude Study Tools/HIV_Drug_Chart.xlsx" "Extract/HIV Drugs.txt"
```

---

## Quick Command Selection Guide

### For Study Guides:

| Your Content Type | Use This Command |
|-------------------|------------------|
| Pharmacology drugs (need Excel) | `/excel` |
| Pharmacology drugs (need HTML for mobile) | `/html-drug` |
| ANY medical topic with learning objectives | `/html-LO` |
| Clinical history & physical exam | `/clinical` |
| Need Word document format | `/word` |
| Drug stories (memorable narratives) | `/biography` |
| Anki flashcards for spaced repetition | `/anki` |
| Verify existing study guide | `/verify-accuracy` |

### For Development Work:

| Your Task | Use This Command |
|-----------|------------------|
| Plan complex feature/refactoring | `/dev-docs` |
| Update docs mid-project | `/dev-docs-update` |
| Research API routes for testing | `/route-research-for-testing` |

---

## Tips for Using Slash Commands

### 1. Always Use Absolute or Relative Paths
```bash
# Good:
/excel Pharmacology/Exam 3/Extract/HIV Drugs.txt

# Bad:
/excel HIV Drugs.txt  # Might not find file
```

### 2. Quote Paths with Spaces
```bash
# Good:
/clinical "Clinical Medicine/Exam 1/Extract/Lower Extremity.txt" "Leg Pain"

# Bad:
/clinical Clinical Medicine/Exam 1/Extract/Lower Extremity.txt Leg Pain
```

### 3. Let Commands Handle Templates
- Slash commands automatically load the correct template
- No need to paste template separately
- Saves ~695-1,144 lines of context

### 4. Commands Include Verification
- All study guide commands include pre-creation verification checklist
- All include post-creation verification
- `/verify-accuracy` does deep 6-step analysis

### 5. Batch Processing with Context Isolation
- All study guide commands support batch mode (semicolon-separated files)
- Each file is processed independently with explicit context isolation
- Verification runs for EACH file (not just once at start)
- Prevents information contamination between files
- Example: `/excel "HIV.txt;COVID.txt;Antibiotics.txt"` creates 3 separate Excel files
- Each file gets complete verification and post-creation checks

### 6. Use Tab Completion
- Type `/` then press Tab
- VS Code will show available commands

---

## File Locations

**Study guide commands:**
```
.claude/commands/
├── word.md
├── excel.md
├── html-LO.md
├── html-drug.md
├── clinical.md
├── biography.md
├── anki.md
└── verify-accuracy.md
```

---

## Related Documentation

- **How to Use Study Guides:** `study-guides/user-docs/HOW_TO_USE.md`
- **Study Guide System Overview:** `study-guides/README.md`
- **Repository Structure:** `CLAUDE.md`
- **Templates:** `study-guides/templates-and-examples/`

---

## Getting Help

**Command not working?**
```bash
# Check if command file exists
ls .claude/commands/word.md

# Verify you're in the right directory
pwd
```

**Need more detail on a specific command?**
```bash
# Read the full command file
cat .claude/commands/excel.md
```

**Want to customize a command?**
- Commands are just markdown files
- Edit the `.md` file in `.claude/commands/`
- Changes take effect immediately

---

**Last Updated:** 2025-11-21
**Total Commands:** 11 (8 study guide + 3 infrastructure)
