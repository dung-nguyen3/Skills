# CLAUDE GENERATOR TEMPLATES - Usage Guide

## Overview

This guide covers **all Claude generator templates** for creating study materials. These templates allow Claude to create complete ready-to-run scripts that generate study guides with minimal token usage.

## Available Templates

### 1. Excel Master Chart Generator
**File:** `excel_master_chart_CLAUDE_GENERATOR.py`
**Purpose:** Generate single-sheet Excel master charts
**Output:** Excel file with auto-colored rows by drug class/category

### 2. Excel Drug Chart Generator
**File:** `Comprehensive Excel Drugs Chart 11-1 template.py`
**Purpose:** Generate 4-tab comprehensive drug analysis charts
**Output:** Excel file with Drug Details, Key Comparisons, Master Chart, High-Yield tabs

### 3. Word Learning Objectives Generator
**File:** `LO Word 11-5 template.py`
**Purpose:** Generate formatted Word documents with learning objectives
**Output:** Word document with Q&A format, mnemonics, clinical pearls

### 4. HTML Learning Objectives Generator
**File:** `HTML_LO_CLAUDE_GENERATOR.py`
**Purpose:** Generate interactive HTML learning objectives
**Output:** HTML file with 4 tabs (LOs, Key Comparisons, Master Tables, Summary)

---

# Excel Master Chart Generator

## Purpose

This template (`excel_master_chart_CLAUDE_GENERATOR.py`) is specifically designed for **Claude to create complete ready-to-run scripts** that generate Excel Master Charts.

## When to Use This Template

Use this template when the user requests:
- "Create Excel master chart for [lecture file]"
- "Generate drug chart for [topic]"
- "Make master chart with [columns]"

## Workflow

### Step 1: Complete Verification Checklist (MANDATORY)

Before touching any files, Claude MUST state the verification checklist:

```
VERIFICATION CHECKLIST:
☑ Source file: /Users/kimnguyen/Documents/Github/Study Guide Creator/[exact path]
☑ Instruction template: Excel Master Chart Only.txt
☑ Source-only policy: I will ONLY use information from source file
☑ MANDATORY: I will use WebSearch to research mnemonics (not for data extraction)
☑ Save location: [Class]/[Exam]/Claude Study Tools/
```

### Step 2: Read the Template

Read the CLAUDE_GENERATOR template:
```
/Users/kimnguyen/Documents/Github/Study Guide Creator/Claude Templates/excel_master_chart_CLAUDE_GENERATOR.py
```

### Step 3: Read the Source File

Read the source file specified by the user (e.g., "24 HIV.txt")

### Step 4: Extract All Data

Extract ALL relevant information from the source file:
- Drug classes/categories
- Drug names (with brand names in parentheses)
- All column information (Route, Mechanism, Uses, etc.)
- Group drugs by class (all drugs in same class must be consecutive)

### Step 5: Fill in the Template

Copy the template and fill in these sections:

#### SOURCE_INFO Section (lines 40-46)
```python
SOURCE_FILE = "24 HIV.txt"  # Actual source file name
LECTURE_TOPIC = "HIV Drugs"  # Topic name
CREATION_DATE = "2025-01-19"  # Today's date
```

#### HEADERS Section (lines 79-92)

Choose the appropriate column set:

**For Drug Charts (11 columns):**
```python
HEADERS = [
    'Drug Class',
    'Drug Name (Brand)',
    'Route',
    'Mechanism',
    'Uses',
    'Adverse Effects',
    'Contraindications',
    'Resistance',
    'Drug Interactions',
    'Drug Combinations',
    'Special Considerations'
]
```

**For Condition Charts (7 columns):**
```python
HEADERS = [
    'Condition',
    'Epidemiology',
    'Risk Factors',
    'Clinical Presentation',
    'Diagnostics',
    'Labs',
    'Treatment'
]
```

**For Lab Value Charts (5 columns):**
```python
HEADERS = [
    'Test Name',
    'Normal Range',
    'Increased In',
    'Decreased In',
    'Clinical Significance'
]
```

#### DATA Section (lines 121-126)

**CRITICAL RULES:**
1. Group all drugs by class - drugs in same class MUST be together
2. Each row must have EXACTLY the same number of values as HEADERS
3. Use newlines (`\n`) for multi-line content within cells
4. Use emojis: 🟢 (first-line), ⚠️ (warnings), 🚫 (contraindications), ✅, ❌

