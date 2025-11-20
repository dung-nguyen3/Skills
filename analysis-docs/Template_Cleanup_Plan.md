# Template Cleanup Implementation Plan

## Status: 4/9 Complete

### ✅ Completed:
1. Excel_Color_Reference.txt - Shared color scheme
2. Excel_Drug_Example.py - Complete 4-tab implementation
3. Excel_Master_Chart_Example.py - Single-sheet examples
4. Word_LO_Example.py - Complete 4-section implementation

### 🔄 Remaining Work:

---

## 5. Excel Drugs Chart Template (1,144 → ~550 lines)

**Remove (440 lines):**
- Lines 8-61: Verification checklist & policies → Reference CLAUDE.md
- Lines 103-138: Analysis workflow & WebSearch → Move to /create-excel slash command
- Lines 165-262: Color schemes → Reference Excel_Color_Reference.txt
- Lines 600-900: Python code examples → Reference Excel_Drug_Example.py

**Keep:**
- Purpose & 4-tab structure
- Data extraction requirements (drug-specific rules)
- Analogy requirements for mechanisms
- Tab-specific content organization
- Row height guidelines

**Add:**
- Reference to CLAUDE.md at top
- Reference to Excel_Color_Reference.txt
- Reference to Excel_Drug_Example.py

---

## 6. Excel Master Chart Template (495 → ~280 lines)

**Remove (215 lines):**
- Lines 46-100: Color scheme → Reference Excel_Color_Reference.txt
- Lines 194-310: Python code → Reference Excel_Master_Chart_Example.py
- Duplicate common mistakes → Keep concise version only

**Keep:**
- Single-sheet structure explanation
- Flexible column approach
- User-defined categories
- Simple examples

**Add:**
- Reference to CLAUDE.md
- Reference to Excel_Color_Reference.txt
- Reference to Excel_Master_Chart_Example.py

---

## 7. HTML LO Template (137 → ~125 lines)

**Remove (12 lines):**
- Lines 3-8: Source-only policy → Reference CLAUDE.md
- Verification checklist → Reference CLAUDE.md

**Keep (ALL other content - it's good):**
- Tab structure explanations
- HTML formatting examples
- Color-coding guidelines
- Clinical decision support focus

**Add:**
- Reference to CLAUDE.md at top

---

## 8. Autobiography Template (252 → ~245 lines)

**Remove (7 lines):**
- Lines 237-238: Source policy → Reference CLAUDE.md

**Keep (ALL creative content):**
- Character development
- Narrative structure
- Creative analogies catalog
- Dialogue examples
- Storytelling elements

**Add:**
- Reference to CLAUDE.md
- "MANDATORY: WebSearch for creative analogies and metaphors"

---

## 9. Update Slash Commands

**Files to update:**
- `/create-excel` - Reference Excel templates + example files
- `/create-word` - Reference Word template + example file
- `/create-lo-guide` - Reference HTML template

**Changes needed:**
```markdown
### Step 2: Load Resources

Read these files in order:
1. Template: `templates-and-examples/[Template].txt`
2. Example Code: `templates-and-examples/Python_Examples/[Example].py`
3. Color Reference (Excel only): `templates-and-examples/Excel_Color_Reference.txt`
4. Source: $ARGUMENTS

Use template for structure/rules, examples for code reference, source for content.
```

---

## Implementation Order:

1. **Excel Drugs Chart** (biggest impact - 52% reduction)
2. **Excel Master Chart** (43% reduction)
3. **HTML LO** (9% reduction - quick)
4. **Autobiography** (3% reduction - quick)
5. **Update all slash commands** (add example file references)

---

## Expected Final Results:

**Before:**
- Total template lines: 2,723
- With redundancy and long Python code

**After:**
- Total template lines: ~1,650 (39% reduction)
- Clean references to shared files
- All unique content preserved
- Easier to maintain

**New reference files created:**
- Excel_Color_Reference.txt (1 file for 2 templates)
- Python_Examples/ folder (3 complete working examples)

---

## Next Steps:

**Option A: Continue automatically**
- I create all 4 cleaned templates
- Update all slash commands
- Commit everything

**Option B: Review first**
- You review this plan
- I proceed with approved changes
- More control over final result

**Which would you prefer?**
