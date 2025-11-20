# Template Analysis - All Study Guide Templates

## Summary Overview

**Templates Analyzed:**
1. Excel Drugs Chart 11-1.txt (1,144 lines) ⚠️ MOST REDUNDANT
2. Excel Master Chart Only.txt (495 lines) ⚠️ REDUNDANT
3. HTML LO with Master Chart 10-30.txt (137 lines) ✅ LEAN
4. Autobiography Drug Stories.txt (252 lines) ✅ MOSTLY UNIQUE
5. Word LO 11-5.txt (695 lines) ⚠️ REDUNDANT (Already revised)

---

## 1. EXCEL DRUGS CHART 11-1.TXT (1,144 lines)

### CRITICAL ISSUES:
- **440+ lines of redundant content** (38% of file)
- Repeats policies already in CLAUDE.md 8+ times
- Massive Python code examples (250+ lines) could be separate file

### REDUNDANT WITH CLAUDE.MD:
- ❌ Lines 8-22: Verification checklist (already in CLAUDE.md lines 36-48)
- ❌ Lines 25-38: Source-only policy (already in CLAUDE.md lines 54-59)
- ❌ Lines 39-43: WebSearch requirement (already in CLAUDE.md lines 61-67)
- ❌ Lines 52-61: Verification statements (already in CLAUDE.md)
- ❌ Lines 103-125: Analysis process (slash command workflow, not template content)
- ❌ Lines 122-138: WebSearch strategy (generic, already in CLAUDE.md)

### REDUNDANT WITHIN FILE:
- "Source file only" repeated 8+ times
- Color schemes repeated in every code section
- Row height checking repeated 3 times
- Same mnemonic research instructions repeated 4 times

### SHOULD MOVE TO:
- **Slash command (/create-excel):** Lines 103-125 (analysis workflow)
- **CLAUDE.md:** Lines 8-61 (policies already there)
- **Separate file (Excel_Drug_Example.py):** Lines 600-900 (Python code examples)
- **SKILL (mnemonic-researcher):** Lines 122-138 (WebSearch strategy)

### RECOMMENDED CHANGES:
- ✂️ Remove lines 8-61 → Replace with: "See parent CLAUDE.md for verification and source policies"
- ✂️ Remove lines 103-125 → Move to /create-excel slash command
- ✂️ Consolidate color schemes (currently shown 5+ times)
- ✂️ Move Python examples to separate reference file
- 📉 **Reduce from 1,144 → ~550 lines (52% reduction)**

### UNIQUE CONTENT TO KEEP:
- Tab structure for drug charts (4 tabs specific format)
- Drug-specific data extraction rules
- Analogy requirements for drug mechanisms
- Color scheme for drug classes
- Table formatting specifications

---

## 2. EXCEL MASTER CHART ONLY.TXT (495 lines)

### REDUNDANT WITH CLAUDE.MD:
- ❌ Lines 1-5: Purpose statement (generic)
- ❌ No verification checklist but should reference CLAUDE.md

### REDUNDANT WITH EXCEL DRUGS CHART:
- ❌ Lines 46-100: Color scheme (IDENTICAL to Excel Drugs Chart)
- ❌ Lines 194-310: Python template (similar pattern to Excel Drugs Chart)
- ❌ Lines 413-441: Common mistakes (overlaps with Excel Drugs Chart)

### SHOULD CONSOLIDATE:
- **Merge color schemes:** Create single "Excel Color Reference.txt" shared by both templates
- **Consolidate Python code:** Create "Excel_Python_Functions.py" shared reference

### RECOMMENDED CHANGES:
- ✂️ Lines 46-100: Replace with "See Excel Color Reference for color scheme"
- ✂️ Lines 194-310: Shorten to structure only, reference shared Python file
- ➕ Add verification checklist reference to CLAUDE.md
- 📉 **Reduce from 495 → ~280 lines (43% reduction)**

### UNIQUE CONTENT TO KEEP:
- Single-sheet structure (different from 4-tab drug chart)
- Flexible column approach (user-defined)
- Master chart specific formatting
- Simple color rotation logic

---

## 3. HTML LO WITH MASTER CHART 10-30.TXT (137 lines)

