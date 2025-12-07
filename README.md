# Skills Repository - Quick Commands Reference

Pharmacy study guide generation system using Claude Code.

---

## Study Guide Commands

All commands support **single**, **batch separate**, and **batch merge** modes:

### Word Study Guide

```bash
# Single file
/LO-word "lecture.txt"

# Single directory
/LO-word "/path/to/directory"

# Batch separate (N files → N outputs)
/LO-word "lec1.txt;lec2.txt;lec3.txt"

# Batch merge (N files → 1 merged output)
/LO-word --merge "lec1.txt;lec2.txt;lec3.txt"

# Batch merge with directories
/LO-word --merge "/path/to/dir1;/path/to/dir2"
```

### Excel Drug Chart

```bash
# Single file
/drugs-3-tab-excel "drugs.txt"

# Single directory (auto-finds all .txt)
/drugs-3-tab-excel "/path/to/Extract"

# Batch separate
/drugs-3-tab-excel "HIV.txt;Antibiotics.txt"

# Batch merge (intelligent merge with overlap resolution)
/drugs-3-tab-excel --merge "HIV-PIs.txt;HIV-NRTIs.txt"

# Batch merge with directories
/drugs-3-tab-excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```

### Excel Comparison Chart (Any Medical Topic)

```bash
# Single file
/key-comparisons-excel "Hypersensitivity.txt"

# Single directory
/key-comparisons-excel "/path/to/Extract"

# Batch separate
/key-comparisons-excel "TypeI.txt;TypeII.txt;TypeIII.txt"

# Batch merge (creates comprehensive comparison)
/key-comparisons-excel --merge "Mechanisms.txt;Clinical.txt;Treatment.txt"

# Batch merge with directories
/key-comparisons-excel --merge "/path/to/dir1;/path/to/dir2"
```

Creates 3-tab comparison chart: Key Comparisons, Master Chart, Summary

### Excel Master Chart (Quick Reference - Single Sheet)

```bash
# Single file
/master-chart-excel "drugs.txt"

# Single directory
/master-chart-excel "/path/to/Extract"

# Batch separate
/master-chart-excel "HIV.txt;Antibiotics.txt"

# Batch merge
/master-chart-excel --merge "HIV.txt;Hepatitis.txt;Herpes.txt"
```

Creates single-sheet Master Chart with user-defined columns. Flexible for drugs, conditions, or labs.

### HTML Learning Objectives Guide

```bash
# Single file
/LO-html "lecture.txt"

# Directory mode
/LO-html "/path/to/directory"

# Batch merge with directories
/LO-html --merge "/path/to/dir1;/path/to/dir2"
```

### HTML Drug Reference (Mobile)

```bash
# Single file
/drugs-html "drugs.txt"

# Directory mode
/drugs-html "/path/to/directory"

# Batch merge with directories
/drugs-html --merge "/path/to/dir1;/path/to/dir2"
```

### Clinical Assessment Guide

```bash
# Single file
/clinical-assessment-html "source.txt" "Chief Complaint"

# Single directory (auto-finds all .txt files)
/clinical-assessment-html "/path/to/Extract" "Back Pain"

# Batch merge (analyzes multiple files for one chief complaint)
/clinical-assessment-html --merge "Lower-Back.txt;Spine.txt;Neuro.txt" "Back Pain"

# Batch merge with directories
/clinical-assessment-html --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt" "Back Pain"
```

### Drug Biography Stories

```bash
/autobiography-trick "path/to/drugs.txt"
```

### Anki Flashcard Deck

```bash
/anki "path/to/source.txt"
```

---

## Multi-Format Study Bundles

### Word + Excel + Anki Bundle

```bash
# Single file (creates 3 formats)
/word-excel-anki "HIV_Drugs.txt"

# Directory mode (smart tracking - skips already-processed files)
/word-excel-anki "/Users/kimnguyen/.../Clinical Medicine 3/Exam 1"

# Batch separate (N files → N×3 study guides)
/word-excel-anki "file1.txt;file2.txt;file3.txt"
```

Creates: Word LO Study Guide + Excel Comparison Chart + Anki Flashcards

**Token efficiency:** ~35-40k tokens saved vs running 3 separate commands

### Interactive Study Guide Creator

```bash
# Interactive mode - choose which formats to create
/study-guides "HIV_Drugs.txt"

# Directory mode with smart tracking
/study-guides "/Users/kimnguyen/.../Pharmacology 3/Exam 2"

# Batch mode with formats pre-specified
/study-guides "file1.txt;file2.txt" "word,excel-comparison,anki"
```

**Available formats:**
- `word` - Word LO study guide
- `excel-4tab`, `excel-comparison`, `excel-master`, `excel-clinical` - Excel charts
- `anki` - Anki flashcards
- `html-lo`, `html-drugs`, `html-clinical` - HTML guides
- `biography` - Drug autobiography stories

**Quick bundles:**
- `comprehensive` - All formats
- `study-bundle` - Core 3 (word, excel-comparison, anki)
- `quick-reference` - Fast lookup (excel-master, html-lo)
- `memorization` - Memory-focused (anki, biography)

### Full Workflow Orchestrator

```bash
# All default formats for the course (auto-detected from path)
/create-all "HIV_Drugs.txt"

# Custom format selection
/create-all "Beta_Blockers.txt" --formats word,excel-4tab,anki,biography

# With post-creation verification
/create-all "ACE_Inhibitors.txt" --verify

# Directory mode with smart tracking
/create-all "/Users/kimnguyen/.../Pharmacology 3/Exam 2/Extract"
```

