# Complete Source-Only Enforcement Examples

## Purpose

Real-world examples demonstrating proper source-only enforcement across different template types and scenarios.

---

## Example 1: Excel Drug Chart (Good)

### Source File: HIV_Drugs.txt
```
NRTI Class:

Zidovudine (AZT):
- Mechanism: Inhibits HIV reverse transcriptase
- Indications: HIV treatment, prevention of maternal-to-fetal transmission
- Side Effects: Bone marrow suppression, anemia, neutropenia
- Monitoring: CBC every 3 months

Lamivudine (3TC):
- Mechanism: Inhibits HIV reverse transcriptase
- Indications: HIV treatment, Hepatitis B treatment
- Side Effects: Minimal toxicity, well-tolerated
```

### Study Guide Output (Excel Drug Chart) - CORRECT
```
Drug Tab:
| Drug Name | Mechanism | Indications | Side Effects | Monitoring |
|-----------|-----------|-------------|--------------|------------|
| Zidovudine (AZT) | Inhibits HIV reverse transcriptase | HIV treatment, prevention of maternal-to-fetal transmission | Bone marrow suppression, anemia, neutropenia | CBC every 3 months |
| Lamivudine (3TC) | Inhibits HIV reverse transcriptase | HIV treatment, Hepatitis B treatment | Minimal toxicity, well-tolerated | [Not covered in source] |

Mnemonics Tab:
NRTI Side Effects - AZT: "Bone marrow loves AZT"* (r/medicalschool, 4-star)
```

