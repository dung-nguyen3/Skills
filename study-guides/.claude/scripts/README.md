# Automated Quality Gate Scripts

## Purpose

Standalone scripts for automated quality validation of study guides. These scripts can be run manually or integrated into CI/CD pipelines.

---

## Available Scripts

### check-study-guides.sh

**Purpose:** Comprehensive quality gate check for all study guides in a directory

**Usage:**
```bash
# Check current directory
./check-study-guides.sh

# Check specific directory
./check-study-guides.sh "/path/to/study/guides"
```

**Checks performed:**
1. File size validation (warns if < 10KB - likely incomplete)
2. Source file presence (searches common locations)
3. File readability

**Exit codes:**
- 0: All checks passed
- 1: Issues detected

**Output:**
- Summary of total guides, issues found
- Detailed list of problematic files
- Clear PASS/FAIL status

---

## Integration with Hooks

These scripts complement the hook system:

**Hooks (real-time):**
- Run automatically during creation
- Provide immediate feedback
- Prevent issues before they occur

**Scripts (batch validation):**
- Run on-demand or scheduled
- Check multiple files at once
- Suitable for CI/CD integration
- Can validate existing study guides

---

## Future Scripts

**Planned for future phases:**

`check-medical-accuracy.sh` - Basic fact-checking against source files

`check-template-compliance.sh` - Validate template structure

`validate-mnemonics.sh` - Check all mnemonics properly marked

`batch-verify.sh` - Run study-guide-analyzer on multiple files

---

## Usage in CI/CD

**Example GitHub Actions workflow:**
```yaml
name: Study Guide Quality Check

on: [push, pull_request]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run quality checks
        run: |
          chmod +x .claude/scripts/check-study-guides.sh
          .claude/scripts/check-study-guides.sh "path/to/guides"
```

---

## Manual Validation Workflow

**After creating multiple study guides:**
```bash
# 1. Run quality gate check
cd "/path/to/Copy Study Guide Claude Q3 2"
.claude/scripts/check-study-guides.sh "Claude Study Tools"

# 2. Review output
# 3. Fix any issues detected
# 4. Re-run until passing
```

---

## Notes

- Scripts are independent of Claude Code
- Can run in any bash environment
- Designed for batch validation
- Complement (don't replace) hook system
- Exit codes suitable for automation

---

**See also:**
- Hook system: `.claude/hooks/`
- Skills: `.claude/skills/`
- Phase 5.4 documentation: `PHASE_5_IMPLEMENTATION.md`
