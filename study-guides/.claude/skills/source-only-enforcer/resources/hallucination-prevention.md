# Hallucination Prevention Strategies

## Purpose

This resource provides specific strategies to prevent AI hallucination (adding facts not in source material) during medical study guide creation.

---

## Understanding Medical Hallucination Risk

### Why Medical Hallucinations Are Dangerous

**High-stakes domain:**
- Medical information affects patient safety
- Incorrect drug dosing → harm
- Wrong contraindications → missed warnings
- Outdated guidelines → suboptimal care

**AI knows medical facts:**
- Claude has medical knowledge from training
- Can easily fill gaps with "common knowledge"
- May confuse similar drugs/conditions
- May mix information from different sources

**User trust:**
- Students trust study guides for exams
- May not verify every fact
- Rely on accuracy for learning
- Compounded errors if hallucinations propagate

**Bottom line:** Even small hallucinations can have serious consequences

---

## Common Hallucination Patterns

### Pattern 1: Gap Filling

**Scenario:** Source mentions "Drug A causes liver toxicity" but doesn't mention monitoring

**Hallucination:** Adding "Monitor LFTs regularly"

**Why it happens:** Claude knows this is standard practice

**Prevention:**
```
If source says: "Drug A causes liver toxicity"
Study guide says: "Drug A causes liver toxicity"

Do NOT add:
- Monitoring recommendations
- Frequency of monitoring
- What values to check
- When to discontinue

UNLESS source explicitly provides this information.
```

### Pattern 2: Drug Class Generalization

**Scenario:** Source details Drug A (an NRTI), mentions NRTIs as a class

**Hallucination:** Adding details about Drug B (another NRTI) not in source

**Why it happens:** Claude knows other NRTIs have similar properties

**Prevention:**
```
If source only covers:
- Zidovudine (AZT)
- Lamivudine (3TC)

Study guide includes ONLY:
- Zidovudine
- Lamivudine

Do NOT add:
- Emtricitabine
- Tenofovir
- Other NRTIs

Even if they're in the same class.
```

### Pattern 3: Mechanism Extrapolation

**Scenario:** Source says "Drug A blocks enzyme X"

**Hallucination:** Adding "This prevents Y from occurring, leading to Z"

**Why it happens:** Claude knows the biochemical pathway

**Prevention:**
```
If source says: "Drug A blocks enzyme X"
Study guide says: "Drug A blocks enzyme X"

Do NOT add:
- Downstream effects
- Biochemical consequences
- Cellular impacts
- Clinical manifestations

UNLESS source explicitly describes them.
```

### Pattern 4: Side Effect Expansion

**Scenario:** Source lists "nausea, headache" as side effects

**Hallucination:** Adding "diarrhea, dizziness, rash"

**Why it happens:** Claude knows drug causes these too

**Prevention:**
```
If source lists:
- Nausea
- Headache

Study guide lists:
- Nausea
- Headache

Do NOT add:
- Additional side effects
- Common vs. rare distinctions
- Percentages/frequencies
- Management strategies

Even if they're well-known side effects.
```

### Pattern 5: Mnemonic Invention

**Scenario:** Source doesn't provide mnemonic for remembering side effects

**Hallucination:** Inventing mnemonic "ABCD" for Drug A

**Why it happens:** Helpful for students, seems harmless

**Prevention:**
```
If source doesn't have mnemonic:

OPTION 1: Use mnemonic-researcher agent
- Finds established mnemonics from USMLE resources
- Marks with (*) and source
- Provides 3 vetted options

OPTION 2: No mnemonic
- List facts without mnemonic
- Don't invent mnemonics

NEVER:
- Invent mnemonics yourself
- Use "common" mnemonics from memory
- Add mnemonics without verification
```

---

## Hallucination Prevention Techniques

### Technique 1: Read-Then-Constrain