**Why this is correct:**
- ✅ All facts from source only
- ✅ Monitoring for 3TC marked as missing (source didn't provide)
- ✅ Mnemonic researched and marked with (*)
- ✅ No external additions

---

## Example 2: Excel Drug Chart (Bad - Hallucinations)

### Same Source as Example 1

### Study Guide Output - INCORRECT
```
| Drug Name | Mechanism | Indications | Side Effects | Monitoring |
|-----------|-----------|-------------|--------------|------------|
| Zidovudine (AZT) | Inhibits HIV reverse transcriptase | HIV treatment, prevention of maternal-to-fetal transmission | Bone marrow suppression, anemia, neutropenia, GI upset | CBC every 3 months |
| Lamivudine (3TC) | Inhibits HIV reverse transcriptase | HIV treatment, Hepatitis B treatment | Minimal toxicity, well-tolerated | LFTs if used for Hep B |
| Emtricitabine (FTC) | Similar to 3TC | HIV treatment | Headache, nausea | No routine monitoring |
```

**Hallucinations identified:**
- ❌ "GI upset" for AZT - NOT in source
- ❌ "LFTs if used for Hep B" for 3TC - NOT in source (monitoring was missing)
- ❌ Entire Emtricitabine row - NOT in source at all

**Why this happened:**
- Added common side effect (GI upset) from general knowledge
- Inferred monitoring based on indication
- Included related NRTI not in source

---

## Example 3: HTML Learning Objectives Guide (Good)

### Source File: Diabetes_LO.txt
```
Learning Objective 1: Describe the pathophysiology of Type 2 Diabetes

Answer: Type 2 diabetes results from insulin resistance and relative insulin deficiency. Pancreatic beta cells initially compensate by producing more insulin, but eventually fail to maintain normoglycemia. Risk factors include obesity, family history, and sedentary lifestyle.

Learning Objective 2: List first-line medications for Type 2 Diabetes

Answer: Metformin is first-line therapy. It decreases hepatic glucose production and improves insulin sensitivity.
```

### Study Guide Output - CORRECT
```
## LO Q&A Tab

**LO 1: Describe the pathophysiology of Type 2 Diabetes**

Type 2 diabetes results from insulin resistance and relative insulin deficiency. Pancreatic beta cells initially compensate by producing more insulin, but eventually fail to maintain normoglycemia. Risk factors include obesity, family history, and sedentary lifestyle.

**LO 2: List first-line medications for Type 2 Diabetes**

Metformin is first-line therapy. It decreases hepatic glucose production and improves insulin sensitivity.

## Key Comparisons Tab

[Not covered in source material - source only answered LO questions without comparison tables]

## Master Tables Tab

Type 2 Diabetes Risk Factors:
- Obesity
- Family history
- Sedentary lifestyle

First-Line Medication:
- Metformin: Decreases hepatic glucose production, improves insulin sensitivity
```

**Why this is correct:**
- ✅ LO answers directly from source
- ✅ Marked comparison section as "Not covered"
- ✅ Master table built from facts in LO answers (no new facts added)
- ✅ No external additions

---

## Example 4: HTML Learning Objectives Guide (Bad)

### Same Source as Example 3

### Study Guide Output - INCORRECT
```
**LO 1: Describe the pathophysiology of Type 2 Diabetes**

Type 2 diabetes results from insulin resistance and relative insulin deficiency. Pancreatic beta cells initially compensate by producing more insulin, but eventually fail to maintain normoglycemia due to glucotoxicity and lipotoxicity. Risk factors include obesity (BMI >30), family history, sedentary lifestyle, and age >45.

Mnemonic: "OBESE"
- Obesity
- Beta cell failure
- Environmental factors
- Sedentary lifestyle
- Elderly

**LO 2: List first-line medications for Type 2 Diabetes**

Metformin is first-line therapy. It decreases hepatic glucose production and improves insulin sensitivity. Side effects include GI upset, lactic acidosis (rare). Contraindicated in renal disease (GFR <30).
```

**Hallucinations identified:**
- ❌ "glucotoxicity and lipotoxicity" - mechanisms NOT in source
- ❌ "BMI >30" - specific cutoff NOT in source
- ❌ "age >45" - specific age NOT in source
- ❌ "OBESE" mnemonic - invented, not researched
- ❌ Metformin side effects - NOT in source
- ❌ Metformin contraindications - NOT in source

---

## Example 5: With Researched Mnemonics (Good)

### Source File: Hypercalcemia_Causes.txt
```
Causes of Hypercalcemia:
- Primary hyperparathyroidism
- Malignancy (most common in hospitalized patients)
- Thiazide diuretics
- Vitamin D intoxication
- Sarcoidosis
```

### Study Guide Output - CORRECT
```
Causes of Hypercalcemia:
1. Primary hyperparathyroidism
2. Malignancy (most common in hospitalized patients)
3. Thiazide diuretics
4. Vitamin D intoxication
5. Sarcoidosis

Mnemonic: "CHIMPANZEES"* (r/medicalschool, 5-star, widely used)
- C: Calcium supplementation [not in source - excluded]
- H: Hyperparathyroidism ✓
- I: Iatrogenic (thiazides) ✓
- M: Malignancy ✓
- P: Paget's disease [not in source - excluded]
- ...
- S: Sarcoidosis ✓
- Vitamin D ✓

Note: Only using mnemonic components covered in source material
```

**Why this is correct:**
- ✅ Mnemonic researched and marked (*)
- ✅ Noted which components NOT in source
- ✅ Only used relevant parts of mnemonic
- ✅ Transparent about exclusions

---

## Example 6: Gap Marking (Good)

### Source File: Asthma_Treatment.txt
```
Asthma Treatment Steps:

Step 1: SABA as needed
Step 2: Add low-dose ICS
Step 3: Increase ICS or add LABA

If not controlled, refer to specialist.
```

### Study Guide Output - CORRECT
```
Asthma Treatment Stepwise Approach:

| Step | Treatment | When to Use |
|------|-----------|-------------|
| 1 | SABA as needed | [Not specified in source] |
| 2 | Add low-dose ICS | [Not specified in source] |
| 3 | Increase ICS or add LABA | [Not specified in source] |
| Uncontrolled | Refer to specialist | If not controlled at Step 3 |

Notes:
- Source provided treatment steps but not specific indications for when to use each step
- Consider referring to national asthma guidelines for complete criteria
```

**Why this is correct:**
- ✅ Included treatment steps (from source)
- ✅ Marked missing "when to use" criteria
- ✅ Noted what's missing and suggested alternative resources
- ✅ Transparent about gaps rather than filling with external knowledge

---

## Summary of Patterns

### DO:
- Extract facts verbatim from source
- Mark missing sections as "Not covered"
- Research mnemonics when helpful
- Mark researched content with (*)
- Note source gaps explicitly

### DON'T:
- Add "common knowledge" facts
- Infer information from source
- Expand abbreviations without source definition
- Invent mnemonics
- Fill gaps silently with external info

### When in Doubt:
- Leave it out
- Mark as [VERIFY] if uncertain
- Note what's missing
- Prefer incomplete but accurate over complete but hallucinated

---

**See also:**
- [Source Validation Guide](source-validation-guide.md)
- [Hallucination Prevention](hallucination-prevention.md)
- [External Info Marking](external-info-marking.md)
