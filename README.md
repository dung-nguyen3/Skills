# Skills Repository - Quick Commands Reference

Pharmacy study guide generation system using Claude Code.

---

## Study Guide Commands

All commands support **single**, **batch separate**, and **batch merge** modes:

### Word Study Guide
```bash
# Single file
/word "lecture.txt"

# Batch separate (N files → N outputs)
/word "lec1.txt;lec2.txt;lec3.txt"

# Batch merge (N files → 1 merged output)
/word --merge "lec1.txt;lec2.txt;lec3.txt"
```

### Excel Drug Chart
```bash
# Single file
/excel "drugs.txt"

# Batch separate
/excel "HIV.txt;Antibiotics.txt"

# Batch merge (intelligent merge with overlap resolution)
/excel --merge "HIV-PIs.txt;HIV-NRTIs.txt"
```

### HTML Learning Objectives Guide
```bash
# Single file
/html-LO "lecture.txt"

# Batch modes available (use --merge for combined output)
```

### HTML Drug Reference (Mobile)
```bash
# Single file
/html-drug "drugs.txt"

# Batch modes available (use --merge for combined output)
```

### Clinical Assessment Guide
```bash
# Single file
/clinical "source.txt" "Chief Complaint"

# Batch merge (analyzes multiple files for one chief complaint)
/clinical --merge "Lower-Back.txt;Spine.txt;Neuro.txt" "Back Pain"
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
```
/verify-accuracy "path/to/study-guide.xlsx" "path/to/source.txt"
```

---

## Batch Processing Modes

### Single Mode (1 file → 1 output)
```bash
/excel "HIV_Drugs.txt"
```
Standard single-file processing.

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

**Clinical Example:**
```bash
/clinical --merge "Lower-Back.txt;Spine.txt;Neuro.txt" "Back Pain"
```
Analyzes all 3 files, extracts ONLY back pain info, creates 1 clinical guide.

---

## Which Command Should I Use?

| Content Type | Command |
|--------------|---------|
| Pharmacology drugs (Excel) | `/excel` |
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
