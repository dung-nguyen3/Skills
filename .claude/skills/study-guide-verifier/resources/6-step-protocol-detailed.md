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

**Checks in this step:**
- 3.1: Source Accuracy
- 3.2: Completeness
- 3.3: Template Compliance (Comprehensive)
- 3.4: Mnemonic Verification
- 3.5: Citation Verification
- 3.6: Quality Checks
- 3.7: Learning Objective Text Fidelity (CRITICAL)
- 3.8: Comparison Table Completeness (CRITICAL)

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
- Reorganization (facts in different order)
- Formatting (tables vs. paragraphs)
- Paraphrasing of ANSWERS/CONTENT (same meaning, different words)

**NOT acceptable:**
- Adding facts not in source
- Changing meaning
- Inferring unstated information
- Extrapolating from source
- **Paraphrasing learning objective STATEMENTS** (see Check 3.7)

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

### Check 3.3: Template Compliance (COMPREHENSIVE)

**CRITICAL: Verify ALL template requirements, not just tab existence.**

---

#### Excel Drug Chart (4 tabs)

**Tab Structure:**
- [ ] Tab 1: "Drug Details" exists
- [ ] Tab 2: "Key Comparisons" exists
- [ ] Tab 3: "Master Chart" exists
- [ ] Tab 4: "High-Yield & Pearls" exists

**Tab 1 (Drug Details) Requirements:**
- [ ] One comparison table per drug class (NOT all classes in one table)
- [ ] Columns = drugs, Rows = properties
- [ ] Analogy column (Column G) present with 2-4 sentence analogies
- [ ] Memory tricks row after EACH drug class table
- [ ] Merged cells ONLY for class-wide information (not drug-specific)

**Tab 2 (Key Comparisons) Requirements:**
- [ ] Comparisons ACROSS drug classes (not within single class)
- [ ] Categories: Mechanisms, Toxicities, Uses, Interactions

**Tab 3 (Master Chart) Requirements:**
- [ ] ALL drugs in ONE table (no missing drugs)
- [ ] Header row frozen
- [ ] Rows = individual drugs, Columns = characteristics