### STATUS: ✅ MOSTLY LEAN - Well-structured

### MINOR REDUNDANCIES:
- ❌ Lines 3-8: Source-only policy (shortened but still redundant with CLAUDE.md)
- ❌ Line 5: "Verbatim objectives" (generic rule, could be in CLAUDE.md)

### RECOMMENDED CHANGES:
- ✂️ Lines 3-8: Replace with "See CLAUDE.md for source-only policy"
- ➕ Add reference to parent CLAUDE.md at top
- 📉 **Reduce from 137 → ~125 lines (9% reduction)** - minimal changes needed

### UNIQUE CONTENT TO KEEP (ALL GOOD):
- Tab structure explanation (clear purpose for each tab)
- HTML formatting examples with color codes
- Emergency level color-coding (red/orange/white)
- Inline highlighting classes
- Complete differential diagnosis approach
- Clinical decision support focus

### WHY THIS TEMPLATE IS GOOD:
- Focused on structure and purpose
- Minimal redundancy
- Clear examples
- No Python code bloat
- HTML-specific formatting only

---

## 4. AUTOBIOGRAPHY DRUG STORIES.TXT (252 lines)

### STATUS: ✅ UNIQUE CREATIVE FORMAT - Minimal redundancy

### REDUNDANCIES:
- ❌ Line 237: "Use exact information from source" (CLAUDE.md policy)
- ❌ Line 238: "Don't add external knowledge" (CLAUDE.md policy)

### RECOMMENDED CHANGES:
- ✂️ Lines 237-238: Replace with "See CLAUDE.md for source-only policy"
- ➕ Add: "MANDATORY: WebSearch for creative analogies and metaphors"
- 📉 **Reduce from 252 → ~245 lines (3% reduction)** - barely any changes

### UNIQUE CONTENT TO KEEP (ALL CREATIVE):
- Character development guidelines
- Narrative structure (introduction, mechanism as story, interactions)
- Creative analogies catalog
- Dialogue format examples
- Dramatic elements (reveals, warnings, rescue scenarios)
- Family dynamics framework
- Tone guidelines
- All storytelling elements

### WHY THIS TEMPLATE IS GOOD:
- Completely unique format
- Creative educational approach
- No policy redundancy (just 2 lines)
- Focused on creative storytelling
- No code examples

---

## 5. WORD LO 11-5.TXT (695 lines) - ✅ ALREADY REVISED

**See:** Word_LO_11-5_REVISED.txt (450 lines)
- Already analyzed and cleaned up
- 35% reduction achieved
- Fixed table text color issue
- Removed redundancies with CLAUDE.md

---

## CROSS-TEMPLATE REDUNDANCIES

### Color Schemes (Repeated in 3 templates):
- Excel Drugs Chart: Lines 165-262
- Excel Master Chart: Lines 46-100
- Word LO: Lines 163-213

**SOLUTION:** Create shared color reference files:
- `Excel_Color_Reference.txt` (for both Excel templates)
- Keep Word colors in Word template (different color scheme)

### Python Code Examples (Repeated patterns):
- Excel Drugs Chart: 250+ lines of Python
- Excel Master Chart: 150+ lines of Python
- Word LO: 150+ lines of Python

**SOLUTION:** Create separate example files:
- `Excel_Drug_Example.py` (complete working example)
- `Excel_Master_Chart_Example.py` (complete working example)
- `Word_LO_Example.py` (complete working example)
- Keep only essential helper functions in templates

### Source-Only Policy (In ALL 5 templates):
- Excel Drugs Chart: 8+ mentions
- Excel Master Chart: Implied but not stated
- HTML LO: Lines 3-8
- Autobiography: Lines 237-238
- Word LO: Already fixed in REVISED version

**SOLUTION:** All templates should just reference CLAUDE.md:
```
## Core Requirements
See parent CLAUDE.md for:
- Source-only policy
- WebSearch requirements for mnemonics
- Verification checklists
- File organization
```

### WebSearch/Mnemonic Requirements (In 4 templates):
- Excel Drugs Chart: Lines 122-138 + multiple repeats
- Excel Master Chart: Not mentioned (should be)
- HTML LO: Not mentioned (should be)
- Autobiography: Should be added for creative analogies
- Word LO: Already fixed in REVISED version