**Example Data Format:**
```python
DATA = [
    # NRTI Class (all NRTIs together)
    ['NRTI', 'Tenofovir (Viread)', 'Oral', 'Adenosine analogue → inhibits RT', '🟢 HIV - First line\nPrEP', 'GI, flatulence\n⚠️ Lactic acidosis', 'Severe renal impairment', 'Rapid if alone', 'None major', 'Truvada (with emtricitabine)', 'Monitor renal function'],
    ['NRTI', 'Lamivudine (Epivir)', 'Oral', 'Cytosine analogue → inhibits RT', 'HIV treatment\nHBV', 'Headache, fatigue', 'None absolute', 'Rapid if alone', 'None major', 'With abacavir', '✅ Safe in pregnancy'],
    ['NRTI', 'Emtricitabine (Emtriva)', 'Oral', 'Cytosine analogue → inhibits RT', 'HIV treatment', 'Headache, nausea', 'None absolute', 'Rapid if alone', 'None major', 'Truvada, Descovy', 'Similar to lamivudine'],

    # NNRTI Class (new class starts)
    ['NNRTI', 'Rilpivirine (Edurant)', 'Oral', 'Binds RT allosteric site', 'HIV (with NRTIs)', 'Depression, headache', 'Hepatitis co-infection', 'Rapid if alone', 'None major', 'Cabenuva', 'Must use with NRTIs'],
    ['NNRTI', 'Efavirenz (Sustiva)', 'Oral', 'Binds RT allosteric site', 'HIV treatment', '⚠️ CNS effects, rash', '🚫 Pregnancy (1st trimester)', 'Rapid if alone', 'CYP450 inducer', 'Atripla', 'Take at bedtime'],
]
```

#### OUTPUT_FILENAME (line 129)
```python
OUTPUT_FILENAME = 'HIV_Drugs_Master_Chart.xlsx'  # Descriptive name
```

### Step 6: Save the Script

Save the completed script with a descriptive name:
```
[LectureNumber]_[Topic]_Master_Chart_Generator.py
```

Examples:
- `24_HIV_Master_Chart_Generator.py`
- `Diabetes_Conditions_Master_Chart_Generator.py`
- `Lab_Values_Master_Chart_Generator.py`

Save location: Same directory as source file, or in `Claude Study Tools/` folder

### Step 7: Inform User

Tell the user:
```
Created: [filename]
To generate Excel: python3 [filename]
Excel will open automatically with perfectly formatted chart.
```

## Auto-Coloring Behavior

The script automatically:
1. Detects when Drug Class (first column) changes
2. Assigns next color from 10-color rotation
3. All drugs in same class get same color

**Example:**
```
Row 1: NRTI → Ice Blue (#D9E2F3)
Row 2: NRTI → Ice Blue (same class)
Row 3: NRTI → Ice Blue (same class)
Row 4: NNRTI → Seafoam (#C8E6C9) - NEW CLASS!
Row 5: NNRTI → Seafoam (same class)
```

## Color Rotation Scheme

