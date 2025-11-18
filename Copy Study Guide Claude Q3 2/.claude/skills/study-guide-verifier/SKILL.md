---
name: study-guide-verifier
description: |
  CRITICAL: Systematic verification of study guide accuracy against source files.

  ACTIVATES when user requests accuracy verification, post-creation validation,
  or analysis of existing study guides.

  Implements the 6-step verification protocol to ensure study guides contain
  only source-accurate information with complete coverage and proper formatting.
skill_type: domain
enforcement_level: suggest
priority: critical
version: 1.0.0
tools_required:
  - Read
  - Grep
activation_confidence: high
---

# Study Guide Verifier

## Core Responsibility

Systematic verification of study guide accuracy against source files using the 6-step protocol.

## When This Activates

**Prompt triggers:**
- "verify accuracy"
- "check study guide"
- "analyze accuracy"
- "/verify-accuracy [file] [source]"
- "post-creation verification"

**File triggers:**
- Study guide files in `Claude Study Tools/`
- Files ending in `.xlsx`, `.docx`, `.html`

## 6-Step Verification Protocol

When activated, follow this systematic approach:

### Step 1: File Identification
- Read the study guide file completely
- Read the source file completely
- Identify template type (Excel, Word, HTML)

### Step 2: Source Accuracy Check
Verify:
- ✓ All information from source file only (except mnemonics)
- ✓ External additions marked with asterisk (*)
- ✓ Page references included where required
- ✓ No invented facts or assumptions

### Step 3: Template Compliance
Verify:
- ✓ ALL template instructions followed exactly
- ✓ Correct structure (all tabs/sections present)
- ✓ Correct formatting (colors, fonts, styles)
- ✓ All required elements included

### Step 4: Completeness Check
Verify:
- ✓ All learning objectives answered (all parts)
- ✓ All comparison tables created
- ✓ Master chart includes ALL topics
- ✓ No missing content from source

### Step 5: Quality Checks
Verify:
- ✓ No incorrect groupings or merged cells
- ✓ No spelling errors
- ✓ Proper formatting throughout
- ✓ Consistent terminology

### Step 6: Final Report
Provide comprehensive report:
```markdown
## Verification Report

**Source Accuracy:** [PASS/FAIL]
- Issues found: [list or "None"]

**Template Compliance:** [PASS/FAIL]
- Issues found: [list or "None"]

**Completeness:** [PASS/FAIL]
- Missing content: [list or "None"]

**Quality:** [PASS/FAIL]
- Issues found: [list or "None"]

**Overall Assessment:** [PASS/FAIL]

**Recommended Actions:**
1. [specific fixes needed]
2. [improvements to make]
```

## Usage Examples

**Manual verification:**
```
User: "Verify accuracy of HIV_Drug_Chart.xlsx against source"
You:
1. Read study guide completely
2. Read source file completely
3. Run 6-step protocol
4. Provide detailed report
```

**Slash command verification:**
```
/verify-accuracy "Pharmacology/Exam 3/Claude Study Tools/HIV_Drug_Chart.xlsx" "Pharmacology/Exam 3/Extract/HIV Antivirals.txt"
```

## Common Issues to Check

### Source Accuracy
- External medical facts added without source
- Invented mnemonics (should be researched via WebSearch)
- Assumptions or generalizations not in source
- Missing page references

### Template Compliance
- Wrong color scheme (must match template)
- Missing tabs/sections
- Incorrect structure
- Missing required elements

### Completeness
- Partial answers to learning objectives
- Missing comparison tables
- Incomplete master chart
- Skipped topics

### Quality
- Spelling errors
- Inconsistent formatting
- Incorrect drug groupings
- Merged cells where not appropriate

## Integration with Other Skills

Works with:
- **source-only-enforcer:** Verifies source-only policy was followed
- **template-compliance-checker:** Deep-checks template adherence
- **mnemonic-researcher:** Verifies mnemonics were researched, not invented

## Tips

💡 Use `/verify-accuracy` slash command for automated 6-step protocol

💡 Run verification immediately after creation (post-creation verification)

💡 Re-verify if making significant edits to study guide

💡 Keep source file open during verification for quick reference
