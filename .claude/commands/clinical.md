---
description: Create clinical assessment guide for history and physical exam
argument-hint: Source file(s) and chief complaint. Use --merge for combined output (e.g., "file.txt" "Chief Complaint" OR "f1.txt;f2.txt" "Chief Complaint" OR "--merge f1.txt;f2.txt" "Chief Complaint")
---

Create a clinical assessment guide from: $ARGUMENTS

## Instructions

### Step 0: Detect Mode & Parse Arguments (Single / Batch Separate / Batch Merge)

**Parse arguments to detect mode:**

**Arguments format:** `[files] "Chief Complaint"`
- Last argument is always the chief complaint (quoted string)
- Everything before it is the file path(s)

**Check for --merge flag:**
- If first argument is `--merge`: **BATCH MERGE MODE**
- Strip `--merge`, extract file list and chief complaint

**Check for semicolons in file argument:**
- If file argument contains semicolons (`;`): **BATCH SEPARATE MODE**
- Split by semicolon to get file list

**Otherwise: SINGLE MODE**

**State which mode detected:**
```
MODE DETECTED: [SINGLE / BATCH SEPARATE / BATCH MERGE]
File count: [#]
Files: [list]
Chief Complaint: [extract from last argument]
```

**Mode Descriptions:**
- **SINGLE**: 1 file → 1 clinical guide (inline processing)
- **BATCH SEPARATE**: N files → N clinical guides (agent per file, isolated contexts)
- **BATCH MERGE**: N files → 1 merged clinical guide (orchestrator agent, filters relevant content from all files)

---


### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: [file path]
☐ Chief complaint: [chief complaint from arguments]
☐ Template files: Clinical_Physical_Assessment_REVISED.txt, Clinical_Medical_History_Card.txt
☐ Source-only policy: I will ONLY use information from source file
☐ No external medical facts will be added
☐ Output format: Interactive HTML with 5 tabs
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then proceed with Step 2 (inline processing).**

---

#### For BATCH SEPARATE MODE:

**MANDATORY - State this checklist:**

```
BATCH SEPARATE VALIDATION:
☐ Source files: [list all files]
☐ Chief complaint: [from arguments - applies to ALL files]
☐ File validation: All files exist and are readable
☐ Homogeneity check: All files are clinical content
☐ Template files: Clinical_Physical_Assessment_REVISED.txt, Clinical_Medical_History_Card.txt (per file)
☐ Output: N files → N clinical guides
☐ Agent: batch-separate-processor (launched N times)
☐ Architectural isolation: Each file processed in separate agent context
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-separate-processor agent:**

```
I'll use the batch-separate-processor agent to process your files with architectural isolation.

Chief Complaint: [chief complaint]

Launching agent [X] times:
- File 1: batch-separate-processor → [Output1_ChiefComplaint.html]
- File 2: batch-separate-processor → [Output2_ChiefComplaint.html]
...
- File N: batch-separate-processor → [OutputN_ChiefComplaint.html]

Each agent invocation is architecturally isolated (zero cross-contamination).
```

**STOP HERE - Do NOT continue with Steps 2-7. The agent handles all processing.**

---

#### For BATCH MERGE MODE:

**MANDATORY - State this checklist:**

```
BATCH MERGE VALIDATION:
☐ Source files: [list all files]
☐ Chief complaint: [from arguments - filters content from ALL files]
☐ File validation: All files exist and are readable
☐ Files contain clinical content (conditions, presentations, workups)
☐ Template files: Clinical_Physical_Assessment_REVISED.txt, Clinical_Medical_History_Card.txt (unified)
☐ Output: N files → 1 merged clinical guide (filtered by chief complaint)
☐ Agent: batch-merge-orchestrator (launched once)
☐ Merge features: Extracts ONLY chief complaint relevant info from each file
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**Then invoke batch-merge-orchestrator agent:**

```
I'll use the batch-merge-orchestrator agent to intelligently merge relevant content.

Chief Complaint: [chief complaint]

Agent will:
1. Read all N files completely
2. Extract ONLY content relevant to "[chief complaint]" from each file
3. Create content matrix (which conditions/findings in which files)
4. Identify overlaps and gaps
5. Resolve conflicts with source traceability
6. Merge into ONE comprehensive clinical guide for "[chief complaint]"
7. Create merge report with traceability map

Output:
- 1 merged clinical guide: [ChiefComplaint]_Clinical_Guide.html
- 1 merge report: [ChiefComplaint]_Clinical_Guide_merge_report.md

Example: For chief complaint "Back Pain"
- Extracts back pain info from Lower-Back.txt
- Extracts spinal disorder info from Spine-Disorders.txt
- Extracts radiculopathy info from Neurology.txt
- Skips unrelated conditions
- Merges all back pain content into one guide
```

**STOP HERE - Do NOT continue with Steps 2-7. The agent handles all processing.**

---

**IMPORTANT FOR BATCH MODES:**
- Batch separate/merge use agents (subagent architecture)
- Single mode uses inline processing (Steps 2-7)
- Do NOT mix - if agent is launched, STOP and let agent complete the work
- Chief complaint parameter is preserved and passed to agents

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

**If BATCH MODE, process each file independently:**

For each source file in the batch:
1. **Announce file**: "Processing file X of Y: [filename]"

2. **CRITICAL - Context Isolation Check**:
   ```
   CONTEXT ISOLATION VERIFICATION:
   ☐ I will FORGET all clinical content from previous files
   ☐ I will ONLY extract information from THIS source file: [filename]
   ☐ I will verify clinical content is ONLY from THIS file (not previous files)
   ☐ This guide will contain ZERO content from previous files
   ```

3. **Per-File Verification** - Run complete verification checklist for THIS file

4. **Read source file** - Read THIS file completely, extract THIS file's clinical content only

5. **MANDATORY - State clinical scope**: "Clinical topics in [filename]: [list main conditions/complaints]"
   - This proves you're only using THIS file's content
   - If you see topics from previous files, STOP and re-read source

6. **Create clinical guide** - For THIS file only, using ONLY content from step 5

7. **Post-creation verification** - Verify THIS guide contains ONLY THIS file's content

8. **MANDATORY - Isolation Confirmation**: "File [X] complete. Cleared all data. Ready for next file."

**Critical for Batch:**
- Each file gets complete verification (not once at start)
- Explicitly state clinical scope from each file before creating guide
- Verify no content from previous files contaminated output
- Clear all data between files
- Each file gets its own HTML output

**Batch Summary**: After all files, provide summary of guides created, conditions covered, and any issues.

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

