---
description: Interactive study guide creation - choose which formats to create
argument-hint: <source-file-or-directory> [formats separated by semicolons for batch mode]
---

Create study guides from: $ARGUMENTS

## Instructions

### Step 1: Parse Input

**Extract source file(s):**
- Check if $ARGUMENTS is directory, multiple files (semicolon), or single file
- Validate files exist

**Detect if formats already specified (batch mode):**
- If $ARGUMENTS contains format keywords after source path
- Example: "source.txt word,excel,anki" → formats already specified
- If no formats specified → Interactive mode

---

### Step 1.5: Handle Directory Input with Tracking

**If $ARGUMENTS is a directory path:**

**Step 1.5.1: Scan directory for source files**
```bash
# Find all .txt and .pdf files in directory
source_dir="$ARGUMENTS"
source_files=$(find "$source_dir" -maxdepth 1 -type f \( -name "*.txt" -o -name "*.pdf" \) | sort)
```

**Step 1.5.2: Check for processed files tracker**
```bash
# Read .processed_files.txt to get already-processed files
tracker_file="$source_dir/.processed_files.txt"

if [[ -f "$tracker_file" ]]; then
    mapfile -t processed_files < "$tracker_file"
else
    processed_files=()
fi
```

**Step 1.5.3: Filter to get NEW files only**
```bash
# Compare source files vs processed files
new_files=()

for file in $source_files; do
    basename=$(basename "$file")

    # Check if this file was already processed
    if ! printf '%s\n' "${processed_files[@]}" | grep -q "^$basename$"; then
        new_files+=("$basename")
    fi
done
```

**Step 1.5.4: Display tracking status**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIRECTORY MODE - SMART TRACKING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Directory: [source_dir]
Total source files: [N total]

Status:
  ✓ Already processed: [M files] (will skip)
  ⏳ New files to process: [K files]

[If M > 0]:
Previously processed files (skipping):
  1. [file1.txt]
  2. [file2.txt]
  ...

[If K > 0]:
New files to process:
  1. [new_file1.txt]
  2. [new_file2.txt]
  ...

[If K == 0]:
✅ All files already processed - nothing to do!
Run /batch-status to verify completion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**If no new files, exit early. Otherwise, continue with new files only.**

**Step 1.5.5: Update file list**
```python
# Replace source file list with NEW files only
source_files = new_files
file_count = len(new_files)
```

**If not directory mode, skip to Step 2.**

---

### Step 2: Interactive Format Selection (if not specified)

**If formats NOT in arguments, ask user:**

```
Which formats would you like to create?

Available Formats:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 WORD FORMATS:
  • word - Word LO study guide (learning objectives format)

📊 EXCEL FORMATS:
  • excel-4tab - 4-tab Excel drug chart (Drug Details, Key Comparisons, Master Chart, High-Yield)
  • excel-comparison - 3-tab Excel comparison chart (focused comparisons)
  • excel-master - Single-sheet Excel master chart (quick reference)
  • excel-clinical - 4-tab Excel clinical assessment chart (OLDCAARTS format)

🎴 FLASHCARD FORMATS:
  • anki - Anki flashcard deck (.apkg file)

🌐 HTML FORMATS:
  • html-lo - HTML learning objectives guide (interactive, 4 tabs)
  • html-drugs - HTML drug reference chart (pharmacology)
  • html-clinical - HTML clinical assessment guide (H&P format)

📖 SPECIALTY FORMATS:
  • biography - Drug autobiography stories (personified characters)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Course-Specific Recommendations:
  Pharmacology: word, excel-comparison, anki (memorization-focused)
  Clinical Medicine: word, html-lo (quick reference)
  Pathophysiology: word, excel-comparison (understanding-focused)

Quick Bundles:
  • comprehensive - All formats (word, excel-4tab, excel-comparison, anki, html-lo, biography)
  • study-bundle - Core 3 (word, excel-comparison, anki)
  • quick-reference - Fast lookup (excel-master, html-lo)
  • memorization - Memory-focused (anki, biography)

Type format names separated by commas, or use a bundle name:
```

**Wait for user response.**

---

### Step 3: Process User Selection

