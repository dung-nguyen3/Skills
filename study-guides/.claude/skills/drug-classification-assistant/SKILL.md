# Drug Classification Assistant

**Version:** 1.0.0
**Type:** Domain Knowledge (Suggest)
**Priority:** MEDIUM
**Status:** Active

---

## Purpose

Assists with verifying drug classifications, mechanisms of action (MOA), and treatment designations. Helps distinguish between class-wide and drug-specific information to prevent incorrect groupings in study guides.

---

## When I Activate

I automatically suggest myself when you:
- Question drug classifications
- Ask about mechanisms of action
- Verify first-line designations
- Check drug-of-choice (DOC) status
- Need to distinguish class-wide vs drug-specific info

**Trigger Keywords:**
- drug class, classification
- MOA, mechanism, mechanism of action
- first-line, second-line, DOC
- class-wide, drug-specific
- pharmacology, therapeutic class

---

## What I Help With

### 1. Drug Classification Verification

**Common Classifications:**

**By Mechanism:**
- Beta-blockers (β-blockers)
- ACE inhibitors
- Calcium channel blockers
- Proton pump inhibitors (PPIs)
- SSRIs, SNRIs, TCAs
- Antihistamines (H1, H2)
- Antibiotics (beta-lactams, macrolides, fluoroquinolones)

**By Therapeutic Use:**
- Antihypertensives
- Antiarrhythmics
- Anticoagulants vs Antiplatelets
- Antidiabetics (oral vs injectable)
- Bronchodilators

**By Chemical Structure:**
- Penicillins
- Cephalosporins (generations)
- Benzodiazepines
- Opioids

### 2. Mechanism of Action (MOA) Accuracy

**I help verify:**
- MOA is stated correctly from source
- MOA is specific to the drug (not generalized)
- MOA differences between drugs in same class
- When to group drugs with IDENTICAL MOA

**Common MOA patterns:**

**Class-wide MOA (OK to group):**
- All ACE inhibitors → Block angiotensin-converting enzyme
- All beta-blockers → Block β-adrenergic receptors
- All PPIs → Irreversibly inhibit H+/K+ ATPase

**Drug-specific MOA (DO NOT group):**
- Carvedilol → Blocks α and β receptors (unique among beta-blockers)
- Amiodarone → Multi-channel blocker (unique mechanism)
- Aspirin → Irreversible COX inhibition (vs reversible NSAIDs)

### 3. First-Line / Drug-of-Choice Designations

**I help verify:**
- Source explicitly states "first-line" designation
- Context is clear (first-line for WHAT condition?)
- DOC designation from source (not assumed)
- Alternative agents mentioned in source

**Critical Rule:**
❌ **NEVER assume first-line status**
✅ **ONLY mark as first-line if source explicitly states it**

**Examples of proper verification:**

**✅ Source says:** "Metformin is first-line for type 2 diabetes"
**✅ Study guide:** Mark as first-line

**❌ Source says:** "Metformin is commonly used for diabetes"
**❌ Study guide:** Do NOT mark as first-line

### 4. Class-Wide vs Drug-Specific Information

**The most critical distinction for preventing incorrect groupings.**

**Class-wide information (IDENTICAL across all drugs):**
- Shared mechanism of action
- Common side effects (ALL drugs have them)
- Shared contraindications
- Same monitoring requirements

**Drug-specific information (DIFFERENT between drugs):**
- Unique side effects (only ONE drug has it)
- Specific indications (one drug for specific condition)
- Different dosing
- Unique contraindications

---

## Critical Verification Rule

### Before Merging Cells or Grouping Drugs

**STOP and verify:**

1. **Read source for EACH drug individually**
2. **Check if information is IDENTICAL for all drugs**
3. **If even ONE drug differs → DO NOT GROUP**

**Examples:**

**✅ Safe to group (IDENTICAL information):**
```
All ACE inhibitors:
- MOA: Block ACE enzyme
- Side effect: Dry cough (all have this)
- Contraindication: Pregnancy (all contraindicated)
```

**❌ UNSAFE to group (DIFFERENT information):**
```
Beta-blockers - Cardioselectivity:
- Metoprolol: β1-selective
- Carvedilol: β1 + β2 + α1 (NON-selective)
- Propranolol: β1 + β2 (NON-selective)

→ DO NOT merge cells - they differ!
```

---

## Common Classification Mistakes

### ❌ Mistake 1: Assuming Class-Wide Effects

**Wrong:**
"All beta-blockers cause bronchospasm"

**Correct:**
"Non-selective beta-blockers (propranolol, carvedilol) can cause bronchospasm by blocking β2 receptors. Selective β1 blockers (metoprolol) have lower risk."

### ❌ Mistake 2: Grouping Different Generations

**Wrong:**
"All cephalosporins have same spectrum"

**Correct:**
- 1st gen: Gram-positive focus
- 2nd gen: Broader gram-negative
- 3rd gen: Excellent gram-negative, cross BBB
- 4th gen: Pseudomonal coverage

→ Each generation = separate row in comparison table

### ❌ Mistake 3: Merging Unique Indications

**Wrong:**
"All SSRIs treat depression" (merged cell)

**Correct:**
- Fluoxetine: Depression, OCD, bulimia
- Sertraline: Depression, OCD, PTSD, social anxiety
- Paroxetine: Depression, OCD, panic disorder

→ Different indications = separate cells

### ❌ Mistake 4: Assuming First-Line Without Source

**Wrong:**
Adding "First-line" marker when source doesn't state it

**Correct:**
Only mark "First-line" if source explicitly says:
- "first-line treatment"
- "drug of choice"
- "preferred initial therapy"

