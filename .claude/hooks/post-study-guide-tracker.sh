#!/bin/bash
set -eo pipefail

# Enhanced PostToolUse hook for study guide creation tracking
# This runs AFTER Edit, MultiEdit, or Write tools complete successfully
# Tracks: file creation, source associations, template types, metadata

# Emergency override: Skip all verification checks
if [[ -n "$SKIP_STUDY_GUIDE_VERIFICATION" ]]; then
    exit 0
fi

# Check for jq dependency
if ! command -v jq &>/dev/null; then
    exit 0  # Fail-open if jq is missing
fi

# Read tool information from stdin
tool_info=$(cat)

# Extract relevant data with error handling
tool_name=$(echo "$tool_info" | jq -r '.tool_name // empty' 2>/dev/null || echo "")
file_path=$(echo "$tool_info" | jq -r '.tool_input.file_path // empty' 2>/dev/null || echo "")
session_id=$(echo "$tool_info" | jq -r '.session_id // empty' 2>/dev/null || echo "")

# Fallback session ID if extraction failed
if [[ -z "$session_id" ]]; then
    session_id="fallback-$(date +%Y%m%d-%H%M%S)"
fi

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

# State directory for tracking (using study-guide-cache)
cache_dir="$CLAUDE_PROJECT_DIR/.claude/study-guide-cache/${session_id}"
mkdir -p "$cache_dir"

# Create metadata directory
mkdir -p "$cache_dir/metadata"

# Log file creation with timestamp
timestamp=$(date +%s)
echo "$timestamp:$file_path:created" >> "$cache_dir/created-files.log"

# Detect and log template type
helpers_dir="$CLAUDE_PROJECT_DIR/.claude/hooks/helpers"
if [[ -x "$helpers_dir/detect-template-type.sh" ]]; then
    template_type=$("$helpers_dir/detect-template-type.sh" "$file_path" 2>/dev/null || echo "unknown")
    echo "$file_path|$template_type|$timestamp" >> "$cache_dir/template-types.txt"
fi

# Detect and log source file association
if [[ -x "$helpers_dir/detect-source-association.sh" ]]; then
    source_file=$("$helpers_dir/detect-source-association.sh" "$file_path" "$cache_dir" 2>/dev/null || echo "")

    if [[ -z "$source_file" ]]; then
        # No source found - log as critical issue
        echo "$file_path|NO_SOURCE|$timestamp" >> "$cache_dir/critical-issues.log"
    fi
fi

# Log file metadata (size, modification time, etc.)
if [[ -f "$file_path" ]]; then
    file_size=$(stat -c%s "$file_path" 2>/dev/null || echo "0")
    echo "$file_path|$file_size|$timestamp" >> "$cache_dir/file-sizes.txt"
fi

# Exit silently - don't show output (other hook will show reminder)
exit 0
