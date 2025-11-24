---
description: Create clinical assessment guide for history and physical exam
argument-hint: Single file OR batch files separated by semicolon (e.g., "file1.txt" OR "file1.txt;file2.txt")
---

Create a clinical assessment guide from source file: $ARGUMENTS

## Instructions

### Step 0: Detect Mode (Single vs Batch)

**Parse arguments:** If $ARGUMENTS contains `;` → BATCH MODE (multiple files), otherwise SINGLE MODE.

**State mode:** MODE DETECTED: [SINGLE/BATCH], File count: [#], Files: [list]

---


### Step 1: Pre-Creation Verification

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: [identified from $ARGUMENTS]
☐ Chief complaint: [identified from $ARGUMENTS or source]
☐ Template files: Clinical_Physical_Assessment_REVISED.txt, Clinical_Medical_History_Card.txt
☐ Source-only policy: I will ONLY use information from source file
☐ No external medical facts will be added
☐ Output format: Interactive HTML with 5 tabs
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

### Step 2: Load Resources

Read these files in order:
1. **Physical Assessment Template**: `study-guides/templates-and-examples/Clinical_Physical_Assessment_REVISED.txt`
   - HTML structure and formatting guide
   - Tab organization requirements
   - Example HTML code

2. **Medical History Card**: `study-guides/templates-and-examples/Clinical_Medical_History_Card.txt`
   - Complete HPI (OLDCAARTS) components
   - PMH, FH, SH elements
   - Full ROS by system

3. **Source File**: $ARGUMENTS
   - Extract all conditions/differentials
   - Note physical exam findings
   - Identify specialized tests

### Step 3: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL conditions mentioned
- Group by onset pattern (acute, subacute, chronic)
- Extract physical exam maneuvers
- Note specialized tests
- Document decision points

### Step 4: Create 5-Tab HTML Guide

**Required Tabs:**

**Tab 1: Acute Onset (Hours to Days)**
- Top differentials for acute presentation
- Complete HPI (OLDCAARTS) with exact questions in quotes
- Essential PMH, FH, SH
- Focused ROS with checkboxes
- Physical Exam Focus (Inspection, Palpation, ROM, Special Tests)

**Tab 2: Subacute Onset (Days to Weeks)**
- Top differentials for subacute presentation
- Same structure as acute with condition-specific questions

**Tab 3: Chronic Onset (Weeks to Months)**
- Top differentials for chronic presentation
- Same structure with chronic-specific considerations

**Tab 4: Focused Physical Exam**
- Detailed physical examination by anatomical region
- Inspection: What to look for (be specific)
- Palpation: What to feel for
- Special tests: Named maneuvers with technique
- Group conditions with same physical exam together

**Tab 5: Quick Reference Chart**
- "If patient answers X, ask Y"
- "If examination X is positive, do Y"
- Red flags requiring immediate action
- Decision support tables

### Step 5: HPI Format (OLDCAARTS)

**All questions must be in quotes for direct patient use:**
- **O**nset: "When exactly did this start?"
- **L**ocation: "Where exactly is the problem?" "Point with one finger"
- **D**uration: "How long does it last? Constant or comes and goes?"
- **C**haracter: "What does it feel like? Sharp/dull/burning/aching?" "Rate 0-10"
- **A**ggravating factors: "What makes it worse?"
- **A**lleviating factors: "What makes it better? What have you tried?"
- **A**ssociated symptoms: "Any other symptoms with this?"
- **R**adiation: "Does it spread anywhere?"
- **T**iming: "Any pattern? Time of day? After activities?"
- **S**etting: "What were you doing when it started?"

### Step 6: Essential History (from Medical History Card)

**PMH:**
- Allergies: "Any allergies to medications, latex, food?"
- Medications: "What medications do you take? Prescription, OTC, supplements?"
- Medical Conditions: "Do you have any medical conditions?"
- Surgeries/Hospitalizations: "Any surgeries or hospital stays?"
- Accidents/Injuries: "Any accidents or injuries?"

**FH:**
- Father: "Is your father living? Any medical conditions?"
- Mother: "Is your mother living? Any medical conditions?"
- Siblings: "Any brothers or sisters? Medical conditions?"
- Relevant conditions: Heart disease, cancer, diabetes, etc.

**SH:**
- Occupation: "What do you do for work?"
- Tobacco: "Do you smoke or vape?"
- Alcohol: "Do you drink alcohol? How much?"
- Drugs: "Any recreational drugs?"
- Exercise: "Do you exercise?"

### Step 7: Focused ROS

Use checkbox format (☐) for each system:
- **General**: Fever, chills, weight change, fatigue, night sweats
- **Skin**: Rash, itching, changes
- **MSK**: Joint pain, stiffness, swelling, ROM limitations
- **Neuro**: Weakness, numbness, tingling, falls
- **CV**: Chest pain, palpitations, edema
- **Other systems as relevant to chief complaint**

### Step 8: Physical Exam Specificity

**Be specific about what to examine FOR:**
- ✅ "Inspect skin for erythema, edema, ecchymosis, deformity"
- ❌ "Inspect skin"

- ✅ "Palpate for warmth, point tenderness, crepitus, effusion"
- ❌ "Palpate joint"

- ✅ "Test ROM: flexion (0-140°), extension (0°), internal rotation (0-40°)"
- ❌ "Test ROM"

### Step 9: HTML Formatting

**Required:**
- Inline CSS styles (no external stylesheets)
- Interactive tabs with onclick navigation
- Responsive grid layouts
- Color-coded sections:
  - Red (#dc2626): Acute/Emergency
  - Orange (#f97316): Subacute/Urgent
  - Green (#22c55e): Chronic
  - Blue (#3b82f6): Information sections

### Step 10: Use TodoWrite

Track your progress:
- Create todo for each tab
- Create todo for each major section
- Mark completed as you finish
- Keep user informed

### Step 11: Post-Creation Verification

**Automatically verify the completed file:**

1. **Source Accuracy**
   - All medical facts from source file only
   - No external conditions or treatments added
   - Terminology matches source exactly

2. **Template Compliance**
   - All 5 tabs present (Acute, Subacute, Chronic, Focused PE, Quick Reference)
   - OLDCAARTS complete with all 10 elements (in quotes)
   - PMH/FH/SH/ROS following Medical History Card format
   - Physical exam following Assessment template structure

3. **Completeness**
   - All conditions from source included
   - All physical exam maneuvers included
   - Decision trees for all major differentials
   - Quick reference populated

4. **Quality**
   - All patient questions in quotes
   - Specific exam findings (what to inspect FOR)
   - Color-coded sections by urgency
   - Interactive tabs functional

**CRITICAL: State "Post-creation verification complete" and report any issues. Fix immediately.**

### Step 12: Save File

- Save to: `[Class]/[Exam]/Claude Study Tools/[Chief_Complaint]_Clinical_Assessment_Guide.html`
- Create Claude Study Tools folder if doesn't exist
- Confirm file saved successfully


---

### Batch Processing (BATCH MODE ONLY)

If BATCH MODE, repeat previous steps for EACH file with progress tracking and batch summary at end.

---

## Common Mistakes to Avoid

❌ Asking for specific medications instead of open-ended "What medications do you take?"
❌ Missing OLDCAARTS elements
❌ Generic physical exam without specifics ("Inspect skin" vs "Inspect skin for edema, warmth")
❌ Not grouping similar conditions
❌ White backgrounds instead of color-coded sections
❌ Missing decision support ("If X, Think Y")
❌ Questions not in quotes

## Example Usage

**Single:** Command with one file

**Batch:** Command with semicolon-separated files → Creates separate output files

