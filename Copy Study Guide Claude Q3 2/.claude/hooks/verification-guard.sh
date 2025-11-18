#!/bin/bash
set -e

# PreToolUse hook that blocks study guide creation without verification checklist
# This runs BEFORE Edit, MultiEdit, or Write tools execute

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
    exit 0  # Not a study guide file, allow
fi

# Check if file is Excel, Word, or HTML study guide
if [[ ! "$file_path" =~ \.(xlsx|docx|html)$ ]]; then
    exit 0  # Not a study guide format, allow
fi

# State directory for tracking verification (using study-guide-cache)
state_dir="$CLAUDE_PROJECT_DIR/.claude/study-guide-cache/${session_id}"
mkdir -p "$state_dir"

verification_file="$state_dir/verification.json"

# Check if verification checklist was completed this session
if [[ -f "$verification_file" ]]; then
    # Verification was done, log this file creation attempt
    echo "$(date +%s):$file_path:pre-verified" >> "$state_dir/operations.log"
    exit 0
fi

# Verification NOT done - BLOCK the operation
cat >&2 <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⛔ BLOCKED - Pre-Creation Verification Required
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You are attempting to create/edit a study guide file:
📁 $file_path

🚫 VERIFICATION CHECKLIST NOT COMPLETED

Before creating ANY study guide, you MUST state:

VERIFICATION CHECKLIST:
☐ Source file: [exact filename and path]
☐ Instruction template: [template name]
☐ Source-only policy: I will ONLY use information from source file
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: [Class]/[Exam]/Claude Study Tools/

📋 REQUIRED ACTIONS:
1. Read the ENTIRE source file first
2. Read the COMPLETE template file
3. STATE the verification checklist above
4. Mark verification as complete
5. ONLY then proceed with creation

💡 TIP: Use slash commands which automatically handle verification:
   /create-excel [source-file]
   /create-word [source-file]

⚠️  This block ensures source-only policy and quality standards.

To mark verification complete, I need to:
1. Read the entire source file
2. State the verification checklist
3. Create verification marker with:
   echo '{"verified":true,"timestamp":"'"\$(date -Iseconds)"'","file":"$file_path"}' > "$verification_file"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

exit 2  # Exit 2 blocks the operation and shows stderr to Claude
