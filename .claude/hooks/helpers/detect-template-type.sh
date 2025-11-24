#!/bin/bash
# Helper script to detect template type for study guides
# Called by PostToolUse hook to categorize study guides

set -eo pipefail

file_path="$1"

if [[ -z "$file_path" ]]; then
    exit 0
fi

filename=$(basename "$file_path")
file_ext="${filename##*.}"

# Template type detection based on filename patterns and file type
template_type="unknown"

case "$file_ext" in
    xlsx)
        # Excel files - Drug Chart template (4-tab)
        template_type="excel-drug-chart"
        ;;
    docx)
        # Word files - Learning Objectives template
        if [[ "$filename" =~ [Cc]linical|[Hh]istory|[Ee]xam|[Pp]hysical ]]; then
            template_type="word-clinical-assessment"
        else
            template_type="word-learning-objectives"
        fi
        ;;
    html)
        # HTML files - could be Drug Chart HTML or LO HTML
        if [[ "$filename" =~ [Dd]rug.*[Cc]hart ]]; then
            template_type="html-drug-chart"
        elif [[ "$filename" =~ [Cc]linical|[Hh]istory|[Ee]xam ]]; then
            template_type="html-clinical-assessment"
        else
            template_type="html-learning-objectives"
        fi
        ;;
    *)
        template_type="unknown"
        ;;
esac

echo "$template_type"
exit 0
