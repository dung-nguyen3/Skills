# Source Validation Guide

## Purpose

This resource provides comprehensive guidance on validating source files and ensuring all study guide content comes exclusively from the source.

---

## Source File Requirements

### Valid Source Files

**Accepted formats:**
- `.txt` - Plain text lecture notes, transcripts
- `.md` - Markdown formatted notes
- `.pdf` - Lecture slides, textbook excerpts
- `.docx` - Word documents with notes

**Required characteristics:**
1. **Medical content** - Must contain medical information relevant to study guide topic
2. **Sufficiently detailed** - Must have enough information to create comprehensive study guide
3. **Readable by Claude** - Must be accessible via Read tool

### Invalid Source Files

**DO NOT accept:**
- Empty files or files with < 100 words
- Files with only headings/outlines (insufficient detail)
- Files requiring external knowledge to understand
- Files in languages Claude cannot process
- Corrupted or unreadable files

---

## Source Validation Protocol

### Step 1: Verify Source File Exists

```
1. User provides source file path
2. Use Read tool to load source file
3. Confirm file exists and is readable
4. If file doesn't exist → BLOCK and request valid path
```

**Error handling:**
```
If Read tool fails:
- Check if path is correct (typos, wrong directory)
- Check if file format is supported
- Request user to verify file location
- NEVER proceed without valid source file
```

### Step 2: Validate Source Content

```
1. Read entire source file (no skipping)
2. Check word count (minimum 100 words for basic guides)
3. Verify content is medical/educational
4. Confirm sufficient detail for requested guide type
```

**Insufficient content indicators:**
- Only bullet points without explanations
- Just headings/titles
- Outline format without details
- Less than 1 page of actual content

**Action if insufficient:**
- Inform user source lacks detail
- Suggest finding more comprehensive source
- BLOCK creation until adequate source provided

### Step 3: Map Source to Template

```
1. Identify what information source contains
2. Match to appropriate template type:
   - Drug info → Excel/HTML Drug Chart
   - Learning objectives → HTML LO Guide
   - Clinical scenarios → Clinical Assessment Guide
3. Verify source has content for ALL required template sections
```

**Template-specific validation:**

**Drug Chart (Excel/HTML):**
- Requires: Drug names, mechanisms, indications, contraindications, side effects
- Optional: Dosing, monitoring, drug interactions
- If missing key categories → warn user of incomplete sections

**Learning Objectives Guide (HTML):**
- Requires: LO questions AND answers in source
- Requires: Sufficient detail for comparisons, master tables
- If only questions without answers → BLOCK

**Clinical Assessment Guide (HTML):**
- Requires: Chief complaints, history-taking approach, physical exam findings
- Requires: OLDCAARTS components (if using that framework)
- If insufficient clinical detail → warn or BLOCK

---

## Content Coverage Verification

### Before Creation Checklist

**For ALL template types:**
- [ ] Source file read completely
- [ ] Source contains medical facts (not just outlines)
- [ ] Source is comprehensive enough for template type
- [ ] All template sections can be filled from source
- [ ] No external information needed (except mnemonics)

**If ANY checkbox unchecked:**
→ Request additional source material or switch template types

### During Creation Monitoring

**As study guide is built:**
1. Cross-reference every fact against source
2. If information not in source → DO NOT ADD
3. If section empty due to lack of source content → Mark as "Not covered in source material"
4. Never invent, assume, or extrapolate medical facts

**Exception: Researched Mnemonics**
- If mnemonic found in source → use it
- If no mnemonic in source → use mnemonic-researcher agent to find established ones
- ALWAYS mark researched mnemonics with asterisk (*) and source

---

## Common Source Validation Errors

### Error 1: Accepting Outline-Only Sources

**Problem:** Source has headings but no details
```
Example BAD source:
# HIV Medications
- NRTIs
- NNRTIs
- Protease Inhibitors
```

**Why it's bad:** No mechanisms, indications, side effects - can't create comprehensive guide without external knowledge

**Solution:** Request detailed notes or lecture transcript

### Error 2: Using Multiple Unrelated Sources

**Problem:** User provides 3 different files for different topics

**Why it's bad:** Hard to track which facts came from which source, verification becomes impossible

**Solution:**
- Use ONE primary source per study guide
- If multi-source needed, user must combine into single source file first
- Document in pre-creation verification which source used

### Error 3: Assuming Common Knowledge

**Problem:** Source says "standard HIV treatment" without details, creator assumes facts

**Why it's bad:** "Common knowledge" may be outdated, incorrect, or not what source intended

