# Study Guide Creation - Core Protocol

## Purpose
Create comprehensive pharmacy study guides (Word, Excel, HTML) from source materials with strict quality controls.

## Templates Available
- **Word**: `Claude Templates/Word LO 11-5.txt` - Learning objectives with tables
- **Excel**: `Claude Templates/Excel Drugs Chart 11-1.txt` - 4-tab drug charts
- **HTML**: `Claude Templates/HTML LO with Master Chart 10-30.txt` - Interactive lessons

---

## MANDATORY: Pre-Creation Verification

**Before creating ANY study guide, STATE this checklist:**

```
VERIFICATION CHECKLIST:
☐ Source file: [exact filename and path]
☐ Instruction template: [template name]
☐ Source-only policy: I will ONLY use information from [source file]
☐ Exception: Memory tricks/mnemonics WILL be researched via WebSearch
☐ MANDATORY: I will WebSearch for mnemonics/analogies - I will NOT invent them
☐ Save location: [Class]/[Exam]/Claude Study Tools/
```

**This applies to EACH new study guide.** If user says "do this for file 35", complete full verification again.

---

## Core Rules (MANDATORY)

### 1. Source-Only Policy
- **Use ONLY source file information** for medical content
- **NO external medical facts** unless marked with asterisk (*)
- **Exception:** MUST WebSearch for mnemonics, analogies, memory tricks
- Cite page numbers when referencing source
- Ask user which file to use if unclear

### 2. WebSearch Requirement
**MANDATORY for ALL study guides:**
- Research PROVEN, ESTABLISHED mnemonics (never invent)
- Find GOOD analogies for drug mechanisms and concepts
- Look for "If X think Y" clinical associations
- **CRITICAL: Cannot skip WebSearch for memory aids**

### 3. Learning Objectives Completeness
- Answer ALL parts of each learning objective
- Example: "Describe components. Describe findings. Demonstrate technique" = 3 parts
- Verify all parts answered before moving on

### 4. Data Accuracy
- **Before merging cells/grouping:** Verify items share IDENTICAL information
- Do NOT group drugs/conditions unless source explicitly groups them
- Verify drug-specific vs class-wide information
- Double-check all classifications

### 5. Template Compliance
- Follow template instructions EXACTLY
- Read entire template file before starting
- All required sections/tabs must be present
- Use specified colors, formatting, structure

### 6. File Organization
- Save to: `[Class]/[Exam]/Claude Study Tools/`
- Create folder if doesn't exist
- Never save to home directory

---

## MANDATORY: Post-Creation Verification

**After creating ANY study guide, automatically verify:**

### 1. Source Accuracy
- ✓ All information from source file only (except mnemonics)
- ✓ External additions marked with asterisk (*)
- ✓ Page references included where required

### 2. Template Compliance
- ✓ ALL template instructions followed exactly
- ✓ Correct structure (all tabs/sections present)
- ✓ Correct formatting (colors, fonts, styles)
- ✓ All required elements included (tables, boxes, mnemonics)

### 3. Completeness
- ✓ All learning objectives answered (all parts)
- ✓ All comparison tables created as specified
- ✓ Master chart includes ALL topics from source
- ✓ No missing content

### 4. Quality Checks
- ✓ No incorrect groupings or merged cells
- ✓ No spelling errors
- ✓ Proper formatting throughout
- ✓ TodoWrite tool used to track progress

**CRITICAL: State "Post-creation verification complete" and report any issues. Fix immediately.**

---

## Key Comparison Charts

Create comparison charts when 2+ items need differentiation:
- Drugs with different mechanisms
- Similar conditions with different presentations
- Exam techniques that need contrast
- **For drug mechanisms:** Include "Analogy" column with researched analogies

---

## Detailed Analysis Protocol

For in-depth accuracy analysis of existing study guides, use:
- **Slash command:** `/verify-accuracy [filename]` (when available)
- **Manual:** Request "analyze [file] for accuracy against [source]"

Detailed protocol includes:
- Systematic verification of all content
- Name/classification accuracy checks
- Merged cell verification
- Format/color compliance
- 6-step analysis with re-verification

---

## Common Mistakes to Avoid

❌ Inventing mnemonics instead of researching
❌ Adding external medical facts without asterisks
❌ Grouping drugs/items that don't share identical info
❌ Missing parts of multi-part learning objectives
❌ Skipping pre-creation verification checklist
❌ Not stating "Post-creation verification complete"
❌ Creating files outside Claude Study Tools folder

---

## Workflow Summary

1. **Pre-Creation:** State verification checklist
2. **Read:** Load and read template file completely
3. **Create:** Follow template exactly, use only source info
4. **Research:** WebSearch for mnemonics/analogies (mandatory)
5. **Track:** Use TodoWrite throughout creation
6. **Post-Creation:** Run verification checks automatically
7. **Report:** State "Post-creation verification complete"
8. **Fix:** Address any issues immediately
