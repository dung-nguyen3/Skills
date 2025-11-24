# 6-Step Verification Protocol (Detailed Guide)

## Purpose

Comprehensive guide to the study-guide-analyzer agent's 6-step verification methodology.

---

## Overview

The 6-step protocol ensures systematic verification of every study guide against its source material.

**Steps:**
1. Read Source File Completely
2. Read Study Guide Completely
3. Systematic Verification Checks
4. Document All Issues (Critical/Important/Minor)
5. Save Analysis Report
6. Return to Parent Process and Request Approval

---

## Step 1: Read Source File Completely

**Goal:** Load entire source into context for comparison

**Process:**
```
1. User provides source file path
2. Use Read tool to load complete source
3. If source >2000 lines → read in chunks
4. Note source structure (sections, pages, organization)
5. Identify key topics covered
```

**What to capture:**
- All medical facts presented
- How information is organized
- What's explicitly stated vs. implied
- Any mnemonics source provides
- Level of detail for each topic

**Common issues:**
- Source file path incorrect → request valid path
- Source file too large → read in multiple passes
- Source file unreadable → report error

---

## Step 2: Read Study Guide Completely

**Goal:** Load entire study guide for verification

**Process:**
```
1. Use Read tool for study guide file
2. Note template type (Excel/HTML/Word)
3. Identify all sections/tabs
4. Note which sections filled vs. empty
5. Capture all facts, tables, comparisons
```

**What to capture:**
- Every fact stated in study guide
- All mnemonics (source vs. researched)
- Template structure and organization
- Sections marked as "Not covered"
- Any citations or source references

**Excel-specific:**
- Read all tabs (Drug Details, Key Comparisons, Master Chart, High-Yield)
- Note formulas/formatting
- Check for hidden rows/columns

**HTML-specific:**
- Read all tabs/sections
- Note styling and organization
- Check for links or external references

---

## Step 3: Systematic Verification Checks

**Goal:** Compare study guide against source fact-by-fact

### Check 3.1: Source Accuracy

**For EVERY fact in study guide:**
```
1. Locate fact in source file
2. Verify exact match (or paraphrase if acceptable)
3. Flag if not found in source (hallucination)
4. Flag if contradicts source
5. Flag if source says something different
```

**Acceptable variations:**
- Paraphrasing (same meaning, different words)
- Reorganization (facts in different order)
- Formatting (tables vs. paragraphs)

**NOT acceptable:**
- Adding facts not in source
- Changing meaning
- Inferring unstated information
- Extrapolating from source

### Check 3.2: Completeness

**Verify all source content included:**
```
1. List all topics in source
2. Check if each topic addressed in study guide
3. Flag missing topics (if they should be included)
4. Verify detail level matches source
```

**Note:** Missing topics are OK if:
- Source topic irrelevant to template type
- User requested specific topics only
- Marked as "Not covered in source"

### Check 3.3: Template Compliance

**Verify template structure followed:**

**Excel Drug Chart:**
- [ ] All 4 tabs present (Drug Details, Key Comparisons, Master Chart, High-Yield)
- [ ] Drug Details tab has all columns
- [ ] Key Comparisons has comparison tables
- [ ] Master Chart has ALL drugs
- [ ] High-Yield has summary

**HTML Learning Objectives:**
- [ ] All 4 tabs present (LO Q&A, Key Comparisons, Master Tables, Summary)
- [ ] LO Q&A has questions AND answers
- [ ] Key Comparisons has comparison tables
- [ ] Master Tables has organized reference tables
- [ ] Summary has high-yield review

**Clinical Assessment:**
- [ ] Organized by chief complaint
- [ ] History-taking sections present
- [ ] Physical exam sections present
- [ ] OLDCAARTS format if applicable

### Check 3.4: Mnemonic Verification

**For every mnemonic:**
```
1. Check if mnemonic is from source
   - If yes → should NOT have asterisk (*)
   - If no → should have asterisk (*) and source attribution

2. For researched mnemonics:
   - Verify asterisk (*) present
   - Verify source attribution (r/medicalschool, First Aid, etc.)
   - Verify mnemonic components match study guide facts
   - Check reliability rating if provided

3. Flag issues:
   - Invented mnemonics (not from source, not researched)
   - Unmarked researched mnemonics
   - Mnemonics with incorrect components
   - Vague source attribution ("common mnemonic")
```

### Check 3.5: Citation Verification

**If study guide uses citations:**
```
1. Verify page numbers correct
2. Check section references accurate
3. Confirm all citations point to source file (not external)
4. Flag broken or incorrect citations
```

### Check 3.6: Quality Checks

**Additional quality verification:**
- [ ] No spelling errors in medical terms
- [ ] Drug names spelled correctly
- [ ] Abbreviations defined or used consistently
- [ ] Formatting consistent throughout
- [ ] No broken tables or missing data
- [ ] No placeholder text left in guide

---

## Step 4: Document All Issues

**Goal:** Categorize and describe every issue found

### Issue Categorization

**CRITICAL Issues** (must fix before use):
- Medical facts not in source (hallucinations)
- Facts contradicting source
- Invented mnemonics
- Missing required template sections
- Medical inaccuracies

**IMPORTANT Issues** (should fix):
- Unmarked researched mnemonics
- Missing citations
- Incomplete sections that should be complete
- Template compliance violations
- Formatting inconsistencies

