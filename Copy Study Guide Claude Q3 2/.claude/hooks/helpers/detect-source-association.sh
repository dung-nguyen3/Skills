#!/bin/bash
# Helper script to detect source file associations for study guides
# Called by PostToolUse hook to track which source file goes with which study guide

set -eo pipefail

study_guide_file="$1"
session_cache_dir="$2"

if [[ -z "$study_guide_file" ]] || [[ -z "$session_cache_dir" ]]; then
    exit 0
fi

# Extract directory containing the study guide
study_guide_dir=$(dirname "$study_guide_file")
study_guide_name=$(basename "$study_guide_file")

# Common source file locations to check (in order of priority)
search_dirs=(
    "$study_guide_dir"                    # Same directory as study guide
    "$study_guide_dir/../Extract"         # Extract folder (sibling)
    "$study_guide_dir/../Sources"         # Sources folder (sibling)
    "$study_guide_dir/../../Extract"      # Extract folder (parent sibling)
    "$study_guide_dir/../../Sources"      # Sources folder (parent sibling)
)

# Common source file patterns
source_patterns=(
    "*.txt"
    "*.md"
    "*.pdf"
    "*Lecture*.txt"
    "*Notes*.txt"
    "*Source*.txt"
)

# Try to find source file in common locations
found_source=""

for dir in "${search_dirs[@]}"; do
    if [[ ! -d "$dir" ]]; then
        continue
    fi

    for pattern in "${source_patterns[@]}"; do
        # Find files matching pattern (most recently modified first)
        while IFS= read -r file; do
            if [[ -f "$file" ]]; then
                # Found a potential source file
                found_source="$file"
                break 2
            fi
        done < <(find "$dir" -maxdepth 1 -type f -name "$pattern" -printf '%T@ %p\n' 2>/dev/null | sort -rn | cut -d' ' -f2-)
    done
done

# If found, save association
if [[ -n "$found_source" ]]; then
    echo "$study_guide_file|$found_source|$(date +%s)" >> "$session_cache_dir/source-associations.txt"
    echo "$found_source"  # Return source path
    exit 0
else
    # No source found - mark as missing
    echo "$study_guide_file|MISSING|$(date +%s)" >> "$session_cache_dir/source-associations.txt"
    exit 1
fi
