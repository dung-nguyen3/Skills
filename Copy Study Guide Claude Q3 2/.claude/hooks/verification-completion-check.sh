#!/bin/bash
set -e

# Stop hook that checks for incomplete verification at session end
# This runs when Claude Code session stops

# Read session information from stdin
session_info=$(cat)

# Extract session ID
session_id=$(echo "$session_info" | jq -r '.session_id // empty')

# State directory
state_dir="$CLAUDE_PROJECT_DIR/.claude/hooks/state"

# Check if state directory exists
if [[ ! -d "$state_dir" ]]; then
    exit 0  # No state to check
fi

verification_file="$state_dir/${session_id}_verification.json"
post_verification_file="$state_dir/${session_id}_post_verification.json"

# Check for incomplete work scenarios
incomplete_work=false
warnings=()

# Scenario 1: Pre-verification done but post-verification not done
if [[ -f "$verification_file" ]] && [[ ! -f "$post_verification_file" ]]; then
    incomplete_work=true
    warnings+=("⚠️  Pre-creation verification was completed, but post-creation verification was NOT completed")
fi

# Scenario 2: Check if any study guide files were created this session
created_files_log="$state_dir/${session_id}_created_files.log"
if [[ -f "$created_files_log" ]]; then
    file_count=$(wc -l < "$created_files_log" 2>/dev/null || echo "0")
    if [[ $file_count -gt 0 ]] && [[ ! -f "$post_verification_file" ]]; then
        incomplete_work=true
        warnings+=("⚠️  Created $file_count study guide file(s) but did not run post-verification")
    fi
fi

# If no incomplete work, exit cleanly
if [[ "$incomplete_work" = false ]]; then
    # Clean up old session state files (keep only last 5 sessions)
    cd "$state_dir"
    ls -t ${session_id}_*.json 2>/dev/null | tail -n +6 | xargs rm -f 2>/dev/null || true
    exit 0
fi

# Display warnings about incomplete work
cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  INCOMPLETE VERIFICATION DETECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Session ending with incomplete verification work:

$(printf '%s\n' "${warnings[@]}")

📋 WHAT THIS MEANS:
Study guides were created but NOT verified for accuracy.
This could mean:
- Incorrect information from source
- Template non-compliance
- Merged cells incorrectly grouped
- Missing content

🎯 RECOMMENDED ACTIONS FOR NEXT SESSION:
1. Run post-creation verification on created files
2. Use: /verify-accuracy "[file]" "[source]"
3. Or manually verify all 4 quality checks

💡 FILES THAT NEED VERIFICATION:
EOF

# List files that were created
if [[ -f "$created_files_log" ]]; then
    while IFS= read -r file; do
        echo "   📄 $file"
    done < "$created_files_log"
fi

cat <<EOF

To prevent this warning:
- Always state "Post-creation verification complete" after creating study guides
- Use slash commands which enforce verification workflows
- Complete all quality checks before ending session

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

# Exit 0 - this is a warning, not an error
exit 0