**MINOR Issues** (nice to fix):
- Spelling errors in non-medical terms
- Formatting preferences
- Optional enhancements
- Stylistic improvements

### Issue Documentation Format

**For each issue:**
```
Category: [CRITICAL/IMPORTANT/MINOR]
Location: [Tab name, section, line number]
Issue: [Description]
Evidence: [Quote from study guide]
Source Check: [What source says, or "Not found in source"]
Recommendation: [How to fix]
```

**Example:**
```
Category: CRITICAL
Location: Drug Details tab, Row 5 (Zidovudine), Side Effects column
Issue: Hallucination - "GI upset" added but not in source
Evidence: Study guide states "Side effects: Bone marrow suppression, anemia, neutropenia, GI upset"
Source Check: Source lists "Side effects: Bone marrow suppression, anemia, neutropenia" (no GI upset mentioned)
Recommendation: Remove "GI upset" from side effects list
```

---

## Step 5: Save Analysis Report

**Goal:** Create detailed analysis document for user review

### Report Structure

```markdown
# Study Guide Verification Report

**Study Guide:** [filename]
**Source File:** [source filename]
**Template Type:** [type]
**Verification Date:** [date]
**Verified By:** study-guide-analyzer agent

---

## Verification Summary

**Total Issues Found:** [count]
- Critical: [count]
- Important: [count]
- Minor: [count]

**Recommendation:** [APPROVED / NEEDS REVISION / FAILED]

---

## Critical Issues

[List all critical issues with full documentation]

---

## Important Issues

[List all important issues]

---

## Minor Issues

[List all minor issues]

---

## Source Accuracy Analysis

**Facts verified:** [X/Y total facts]
**Hallucinations detected:** [count]
**Missing content:** [list or none]

---

## Template Compliance

[Check results for template structure]

---

## Mnemonic Verification

**Total mnemonics:** [count]
- From source: [count]
- Researched (marked): [count]
- Issues: [count]

---

## Recommendations

[Specific actions needed before approving study guide]

---

## Verification Checklist

- [ ] All critical issues resolved
- [ ] Important issues addressed
- [ ] Study guide ready for use

---

**Next Steps:**
1. Review all critical issues
2. Fix issues in study guide
3. Re-run verification if major changes made
4. Approve for use once clean
```

### Report Filename

**Convention:** `[study-guide-name]-verification-report.md`

**Example:** `HIV_Drug_Chart-verification-report.md`

**Location:** Same directory as study guide

---

## Step 6: Return to Parent Process and Request Approval

**Goal:** Present findings and get user approval

### Report Presentation

```
1. Show verification summary (counts of issues)
2. Highlight critical issues
3. Present recommendation (APPROVED/NEEDS REVISION/FAILED)
4. Ask user:
   - Review full report?
   - Proceed with fixes?
   - Approve despite issues?
```

### Approval Workflow

**If APPROVED (0 critical issues):**
```
- Congratulate user on clean study guide
- Save verification completion marker
- Study guide ready for use
```

**If NEEDS REVISION (1-5 critical issues):**
```
- List specific fixes needed
- Offer to help fix issues
- Recommend re-verification after fixes
- Mark study guide as "pending revision"
```

**If FAILED (6+ critical issues or systematic hallucination):**
```
- Recommend recreating study guide
- Identify root cause (sparse source, rushing, etc.)
- Suggest using stricter creation method
- Do NOT approve for use
```

---

## Best Practices

### Thoroughness
- Don't skip steps
- Verify every fact (random sampling not sufficient)
- Check all tabs/sections
- Document ALL issues (even minor ones)

### Objectivity
- Flag issues even if "probably fine"
- Don't excuse hallucinations as "minor additions"
- Strict interpretation of source-only policy
- User can decide to ignore minor issues

### Clarity
- Use specific examples in report
- Quote exact text from study guide and source
- Provide clear fix recommendations
- Make report actionable

### Efficiency
- Use systematic approach (don't jump around)
- Document as you verify (don't wait until end)
- Group similar issues together
- Prioritize critical issues in report

---

## Common Pitfalls

**Pitfall 1: Confirmation Bias**
- Assuming study guide is correct
- Skimming instead of careful verification
- Missing subtle hallucinations

**Solution:** Approach skeptically, verify everything

**Pitfall 2: False Positives**
- Flagging acceptable paraphrasing as hallucination
- Marking reorganization as error
- Being too strict on wording

**Solution:** Focus on meaning, not exact wording

**Pitfall 3: Missing Context**
- Verifying facts in isolation
- Not considering full source context
- Missing nuances

**Solution:** Re-read source sections for full context

---

## Summary

**6 steps ensure:**
1. Complete source understanding
2. Complete study guide understanding
3. Systematic fact-by-fact verification
4. Clear issue categorization
5. Documented findings
6. User approval workflow

**Success criteria:**
- Every fact verified against source
- All issues documented and categorized
- Clear recommendation provided
- User can make informed decision

**Remember:**
- Thoroughness over speed
- Objectivity over leniency
- Clarity over brevity
- Source fidelity is paramount

---

**See also:**
- [Template Compliance Guide](template-compliance.md)
- [Accuracy Checking Methods](accuracy-checking.md)
- [Common Errors Guide](common-errors.md)
