#!/bin/bash
set -e

# PostToolUse hook that reminds to run post-creation verification
# This runs AFTER Edit, MultiEdit, or Write tools complete successfully

# Read tool information from stdin
tool_info=$(cat)

# Extract relevant data
tool_name=$(echo "$tool_info" | jq -r '.tool_name // empty')
file_path=$(echo "$tool_info" | jq -r '.tool_input.file_path // empty')
session_id=$(echo "$tool_info" | jq -r '.session_id // empty')

# Only check Write/Edit/MultiEdit tools
if [[ ! "$tool_name" =~ ^(Edit|MultiEdit|Write)$ ]]; then
    exit 0
fi

# Skip if no file path
if [[ -z "$file_path" ]]; then
    exit 0
fi

# Check if this is a study guide file (in Claude Study Tools directory)
if [[ ! "$file_path" =~ "Claude Study Tools" ]]; then
    exit 0  # Not a study guide file, skip
fi

# Check if file is Excel, Word, or HTML study guide
if [[ ! "$file_path" =~ \.(xlsx|docx|html)$ ]]; then
    exit 0  # Not a study guide format, skip
fi

# State directory for tracking verification
state_dir="$CLAUDE_PROJECT_DIR/.claude/hooks/state"
mkdir -p "$state_dir"

post_verification_file="$state_dir/${session_id}_post_verification.json"

# Check if post-verification was already completed
if [[ -f "$post_verification_file" ]]; then
    exit 0  # Already done, don't spam
fi

# Extract filename from path
filename=$(basename "$file_path")

# Reminder to run post-creation verification
cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 POST-CREATION VERIFICATION REMINDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Study guide file created/modified:
📁 $filename

⚠️  MANDATORY NEXT STEP: Run post-creation verification

Verify the completed file for:

1. ✓ Source Accuracy
   - All information from source file only (except mnemonics)
   - External additions marked with asterisk (*)
   - Page references included where required

2. ✓ Template Compliance
   - ALL template instructions followed exactly
   - Correct structure (all tabs/sections present)
   - Correct formatting (colors, fonts, styles)
   - All required elements included

3. ✓ Completeness
   - All learning objectives answered (all parts)
   - All comparison tables created
   - Master chart includes ALL topics
   - No missing content

4. ✓ Quality Checks
   - No incorrect groupings or merged cells
   - No spelling errors
   - Proper formatting throughout

🎯 ACTION REQUIRED:
State: "Post-creation verification complete" after checking above

💡 Or use detailed verification:
/verify-accuracy "$file_path" "[source-file]"

To mark post-verification complete, create file:
$post_verification_file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

exit 0  # Exit 0 - this is just a reminder, not a blocker