**Features:**
- Auto-detects course from path (Pharmacology vs Clinical Medicine)
- Uses course-specific format defaults
- Auto-consolidates master charts per quarter
- Auto-generates QUICK_ACCESS index
- Optional accuracy verification (--verify)

---

## Automation & Utilities

### Batch Status Tracker

```bash
# Check single directory
/batch-status "/Users/kimnguyen/.../Pharmacology 3/Exam 2/Extract"

# Check multiple directories
/batch-status "Exam2/Extract;Exam3/Extract"

# Check all directories
/batch-status --all
```

Shows processed/pending/failed files with completion percentages.

### Error Recovery

```bash
# Auto-resume from last checkpoint
/error-recovery-resume

# Retry specific files
/error-recovery-resume "Beta_Blockers.txt;ACE_Inhibitors.txt"
```

**Features:**
- Exponential backoff retry (2s, 4s, 8s delays)
- Circuit breaker after 3 consecutive failures
- Preserves completed work
- Token savings: ~48k per skipped file

### Mnemonic Cache

```bash
# View cache statistics
/mnemonic-cache stats

# Clean expired entries
/mnemonic-cache clean

# List cached mnemonics
/mnemonic-cache list [topic]

# Lookup specific mnemonic
/mnemonic-cache lookup "ACE inhibitors" "toxicity"
```

**Token savings:** ~5k per cache hit after first WebSearch

---

## Verification

### Verify Study Guide Accuracy

```bash
/verify-accuracy "path/to/study-guide.xlsx" "path/to/source.txt"
```

---

## Batch Processing Modes

### Single Mode (1 file → 1 output)

```bash
/drugs-3-tab-excel "HIV_Drugs.txt"
```

Standard single-file processing.

### Directory Mode (auto-finds all .txt files with smart tracking)

```bash
/drugs-3-tab-excel "/path/to/Extract"
```

- Auto-discovers all `.txt` files in directory
- **Smart tracking:** Uses `.processed_files.txt` to skip already-processed files
- **Re-run safe:** Only processes NEW files added to directory
- Processes in batch separate mode (1 output per file)
- Recursive search (finds files in subdirectories)

**Example workflow:**
```bash
# First run - processes all 10 files
/word-excel-anki "/Users/kimnguyen/.../Pharmacology 3/Exam 2/Extract"
# Creates 30 study guides (10 files × 3 formats)

# Add new file: Beta_Blockers.txt

# Second run - only processes new file
/word-excel-anki "/Users/kimnguyen/.../Pharmacology 3/Exam 2/Extract"
# Creates 3 study guides (1 new file × 3 formats)
# Skips 10 already-processed files
# Token savings: ~480k tokens
```

### Batch Separate (N files → N outputs)

```bash
/drugs-3-tab-excel "HIV.txt;Antibiotics.txt;Antivirals.txt"
```

- Creates separate output for each file
- Architectural isolation (zero cross-contamination)
- Uses `batch-separate-processor` agent

### Batch Merge (N files → 1 merged output)

```bash
/drugs-3-tab-excel --merge "HIV-PIs.txt;HIV-NRTIs.txt;HIV-NNRTIs.txt"
```

- Combines multiple files into one comprehensive output
- Intelligent overlap resolution
- Source traceability
- Creates merge report
- Uses `batch-merge-orchestrator` agent

### Batch Merge with Directories (N directories → 1 merged output)

```bash
/drugs-3-tab-excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```

- Auto-discovers all `.txt` files from multiple directories
- Merges all discovered files into 1 comprehensive output
- Ideal for combining content across multiple exam folders

**Clinical Example:**

```bash
/clinical-assessment-html --merge "Lower-Back.txt;Spine.txt;Neuro.txt" "Back Pain"
```

Analyzes all 3 files, extracts ONLY back pain info, creates 1 clinical guide.

**Clinical with Directories:**

```bash
/clinical-assessment-html --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt" "Back Pain"
```

Auto-finds all .txt files from both directories, filters for back pain content, creates 1 guide.

---

## Which Command Should I Use?

| Content Type | Command |
|--------------|---------|
| Pharmacology drugs (detailed Excel) | `/drugs-3-tab-excel` |
| Medical topic comparisons (Excel) | `/key-comparisons-excel` |
| Quick reference chart (single sheet) | `/master-chart-excel` |
| Pharmacology drugs (HTML/mobile) | `/drugs-html` |
| Drug stories (creative/memorable) | `/autobiography-trick` |
| Any medical topic (HTML) | `/LO-html` |
| Any medical topic (Word) | `/LO-word` |
| Clinical exams | `/clinical-assessment-html` |
| Flashcards | `/anki` |
| Verify existing guide | `/verify-accuracy` |

---

## Mnemonics

Mnemonics are automatically researched when creating study guides.

To research mnemonics manually: "Find mnemonics for [topic]"

---

## Full Documentation

- [QUICK_START.md](QUICK_START.md) - Complete interactive guide
- [SLASH_COMMANDS_REFERENCE.md](SLASH_COMMANDS_REFERENCE.md) - Detailed command docs
- [study-guides/user-docs/HOW_TO_USE.md](study-guides/user-docs/HOW_TO_USE.md) - Full usage guide

---

## Repository Structure

```
.claude/           # Claude infrastructure (commands, skills, hooks)
study-guides/      # Templates and documentation
```

See [CLAUDE.md](CLAUDE.md) for full repository details.
