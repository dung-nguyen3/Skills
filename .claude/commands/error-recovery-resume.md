---
description: Resume failed batch operation from last checkpoint with exponential backoff retry
argument-hint: [optional: specific files to retry, semicolon-separated]
---

Resume error recovery: $ARGUMENTS

## Command Usage

**Auto-resume from last checkpoint:**
```
/error-recovery-resume
```

**Resume specific files only:**
```
/error-recovery-resume "Beta_Blockers.txt;ACE_Inhibitors.txt"
```

---

## Instructions

### Step 1: Parse Arguments

**Determine recovery mode:**
- No arguments: Auto-resume from most recent checkpoint
- With arguments: Manual mode - retry specific files only

### Step 2: Launch Error Recovery Agent

**Invoke error-recovery agent:**

```
I'll use the error-recovery agent to resume your failed batch operation.

Launching agent with:
- Recovery mode: [auto | manual]
- Target files: [from checkpoint | specified files]
```

**Use Task tool:**

```python
Task(
    subagent_type="general-purpose",
    description="Resume failed batch operation",
    prompt=f"""
Use the error-recovery agent to resume batch processing.

Recovery mode: {"auto" if not args else "manual"}
{f"Target files: {args}" if args else "Read from checkpoint"}

Agent will:
1. Read most recent batch-state.json checkpoint
2. Identify completed/failed/pending files
3. Skip completed files (preserve work)
4. Retry failed files with exponential backoff (2s, 4s, 8s)
5. Circuit breaker: Stop after 3 consecutive failures per file
6. Process pending files if retries succeed
7. Save checkpoint after each file

Exponential backoff prevents overwhelming services and respects rate limits.
Circuit breaker protects against permanently broken files.

Report:
- Files recovered
- Files permanently failed (need manual intervention)
- Token savings from skipping completed files
"""
)
```

**STOP HERE** - Agent handles all recovery logic autonomously.

---

## Example Usage

### Auto-Resume from Checkpoint

**User runs:**
```
/error-recovery-resume
```

**Agent execution:**

```
[ERROR RECOVERY AGENT]

Loading checkpoint...
✓ Found: batch-state.json (Batch ID: 20250104-143022)

Original batch: /word-excel-anki
Files total: 10

Status:
  ✓ Completed: 5 files (will skip)
  ↻ Failed: 1 file (will retry)
  ⏳ Pending: 4 files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Skipping completed files (5):
  ✓ HIV.txt
  ✓ COVID.txt
  ✓ Antibiotics.txt
  ✓ Antivirals.txt
  ✓ Fungi.txt

Retrying failed files (1):
  ↻ Beta_Blockers.txt (attempt #3)
    Previous error: WebSearch timeout
    Waiting 8s before retry...
    [8 second delay]
    Processing...
    ✓ Success on retry #3

Processing pending files (4):
  ⏳ ACE_Inhibitors.txt
    Processing...
    ✓ Complete

  ⏳ CCBs.txt
    Processing...
    ✓ Complete

  ⏳ Diuretics.txt
    Processing...
    ✓ Complete

  ⏳ Statins.txt
    Processing...
    ✓ Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ RECOVERY COMPLETE

Recovery Results:
  ✓ Previously completed: 5 files (preserved)
  ✓ Recovered from failure: 1 file
  ✓ Newly processed: 4 files
  ❌ Permanently failed: 0 files

Final Status: 10/10 files (100%)

Token Efficiency:
  Tokens used: ~60k (5 new files)
  Tokens saved: ~240k (5 skipped files)

Study guides location:
  Pharmacology 3/Exam 2/Claude Study Tools/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Manual Recovery (Specific Files)

**User runs:**
```
/error-recovery-resume "Beta_Blockers.txt;Diuretics.txt"
```

**Agent execution:**

```
[ERROR RECOVERY AGENT - MANUAL MODE]

Target files: Beta_Blockers.txt, Diuretics.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Retrying specified files:

  ↻ Beta_Blockers.txt
    Processing...
    ✓ Complete

  ↻ Diuretics.txt
    Processing...
    ✓ Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ MANUAL RECOVERY COMPLETE

Files processed: 2/2 (100%)

Study guides created:
  ✓ Beta_Blockers_Study_Guide.docx
  ✓ Beta_Blockers_Comparison_Chart.xlsx
  ✓ Beta_Blockers_Flashcards.apkg
  ✓ Diuretics_Study_Guide.docx
  ✓ Diuretics_Comparison_Chart.xlsx
  ✓ Diuretics_Flashcards.apkg
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Circuit Breaker Activation

**Scenario:** File fails 3 consecutive times