---

## How I Help During Creation

### When Creating Comparison Tables

**I suggest checking:**

1. **Before grouping drugs:**
   - "Does the source state this information is IDENTICAL for all these drugs?"
   - "Have you verified EACH drug individually?"

2. **When marking first-line:**
   - "Does the source explicitly state 'first-line' or 'drug of choice'?"
   - "What is the specific indication/condition?"

3. **When stating MOA:**
   - "Is this MOA stated in the source?"
   - "Is this MOA specific to this drug or shared by the class?"

### During Verification

**I help validate:**

1. **Classification accuracy:**
   - Drug is in correct therapeutic class
   - Generation/subtype is correct
   - Chemical classification matches source

2. **Grouping correctness:**
   - Merged cells only contain IDENTICAL information
   - Each drug verified individually
   - No assumptions about class-wide effects

3. **Designation accuracy:**
   - First-line status confirmed from source
   - DOC designation has source support
   - Alternative agents noted when mentioned

---

## Integration with Other Skills

**Works with:**
- `source-only-enforcer` - Ensures all classifications from source
- `study-guide-verifier` - Validates classification accuracy
- `template-compliance-checker` - Ensures proper formatting

**Workflow:**
1. source-only-enforcer → Requires source file validation
2. drug-classification-assistant → Verifies classifications and groupings
3. study-guide-verifier → Final comprehensive check

---

## Common Verification Scenarios

### Scenario 1: Creating Drug Comparison Table

**Question:** "Can I group these 3 ACE inhibitors with identical side effects?"

**I help you verify:**
1. Read source for EACH of the 3 drugs
2. Check if side effect is listed for ALL 3
3. Verify no drug has unique additional effects
4. If IDENTICAL → Safe to group
5. If ANY difference → Separate cells

### Scenario 2: Marking First-Line Drug

**Question:** "Should I mark metformin as first-line for diabetes?"

**I help you verify:**
1. Search source for "first-line" or "drug of choice"
2. Check if designation is explicit
3. Verify the specific condition (type 2 diabetes)
4. If source states it → Mark as first-line
5. If source doesn't → Do NOT mark

### Scenario 3: Mechanism of Action

**Question:** "Can I say all beta-blockers work the same way?"

**I help you verify:**
1. Check if source lists MOA for each drug
2. Identify if any drugs have unique mechanisms
3. Distinguish selective vs non-selective
4. Separate drugs with different MOA profiles
5. Only group if truly IDENTICAL mechanism

---

## Quick Verification Checklist

**Before finalizing drug information:**

- [ ] Classification verified from source (not assumed)
- [ ] MOA stated in source (not inferred)
- [ ] First-line designation EXPLICIT in source
- [ ] Groupings verified (information IDENTICAL for all)
- [ ] Each drug checked individually (not just class)
- [ ] Unique features highlighted (not grouped)
- [ ] Generations/subtypes distinguished
- [ ] Therapeutic uses specific to each drug
- [ ] Side effects verified for each drug
- [ ] Contraindications checked individually

---

## Common Drug Classes Reference

**For quick lookup during study guide creation:**

### Cardiovascular
- **Beta-blockers:** Selective (metoprolol, atenolol) vs Non-selective (propranolol, carvedilol)
- **ACE inhibitors:** All end in "-pril" (lisinopril, enalapril, ramipril)
- **ARBs:** All end in "-sartan" (losartan, valsartan)
- **CCBs:** Dihydropyridines (-dipine) vs Non-DHP (diltiazem, verapamil)

### Antibiotics
- **Penicillins:** Natural vs Antistaphylococcal vs Aminopenicillins vs Extended-spectrum
- **Cephalosporins:** 1st gen → 2nd gen → 3rd gen → 4th gen (different spectrums)
- **Macrolides:** Azithromycin, clarithromycin, erythromycin
- **Fluoroquinolones:** All end in "-floxacin"

### Antidiabetics
- **Oral:** Metformin, sulfonylureas, DPP-4 inhibitors, SGLT2 inhibitors
- **Injectable:** Insulin, GLP-1 agonists

### Psychiatric
- **SSRIs:** Fluoxetine, sertraline, paroxetine, citalopram, escitalopram
- **SNRIs:** Venlafaxine, duloxetine
- **TCAs:** Amitriptyline, nortriptyline, imipramine

**Note:** Classifications must still be verified from YOUR source file.

---

## When to Consult This Skill

**During creation:**
- Creating comparison tables (before grouping)
- Marking first-line drugs (verify designation)
- Stating mechanisms (confirm from source)

**During verification:**
- Checking merged cells (ensure IDENTICAL info)
- Validating classifications (confirm from source)
- Reviewing groupings (each drug verified)

**When in doubt:**
- ASK: "Does the source explicitly state this?"
- VERIFY: "Have I checked EACH drug individually?"
- SEPARATE: "When in doubt, keep information separate"

---

## Related Documentation

**Source Material:**
- Always reference YOUR specific source file
- Don't rely on general pharmacology knowledge
- Verify every classification from source

**Templates:**
- `/templates-and-examples/Excel_Drugs_Chart_11-1.txt` - Drug chart template
- `/templates-and-examples/Drug_Chart_HTML.txt` - HTML drug chart

**Other Skills:**
- `source-only-enforcer` - Source-only policy
- `study-guide-verifier` - Comprehensive verification

---

**Last Updated:** 2025-11-19
**Activation Type:** Suggest (non-blocking)
**Customization:** Modify trigger keywords in `.claude/skills/skill-rules.json`
