# Slash Commands Reference

Complete list of all available slash commands in the Skills repository.

---

## Study Guide Commands

Location: `study-guides/.claude/commands/`

### /create-word
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
/create-word Pharmacology/Exam 3/Extract/Lecture 42.txt
```

---

### /create-excel
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
/create-excel Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

---

### /create-lo-guide
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
/create-lo-guide Clinical Medicine/Exam 2/Extract/Cardiovascular-Disease.txt
```

---

### /create-drug-html
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
/create-drug-html Pharmacology/Exam 3/Extract/HIV Antivirals.txt
```

---

### /create-clinical-guide
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
/create-clinical-guide "Clinical Medicine/Exam 1/Extract/Lower-Extremity.txt" "Leg Pain"
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

## Infrastructure Example Commands

Location: `infrastructure-examples/.claude/commands/`

### /dev-docs
**Purpose:** Create comprehensive strategic plan with structured task breakdown
**Arguments:** Describe what you need planned (e.g., "refactor authentication system", "implement microservices")
**Output:** Three markdown files:
- `[task]-plan.md` - Strategic plan
- `[task]-context.md` - Key decisions and files
- `[task]-tasks.md` - Checklist format

**Best For:** Complex development tasks, feature planning, refactoring strategies

**What it creates:**
- Executive summary
- Phase breakdown with tasks
- Technical decisions and rationale
- File locations and key code sections
- Actionable checklist format

**Example:**
```
/dev-docs refactor authentication system
```

---

### /dev-docs-update
**Purpose:** Update development documentation before context reset
**Arguments:** Task name or description
**Output:** Updated plan, context, and task files
**Best For:** Updating docs mid-project, capturing progress before session ends

**What it does:**
- Updates existing plan with current progress
- Adds new decisions to context
- Updates task checklist completion status
- Captures current state for next session

**Example:**
```
/dev-docs-update authentication refactor
```

---

### /route-research-for-testing
**Purpose:** Research route patterns for API testing
**Arguments:** None (analyzes current codebase)
**Output:** Comprehensive route analysis report
**Best For:** Understanding API structure, preparing for route testing

**What it creates:**
- List of all API routes
- Authentication requirements
- Request/response patterns
- Test data recommendations

**Example:**
```
/route-research-for-testing
```

---

## Quick Command Selection Guide

### For Study Guides:

| Your Content Type | Use This Command |
|-------------------|------------------|
| Pharmacology drugs (need Excel) | `/create-excel` |
| Pharmacology drugs (need HTML for mobile) | `/create-drug-html` |
| ANY medical topic with learning objectives | `/create-lo-guide` |
| Clinical history & physical exam | `/create-clinical-guide` |
| Need Word document format | `/create-word` |
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
# ✓ Good:
/create-excel Pharmacology/Exam 3/Extract/HIV Drugs.txt

# ✗ Bad:
/create-excel HIV Drugs.txt  # Might not find file
```

### 2. Quote Paths with Spaces
```bash
# ✓ Good:
/create-clinical-guide "Clinical Medicine/Exam 1/Extract/Lower Extremity.txt" "Leg Pain"

# ✗ Bad:
/create-clinical-guide Clinical Medicine/Exam 1/Extract/Lower Extremity.txt Leg Pain
```

### 3. Let Commands Handle Templates
- Slash commands automatically load the correct template
- No need to paste template separately
- Saves ~695-1,144 lines of context

### 4. Commands Include Verification
- All study guide commands include pre-creation verification checklist
- All include post-creation verification
- `/verify-accuracy` does deep 6-step analysis

### 5. Use Tab Completion
- Type `/create` then press Tab
- VS Code will show available commands

---

## File Locations

**Study guide commands:**
```
study-guides/.claude/commands/
├── create-word.md
├── create-excel.md
├── create-lo-guide.md
├── create-drug-html.md
├── create-clinical-guide.md
└── verify-accuracy.md
```

**Infrastructure commands:**
```
infrastructure-examples/.claude/commands/
├── dev-docs.md
├── dev-docs-update.md
└── route-research-for-testing.md
```

---

## Related Documentation

- **How to Use Study Guides:** `study-guides/user-docs/HOW_TO_USE.md`
- **Study Guide System Overview:** `study-guides/README.md`
- **Infrastructure Integration Guide:** `infrastructure-examples/CLAUDE_INTEGRATION_GUIDE.md`
- **Repository Structure:** `CLAUDE.md`

---

## Getting Help

**Command not working?**
```bash
# Check if command file exists
ls study-guides/.claude/commands/create-word.md

# Verify you're in the right directory
pwd
```

**Need more detail on a specific command?**
```bash
# Read the full command file
cat study-guides/.claude/commands/create-excel.md
```

**Want to customize a command?**
- Commands are just markdown files
- Edit the `.md` file in `.claude/commands/`
- Changes take effect immediately

---

**Last Updated:** 2025-11-19
**Total Commands:** 9 (6 study guide + 3 infrastructure)
