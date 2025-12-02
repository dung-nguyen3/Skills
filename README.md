# Skills Repository - Quick Commands Reference

Pharmacy study guide generation system using Claude Code.

---

## Study Guide Commands

All commands support **single**, **batch separate**, and **batch merge** modes:

### Word Study Guide

```bash
# Single file
/word "lecture.txt"

# Single directory
/word "/path/to/directory"

# Batch separate (N files → N outputs)
/word "lec1.txt;lec2.txt;lec3.txt"

# Batch merge (N files → 1 merged output)
/word --merge "lec1.txt;lec2.txt;lec3.txt"

# Batch merge with directories
/word --merge "/path/to/dir1;/path/to/dir2"
```

### Excel Drug Chart

```bash
# Single file
/excel "drugs.txt"

# Single directory (auto-finds all .txt)
/excel "/path/to/Extract"

# Batch separate
/excel "HIV.txt;Antibiotics.txt"

# Batch merge (intelligent merge with overlap resolution)
/excel --merge "HIV-PIs.txt;HIV-NRTIs.txt"

# Batch merge with directories
/excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```

### Excel Comparison Chart (Any Medical Topic)

```bash
# Single file
/excel comparison "Hypersensitivity.txt"

# Single directory
/excel comparison "/path/to/Extract"

# Batch separate
/excel comparison "TypeI.txt;TypeII.txt;TypeIII.txt"

# Batch merge (creates comprehensive comparison)
/excel comparison --merge "Mechanisms.txt;Clinical.txt;Treatment.txt"

# Batch merge with directories
/excel comparison --merge "/path/to/dir1;/path/to/dir2"
```

Creates 3-tab comparison chart: Key Comparisons, Master Chart, Summary

### Excel Master Chart (Quick Reference - Single Sheet)

```bash
# Single file
/excel master "drugs.txt"

# Single directory
/excel master "/path/to/Extract"

# Batch separate
/excel master "HIV.txt;Antibiotics.txt"

# Batch merge
/excel master --merge "HIV.txt;Hepatitis.txt;Herpes.txt"
```

Creates single-sheet Master Chart with user-defined columns. Flexible for drugs, conditions, or labs.

### HTML Learning Objectives Guide

```bash
# Single file
/html-LO "lecture.txt"

# Directory mode
/html-LO "/path/to/directory"

# Batch merge with directories
/html-LO --merge "/path/to/dir1;/path/to/dir2"
```

### HTML Drug Reference (Mobile)

```bash
# Single file
/html-drug "drugs.txt"

# Directory mode
/html-drug "/path/to/directory"

# Batch merge with directories
/html-drug --merge "/path/to/dir1;/path/to/dir2"
```

### Clinical Assessment Guide

```bash
# Single file
/clinical "source.txt" "Chief Complaint"

# Single directory (auto-finds all .txt files)
/clinical "/path/to/Extract" "Back Pain"

# Batch merge (analyzes multiple files for one chief complaint)
/clinical --merge "Lower-Back.txt;Spine.txt;Neuro.txt" "Back Pain"

# Batch merge with directories
/clinical --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt" "Back Pain"
```

### Drug Biography Stories

```bash
/biography "path/to/drugs.txt"
```

### Anki Flashcard Deck

```bash
/anki "path/to/source.txt"
```

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
/excel "HIV_Drugs.txt"
```

Standard single-file processing.

### Directory Mode (auto-finds all .txt files)

```bash
/excel "/path/to/Extract"
```

- Auto-discovers all `.txt` files in directory
- Processes in batch separate mode (1 output per file)
- Recursive search (finds files in subdirectories)

### Batch Separate (N files → N outputs)

```bash
/excel "HIV.txt;Antibiotics.txt;Antivirals.txt"
```

- Creates separate output for each file
- Architectural isolation (zero cross-contamination)
- Uses `batch-separate-processor` agent

### Batch Merge (N files → 1 merged output)

```bash
/excel --merge "HIV-PIs.txt;HIV-NRTIs.txt;HIV-NNRTIs.txt"
```

- Combines multiple files into one comprehensive output
- Intelligent overlap resolution
- Source traceability
- Creates merge report
- Uses `batch-merge-orchestrator` agent

### Batch Merge with Directories (N directories → 1 merged output)

```bash
/excel --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt"
```

- Auto-discovers all `.txt` files from multiple directories
- Merges all discovered files into 1 comprehensive output
- Ideal for combining content across multiple exam folders

**Clinical Example:**

```bash
/clinical --merge "Lower-Back.txt;Spine.txt;Neuro.txt" "Back Pain"
```

Analyzes all 3 files, extracts ONLY back pain info, creates 1 clinical guide.

**Clinical with Directories:**

```bash
/clinical --merge "/path/to/Exam2/Extract;/path/to/Exam4/Txt" "Back Pain"
```

Auto-finds all .txt files from both directories, filters for back pain content, creates 1 guide.

---

## Which Command Should I Use?

| Content Type | Command |
|--------------|---------|
| Pharmacology drugs (detailed Excel) | `/excel` |
| Medical topic comparisons (Excel) | `/excel comparison` |
| Quick reference chart (single sheet) | `/excel master` |
| Pharmacology drugs (HTML/mobile) | `/html-drug` |
| Drug stories (creative/memorable) | `/biography` |
| Any medical topic (HTML) | `/html-LO` |
| Any medical topic (Word) | `/word` |
| Clinical exams | `/clinical` |
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
