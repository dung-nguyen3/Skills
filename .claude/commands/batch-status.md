---
description: Check batch processing status - see processed/pending files in directories
argument-hint: <directory> | --all | <path1;path2;path3>
---

Check batch processing status for: $ARGUMENTS

## Usage

**Single directory:**
```
/batch-status "Pharmacology/Exam 3/Extract"
```

**Multiple directories (semicolon-separated):**
```
/batch-status "Pharmacology/Exam 2/Extract;Pharmacology/Exam 3/Extract"
```

**All directories under course folder:**
```
/batch-status --all
```

---

## Instructions

### Step 1: Parse Arguments

**Detect mode:**
- If `--all`: Scan all course folders (Pharmacology X, Clinical Medicine X)
- If contains `;`: Multiple directories (semicolon-separated)
- Otherwise: Single directory

### Step 2: Scan Directory(ies)

For each directory to check:

1. **Find all source files:**
   ```bash
   find "$directory" -type f \( -name "*.txt" -o -name "*.pdf" \) | sort
   ```

2. **Read .processed_files.txt:**
   ```bash
   if [[ -f "$directory/.processed_files.txt" ]]; then
       mapfile -t processed < "$directory/.processed_files.txt"
   fi
   ```

3. **Compare source files vs processed:**
   - Processed: Files in `.processed_files.txt`
   - Pending: Source files NOT in `.processed_files.txt`
   - Missing: Files in `.processed_files.txt` but no longer in directory

4. **Check for study guides:**
   ```bash
   # Look for study guides in ../Claude Study Tools/
   study_tools_dir="${directory%/*}/Claude Study Tools"
   if [[ -d "$study_tools_dir" ]]; then
       mapfile -t study_guides < <(find "$study_tools_dir" -type f \( -name "*.xlsx" -o -name "*.docx" -o -name "*.html" -o -name "*.apkg" \))
   fi
   ```

### Step 3: Check Batch State

**Read batch state file (if exists):**
```bash
session_cache=".claude/study-guide-cache"
latest_batch=$(ls -t "$session_cache"/*/batch-state.json 2>/dev/null | head -1)

if [[ -n "$latest_batch" ]]; then
    # Extract batch info
    batch_id=$(jq -r '.batch_id' "$latest_batch")
    command=$(jq -r '.command' "$latest_batch")
    files_total=$(jq -r '.files_total' "$latest_batch")
    files_completed=$(jq -r '.files_completed' "$latest_batch")
    files_failed=$(jq -r '.files_failed' "$latest_batch")
    current_file=$(jq -r '.current_file' "$latest_batch")
fi
```

### Step 4: Generate Status Report

**Format output:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 BATCH PROCESSING STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Directory: [directory path]
Source files: [N total]

Status:
  ✓ Processed: [N files] ([percentage]%)
  ⏳ Pending: [N files]
  ❌ Failed: [N files]

[If pending files exist]:
Pending Files:
  1. [filename1.txt]
  2. [filename2.txt]
  3. [filename3.txt]

[If processed files exist]:
Recent Study Guides Created:
  ✓ [filename1_Study_Guide.docx] (Word LO)
  ✓ [filename2_Drug_Chart.xlsx] (4-tab Excel)
  ✓ [filename3_Flashcards.apkg] (Anki)

[If batch state exists]:
Last Batch Run:
  Batch ID: [batch-id]
  Command: [/word-excel-anki | /4-tab-excel | etc.]
  Status: [completed | failed | in-progress]
  Files: [N completed] / [M total]

[If failed files exist]:
Failed Files (require attention):
  ❌ [filename.txt] - [error reason if available]

Quick Actions:
  [If pending files exist]:
  ▶ Process pending: /word-excel-anki "$directory"
  ▶ Process single: /word-excel-anki "$directory/[pending-file].txt"

  [If failed files exist]:
  ▶ Resume failed: /error-recovery-resume
  ▶ Retry failed: /word-excel-anki "[failed-file1.txt;failed-file2.txt]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 5: Statistics Summary (if --all)

**For --all mode, show course-level summary:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 BATCH PROCESSING STATUS - ALL COURSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pharmacology 3:
  Exam 1: ✓ 8/8 files (100%)
  Exam 2: ⏳ 5/10 files (50%) - 5 pending
  Exam 3: ⏳ 0/12 files (0%) - 12 pending
  ─────────────────────────────
  Total: 13/30 files (43%)

Clinical Medicine 3:
  Exam 1: ✓ 6/6 files (100%)
  Exam 2: ✓ 4/4 files (100%)
  ─────────────────────────────
  Total: 10/10 files (100%)

Overall Progress:
  Total source files: 40
  Processed: 23 (57.5%)
  Pending: 17 (42.5%)
  Failed: 0 (0%)

Study Guides Created:
  Word LO guides: 18
  Excel charts: 15
  Anki decks: 12
  HTML guides: 8
  Total: 53 study guides