**Parse user input:**
```python
user_input = [user response]

# Check for bundle keywords
if user_input.lower() == "comprehensive":
    formats = ["word", "excel-4tab", "excel-comparison", "anki", "html-lo", "biography"]
elif user_input.lower() == "study-bundle":
    formats = ["word", "excel-comparison", "anki"]
elif user_input.lower() == "quick-reference":
    formats = ["excel-master", "html-lo"]
elif user_input.lower() == "memorization":
    formats = ["anki", "biography"]
else:
    # Parse comma-separated list
    formats = [f.strip() for f in user_input.split(',')]

# Validate formats
valid_formats = ["word", "excel-4tab", "excel-comparison", "excel-master", "excel-clinical",
                 "anki", "html-lo", "html-drugs", "html-clinical", "biography"]

invalid = [f for f in formats if f not in valid_formats]
if invalid:
    print(f"❌ Invalid formats: {', '.join(invalid)}")
    print(f"Valid options: {', '.join(valid_formats)}")
    exit(1)
```

---

### Step 4: Pre-Creation Verification

**MANDATORY - State verification checklist:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-CREATION VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Source file(s): [list files]
Formats selected: [list formats]
File count: [N files]
Total outputs: [N files × M formats = X study guides]

VERIFICATION CHECKLIST:
☐ Source files validated: All exist and readable
☐ Templates identified: [list templates for selected formats]
☐ Source-only policy: I will ONLY use information from source files
☐ Learning objectives: I will extract LO statements EXACTLY as written (NO paraphrasing)
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: [Class]/[Exam]/Claude Study Tools/
☐ Post-processing: Auto-consolidation and QUICK_ACCESS update will run automatically

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Step 5: Determine Processing Mode

**Based on file count:**

**Single file:**
- Process inline (no agent needed for just 1 file)
- Create formats sequentially

**Multiple files (2-10 files):**
- Use batch-separate-processor agent per file
- Architectural isolation (each file in own context)
- Can run in parallel

**Many files (10+ files):**
- Use batch-separate-processor agent
- Parallel execution (10 at a time)
- Progress tracking with checkpoints

---

### Step 6: Launch Processing

**For each source file:**

**If single file - Process inline:**
```
Processing: [filename]
Creating [N] formats...

[For each format]:
  Format 1/N: [format name]
  → Invoke appropriate command internally
  ✓ [output filename]

[Mnemonic cache check for each format]
[Post-processing automation triggers after creation]
```

**If multiple files - Use agents:**
```
Processing [N] source files with [M] formats each...

Launching batch-separate-processor agent [N] times:

File 1/N: [filename1]
  [Agent creates M formats in isolated context]
  ✓ [M outputs created]

File 2/N: [filename2]
  [Agent creates M formats in isolated context]
  ✓ [M outputs created]

[Agents can run in parallel - up to 10 at once]
[Each agent has own context window - no pollution]
[Progress checkpoints saved after each file]
```

---

### Step 7: Post-Processing

**Automatically triggered by hook after each file:**

```
POST-PROCESSING AUTOMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[For each Excel file with Master Chart]:
  ✓ Consolidated to [Course]_Master_Reference.xlsx
  → Added [N] drugs/conditions

[After all files complete]:
  ✓ QUICK_ACCESS index updated
  → Indexed [N] total entities
  → Location: [Course]/QUICK_ACCESS_[Course].md

Token cost: ~1,400 tokens (minimal overhead)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Step 7.5: Update Tracker (Directory Mode Only)

**If in directory mode, update `.processed_files.txt` after each file completes:**

```bash
# Append successfully processed file to tracker
tracker_file="$source_dir/.processed_files.txt"