**SOLUTION:** Reference CLAUDE.md + add to SKILL:
- Create/enhance `mnemonic-researcher` SKILL with WebSearch strategy
- Templates just say: "MANDATORY: WebSearch for mnemonics (see CLAUDE.md)"

---

## CONSOLIDATION OPPORTUNITIES

### 1. Create Shared Reference Files

**Excel_Color_Reference.txt:**
- Consolidate color schemes from both Excel templates
- Single source of truth for Excel colors
- Both Excel templates reference this file

**Python_Examples/ folder:**
- `Excel_Drug_Complete_Example.py`
- `Excel_Master_Chart_Complete_Example.py`
- `Word_LO_Complete_Example.py`
- Full working code with comments
- Templates only show helper functions

### 2. Move to CLAUDE.md

**Already in CLAUDE.md but repeated in templates:**
- Source-only policy
- WebSearch requirements
- Verification checklists
- File organization
- Post-creation verification

**Should add to CLAUDE.md:**
- "NO page references in Word documents" (specific to Word)
- "Include page references in Excel documents" (specific to Excel)

### 3. Move to Slash Commands

**Analysis workflows (currently in templates):**
- Excel Drugs Chart lines 103-125 → `/create-excel`
- Data extraction process → `/create-excel`
- Step-by-step workflow → All slash commands

### 4. Enhance Skills

**mnemonic-researcher SKILL:**
- Add WebSearch strategies from templates
- Automate mnemonic research
- Return researched mnemonics

**template-compliance-checker SKILL:**
- Verify color schemes
- Check structure (4 tabs, etc.)
- Validate formatting

---

## RECOMMENDED ACTION PLAN

### PRIORITY 1: Excel Drugs Chart (Biggest Impact)
1. Remove 440 lines of redundancy
2. Move Python code to separate file
3. Reference CLAUDE.md for policies
4. Move workflows to /create-excel slash command
5. **Result:** 1,144 → 550 lines (52% reduction)

### PRIORITY 2: Excel Master Chart
1. Remove duplicate color schemes
2. Consolidate Python code
3. Reference shared Excel color file
4. **Result:** 495 → 280 lines (43% reduction)

### PRIORITY 3: Create Shared Files
1. Excel_Color_Reference.txt (shared by both Excel templates)
2. Python_Examples/ folder with complete working code
3. Update templates to reference these files

### PRIORITY 4: HTML LO (Minor)
1. Remove source-only policy lines (reference CLAUDE.md)
2. **Result:** 137 → 125 lines (9% reduction)

### PRIORITY 5: Autobiography (Minimal)
1. Remove 2 lines referencing source policy
2. Add WebSearch requirement for creative analogies
3. **Result:** 252 → 245 lines (3% reduction)

---

## TOTAL IMPACT

**Before:**
- Excel Drugs Chart: 1,144 lines
- Excel Master Chart: 495 lines
- HTML LO: 137 lines
- Autobiography: 252 lines
- Word LO: 695 lines (original)
- **TOTAL: 2,723 lines**

**After Cleanup:**
- Excel Drugs Chart: ~550 lines (-52%)
- Excel Master Chart: ~280 lines (-43%)
- HTML LO: ~125 lines (-9%)
- Autobiography: ~245 lines (-3%)
- Word LO: 450 lines (already revised, -35%)
- **TOTAL: ~1,650 lines**

**Overall Reduction: 1,073 lines (39% reduction)**

---

## FILES TO CREATE

### New Reference Files:
1. `Excel_Color_Reference.txt` (consolidate Excel color schemes)
2. `Python_Examples/Excel_Drug_Complete_Example.py`
3. `Python_Examples/Excel_Master_Chart_Complete_Example.py`
4. `Python_Examples/Word_LO_Complete_Example.py`

### Updated in CLAUDE.md:
- Add: "Word documents: NO page references"
- Add: "Excel documents: Include page references for verification"
- Ensure all policies are comprehensive and referenced by templates

### Enhanced Skills:
- `mnemonic-researcher/SKILL.md` - Add WebSearch strategies
- `template-compliance-checker/SKILL.md` - Add color/structure validation

---

**End of Analysis**