Next Recommended Action:
  ▶ Process Pharmacology 3 Exam 2 pending: /word-excel-anki "Pharmacology 3/Exam 2/Extract"
  ▶ Process Pharmacology 3 Exam 3 pending: /word-excel-anki "Pharmacology 3/Exam 3/Extract"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Implementation Details

### File Discovery

```bash
# Find all source files in directory
find_source_files() {
    local dir="$1"
    find "$dir" -maxdepth 1 -type f \( -name "*.txt" -o -name "*.pdf" \) | sort
}

# Read processed files list
read_processed_files() {
    local dir="$1"
    local processed_file="$dir/.processed_files.txt"

    if [[ -f "$processed_file" ]]; then
        cat "$processed_file" | sort
    fi
}

# Compare and categorize
categorize_files() {
    local source_files=("$@")
    local processed_files=($(read_processed_files "$dir"))

    local pending=()
    local processed=()

    for file in "${source_files[@]}"; then
        basename=$(basename "$file")
        if printf '%s\n' "${processed_files[@]}" | grep -q "^$basename$"; then
            processed+=("$basename")
        else
            pending+=("$basename")
        fi
    done

    echo "processed=${#processed[@]}"
    echo "pending=${#pending[@]}"
}
```

### Study Guide Discovery

```bash
# Find study guides created from source files
find_study_guides() {
    local dir="$1"
    local study_tools="${dir%/*}/Claude Study Tools"

    if [[ ! -d "$study_tools" ]]; then
        return
    fi

    # Find all study guides
    local guides=$(find "$study_tools" -type f \( \
        -name "*.xlsx" -o \
        -name "*.docx" -o \
        -name "*.html" -o \
        -name "*.apkg" \
    \) -printf '%T@ %p\n' | sort -rn | cut -d' ' -f2-)

    # Categorize by type
    while IFS= read -r guide; do
        case "$guide" in
            *.xlsx) echo "Excel: $(basename "$guide")" ;;
            *.docx) echo "Word: $(basename "$guide")" ;;
            *.html) echo "HTML: $(basename "$guide")" ;;
            *.apkg) echo "Anki: $(basename "$guide")" ;;
        esac
    done <<< "$guides"
}
```

### Batch State Reading

```bash
# Read latest batch state
read_batch_state() {
    local cache_dir=".claude/study-guide-cache"

    # Find most recent batch-state.json
    local latest=$(find "$cache_dir" -name "batch-state.json" -type f -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)

    if [[ -z "$latest" ]]; then
        echo "No batch state found"
        return
    fi

    # Extract info using jq
    local batch_id=$(jq -r '.batch_id' "$latest" 2>/dev/null || echo "unknown")
    local command=$(jq -r '.command' "$latest" 2>/dev/null || echo "unknown")
    local files_total=$(jq -r '.files_total' "$latest" 2>/dev/null || echo "0")
    local files_completed=$(jq -r '.files_completed' "$latest" 2>/dev/null || echo "0")

    echo "Batch ID: $batch_id"
    echo "Command: $command"
    echo "Progress: $files_completed / $files_total"
}
```

---

## Example Usage

### Check Single Directory

**Input:**
```
/batch-status "Pharmacology 3/Exam 2/Extract"
```

**Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 BATCH PROCESSING STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Directory: Pharmacology 3/Exam 2/Extract
Source files: 10 total

Status:
  ✓ Processed: 7 files (70%)
  ⏳ Pending: 3 files
  ❌ Failed: 0 files

Pending Files:
  1. Beta_Blockers.txt
  2. ACE_Inhibitors.txt
  3. Calcium_Channel_Blockers.txt

Recent Study Guides Created:
  ✓ HIV_Antivirals_Study_Guide.docx (Word LO)
  ✓ COVID_Drugs_Drug_Chart.xlsx (4-tab Excel)
  ✓ Antibiotics_Flashcards.apkg (Anki)
  (... 4 more)

Last Batch Run:
  Batch ID: 20250104-143022
  Command: /word-excel-anki
  Status: completed
  Files: 7 / 7

Quick Actions:
  ▶ Process pending: /word-excel-anki "Pharmacology 3/Exam 2/Extract"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Check All Courses

**Input:**
```
/batch-status --all
```

**Output:**
```
(See "Statistics Summary (if --all)" section above)
```

---

## Integration with Other Commands

**Works with:**
- `/word-excel-anki` - See which files still need processing
- `/4-tab-excel` - Check pending drug chart sources
- `/error-recovery-resume` - Resume failed batch operations

**Workflow:**
1. Run `/batch-status --all` to see overall progress
2. Identify directories with pending files
3. Run batch commands on pending directories
4. Re-check with `/batch-status` to verify completion

---

## Performance

**Token cost:** ~500-1000 tokens (mostly Bash operations, minimal LLM usage)

**Speed:** Near-instant (file system operations only)

**No side effects:** Read-only command, doesn't modify anything

---

## Notes

- Tracker file (`.processed_files.txt`) created automatically by batch commands
- If tracker missing, all files shown as "pending"
- Failed files require manual intervention or `/error-recovery-resume`
- `--all` mode scans entire course folder hierarchy