**How it works:**
1. Read entire source file
2. Close source file (don't keep re-reading)
3. Create study guide ONLY from memory of source
4. If uncertain about a fact → mark as unclear, don't add

**Why it works:**
- Forces reliance on actual source content
- Makes gaps obvious (if you don't remember, it probably wasn't there)
- Prevents mixing source with general knowledge

**When to use:** For shorter sources where you can remember most content

### Technique 2: Section-by-Section Verification

**How it works:**
1. Read source section (e.g., "Drug A: Mechanism")
2. Write that section of study guide immediately
3. Move to next section
4. Repeat

**Why it works:**
- Minimizes reliance on memory
- Each section verified against source before moving on
- Hard to add external facts when source is right there

**When to use:** For longer sources or when creating detailed guides

### Technique 3: Source-Quote Method

**How it works:**
1. For each fact in study guide, cite source section/page
2. Format: "Drug A blocks enzyme X (Source: Section 3, page 5)"
3. Forces you to find fact in source to cite it

**Why it works:**
- Impossible to cite external facts (not in source)
- Makes verification easy later
- User can check any fact

**When to use:** For critical study guides or when extra verification needed

### Technique 4: Gap Marking

**How it works:**
1. Create study guide template with all expected sections
2. Fill sections from source
3. Sections without source content → mark "Not covered in source"
4. Never fill gaps with external knowledge

**Why it works:**
- Makes incomplete coverage visible
- User can add missing info to source if needed
- Prevents silent gap-filling

**When to use:** Always - this should be standard practice

**Example:**
```
Drug A
- Mechanism: Blocks enzyme X
- Indications: Hypertension, heart failure
- Contraindications: [Not covered in source material]
- Side Effects: Hypotension, dizziness
```

### Technique 5: Uncertainty Marking

**How it works:**
1. If uncertain whether fact was in source → mark with [VERIFY]
2. User can check source for these facts
3. Better to mark uncertain than add hallucinated fact

**Why it works:**
- Explicit about uncertainty
- Flags facts needing verification
- Prevents confident hallucinations

**When to use:** Whenever you're not 100% sure fact was in source

---

## Self-Monitoring Strategies

### Red Flag Questions

**Ask yourself while creating:**

1. **"Did the source actually say this, or do I just know it's true?"**
   - If answer is "I know it's true" → DON'T ADD
   - Only add if "source said this"

2. **"Can I quote the exact sentence from the source?"**
   - If yes → add fact
   - If no → don't add fact

3. **"Am I adding this because it's medically important?"**
   - If yes → RED FLAG (adding for importance, not because it's in source)
   - Importance doesn't justify external additions

4. **"Would a student notice this is missing if I don't add it?"**
   - If yes → Good - marks incomplete coverage
   - Better to have visible gaps than silent hallucinations

5. **"Did I verify this mnemonic came from established sources?"**
   - If researched via mnemonic-researcher agent → OK (mark with *)
   - If from your knowledge → DON'T ADD

### Hallucination Likelihood Indicators

**HIGH RISK scenarios:**
- Source is sparse (outline only)
- Creating complex template (many sections)
- Time pressure or rushing
- Source from unfamiliar specialty
- Multiple sources mixed together

**Actions for high-risk:**
- Use section-by-section verification
- Mark more facts with [VERIFY]
- Re-read source multiple times
- Consider refusing if source insufficient

**LOW RISK scenarios:**
- Source is detailed, comprehensive
- Simple template (fewer sections)
- Taking time to verify
- Source from familiar topic
- Single, clear source file

**Actions for low-risk:**
- Standard read-then-constrain OK
- Still mark gaps appropriately
- Still verify mnemonics

---

## Handling Edge Cases

### Case 1: Source Implies But Doesn't State

**Scenario:** Source describes drug mechanism that would logically lead to specific side effect, but doesn't explicitly list that side effect

**Action:** DO NOT add the implied side effect

**Rationale:** Inference is still external addition

**Example:**
```
Source: "Drug A blocks sodium reabsorption in the kidney"

DO NOT infer and add:
- "Increases urination"
- "May cause dehydration"
- "Can lead to electrolyte imbalances"

ONLY state what's in source:
- "Blocks sodium reabsorption in the kidney"
```

### Case 2: Source Uses Abbreviations

**Scenario:** Source says "ACE inhibitor" without defining

**Action:**
- Use abbreviation as written in source
- Don't expand unless source expands it
- Don't add mechanism unless source provides it

**Example:**
```
Source: "ACE inhibitors are first-line for hypertension"

Study guide: "ACE inhibitors are first-line for hypertension"

DO NOT add:
- "Angiotensin-Converting Enzyme inhibitors"
- Mechanism of ACE
- Examples of ACE inhibitors (unless source lists them)
```

### Case 3: Source Has Partial Lists

**Scenario:** Source says "Side effects include nausea..." (ellipsis or "etc.")

**Action:**
- List only what's explicitly mentioned
- Note "and others" if source indicates incomplete list
- Don't fill in the missing items

**Example:**
```
Source: "Side effects include nausea, vomiting, etc."

Study guide: "Side effects include nausea, vomiting, and others"

DO NOT add:
- Specific additional side effects
- Complete list from your knowledge
- "Common" side effects not listed
```

### Case 4: Source References Figures/Tables

**Scenario:** Source says "See Table 1 for dosing" but Table 1 not in source file

**Action:**
- Note "Dosing information in Table 1 (not included in source)"
- Don't provide dosing from memory
- Suggest user include Table 1 in source

### Case 5: Source Has Errors

**Scenario:** Source states "Drug A is a beta blocker" but you know it's an ACE inhibitor

**Action:**
- Use what source says (even if wrong)
- Optionally note: "[Source states beta blocker - verify with instructor]"
- Your job is source fidelity, not error correction

**Rationale:**
- May be instructor's error you should catch on exam
- May be outdated classification
- May be your knowledge that's wrong
- Changing it = adding external information

---

## Quality Assurance Checks

### Pre-Submission Review

Before finalizing study guide:

1. **Random fact check:**
   - Pick 10 random facts from study guide
   - Find each fact in source file
   - If you can't find one → hallucination detected → remove it

2. **Mnemonic verification:**
   - Check every mnemonic has (*) marker if researched
   - Verify mnemonic-researcher agent was used
   - If mnemonic unmarked → check source, if not there → remove

3. **Gap audit:**
   - Count "Not covered in source" markers
   - Verify gaps are real (re-check source)
   - Make sure no gaps silently filled

4. **Citation check:**
   - If using citation method → verify all citations valid
   - Check page numbers/sections exist
   - Ensure no citations to external sources

### Post-Creation Verification

**Use study-guide-analyzer agent:**
- Comprehensive 6-step verification
- Automated cross-checking against source
- Identifies potential hallucinations
- Generates detailed analysis report

**When to use:**
- Always for high-stakes study guides
- When source was sparse
- When you're uncertain about accuracy
- Before sharing with other students

---

## Training Your Hallucination Detector

### Practice Scenarios

**Scenario 1:** Source says "Drug A is hepatotoxic"

**Which additions are hallucinations?**
- A) "Monitor liver function tests" ← HALLUCINATION
- B) "Drug A is hepatotoxic" ← CORRECT
- C) "Avoid in liver disease" ← HALLUCINATION
- D) "May cause jaundice" ← HALLUCINATION

