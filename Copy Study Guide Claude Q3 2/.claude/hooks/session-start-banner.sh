#!/bin/bash

# SessionStart hook that displays study guide quality protocol requirements
# This runs when a Claude Code session starts

cat <<'EOF'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 STUDY GUIDE QUALITY PROTOCOL ACTIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  MANDATORY: All study guides require verification

✅ Pre-Creation Verification Checklist:
   - Source file path specified
   - Template identified
   - Source-only policy confirmed
   - Mnemonics will be researched (WebSearch required)

✅ Post-Creation Verification Required:
   - Source accuracy check
   - Template compliance check
   - Completeness check
   - Quality check

💡 Use slash commands for automatic compliance:
   /create-excel [source-file]
   /create-word [source-file]
   /verify-accuracy [file] [source]

🔒 Quality gates are ACTIVE and will enforce these requirements.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

exit 0
