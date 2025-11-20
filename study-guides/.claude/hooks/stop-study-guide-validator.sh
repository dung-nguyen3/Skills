#!/bin/bash
set -eo pipefail

# Stop hook that validates study guide quality metrics
# Runs quick validation checks without blocking
# Complements the main verification-completion-check.sh

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
    exit 0  # No work this session
fi

# Check template types distribution
template_types_file="$cache_dir/template-types.txt"
if [[ -f "$template_types_file" ]]; then
    # Count template types used this session
    excel_count=$(grep -c "excel-drug-chart" "$template_types_file" 2>/dev/null || echo "0")
    word_count=$(grep -c "word-learning-objectives" "$template_types_file" 2>/dev/null || echo "0")
    html_count=$(grep -c "html-learning-objectives\|html-drug-chart" "$template_types_file" 2>/dev/null || echo "0")
    clinical_count=$(grep -c "clinical-assessment" "$template_types_file" 2>/dev/null || echo "0")
    unknown_count=$(grep -c "unknown" "$template_types_file" 2>/dev/null || echo "0")

    total_templates=$((excel_count + word_count + html_count + clinical_count + unknown_count))

    # Show stats if any study guides created
    if [[ $total_templates -gt 0 ]]; then
        # Create summary
        echo "$excel_count" > "$cache_dir/metadata/excel-count.txt"
        echo "$word_count" > "$cache_dir/metadata/word-count.txt"
        echo "$html_count" > "$cache_dir/metadata/html-count.txt"
        echo "$clinical_count" > "$cache_dir/metadata/clinical-count.txt"

        # Log statistics for future analytics
        echo "$(date +%s)|excel:$excel_count|word:$word_count|html:$html_count|clinical:$clinical_count" >> "$cache_dir/metadata/session-stats.txt"
    fi
fi

# Check file sizes (warn about suspiciously small files)
file_sizes_file="$cache_dir/file-sizes.txt"
small_files=()
if [[ -f "$file_sizes_file" ]]; then
    while IFS='|' read -r filepath filesize timestamp; do
        # Warn if file is less than 10KB (likely incomplete)
        if [[ $filesize -lt 10240 ]]; then
            small_files+=("$(basename "$filepath") (${filesize} bytes)")
        fi
    done < "$file_sizes_file"
fi

# Display warnings if any
if [[ ${#small_files[@]} -gt 0 ]]; then
    cat <<EOF

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  FILE SIZE WARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Suspiciously small files detected (< 10 KB):

EOF
    for file in "${small_files[@]}"; do
        echo "   📄 $file"
    done

    cat <<EOF

Small file sizes may indicate incomplete study guides.

Recommend: Open files and verify completeness before use.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
fi

# Exit 0 - non-blocking validation
exit 0