**Solution:**
- If source lacks detail, mark section as incomplete
- Never add facts not explicitly in source
- Suggest user add details to source file if needed

### Error 4: Extrapolating from Source

**Problem:** Source mentions "hepatotoxicity" for Drug A, creator adds "monitor LFTs"

**Why it's bad:** Monitoring isn't explicitly stated in source - this is external addition

**Solution:**
- Only state what source explicitly says: "hepatotoxicity"
- If source says "monitor LFTs" → include it
- If source doesn't mention monitoring → don't add it

---

## Source Organization Best Practices

### Recommended Source Structure

**Well-organized source files:**
```
# Topic: HIV Medications

## NRTI Class Overview
[Detailed mechanism paragraph]

## Individual NRTIs

### Zidovudine (AZT)
**Mechanism:** [Detail from lecture]
**Indications:** [Detail from lecture]
**Side Effects:** [Detail from lecture]
**Monitoring:** [Detail from lecture]

### Lamivudine (3TC)
[Same structure]
```

**Why this works:**
- Clear section headers
- Detailed paragraphs (not just bullets)
- Organized by categories matching template needs
- Easy to extract information

### Poor Source Structure

**Problematic source files:**
```
HIV drugs:
AZT - bone marrow suppression
3TC - minimal toxicity
Combo therapy important
```

**Why this doesn't work:**
- Missing mechanisms, indications
- Vague statements without context
- No details for comprehensive guide
- Would require external knowledge to fill gaps

---

## Verification After Source Read

### Post-Read Checklist

After reading source file, ask yourself:

1. **Can I answer all template questions from this source alone?**
   - For Drug Chart: Do I have mechanism, indications, contraindications, side effects for EACH drug?
   - For LO Guide: Do I have answers to ALL learning objectives?
   - For Clinical Guide: Do I have history/exam details for EACH chief complaint?

2. **Are there any gaps requiring external knowledge?**
   - If YES → document gaps and inform user
   - Suggest adding details to source OR removing those sections from guide

3. **Is the source current and accurate?**
   - Check if source mentions year, guidelines referenced
   - If outdated information noted → warn user
   - Claude doesn't verify medical accuracy (user's responsibility)

4. **Can I cite page numbers or sections?**
   - For PDF sources → note page numbers
   - For text sources → note section headers
   - Citations help verification later

---

## Special Cases

### Case 1: Source Has Conflicting Information

**Example:** Source says "Drug A: 100mg dose" on page 1, "Drug A: 200mg dose" on page 5

**Action:**
- Note both pieces of information
- Include both in study guide with citations: "100mg (page 1), 200mg (page 5)"
- Add note: "Source contains conflicting information - verify with instructor"

### Case 2: Source References External Materials

**Example:** Source says "See First Aid page 123 for mechanism"

**Action:**
- If First Aid page provided → use it
- If not provided → mark section as "Refer to First Aid page 123 (not included in source)"
- DO NOT look up First Aid page using external knowledge

### Case 3: Source Has Mnemonics

**Example:** Source provides mnemonic "ABCDE" for Drug A side effects

**Action:**
- Use mnemonic from source (no asterisk needed)
- If source doesn't have mnemonic → use mnemonic-researcher agent
- Always mark researched mnemonics with (*) and source

### Case 4: Source Is Too Long (PDF Book Chapter)

**Example:** 50-page PDF chapter

**Action:**
- Read entire source (required)
- May take multiple Read tool calls if length limited
- Extract only relevant information for study guide topic
- Cite page numbers for all facts

---

## Emergency Override

If source validation is blocking incorrectly:

```bash
export SKIP_STUDY_GUIDE_VERIFICATION=1
```

**When to use:**
- Testing/development only
- Source is valid but skill misidentifying issues
- Temporary workaround while debugging

**NEVER use for:**
- Skipping source validation in actual study guide creation
- Avoiding source-only policy compliance
- Creating study guides without sources

---

## Summary

**Core principle:** If it's not in the source, it doesn't go in the study guide (except researched mnemonics marked with *).

**Validation workflow:**
1. Read entire source file
2. Verify sufficient detail for template type
3. Map source content to template sections
4. Identify any gaps
5. Inform user of gaps or proceed with creation
6. During creation, cross-reference every fact

**Success criteria:**
- 100% of medical facts from source
- Researched mnemonics clearly marked
- Gaps documented (not filled with external knowledge)
- User can verify every fact against source file

---

**See also:**
- [Hallucination Prevention](hallucination-prevention.md) - Strategies to avoid adding external facts
- [Citation Patterns](citation-patterns.md) - How to cite source material properly
- [Complete Examples](complete-examples.md) - Sample source validation workflows
