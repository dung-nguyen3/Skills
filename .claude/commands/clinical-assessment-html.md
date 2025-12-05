---
description: Create clinical assessment guide for history and physical exam
argument-hint: Source file(s)/directory(ies) and chief complaint. Use --merge for combined output (e.g., "file.txt" "Chief Complaint" OR "/path/to/dir" "CC" OR "--merge /dir1;/dir2" "CC")
---

Create a clinical assessment guide from: $ARGUMENTS

## Instructions

### Step 0: Detect Mode & Parse Arguments (Single / Batch Separate / Batch Merge)

**Parse arguments to detect mode:**

**Arguments format:** `[files/directories] "Chief Complaint"`
- Last argument is always the chief complaint (quoted string)
- Everything before it is the file/directory path(s)

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

### Step 0.5: Handle Directory Input

If $ARGUMENTS is a directory, process all .txt/.pdf files within it.
If batch (semicolon-separated), process each path independently.

---


### Step 1: Pre-Creation Verification & Agent Invocation

#### For SINGLE MODE:

**MANDATORY - State this checklist FIRST:**

```
VERIFICATION CHECKLIST:
☐ Source file: [file path]
☐ Chief complaint: [chief complaint from arguments]
☐ Template files: Clinical_Physical_Assessment_REVISED.txt, Complete_Medical_History_Card.txt
☐ Physical exam resources: CloudDocs Practicals directory + source file
☐ Source-only policy: I will ONLY use information from source file
☐ No external medical facts will be added
☐ Output format: Interactive HTML with 6 tabs (including Patient Education)
☐ UI pattern: Accordion-based collapsible sections for conditions
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
☐ Template files: Clinical_Physical_Assessment_REVISED.txt, Complete_Medical_History_Card.txt
☐ Physical exam resources: CloudDocs Practicals directory + source file (per file)
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
☐ Template files: Clinical_Physical_Assessment_REVISED.txt, Complete_Medical_History_Card.txt
☐ Physical exam resources: CloudDocs Practicals directory + source file (unified)
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

2. **Medical History Card**: `study-guides/templates-and-examples/Complete_Medical_History_Card.txt`
   - Complete HPI (OLDCAARTS) components
   - PMH, FH, SH elements
   - Full ROS by system

3. **Physical Exam Resources** (CloudDocs):
   - Protocol: `/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Practicals/Protocol for Complete Physical Exam.pdf`
   - Specialized Exams: `/Users/kimnguyen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Midwestern/Practicals/Specialized Exams update.xlsx`
   - Extract comprehensive PE protocol and specialized exam maneuvers

4. **Source File**: $ARGUMENTS
   - Extract all conditions/differentials
   - Note condition-specific physical exam findings
   - Identify specialized tests
   - **Combine PE findings**: Use BOTH CloudDocs resources AND source file exams

### Step 3: Load Physical Exam Resources from CloudDocs

**Read CloudDocs Practicals directory resources:**

1. **Protocol for Complete Physical Exam.pdf**:
   - Read the comprehensive PE protocol
   - Extract systematic exam approach (Inspection, Palpation, Percussion, Auscultation, ROM)
   - Note general physical exam maneuvers

2. **Specialized Exams update.xlsx**:
   - Read specialized exam database
   - Extract condition-specific maneuvers
   - Note special tests and techniques

**Purpose**: These provide the comprehensive PE foundation that will be combined with condition-specific exams from the source file.

### Step 4: Analyze Source File

**CRITICAL - Read ENTIRE source file:**
- Identify ALL conditions mentioned
- Group by onset pattern (acute, subacute, chronic)
- Extract condition-specific physical exam maneuvers
- Note specialized tests
- Document decision points

**Physical Exam Integration**:
- **Combine** CloudDocs PE protocol (comprehensive baseline) + Source file PE findings (condition-specific)
- For each condition, include BOTH general PE approach AND specialized maneuvers
- Example: For knee pain → General MSK exam (from CloudDocs) + McMurray test, Lachman test (from source)

### Step 5: Create 6-Tab HTML Guide

**Required Tabs:**

**IMPORTANT - UI Structure:**
- Use accordion-based collapsible sections for condition-specific content (Tabs 1-3, Tab 6)
- Place general OLDCAARTS box OUTSIDE accordions (always visible) at top of Tabs 1-3
- Place general Patient Education box OUTSIDE accordions at top of Tab 6
- Use compact styling (13px font, tighter spacing) per template specifications

**Tab 1: Acute Onset (Hours to Days)**
- General OLDCAARTS box at top (OUTSIDE accordion - always visible)
- Condition accordions with:
  - Top differentials for acute presentation
  - Complete HPI (OLDCAARTS) with exact questions in quotes
  - Essential PMH, FH, SH
  - Focused ROS with checkboxes
  - Physical Exam Focus (Inspection, Palpation, ROM, Special Tests)
- Color: Red (#dc2626) for emergency, Orange (#f97316) for acute

**Tab 2: Subacute Onset (Days to Weeks)**
- Same structure as Tab 1 with condition-specific questions
- Color: Yellow (#eab308) for subacute conditions

**Tab 3: Chronic Onset (Weeks to Months)**
- Same structure with chronic-specific considerations
- Color: Green (#22c55e) for chronic conditions

**Tab 4: Focused Physical Exam**
- Detailed physical examination by anatomical region
- **Use combined PE approach**: CloudDocs protocol + source file maneuvers
- Inspection: What to look for (be specific)
- Palpation: What to feel for
- Percussion/Auscultation: When applicable (from CloudDocs protocol)
- ROM: Range of motion testing (from CloudDocs)
- Special tests: Named maneuvers with technique (from BOTH CloudDocs Specialized Exams + source file)
- Group conditions with same physical exam together

**Tab 5: Quick Reference Chart**
- "If patient answers X, ask Y"
- "If examination X is positive, do Y"
- Red flags requiring immediate action
- Decision support tables

**Tab 6: Patient Education (NEW)**
- **General Patient Education Box (at top, NOT in accordion):**
  - Medication information with risks/side effects (NSAIDs, Muscle Relaxants, Corticosteroids, Opioids)
  - Smoking Cessation section (paragraph form)
  - When to Seek Immediate Emergency Care (red flag symptoms)
  - Follow-Up Care expectations
- **Condition-Specific Patient Education (in accordions):**
  - Each condition in collapsible accordion
  - Format: "What It Is", "What to Expect", "Treatment" in paragraph form
  - Color coding matches condition urgency (red=emergency, orange=acute, green=chronic)

### Step 6: HPI Format (OLDCAARTS)

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

### Step 7: Essential History (from Medical History Card)

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

### Step 8: Focused ROS

Use checkbox format (☐) for each system:
- **General**: Fever, chills, weight change, fatigue, night sweats
- **Skin**: Rash, itching, changes
- **MSK**: Joint pain, stiffness, swelling, ROM limitations
- **Neuro**: Weakness, numbness, tingling, falls
- **CV**: Chest pain, palpitations, edema
- **Other systems as relevant to chief complaint**

### Step 9: Physical Exam Specificity

**Be specific about what to examine FOR:**
- ✅ "Inspect skin for erythema, edema, ecchymosis, deformity"
- ❌ "Inspect skin"

- ✅ "Palpate for warmth, point tenderness, crepitus, effusion"
- ❌ "Palpate joint"

- ✅ "Test ROM: flexion (0-140°), extension (0°), internal rotation (0-40°)"
- ❌ "Test ROM"

### Step 10: HTML Formatting

**Required:**
- Inline CSS styles (no external stylesheets)
- Interactive tabs with onclick navigation (6 tabs)
- Accordion UI for condition-specific content (see template for CSS/JS)
- Compact styling (13px base font, tighter spacing)
- Responsive grid layouts
- Color-coded sections:
  - Red (#dc2626): Acute/Emergency
  - Orange (#f97316): Subacute/Urgent
  - Yellow (#eab308): Subacute
  - Green (#22c55e): Chronic
  - Blue (#3b82f6): Information sections
- Mobile responsiveness (@media queries for smaller screens)

### Step 11: Use TodoWrite

Track your progress:
- Create todo for each tab
- Create todo for each major section
- Mark completed as you finish
- Keep user informed

### Step 12: Post-Creation Verification

**Automatically verify the completed file:**

1. **Source Accuracy**
   - All medical facts from source file only
   - No external conditions or treatments added
   - Terminology matches source exactly

2. **Template Compliance**
   - All 6 tabs present (Acute, Subacute, Chronic, Focused PE, Quick Reference, Patient Education)
   - Accordion UI implemented for condition-specific content (Tabs 1-3, Tab 6)
   - General OLDCAARTS box outside accordions (Tabs 1-3)
   - General Patient Education box outside accordions (Tab 6)
   - OLDCAARTS complete with all 10 elements (in quotes)
   - PMH/FH/SH/ROS following Medical History Card format
   - Physical exam following Assessment template structure
   - Patient Education with "What It Is", "What to Expect", "Treatment" format

3. **Completeness**
   - All conditions from source included
   - All physical exam maneuvers included
   - Decision trees for all major differentials
   - Quick reference populated

4. **Quality**
   - All patient questions in quotes
   - Specific exam findings (what to inspect FOR)
   - Color-coded sections by urgency
   - Interactive tabs functional (6 tabs)
   - Accordion toggles working (expand/collapse)
   - Compact styling applied (13px font)
   - Patient Education complete with condition-specific accordions

**CRITICAL: State "Post-creation verification complete" and report any issues. Fix immediately.**

### Step 13: Save Files

**Study Guide Output:**
- Save to: `[Class]/[Exam]/Claude Study Tools/[Chief_Complaint]_Clinical_Assessment_Guide.html`
- Create Claude Study Tools folder if doesn't exist

**Python File:**
- Save to: `[Class]/[Exam]/Claude Study Tools/py/[Chief_Complaint]_Clinical_Assessment_Guide.py`
- Create `py/` subfolder if doesn't exist

- Confirm both files saved successfully


---

## Batch Processing

For batch operations (semicolon-separated files or --merge flag):
@.claude/skills/batch-coordinator/SKILL.md

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

