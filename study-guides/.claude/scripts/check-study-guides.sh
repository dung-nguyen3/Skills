#!/bin/bash
# Automated quality gate: Check all study guides have proper setup
# Usage: ./check-study-guides.sh [directory]
# Returns: 0 if all checks pass, 1 if any failures

set -eo pipefail

# Directory to check (default: current directory)
CHECK_DIR="${1:-.}"

# Initialize counters
total_guides=0
missing_sources=0
small_files=0
errors=()

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STUDY GUIDE QUALITY GATE CHECK"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Checking directory: $CHECK_DIR"
echo ""

# Find all study guide files
while IFS= read -r file; do
    total_guides=$((total_guides + 1))
    filename=$(basename "$file")
    dir=$(dirname "$file")

    # Check 1: File size (warn if < 10KB)
    filesize=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null || echo "0")
    if [[ $filesize -lt 10240 ]]; then
        small_files=$((small_files + 1))
        errors+=("⚠️  $filename: Small file size (${filesize} bytes) - may be incomplete")
    fi

    # Check 2: Look for source file in common locations
    source_found=false
    for source_dir in "$dir" "$dir/../Extract" "$dir/../Sources" "$dir/../../Extract"; do
        if [[ -d "$source_dir" ]]; then
            if find "$source_dir" -maxdepth 1 -type f \( -name "*.txt" -o -name "*.md" -o -name "*.pdf" \) 2>/dev/null | grep -q .; then
                source_found=true
                break
            fi
        fi
    done

    if [[ "$source_found" = false ]]; then
        missing_sources=$((missing_sources + 1))
        errors+=("❌ $filename: No source file found in common locations")
    fi

done < <(find "$CHECK_DIR" -type f \( -name "*.xlsx" -o -name "*.docx" -o -name "*.html" \) 2>/dev/null)

# Display results
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Total study guides found: $total_guides"
echo "Missing source files: $missing_sources"
echo "Small files (< 10KB): $small_files"
echo ""

if [[ ${#errors[@]} -gt 0 ]]; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "ISSUES DETECTED"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    printf '%s\n' "${errors[@]}"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "STATUS: ❌ FAILED - Issues found"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    exit 1
else
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "STATUS: ✅ PASSED - All checks passed"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    exit 0
fi