**Tab 4 (High-Yield) Requirements:**
- [ ] Clinical pearls section (teal background #E0F2F1)
- [ ] Memory tricks section (orange background #FFF3E0)
- [ ] Must-know facts section (purple background #F3E5F5)

---

#### Excel Comparison Chart (3 tabs)

**Tab Structure:**
- [ ] Tab 1: "Key Comparisons" exists
- [ ] Tab 2: "Master Chart" exists
- [ ] Tab 3: "Summary" exists

**Tab 1 (Key Comparisons) Requirements:**
- [ ] MULTIPLE comparison tables (one category per table)
- [ ] NOT one giant table combining all categories
- [ ] Columns = items compared, Rows = features
- [ ] Mnemonics placed DIRECTLY BELOW relevant tables
- [ ] 2-3 blank rows between different comparison tables

**Tab 2 (Master Chart) Requirements:**
- [ ] ALL items in one comprehensive table
- [ ] Header row frozen
- [ ] Color-coded by category

**Tab 3 (Summary) Requirements:**
- [ ] Mnemonics section (with full breakdown)
- [ ] "If X Think Y" associations
- [ ] Critical values (if applicable)
- [ ] Key definitions
- [ ] High-yield pearls

---

#### Excel Master Chart (1 tab)

**Tab Structure:**
- [ ] Single sheet named "Master Chart"

**Requirements:**
- [ ] ALL items from source in one table
- [ ] Header row frozen
- [ ] User-specified columns (or defaults)
- [ ] Color-coded by class/group
- [ ] First column (class/group) bold

---

#### Word Learning Objectives (4 sections)

**Section Structure:**
- [ ] Section 1: Learning Objectives
- [ ] Section 2: Key Comparisons
- [ ] Section 3: Master Chart
- [ ] Section 4: High-Yield Summary

**Section 1 (Learning Objectives) Requirements:**
- [ ] Each LO has: Summary + Tables + Pearls Box + Mnemonics Box + Analogy Box
- [ ] Page break after each LO

**Section 2 (Key Comparisons) Requirements:**
- [ ] Comparison tables for 2+ similar items
- [ ] Analogy column for drug mechanisms

**Section 3 (Master Chart) Requirements:**
- [ ] ALL conditions/topics from source
- [ ] Color-coded rows

**Section 4 (High-Yield Summary) Requirements:**
- [ ] Color-coded boxes grouped by category

**Word Formatting:**
- [ ] Font: Calibri size 12 (11 for dense tables)
- [ ] Table style: 'Table Grid'
- [ ] Headers: Bold, colored background (pastel)
- [ ] Data cells: Black text, white background
- [ ] Margins: 0.8 inches all sides
- [ ] Headings: Purple (118, 75, 162)

---

#### HTML Learning Objectives (4 tabs)

**Tab Structure:**
- [ ] Tab 1: "LO Q&A" exists
- [ ] Tab 2: "Key Comparisons" exists
- [ ] Tab 3: "Master Tables" exists
- [ ] Tab 4: "Summary" exists

**Requirements per tab:** Similar to Word structure
**Formatting:** CSS styles matching color scheme

---

#### Clinical Assessment Guide

- [ ] Organized by chief complaint
- [ ] History-taking sections present (OLDCAARTS)
- [ ] Physical exam sections present
- [ ] Color-coded sections
- [ ] Decision support ("If X, Think Y")

---

#### Formatting Requirements (ALL Excel Files)

**CRITICAL - Verify EVERY formatting requirement:**

**Colors:**
- [ ] Header row: #4472C4 (dark blue), white bold text, size 12
- [ ] Data rows: Pastel colors rotating by category
- [ ] ALL data cells have background color (NOT white/no fill)
- [ ] Same category = same color (one color per category)
- [ ] Colors rotate when category changes

**Color Palette (must use these exact hex codes):**
```
1. #D9E2F3 (Ice Blue)
2. #C8E6C9 (Seafoam)
3. #D1C4E9 (Light Orchid)
4. #F7E7CE (Champagne)
5. #BDD7EE (Sky Blue)
6. #F0F8FF (Pale Azure)
7. #FCE4EC (Blush Pink)
8. #EDE7F6 (Soft Lilac)
9. #FFE8D6 (Soft Tangerine)
10. #BBDEFB (Powder Blue)
```

**Other Formatting:**
- [ ] White borders (#FFFFFF) on all cells
- [ ] Text: Black (#000000), Calibri, size 11
- [ ] Column widths: 25-40 based on content type
- [ ] Row heights: Auto-expand to fit content
- [ ] Text wrapping enabled on all cells
- [ ] Frozen header row on Master Chart tabs

**CRITICAL: Flag as IMPORTANT issue if ANY formatting requirement is not met.**

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

### Check 3.7: Learning Objective Text Fidelity (CRITICAL)

**Learning objective STATEMENTS must be VERBATIM from source.**

<verbatim-requirement>
CRITICAL: Learning objectives must be copied EXACTLY as they appear in the source.
- Copy word-for-word, character-for-character
- Do NOT rephrase, summarize, or "improve" wording
- Preserve original numbering and sequence
- If an LO is long, still copy it completely
</verbatim-requirement>

**For EVERY learning objective statement:**
```
1. Find exact LO text in source file
2. Compare character-by-character with study guide
3. Flag ANY rewording as CRITICAL issue
4. Verify original numbering/order preserved
```

**CORRECT (verbatim):**
```
Source: "1. Describe the mechanism of action of beta-blockers"
Guide:  "1. Describe the mechanism of action of beta-blockers"
Status: ✓ PASS
```

**INCORRECT (paraphrased):**
```
Source: "1. Describe the mechanism of action of beta-blockers"
Guide:  "1. Explain how beta-blockers work"
Status: ✗ FAIL - Learning objective was paraphrased
```

**Note:** This check applies ONLY to LO statements themselves, NOT to answers/explanations. Answers can still be paraphrased from source content.

### Check 3.8: Comparison Table Completeness (CRITICAL)

**Ensure comparison tables include ALL comparable items from source.**

**Purpose:** Prevents the common error of skipping items that should be compared.

#### 3.8.A: Source Item Count

For EACH comparison table in the study guide:
```
1. Identify the comparison category (diagnostics, treatments, mechanisms, etc.)
2. Return to source file
3. Count ALL items mentioned for that category
4. Document: "Source contains [N] items for [category] comparison"
```

#### 3.8.B: Table Item Count

```
1. Count items actually present in the comparison table
2. Document: "Table contains [M] items"
```

#### 3.8.C: Gap Analysis

```
If N ≠ M:
- List EVERY missing item explicitly
- Mark as ERROR: "Comparison table missing: [X, Y, Z]"
- This is an IMPORTANT or CRITICAL issue depending on significance
```

#### 3.8.D: Common Omissions to Check

| Category | Commonly Skipped Items | Verification Action |
|----------|----------------------|---------------------|
| Diagnostic tests | Lab tests, less common imaging, physical exam findings | Count ALL tests mentioned in source |
| Treatments | Secondary options, adjunct therapies, alternatives | Verify ALL treatment options included |
| Drug classes | "Similar" drugs, less common members of class | Each drug name from source gets own column |
| Conditions | Rare differentials, conditions with sparse details | Include even if some table cells sparse |
| Mechanisms | Items mentioned only briefly | Systematic source scan catches all |

#### 3.8.E: LO Style Handling

**When verifying, consider how the LO references items:**

| LO Style | Example | Verification Action |
|----------|---------|---------------------|
| General category | "Compare the diagnostic tools for PE" | Count ALL diagnostic tools for PE in source |
| Specific items | "Compare D-dimer, CT, and V/Q" | Verify exactly those 3 items present |
| Class reference | "Describe NRTIs" | Count ALL individual NRTI drug names in source |

**Key Principle:** If LO says "drug class", "conditions", "diagnostic tools", etc. without listing specifics, verify ALL individual items from that category in the source are included.

#### 3.8.F: Documentation Format

**For each comparison table, document:**
```
COMPARISON TABLE: [Category name]
Source item count: [N]
Table item count: [M]
Status: [PASS if N=M / FAIL if N≠M]
Missing items: [list if any]
```

**Example Issue:**
```
Category: IMPORTANT
Location: Key Comparisons tab, Diagnostic Tests table
Issue: Comparison table missing items from source
Evidence: Table compares 3 tests (CT, D-dimer, ECG)
Source Check: Source mentions 5 tests (CT, D-dimer, ECG, V/Q scan, Chest X-ray)
Missing: V/Q scan, Chest X-ray
Recommendation: Add V/Q scan and Chest X-ray columns to comparison table
```

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
- Flagging acceptable paraphrasing of ANSWERS as hallucination
- Marking reorganization as error
- Being too strict on wording of explanatory content

**Solution:** Focus on meaning for ANSWERS, but require exact wording for LEARNING OBJECTIVE STATEMENTS (see Check 3.7)

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
