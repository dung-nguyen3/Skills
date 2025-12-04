# Path Reference Guide

Quick reference for all important paths in your setup.

## Skills Repository (Claude Code Infrastructure)

**Base path:**
```
/Users/kimnguyen/Documents/Github/Skills
```

### Key Directories

**Commands:**
```
/Users/kimnguyen/Documents/Github/Skills/.claude/commands/
```

**Agents:**
```
/Users/kimnguyen/Documents/Github/Skills/.claude/agents/
```

**Skills:**
```
/Users/kimnguyen/Documents/Github/Skills/.claude/skills/
```

**Hooks:**
```
/Users/kimnguyen/Documents/Github/Skills/.claude/hooks/
```

**Mnemonic Cache:**
```
/Users/kimnguyen/Documents/Github/Skills/.claude/mnemonic-cache/
```

**Templates:**
```
/Users/kimnguyen/Documents/Github/Skills/study-guides/templates-and-examples/
```

**Python Examples:**
```
/Users/kimnguyen/Documents/Github/Skills/study-guides/templates-and-examples/Python_Examples/
```

---

## Study Materials (CloudDocs)

**Base path:**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3
```

### Pharmacology 3

**Course folder:**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3
```

**Source files (example):**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/
```

**Study guides output:**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Claude Study Tools/
```

**Reference files:**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Pharmacology_Master_Reference.xlsx
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/QUICK_ACCESS_Pharmacology.md
```

### Clinical Medicine 3

**Course folder:**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Clinical Medicine 3
```

**Source files (example):**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Clinical Medicine 3/Exam 1/Extract/
```

**Study guides output:**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Clinical Medicine 3/Exam 1/Claude Study Tools/
```

**Reference files:**
```
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Clinical Medicine 3/Clinical_Medicine_Master_Reference.xlsx
/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Clinical Medicine 3/QUICK_ACCESS_Clinical_Medicine.md
```

---

## Quick Copy/Paste Templates

### For Commands (Copy exactly as shown)

**Create all formats from source file:**
```
/create-all "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/HIV_Drugs.txt"
```

**Create all formats from directory:**
```
/create-all "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/"
```

**Check batch status for specific directory:**
```
/batch-status "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/"
```

**Check batch status for all courses:**
```
/batch-status --all
```

**View mnemonic cache statistics:**
```
/mnemonic-cache stats
```

**List cached mnemonics:**
```
/mnemonic-cache list
```

**Clean expired cache entries:**
```
/mnemonic-cache clean
```

**Resume failed batch:**
```
/error-recovery-resume
```

**Verify study guide accuracy:**
```
/verify-accuracy "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Claude Study Tools/HIV_Drug_Chart.xlsx" "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/HIV_Drugs.txt"
```

**Individual format commands:**
```
/4-tab-excel "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/HIV_Drugs.txt"

/LO-word "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/HIV_Drugs.txt"

/anki "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/HIV_Drugs.txt"

/word-excel-anki "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Extract/HIV_Drugs.txt"
```

### For Terminal (Python Scripts)

**Manual consolidation:**
```bash
cd /Users/kimnguyen/Documents/Github/Skills
python3 study-guides/templates-and-examples/Python_Examples/Auto_Consolidate_Master_Charts.py \
  "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Claude Study Tools/HIV_Drug_Chart.xlsx" \
  "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Pharmacology_Master_Reference.xlsx"
```

**Manual QUICK_ACCESS generation:**
```bash
cd /Users/kimnguyen/Documents/Github/Skills
python3 study-guides/templates-and-examples/Python_Examples/Generate_Quick_Access_Index.py \
  "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/" \
  "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/QUICK_ACCESS_Pharmacology.md"
```

**Manual post-processing:**
```bash
cd /Users/kimnguyen/Documents/Github/Skills
python3 .claude/agents/post-processing-automation-runner.py \
  "/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Quarter 3/Pharmacology 3/Exam 1/Claude Study Tools/HIV_Drug_Chart.xlsx"
```

---

## Shortened Versions (Terminal Aliases)

You can create aliases in `~/.zshrc` or `~/.bashrc`:

```bash
# Base paths
export SKILLS_DIR="/Users/kimnguyen/Documents/Github/Skills"
export MIDWESTERN_DIR="/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern"
export QUARTER3_DIR="$MIDWESTERN_DIR/Quarter 3"
export PHARM3_DIR="$QUARTER3_DIR/Pharmacology 3"
export CLIN3_DIR="$QUARTER3_DIR/Clinical Medicine 3"

# Then use like:
# cd $SKILLS_DIR
# ls "$PHARM3_DIR/Exam 1/Extract/"
```

Add to shell config:
```bash
echo 'export SKILLS_DIR="/Users/kimnguyen/Documents/Github/Skills"' >> ~/.zshrc
echo 'export MIDWESTERN_DIR="/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern"' >> ~/.zshrc
echo 'export QUARTER3_DIR="$MIDWESTERN_DIR/Quarter 3"' >> ~/.zshrc
echo 'export PHARM3_DIR="$QUARTER3_DIR/Pharmacology 3"' >> ~/.zshrc
echo 'export CLIN3_DIR="$QUARTER3_DIR/Clinical Medicine 3"' >> ~/.zshrc
source ~/.zshrc
```

---

## Pro Tips

1. **Tab completion:** Start typing path and press Tab
2. **Drag & drop:** Drag file/folder from Finder to Terminal to paste path
3. **Copy path:** Right-click file in Finder → Hold Option → "Copy [filename] as Pathname"
4. **Recent paths:** Terminal remembers recent `cd` commands (use arrow up)

---

## Path Pattern Detection

The post-processing automation agent automatically detects:

**Pharmacology pattern:**
- Any path containing "Pharmacology" followed by optional number
- Examples: "Pharmacology 3", "Pharmacology 4", "Pharmacology"

**Clinical Medicine pattern:**
- Any path containing "Clinical Medicine" followed by optional number
- Examples: "Clinical Medicine 3", "Clinical Medicine 4"

**Works for any quarter:**
- Quarter 3, Quarter 4, Quarter 5, etc.
- Each quarter gets its own reference files automatically