# After each file completes successfully:
echo "$filename" >> "$tracker_file"
```

**Tracker file format:**
```
HIV_Drugs.txt
COVID_Drugs.txt
Antibiotics.txt
Beta_Blockers.txt
```

**Benefits:**
- If batch fails mid-processing, restart will skip completed files
- Run `/batch-status` to see processed vs pending
- Run `/error-recovery-resume` to retry failed files only
- Token savings: ~48k tokens per skipped file

**If NOT directory mode, skip this step.**

---

### Step 8: Completion Report

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ STUDY GUIDES CREATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Source files processed: [N]
Formats per file: [M]
Total study guides: [N × M]

Created Formats:
[List all created files by format type]

Word LO Guides ([N]):
  ✓ [file1]_Study_Guide.docx
  ✓ [file2]_Study_Guide.docx

Excel Charts ([N]):
  ✓ [file1]_Drug_Chart.xlsx
  ✓ [file2]_Comparison_Chart.xlsx

Anki Decks ([N]):
  ✓ [file1]_Flashcards.apkg
  ✓ [file2]_Flashcards.apkg

Location: [Class]/[Exam]/Claude Study Tools/

Post-Processing:
  ✓ Master charts consolidated → [Course]_Master_Reference.xlsx
  ✓ QUICK_ACCESS updated → QUICK_ACCESS_[Course].md

Token Efficiency:
  Study guides: ~[N]k tokens
  Post-processing: ~1.4k tokens
  Mnemonic cache hits: [N] (saved ~[X]k tokens)

[If using agents]:
  Architectural isolation: ✓ (no context pollution)
  Parallel processing: ✓ (up to 10 files at once)
  Accuracy improvement: +90.2% vs single-context

Next Steps:
  ✓ Review study guides in Claude Study Tools folder
  ✓ Import Anki decks to Anki app
  ✓ Use QUICK_ACCESS.md for fast lookups (Ctrl+F)
  ✓ Check /batch-status for processing summary

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Format Command Mapping

**Internal command routing:**

```python
format_commands = {
    "word": "/LO-word",
    "excel-4tab": "/4-tab-excel",
    "excel-comparison": "/key-comparisons-excel",
    "excel-master": "/master-chart-excel",
    "excel-clinical": "/clinical-assessment-excel",
    "anki": "/anki",
    "html-lo": "/LO-html",
    "html-drugs": "/drugs-html",
    "html-clinical": "/clinical-assessment-html",
    "biography": "/autobiography-trick"
}

# For each format, invoke corresponding command
for format_name in selected_formats:
    command = format_commands[format_name]
    # Execute command with source file
```

---

## Batch Processing Features

**Smart tracking:**
- Uses `.processed_files.txt` tracker
- Skips already-processed files on re-run
- Checkpoint saves after each file

**Error recovery:**
- If batch fails, run `/error-recovery-resume`
- Preserves completed work
- Only retries failed files

**Progress monitoring:**
- Run `/batch-status` to check progress
- See processed/pending/failed counts
- Get quick actions for pending work

---

## Example Usage

### Interactive Single File

```
User: /study-guides "Pharm_11 Beta Blockers_text.txt"

Claude: Which formats would you like to create?
        [shows format menu]

User: word, excel-comparison, anki

Claude: [Verification checklist]
        Creating 3 formats...
        ✓ Complete

Creates:
- 11 Beta Blockers.docx
- 11 Beta Blockers.xlsx
- 11 Beta Blockers.apkg
```

### Interactive Directory

```
User: /study-guides "Pharmacology 3/Exam 2/Extract/"

Claude: Which formats would you like to create?
        [shows format menu]

User: study-bundle

Claude: [Verification checklist]
        Processing 10 source files...
        [Uses agents for parallel processing]
        ✓ 30 study guides created (10 files × 3 formats)
```

### Quick Bundle (No Interaction)

```
User: /study-guides "source.txt" comprehensive

Claude: [Detects formats in arguments - skips interactive]
        Creating 6 formats...
        ✓ Complete
```

---

## Integration with Automation

**Works seamlessly with:**

1. **Mnemonic Cache**
   - Checks cache before WebSearch
   - Saves ~5k tokens per cache hit

2. **Post-Processing Automation**
   - Auto-consolidates master charts
   - Updates QUICK_ACCESS index
   - Per-quarter isolation

3. **Error Recovery**
   - Checkpoint after each file
   - Resume with `/error-recovery-resume`

4. **Batch Status**
   - Check progress with `/batch-status`
   - See pending/completed files

---

## Best Practices

1. **Use bundles** for common combinations (study-bundle, comprehensive)
2. **Process directories** for entire exam folders
3. **Let agents handle** multiple files (better accuracy)
4. **Check /batch-status** after large batches
5. **Use /error-recovery-resume** if interrupted

---

## Performance

**Single file (3 formats):**
- Time: 3-5 minutes
- Token cost: ~60k tokens
- Context: Main session

**10 files (3 formats each):**
- Time: 15-20 minutes
- Token cost: ~600k tokens
- Context: Isolated per file (agents)
- Accuracy: +90.2% vs single-context
- Parallelization: 10 files can process simultaneously

**Agents prevent context pollution and improve accuracy!**

---

## Sources

- [Subagents in the SDK](https://docs.claude.com/en/docs/agent-sdk/subagents)
- [Claude Subagents: Complete Guide](https://www.cursor-ide.com/blog/claude-subagents)
- [Claude Agent SDK Best Practices](https://skywork.ai/blog/claude-agent-sdk-best-practices-ai-agents-2025/)
- [Context Management with Subagents](https://www.richsnapp.com/article/2025/10-05-context-management-with-subagents-in-claude-code)
