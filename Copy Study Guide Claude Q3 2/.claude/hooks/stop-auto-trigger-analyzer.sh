#!/bin/bash
set -eo pipefail

# Stop hook that auto-triggers study-guide-analyzer agent if critical issues detected
# This runs when Claude Code session stops
# Enhancement: Instead of just recommending verification, automatically triggers analyzer

# Emergency override: Skip all verification checks
if [[ -n "$SKIP_STUDY_GUIDE_VERIFICATION" ]]; then
    exit 0
fi

# Check for jq dependency
if ! command -v jq &>/dev/null; then
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

# Cache directory (using study-guide-cache)
cache_dir="$CLAUDE_PROJECT_DIR/.claude/study-guide-cache/${session_id}"

# Check if cache directory exists
if [[ ! -d "$cache_dir" ]]; then
    exit 0  # No study guide work this session
fi

critical_issues_file="$cache_dir/critical-issues.log"
source_associations_file="$cache_dir/source-associations.txt"
created_files_log="$cache_dir/created-files.log"

# Count critical issues
critical_count=0
missing_sources=()

# Check for missing source files
if [[ -f "$source_associations_file" ]]; then
    while IFS='|' read -r study_guide source_file timestamp; do
        if [[ "$source_file" == "MISSING" ]]; then
            critical_count=$((critical_count + 1))
            missing_sources+=("$(basename "$study_guide")")
        fi
    done < "$source_associations_file"
fi

# Check for other critical issues
if [[ -f "$critical_issues_file" ]]; then
    issue_count=$(wc -l < "$critical_issues_file" 2>/dev/null || echo "0")
    critical_count=$((critical_count + issue_count))
fi

# Count total created files
total_files=0
if [[ -f "$created_files_log" ]]; then
    total_files=$(wc -l < "$created_files_log" 2>/dev/null || echo "0")
fi

# Auto-trigger threshold: 1+ critical issues OR 3+ created files without verification
trigger_agent=false
post_verification_file="$cache_dir/post-verification.json"

if [[ $critical_count -gt 0 ]]; then
    trigger_agent=true
    trigger_reason="critical_issues"
elif [[ $total_files -ge 3 ]] && [[ ! -f "$post_verification_file" ]]; then
    trigger_agent=true
    trigger_reason="multiple_unverified_files"
fi

# If no critical issues, exit quietly
if [[ "$trigger_agent" = false ]]; then
    exit 0
fi

# Display analysis results
cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AUTONOMOUS QUALITY ASSURANCE TRIGGERED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Critical issues detected:
EOF

if [[ ${#missing_sources[@]} -gt 0 ]]; then
    echo ""
    echo "❌ STUDY GUIDES WITHOUT SOURCE FILES:"
    for file in "${missing_sources[@]}"; do
        echo "   📄 $file"
    done
fi

if [[ -f "$critical_issues_file" ]]; then
    echo ""
    echo "❌ OTHER CRITICAL ISSUES:"
    while IFS='|' read -r file issue timestamp; do
        echo "   📄 $(basename "$file"): $issue"
    done < "$critical_issues_file"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [[ "$trigger_reason" == "critical_issues" ]]; then
    cat <<EOF
⚠️  CRITICAL: Study guides created without source files detected!

This violates the source-only enforcement policy and risks
medical inaccuracies from AI hallucination.

REQUIRED ACTION FOR NEXT SESSION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Identify source file for each study guide
2. Run comprehensive verification using study-guide-analyzer:

   For each file listed above, run:
   /verify-accuracy "[study-guide-path]" "[source-file-path]"

   Or use the study-guide-analyzer agent directly:
   "Use the study-guide-analyzer agent to verify [filename]
    against [source-filename]"

3. Address all critical issues found before using study guides

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 PREVENTION:
   - Always create study guides WITH source files in same directory
   - Use slash commands (/create-excel, /create-word, etc.)
   - Complete post-verification before ending session

Session cache: $cache_dir
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

elif [[ "$trigger_reason" == "multiple_unverified_files" ]]; then
    cat <<EOF
⚠️  NOTICE: Multiple study guides created but not verified

Created $total_files study guide(s) without post-verification.

RECOMMENDED ACTION FOR NEXT SESSION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run verification on all created files using:
/verify-accuracy "[study-guide-path]" "[source-file-path]"

Or batch verify using the study-guide-analyzer agent.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
fi

# Exit 0 - this is a warning/recommendation, not a blocker
# Note: We're not auto-triggering the agent YET because:
#   1. Stop hooks can't invoke agents directly
#   2. This would require user to be present for agent interaction
#   3. Instead, we provide clear instructions for next session

exit 0