**Agent execution:**

```
[ERROR RECOVERY AGENT]

Retrying failed files:

  ↻ Beta_Blockers.txt (attempt #1)
    Previous error: WebSearch timeout
    Waiting 2s before retry...
    ❌ Failed: WebSearch timeout

  ↻ Beta_Blockers.txt (attempt #2)
    Waiting 4s before retry...
    ❌ Failed: WebSearch timeout

  ↻ Beta_Blockers.txt (attempt #3)
    Waiting 8s before retry...
    ❌ Failed: WebSearch timeout

⚠️  CIRCUIT BREAKER ACTIVATED

File: Beta_Blockers.txt
Failures: 3 consecutive
Last error: WebSearch timeout after 30s

This file requires manual intervention:
  1. Check network connectivity
  2. Verify source file is valid
  3. Try WebSearch manually
  4. Review error logs

Marking as permanently failed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  RECOVERY PARTIAL

Completed: 9/10 files (90%)
Permanently failed: 1 file

Failed file: Beta_Blockers.txt
  Reason: 3 consecutive WebSearch timeouts
  Suggestion: Check network, retry manually when connection stable

To retry manually:
  /word-excel-anki "Beta_Blockers.txt"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Common Recovery Scenarios

### Scenario 1: Network Glitch

**Problem:** Temporary network timeout during batch

**Recovery:**
```
/error-recovery-resume
```

**Outcome:** Exponential backoff (2s delay) usually resolves transient network issues

---

### Scenario 2: Missing Library

**Problem:** Python library not installed (e.g., openpyxl)

**Fix before recovery:**
```bash
pip install openpyxl
```

**Then resume:**
```
/error-recovery-resume
```

**Outcome:** Library now available, processing succeeds

---

### Scenario 3: Corrupted Source File

**Problem:** One source file is corrupted

**Agent behavior:**
- Tries 3 times with exponential backoff
- Circuit breaker activates
- Skips corrupted file, processes rest

**User action:**
1. Fix corrupted source file
2. Manually process: `/word-excel-anki "corrupted-file.txt"`

---

## Error Handling

### No Checkpoint Found

```
❌ No batch checkpoint found

No incomplete batch operations detected.

To start new batch:
  /word-excel-anki "[directory or files]"
  /drugs-3-tab-excel "[directory or files]"
```

---

### Checkpoint Corrupted

```
❌ Checkpoint file corrupted

Recovery options:
  1. Check which files were completed:
     ls "Pharmacology 3/Exam 2/Claude Study Tools/"

  2. Start fresh batch (will skip completed files):
     /word-excel-anki "Pharmacology 3/Exam 2/Extract/"
```

---

### All Files Already Completed

```
✓ Batch already complete

Checkpoint shows all files successfully processed.
No recovery needed.

Run /batch-status to verify.
```

---

## Integration with Other Commands

**Workflow:**

1. Run batch command:
   ```
   /word-excel-anki "Pharmacology 3/Exam 2/Extract/"
   ```

2. If batch fails mid-processing:
   ```
   ⚠️  Batch failed on file 6/10
   Checkpoint saved.
   Run /error-recovery-resume to continue.
   ```

3. Resume from checkpoint:
   ```
   /error-recovery-resume
   ```

4. Verify completion:
   ```
   /batch-status "Pharmacology 3/Exam 2/Extract/"
   ```

---

## Best Practices

1. **Don't interrupt recovery** - Let exponential backoff complete
2. **Check network first** - If multiple WebSearch timeouts, check connectivity
3. **Fix root cause** - If circuit breaker activates, diagnose before retrying
4. **Use /batch-status** - Verify what's actually completed vs pending
5. **Manual retry** - For persistently failed files, investigate and retry manually

---

## Performance

**Token efficiency:**
- Skips completed files (saves ~48k tokens each)
- Only processes failed + pending
- Example: 5 completed, 5 remaining = ~240k tokens saved

**Time overhead:**
- Exponential backoff delays: 2-14 seconds total
- Minimal compared to re-processing completed files

---

## When to Use

**Use this command when:**
- ✓ Batch operation failed mid-processing
- ✓ Network timeout interrupted batch
- ✓ Library error was fixed, need to resume
- ✓ Want to preserve completed work

**Don't use when:**
- ✗ No batch has run yet (use normal batch commands)
- ✗ All files completed successfully
- ✗ Want to re-process everything (use normal batch commands with --force)

---

## Notes

- Checkpoint files auto-deleted after 7 days
- Circuit breaker threshold: 3 consecutive failures
- Exponential backoff: 2s, 4s, 8s delays
- State persisted after each file (crash-safe)
