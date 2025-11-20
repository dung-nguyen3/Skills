# Hook State Directory

This directory stores persistent state for hooks across Claude Code sessions.

## Purpose

Hooks can store data here to maintain context between sessions:
- Track which study guides have been verified
- Store verification checklists completion status
- Track mnemonic research history
- Maintain creation timestamps and metadata

## File Naming Convention

`{session_id}_{hook_name}.json` - Session-specific state
`global_{hook_name}.json` - Cross-session persistent state

## Usage Examples

**Verification tracking:**
```json
{
  "study_guides_created": [
    {
      "file": "HIV_Drug_Chart.xlsx",
      "created": "2025-11-18T10:30:00Z",
      "verified": true,
      "source": "HIV Drugs.txt"
    }
  ]
}
```

**Mnemonic cache:**
```json
{
  "mnemonics": {
    "HIV antiretrovirals": "Research completed 2025-11-18",
    "Beta blockers": "Research completed 2025-11-15"
  }
}
```

## Notes

- State files are NOT committed to git (see .gitignore)
- Hooks should handle missing state files gracefully
- Clean up old session state files periodically