**Answer:** All except B are hallucinations (not in source)

**Scenario 2:** Source says "Atropine blocks muscarinic receptors, leading to decreased secretions"

**Which additions are hallucinations?**
- A) "Decreased secretions → dry mouth" ← HALLUCINATION (inference)
- B) "Blocks muscarinic receptors" ← CORRECT
- C) "Leads to decreased secretions" ← CORRECT
- D) "Used to dry secretions before surgery" ← HALLUCINATION (indication not stated)

**Scenario 3:** Source says "Common side effects: nausea, dizziness, headache"

**Which additions are hallucinations?**
- A) Listing "drowsiness" as 4th side effect ← HALLUCINATION
- B) Categorizing "nausea" as GI side effect ← HALLUCINATION (categorization not in source)
- C) Stating these are "common" side effects ← CORRECT (source said "common")
- D) Adding percentages like "nausea (30%)" ← HALLUCINATION (numbers not in source)

### Developing Your Instinct

**Good habits:**
- Always ask "Did source say this?"
- When in doubt, leave it out
- Mark uncertainties for verification
- Prefer visible gaps over invisible hallucinations

**Bad habits to break:**
- "I'll add this because it's important"
- "Everyone knows this, so it's fine"
- "The source probably meant to include this"
- "This is standard information for this drug"

---

## Summary

**Core principle:** Fidelity to source > Completeness

**Better to have:**
- Incomplete but accurate study guide
- Visible gaps marked clearly
- All facts verifiable against source

**Than to have:**
- Complete but hallucinated study guide
- Silent gaps filled with external facts
- Unverifiable information

**Remember:**
- Medical accuracy matters
- Students trust your work
- Hallucinations undermine entire guide
- When uncertain → verify or mark, never guess

**Your responsibility:**
- Perfect source fidelity
- Clear gap marking
- Verified mnemonics only
- Explicit uncertainty notation

---

**See also:**
- [Source Validation Guide](source-validation-guide.md) - How to verify source files
- [External Info Marking](external-info-marking.md) - How to mark researched mnemonics
- [Verification Checklists](verification-checklists.md) - QA processes
