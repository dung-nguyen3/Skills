#!/bin/bash

# SessionStart hook that displays study guide quality protocol requirements
# This runs when a Claude Code session starts

cat <<'EOF'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 STUDY GUIDE QUALITY PROTOCOL ACTIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  MANDATORY: All study guides require verification

✅ Pre-Creation Verification Checklist:
   - Source file path specified
   - Template identified
   - Source-only policy confirmed
   - Mnemonics will be researched (WebSearch required)

✅ Post-Creation Verification Required:
   - Source accuracy check
   - Template compliance check
   - Completeness check
   - Quality check

💡 Use slash commands for automatic compliance:
   /4-tab-excel [source-file]
   /LO-word [source-file]
   /verify-accuracy [file] [source]

🔒 Quality gates are ACTIVE and will enforce these requirements.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

# Weekly Batch Processing Reminder
# Check if it's been 7+ days since last batch operation
LAST_BATCH_FILE="$HOME/.claude/last_batch_date"
CURRENT_DATE=$(date +%s)

if [ -f "$LAST_BATCH_FILE" ]; then
    LAST_BATCH=$(cat "$LAST_BATCH_FILE" 2>/dev/null || echo "0")
    DAYS_DIFF=$(( (CURRENT_DATE - LAST_BATCH) / 86400 ))

    if [ $DAYS_DIFF -ge 7 ]; then
        cat <<'REMINDER'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 WEEKLY REMINDER: Batch Processing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

It's been 7+ days since your last batch operation.

💡 Consider running batch processing on new source files:
   /word-excel-anki "path/to/directory/"
   /4-tab-excel "path/to/directory/"

📁 Check these locations for unprocessed files:
   - [Course]/[Exam]/Extract/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REMINDER
    fi
else
    # First time - create the file
    mkdir -p "$HOME/.claude"
    echo "$CURRENT_DATE" > "$LAST_BATCH_FILE"
fi

exit 0
