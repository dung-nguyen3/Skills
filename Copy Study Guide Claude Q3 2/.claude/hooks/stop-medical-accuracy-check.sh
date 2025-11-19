#!/bin/bash
set -eo pipefail

# Stop hook for basic medical accuracy warning detection
# Checks for common patterns that may indicate accuracy issues
# Does NOT perform full verification - use study-guide-analyzer for that

# Emergency override
if [[ -n "$SKIP_STUDY_GUIDE_VERIFICATION" ]]; then
    exit 0
fi

# Check for jq dependency
if ! command -v jq &>/dev/null; then
    exit 0
fi

# Read session information
session_info=$(cat)
session_id=$(echo "$session_info" | jq -r '.session_id // empty' 2>/dev/null || echo "")

if [[ -z "$session_id" ]]; then
    session_id="fallback-$(date +%Y%m%d-%H%M%S)"
fi

# Cache directory
cache_dir="$CLAUDE_PROJECT_DIR/.claude/study-guide-cache/${session_id}"

if [[ ! -d "$cache_dir" ]]; then
    exit 0
fi

# Get list of created files
created_files_log="$cache_dir/created-files.log"
if [[ ! -f "$created_files_log" ]]; then
    exit 0
fi

# Accuracy warning patterns (basic checks only - not comprehensive)
warnings=()

# Check each created file for warning patterns
while IFS=: read -r timestamp filepath action; do
    if [[ ! -f "$filepath" ]]; then
        continue
    fi

    filename=$(basename "$filepath")
    file_ext="${filename##*.}"

    # Pattern 1: Vague/placeholder language in filenames
    if [[ "$filename" =~ [Dd]raft|[Tt]emp|[Tt]est|WIP|TODO|PLACEHOLDER ]]; then
        warnings+=("📄 $filename - Filename suggests incomplete work")
    fi

    # Pattern 2: Check source association exists
    source_associations_file="$cache_dir/source-associations.txt"
    if [[ -f "$source_associations_file" ]]; then
        if ! grep -q "^$filepath|" "$source_associations_file"; then
            warnings+=("📄 $filename - No source file association found")
        elif grep -q "^$filepath|MISSING|" "$source_associations_file"; then
            warnings+=("📄 $filename - Source file marked as MISSING")
        fi
    fi

    # Pattern 3: For text-based formats, check for common accuracy red flags
    # (Excel/Word/HTML would need special parsing - skip for now)

done < "$created_files_log"

# If no warnings, exit quietly
if [[ ${#warnings[@]} -eq 0 ]]; then
    exit 0
fi

# Display warnings (only if issues found)
cat <<EOF

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  MEDICAL ACCURACY WARNINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Potential accuracy concerns detected:

EOF

printf '%s\n' "${warnings[@]}"

cat <<EOF

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  IMPORTANT: These are automated warnings, not definitive errors.

However, they indicate potential risks:
- Missing source files increase hallucination risk
- Placeholder names suggest incomplete content
- Unverified work may contain medical inaccuracies

STRONGLY RECOMMENDED:
Run comprehensive verification for all flagged files:
/verify-accuracy "[file]" "[source]"

Or use the study-guide-analyzer agent for deep analysis.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

# Exit 0 - warnings only, not blockers
exit 0