The 10 colors rotate automatically:
0. Ice Blue (#D9E2F3)
1. Seafoam (#C8E6C9)
2. Light Orchid (#D1C4E9)
3. Champagne (#F7E7CE)
4. Sky Blue (#BDD7EE)
5. Pale Azure (#F0F8FF)
6. Blush Pink (#FCE4EC)
7. Soft Lilac (#EDE7F6)
8. Soft Tangerine (#FFE8D6)
9. Powder Blue (#BBDEFB)

## Validation

The script includes automatic validation:
- Checks that each data row has correct number of columns
- Reports errors with row numbers if mismatch
- Prevents creation of malformed Excel files

## Common Mistakes to Avoid

### ❌ WRONG: Different number of columns
```python
HEADERS = ['Drug Class', 'Drug Name', 'Route']  # 3 columns
DATA = [
    ['NRTI', 'Tenofovir (Viread)', 'Oral', 'Extra value'],  # 4 values - ERROR!
]
```

### ✅ CORRECT: Matching columns
```python
HEADERS = ['Drug Class', 'Drug Name', 'Route']  # 3 columns
DATA = [
    ['NRTI', 'Tenofovir (Viread)', 'Oral'],  # 3 values - CORRECT!
]
```

### ❌ WRONG: Drug classes scattered
```python
DATA = [
    ['NRTI', 'Tenofovir', ...],
    ['NNRTI', 'Rilpivirine', ...],  # Don't mix classes
    ['NRTI', 'Lamivudine', ...],  # This will get wrong color!
]
```

### ✅ CORRECT: Drug classes grouped
```python
DATA = [
    ['NRTI', 'Tenofovir', ...],
    ['NRTI', 'Lamivudine', ...],  # All NRTIs together
    ['NRTI', 'Emtricitabine', ...],
    ['NNRTI', 'Rilpivirine', ...],  # Then all NNRTIs
    ['NNRTI', 'Efavirenz', ...],
]
```

## Example: Complete HIV Drugs Script

See the file you created earlier for reference:
```
/Users/kimnguyen/Documents/Github/Study Guide Creator/HIV_Master_Chart_Generator.py
```

This shows a complete example with:
- SOURCE_INFO filled in
- 11-column HEADERS for drug chart
- 17 HIV drugs in DATA array
- Proper grouping by drug class
- All auto-color logic working

## Quick Reference

**Template Location:**
```
/Users/kimnguyen/Documents/Github/Study Guide Creator/Claude Templates/excel_master_chart_CLAUDE_GENERATOR.py
```

**Typical User Request:**
```
"Create Excel master chart for 24 HIV.txt"
```

**Claude's Response Steps:**
1. ✅ State verification checklist
2. ✅ Read CLAUDE_GENERATOR.py template
3. ✅ Read 24 HIV.txt source file
4. ✅ Extract all drug data
5. ✅ Fill in SOURCE_INFO, HEADERS, DATA
6. ✅ Save as "24_HIV_Master_Chart_Generator.py"
7. ✅ Inform user: "Run: python3 24_HIV_Master_Chart_Generator.py"

## Testing Your Script

After creating the script, you can verify it works:
```bash
# Navigate to directory
cd "/Users/kimnguyen/Documents/Github/Study Guide Creator/"

# Run the script
python3 24_HIV_Master_Chart_Generator.py

# Excel should open automatically with perfect formatting
```

If validation errors appear, fix the DATA array to match HEADERS count.

---

**Version:** 1.0
**Created:** 2025-01-19
**Template:** excel_master_chart_CLAUDE_GENERATOR.py
**Compliance:** Excel Master Chart Only.txt

---

# HTML Learning Objectives Generator

## Purpose

This template (`HTML_LO_CLAUDE_GENERATOR.py`) is specifically designed for **Claude to create complete ready-to-run HTML learning objectives** with interactive 4-tab navigation.

## When to Use This Template

Use this template when the user requests:
- "Create HTML learning objectives for [lecture file]"
- "Generate interactive LO for [topic]"
- "Make HTML study guide for [file]"

## Workflow

### Step 1: Complete Verification Checklist (MANDATORY)

Before touching any files, Claude MUST state the verification checklist:

```
VERIFICATION CHECKLIST:
☑ Source file: /Users/kimnguyen/Documents/Github/Study Guide Creator/[exact path]
☑ Instruction template: HTML LO with Master Chart 10-30.txt
☑ Source-only policy: I will ONLY use information from source file
☑ MANDATORY: I will use WebSearch to research mnemonics (not for data extraction)
☑ Save location: [Class]/[Exam]/Claude Study Tools/
```

### Step 2: Read the Template

Read the HTML_LO_CLAUDE_GENERATOR template:
```
/Users/kimnguyen/Documents/Github/Study Guide Creator/Claude Templates/Py for Claude/HTML_LO_CLAUDE_GENERATOR.py
```

### Step 3: Read the Source File

Read the source file specified by the user (e.g., "Red Eye Lecture.txt")

### Step 4: Extract All Data

Extract ALL relevant information from the source file:
- **Learning objectives** (verbatim - do NOT paraphrase)
- Answers to each objective
- Conditions/topics for comparison tables
- Emergency vs urgent vs routine classifications
- Mnemonics (research using WebSearch)
- If-Then clinical rules
- Critical values and definitions

### Step 5: Fill in the Template

Copy the template and fill in these sections:

#### SOURCE_INFO Section
```python
SOURCE_FILE = "Red Eye Lecture.txt"
LECTURE_TOPIC = "Red Eye Differential Diagnosis"
CREATION_DATE = "2025-01-19"
```

#### Tab 1: LEARNING_OBJECTIVES
```python
LEARNING_OBJECTIVES = [
    {
        'number': 1,
        'objective': 'Describe the pathophysiology of conjunctivitis',
        'answer': '''
            <h4>Pathophysiology of Conjunctivitis</h4>
            <p>Inflammation of the conjunctiva caused by:</p>
            <ul>
                <li><strong>Viral:</strong> Adenovirus (most common), HSV, VZV</li>
                <li><strong>Bacterial:</strong> S. aureus, S. pneumoniae, H. influenzae</li>
                <li><strong>Allergic:</strong> IgE-mediated hypersensitivity</li>
            </ul>
            <p><span class="highlight-blue">Key mechanism:</span> Vasodilation and inflammatory cell infiltration</p>
        '''
    },
    {
        'number': 2,
        'objective': 'Differentiate acute angle-closure glaucoma from other red eye causes',
        'answer': '''
            <h4>Acute Angle-Closure Glaucoma vs Other Red Eye</h4>
            <table>
                <tr>
                    <th>Feature</th>
                    <th>Acute Angle-Closure</th>
                    <th>Other Red Eye</th>
                </tr>
                <tr class="emergency">
                    <td>Pupil</td>
                    <td><span class="highlight-red">Mid-dilated, fixed</span></td>
                    <td>Normal or reactive</td>
                </tr>
                <tr class="emergency">
                    <td>IOP</td>
                    <td><span class="highlight-red">>40 mmHg</span></td>
                    <td>Normal (10-21 mmHg)</td>
                </tr>
            </table>
        '''
    }
]
```

#### Tab 2: KEY_COMPARISONS
```python
KEY_COMPARISONS = [
    {
        'title': 'Viral vs Bacterial vs Allergic Conjunctivitis',
        'headers': ['Feature', 'Viral', 'Bacterial', 'Allergic'],
        'rows': [
            {
                'urgency': 'routine',
                'cells': ['Discharge', 'Watery', '<strong>Purulent</strong>', 'Stringy mucoid']
            },
            {
                'urgency': 'routine',
                'cells': ['Itching', 'Minimal', 'Minimal', '<strong>Severe</strong>']
            },
            {
                'urgency': 'routine',
                'cells': ['Treatment', 'Supportive', 'Topical antibiotics (erythromycin)', 'Antihistamines (olopatadine)']
            }
        ]
    },
    {
        'title': 'Episcleritis vs Scleritis',
        'headers': ['Feature', 'Episcleritis', 'Scleritis'],
        'rows': [
            {
                'urgency': 'routine',
                'cells': ['Pain', 'Mild', '<span class="highlight-yellow">Severe, deep</span>']
            },
            {
                'urgency': 'routine',
                'cells': ['Vision', 'Normal', 'May be decreased']
            },
            {
                'urgency': 'urgent',
                'cells': ['Urgency', 'Routine', '<span class="highlight-yellow">URGENT referral</span>']
            }
        ]
    }
]
```

#### Tab 3: MASTER_TABLES
```python
MASTER_TABLES = [
    {
        'title': 'Complete Red Eye Differential Diagnosis',
        'description': 'Comprehensive comparison of ALL red eye conditions from lecture (14 total conditions)',
        'headers': ['Condition', 'Vision', 'Pain', 'Discharge', 'Pupil', 'Key Features', 'Management'],
        'rows': [
            {
                'urgency': 'emergency',  # Red background
                'cells': [
                    '<strong>Acute Angle-Closure Glaucoma</strong>',
                    '<span class="highlight-red">Severely decreased</span>',
                    '<span class="highlight-red">Severe</span>',
                    'None',
                    'Mid-dilated, fixed',
                    'IOP >40, corneal edema, nausea/vomiting, halos around lights',
                    '<span class="highlight-red">EMERGENCY:</span> Immediate ophthalmology, acetazolamide, topical beta-blocker'
                ]
            },
            {
                'urgency': 'urgent',  # Orange background
                'cells': [
                    '<strong>Corneal Ulcer</strong>',
                    'Decreased',
                    'Severe',
                    'Purulent',
                    'Normal or miotic',
                    'White infiltrate, hypopyon possible, contact lens wearer',
                    '<span class="highlight-yellow">URGENT:</span> Ophthalmology within 24h, topical fluoroquinolone'
                ]
            },
            {
                'urgency': 'routine',  # White background
                'cells': [
                    '<strong>Viral Conjunctivitis</strong>',
                    'Normal',
                    'Minimal',
                    'Watery',
                    'Normal',
                    'Preauricular LAD, follicles, highly contagious',
                    'Supportive care (cool compresses), no antibiotics needed'
                ]
            },
            # ... continue for all 14 conditions
        ]
    }
]
```

#### Tab 4: SUMMARY_DATA
```python
SUMMARY_DATA = {
    'key_points': [
        'Acute angle-closure glaucoma = mid-dilated fixed pupil + IOP >40 + severe pain → EMERGENCY ophthalmology',
        'Viral conjunctivitis = watery discharge + preauricular LAD + follicles → supportive care, highly contagious 10-12 days',
        'Corneal ulcer = white infiltrate + contact lens wearer → URGENT ophthalmology within 24h',
        'HSV keratitis = dendritic lesion on fluorescein → oral acyclovir, never use steroids',
    ],

    'mnemonics': [
        {
            'topic': 'Corneal Ulcer Red Flags (researched)',
            'mnemonic': 'FEVER',
            'breakdown': {
                'F': 'Fluorescein uptake (dendritic pattern)',
                'E': 'Eye pain severe',
                'V': 'Vision decreased',
                'E': 'Epithelial defect visible',
                'R': 'Referral urgent to ophthalmology'
            }
        }
    ],

    'if_then_rules': [
        {
            'if': 'Mid-dilated fixed pupil + severe eye pain + nausea',
            'then': 'Think acute angle-closure glaucoma → EMERGENCY ophthalmology + acetazolamide'
        },
        {
            'if': 'Dendritic lesion on fluorescein staining',
            'then': 'Think HSV keratitis → oral acyclovir + NEVER use steroids'
        },
        {
            'if': 'Contact lens wearer + purulent discharge + severe pain',
            'then': 'Think Pseudomonas corneal ulcer → URGENT ophthalmology + fluoroquinolone'
        }
    ],

    'critical_values': [
        {'parameter': 'Normal IOP', 'value': '10-21 mmHg'},
        {'parameter': 'Emergency IOP', 'value': '>40 mmHg (acute angle-closure glaucoma)'},
        {'parameter': 'Elevated IOP', 'value': '25-35 mmHg (ophthalmology consultation)'}
    ],

    'definitions': [
        {'term': 'Hyphema', 'definition': 'Blood in anterior chamber (trauma, bleeding disorder)'},
        {'term': 'Hypopyon', 'definition': 'Pus in anterior chamber (corneal ulcer, endophthalmitis)'},
        {'term': 'Ciliary flush', 'definition': 'Ring of redness around cornea (iritis, glaucoma, keratitis)'}
    ],

    'pearls': [
        '⚠️ Never patch a contact lens wearer with corneal abrasion (risk of Pseudomonas infection)',
        '✅ Viral conjunctivitis is self-limited but highly contagious for 10-12 days',
        '🚫 Never use topical steroids for HSV keratitis (causes geographic ulcer)',
        '⚠️ Acute angle-closure glaucoma can present with nausea/vomiting - don\'t miss the eye exam!',
        '✅ Preauricular LAD is pathognomonic for viral conjunctivitis (not bacterial)'
    ]
}
```

#### OUTPUT_FILENAME
```python
OUTPUT_FILENAME = 'Red_Eye_Learning_Objectives.html'
```

### Step 6: Save the Script

Save the completed script with a descriptive name:
```
[LectureNumber]_[Topic]_Learning_Objectives.py
```

Examples:
- `Red_Eye_Learning_Objectives.py`
- `Pharyngitis_Learning_Objectives.py`
- `24_HIV_Learning_Objectives.py`

Save location: Same directory as source file, or in `Claude Study Tools/` folder

### Step 7: Inform User

Tell the user:
```
Created: Red_Eye_Learning_Objectives.py
To generate HTML: python3 Red_Eye_Learning_Objectives.py
HTML will open automatically in browser with 4 interactive tabs.
```

## HTML Styling Features

### Color-Coded Urgency Levels

**Emergency (Red background):**
- `'urgency': 'emergency'`
- Background: `#ffebee` (light red)
- Use for: Life-threatening conditions (acute angle-closure glaucoma, orbital cellulitis)

**Urgent (Orange background):**
- `'urgency': 'urgent'`
- Background: `#fff3e0` (light orange)
- Use for: Time-sensitive conditions (corneal ulcer, scleritis, iritis)

**Routine (White background):**
- `'urgency': 'routine'`
- Background: white
- Use for: Non-urgent conditions (viral conjunctivitis, subconjunctival hemorrhage)

### Inline Highlighting

Use these highlight spans within cell content:

```html
<span class="highlight-red">EMERGENCY</span> - Life-threatening
<span class="highlight-yellow">URGENT</span> - Time-sensitive
<span class="highlight-purple">Pathognomonic sign</span> - Diagnostic feature
<span class="highlight-blue">Distinguishing feature</span> - Differentiating finding
<span class="highlight-green">Normal value</span> - Expected range
```

### HTML Formatting in Answers

You can use HTML in the `answer` field:

```python
answer: '''
    <h4>Section Title</h4>
    <p>Paragraph text with <strong>bold</strong> and <em>italic</em>.</p>
    <ul>
        <li>Bullet point 1</li>
        <li>Bullet point 2</li>
    </ul>
    <table>
        <tr><th>Column 1</th><th>Column 2</th></tr>
        <tr><td>Data 1</td><td>Data 2</td></tr>
    </table>
'''
```

## Common Mistakes to Avoid

### ❌ WRONG: Paraphrasing learning objectives
```python
# Source says: "Describe the pathophysiology and clinical presentation of conjunctivitis"
'objective': 'Explain how conjunctivitis works'  # DON'T PARAPHRASE!
```

### ✅ CORRECT: Verbatim objectives
```python
'objective': 'Describe the pathophysiology and clinical presentation of conjunctivitis'
```

### ❌ WRONG: Inventing mnemonics
```python
'mnemonics': [
    {
        'topic': 'Red Eye Causes',
        'mnemonic': 'REDEYE',  # Claude invented this!
        'breakdown': {...}
    }
]
```

### ✅ CORRECT: Researched mnemonics
```python
# After using WebSearch to find established mnemonics:
'mnemonics': [
    {
        'topic': 'Corneal Ulcer Red Flags',
        'mnemonic': 'FEVER',  # Found via WebSearch
        'breakdown': {
            'F': 'Fluorescein uptake',
            # ...
        }
    }
]
```

### ❌ WRONG: Missing urgency classification
```python
'rows': [
    {
        'cells': ['Acute Angle-Closure Glaucoma', ...]  # No urgency!
    }
]
```

### ✅ CORRECT: Proper urgency classification
```python
'rows': [
    {
        'urgency': 'emergency',  # Red background
        'cells': ['<strong>Acute Angle-Closure Glaucoma</strong>', ...]
    }
]
```

## Token Savings

**WITHOUT HTML template:**
- Claude generates full HTML structure from scratch: ~3,500 tokens
- Includes CSS, JavaScript, table formatting

**WITH HTML template:**
- Claude fills in data sections only: ~1,500 tokens
- **Savings: ~2,000 tokens per HTML file (57% reduction)**

## Quick Reference

**Template Location:**
```
/Users/kimnguyen/Documents/Github/Study Guide Creator/Claude Templates/Py for Claude/HTML_LO_CLAUDE_GENERATOR.py
```

**Typical User Request:**
```
"Create HTML learning objectives for Red Eye Lecture.txt"
```

**Claude's Response Steps:**
1. ✅ State verification checklist
2. ✅ Read HTML_LO_CLAUDE_GENERATOR.py template
3. ✅ Read Red Eye Lecture.txt source file
4. ✅ Extract learning objectives (verbatim), answers, comparisons
5. ✅ Research mnemonics using WebSearch
6. ✅ Fill in all 4 tab data sections
7. ✅ Save as "Red_Eye_Learning_Objectives.py"
8. ✅ Inform user: "Run: python3 Red_Eye_Learning_Objectives.py"

---

**Version:** 2.0
**Last Updated:** 2025-01-19
**Templates Included:** Excel Master Chart, Excel Drug Chart, Word LO, HTML LO
