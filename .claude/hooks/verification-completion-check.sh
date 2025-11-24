#!/bin/bash
set -eo pipefail

# Stop hook that checks for incomplete verification and runs accuracy validation
# This runs when Claude Code session stops

# Emergency override: Skip all verification checks
if [[ -n "$SKIP_STUDY_GUIDE_VERIFICATION" ]]; then
    exit 0
fi

# Check for jq dependency
if ! command -v jq &>/dev/null; then
    echo "⚠️  Warning: jq not found, skipping session check" >&2
    exit 0  # Fail-open if jq is missing
fi

# Read session information from stdin
session_info=$(cat)

# Extract session ID with error handling
session_id=$(echo "$session_info" | jq -r '.session_id // empty' 2>/dev/null || echo "")

# Fallback session ID if extraction failed
if [[ -z "$session_id" ]]; then
    session_id="fallback-$(date +%Y%m%d-%H%M%S)"
fi

# State directory (using study-guide-cache)
cache_dir="$CLAUDE_PROJECT_DIR/.claude/study-guide-cache/${session_id}"

# Check if cache directory exists
if [[ ! -d "$cache_dir" ]]; then
    exit 0  # No study guide work this session
fi

verification_file="$cache_dir/verification.json"
post_verification_file="$cache_dir/post-verification.json"
created_files_log="$cache_dir/created-files.log"

# Initialize check results
incomplete_work=false
warnings=()
accuracy_issues=()

# Scenario 1: Pre-verification done but post-verification not done
if [[ -f "$verification_file" ]] && [[ ! -f "$post_verification_file" ]]; then
    incomplete_work=true
    warnings+=("⚠️  Pre-creation verification completed, but post-creation verification was NOT completed")
fi

# Scenario 2: Check if study guide files were created
if [[ -f "$created_files_log" ]]; then
    file_count=$(wc -l < "$created_files_log" 2>/dev/null || echo "0")

    if [[ $file_count -gt 0 ]]; then
        if [[ ! -f "$post_verification_file" ]]; then
            incomplete_work=true
            warnings+=("⚠️  Created $file_count study guide file(s) but did not run post-verification")
        fi

        # ACCURACY VALIDATION: Check created files for common issues
        while IFS=: read -r timestamp filepath action; do
            filename=$(basename "$filepath")

            # Check for vague language indicators in filename
            if [[ "$filename" =~ [Dd]raft|[Tt]emp|[Tt]est|WIP ]]; then
                accuracy_issues+=("📄 $filename - Filename suggests incomplete work (draft/temp/test)")
            fi

            # Log file for accuracy tracking
            echo "$filepath" >> "$cache_dir/files-needing-verification.txt"
        done < "$created_files_log"
    fi
fi

# If no issues, clean up and exit
if [[ "$incomplete_work" = false ]] && [[ ${#accuracy_issues[@]} -eq 0 ]]; then
    # Clean up old session caches (keep last 5 sessions)
    parent_dir="$CLAUDE_PROJECT_DIR/.claude/study-guide-cache"
    if [[ -d "$parent_dir" ]]; then
        cd "$parent_dir"
        ls -t | tail -n +6 | xargs rm -rf 2>/dev/null || true
    fi
    exit 0
fi

# Display warnings
cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  STUDY GUIDE QUALITY CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EOF

if [[ "$incomplete_work" = true ]]; then
    echo "INCOMPLETE VERIFICATION DETECTED:"
    echo ""
    printf '%s\n' "${warnings[@]}"
    echo ""
fi

if [[ ${#accuracy_issues[@]} -gt 0 ]]; then
    echo "POTENTIAL ACCURACY ISSUES:"
    echo ""
    printf '%s\n' "${accuracy_issues[@]}"
    echo ""
fi

# Show files needing verification
if [[ -f "$cache_dir/files-needing-verification.txt" ]]; then
    echo "FILES REQUIRING VERIFICATION:"
    while IFS= read -r file; do
        echo "   📄 $(basename "$file")"
    done < "$cache_dir/files-needing-verification.txt"
    echo ""
fi

# Recommendations based on issue count
total_issues=$((${#warnings[@]} + ${#accuracy_issues[@]}))

if [[ $total_issues -ge 3 ]]; then
    cat <<EOF
🤖 RECOMMENDED: Use accuracy verification agent
   Multiple issues detected - automated verification recommended

   Next session, run:
   /verify-accuracy [file-path] [source-path]

EOF
else
    cat <<EOF
🎯 RECOMMENDED ACTIONS FOR NEXT SESSION:
   1. Run post-creation verification on all files
   2. Use /verify-accuracy for deep analysis
   3. Verify source-only policy followed
   4. Check for vague language or invented information

EOF
fi

cat <<EOF
💡 PREVENTION:
   - Always complete post-verification before ending session
   - Use slash commands (/excel, /word) for automatic verification
   - State "Post-creation verification complete" after checks

Session cache: $cache_dir
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

# Exit 0 - this is a warning, not an error
exit 0
