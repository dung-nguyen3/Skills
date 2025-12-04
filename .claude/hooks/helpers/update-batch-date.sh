#!/bin/bash
# Helper script to update last batch processing date
# Call this from batch commands to reset the weekly reminder timer

LAST_BATCH_FILE="$HOME/.claude/last_batch_date"
mkdir -p "$HOME/.claude"
date +%s > "$LAST_BATCH_FILE"
