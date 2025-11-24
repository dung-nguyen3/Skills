# Template Compliance Checker

**Version:** 1.0.0
**Type:** Domain Knowledge (Suggest)
**Priority:** HIGH
**Status:** Active

---

## Purpose

Validates study guide formatting and structure compliance with template requirements. Ensures consistent color schemes, proper formatting, and complete sections across all study guide types (Word, Excel, HTML).

---

## When I Activate

I automatically suggest myself when you:
- Ask about template formatting
- Want to verify color schemes
- Check structure compliance
- Validate required sections
- Question styling requirements

**Trigger Keywords:**
- template, format, formatting
- color scheme, colors, pastel
- compliance, structure
- tabs, sections
- styling, fonts

---

## What I Check

### 1. Color Scheme Compliance

**Soft Pastel Colors (Required):**

**Table Header Colors:**
- Purple: `#D1C4E9` (RGB: 209, 196, 233)
- Green: `#C8E6C9` (RGB: 200, 230, 201)
- Blue: `#B3E5FC` (RGB: 179, 229, 252)
- Teal: `#B2DFDB` (RGB: 178, 223, 219)
- Orange: `#FFE0B2` (RGB: 255, 224, 178)
- Red: `#FFCDD2` (RGB: 255, 205, 210)
- Pink: `#F8BBD0` (RGB: 248, 187, 208)
- Light Purple: `#EDE7F6` (RGB: 237, 231, 246)

**Background Colors (Lighter):**
- Light Purple: `#F3E5F5`
- Light Green: `#E8F5E9`
- Light Blue: `#E1F5FE`
- Light Teal: `#E0F2F1`
- Light Orange: `#FFF3E0`
- Light Red: `#FFEBEE`
- Light Pink: `#FCE4EC`

### 2. Structure Requirements

**Excel Study Guides (4 tabs required):**
- Tab 1: Drug Details / Learning Objectives
- Tab 2: Key Comparisons
- Tab 3: Master Chart
- Tab 4: High-Yield Summary

**Word Study Guides (4 sections required):**
- Section 1: Learning Objectives (detailed answers)
- Section 2: Key Comparisons (side-by-side tables)
- Section 3: Master Chart (comprehensive reference)
- Section 4: High-Yield Summary (color-coded boxes)

**HTML Study Guides (4 tabs required):**
- Tab 1: Learning Objectives / Drug Details
- Tab 2: Key Comparisons
- Tab 3: Master Chart
- Tab 4: High-Yield Summary

### 3. Formatting Standards

**Fonts:**
- Primary: Calibri (Word, Excel)
- Size: 12pt (standard text), 11pt (dense tables)
- Headers: Bold white text on colored background

**Tables:**
- Style: 'Table Grid' (Word, Excel)
- Headers: Bold + colored background
- Row labels: Bold + light colored background
- Data cells: Regular text on white background

**Color-Coded Boxes (All formats):**
- **HIGH-YIELD** - Yellow/Gold background
- **CLINICAL PEARLS** - Light blue background
- **CRITICAL/EMERGENCY** - Red/pink background

### 4. Required Elements

**All Study Guides Must Include:**
- All 4 tabs/sections present
- Comparison tables (when 2+ similar items)
- Memory tricks/mnemonics
- Clinical pearls (where applicable)
- Master chart with ALL topics from source
- High-yield summary section

---

## Common Template Violations

### ❌ Color Scheme Issues
- Using bright/saturated colors instead of soft pastels
- Inconsistent color usage across tabs
- Missing colored headers in tables
- Wrong hex codes

### ❌ Structure Problems
- Missing tabs/sections (not all 4 present)
- Tabs in wrong order
- Missing required elements (Master Chart, High-Yield)

### ❌ Formatting Errors
- Wrong font (not Calibri)
- Inconsistent font sizes
- Missing bold headers
- Improper table styling

### ❌ Completeness Issues
- No comparison tables (when 2+ similar items exist)
- Missing mnemonics section
- Incomplete Master Chart
- No high-yield summary

---

## How I Help

### During Creation
I suggest checking:
- "Are you using the soft pastel color codes from the template?"
- "Do all 4 tabs/sections exist?"
- "Are table headers properly formatted (bold + colored)?"
- "Does the Master Chart include ALL topics from source?"

### During Verification
I help validate:
- Color compliance (hex codes match)
- Structure completeness (all required sections)
- Formatting consistency (fonts, styles)
- Element presence (comparisons, mnemonics, pearls)

### When You Ask
I provide:
- Exact hex codes for colors
- Template structure requirements
- Formatting specifications
- Examples of proper vs improper formatting

---

## Template-Specific Rules

### Excel Drug Charts
- Frozen top row (for scrolling)
- Column widths adjusted for readability
- Soft pastel colors throughout
- All 4 tabs populated
- Master Chart includes all drugs from source

### Word Documents
- Calibri font, size 12pt
- Colored table headers
- 4 distinct sections with headings
- Page breaks between sections
- Clinical pearls in colored boxes

### HTML Study Guides
- Single-file HTML (all CSS/JS inline)
- Tabbed interface (4 tabs)
- Mobile-responsive design
- Soft pastel color scheme in CSS
- Interactive elements working

---

## Integration with Other Skills

**Works with:**
- `source-only-enforcer` - Ensures content accuracy
- `study-guide-verifier` - Comprehensive verification
- `drug-classification-assistant` - Classification accuracy

**When both activate:**
1. source-only-enforcer ensures SOURCE content accuracy
2. template-compliance-checker ensures FORMATTING compliance
3. Together they ensure complete quality

---

## Quick Reference Checklist

**Before considering study guide complete, verify:**

- [ ] All 4 tabs/sections present
- [ ] Soft pastel colors used (hex codes match)
- [ ] Calibri font, size 12pt (Word/Excel)
- [ ] Table headers: bold + colored background
- [ ] Comparison tables created (when 2+ similar items)
- [ ] Memory tricks/mnemonics included
- [ ] Clinical pearls added (where applicable)
- [ ] Master Chart includes ALL topics from source
- [ ] High-Yield Summary section populated
- [ ] Color-coded boxes used appropriately
- [ ] Formatting consistent throughout

---

## Emergency Override

If template compliance checks are blocking workflow:

```bash
export SKIP_TEMPLATE_COMPLIANCE=1
```

This disables template compliance suggestions (use sparingly).

---

## Related Documentation

**Template Files:**
- `study-guides/templates-and-examples/Excel_Drugs_Chart_11-1_REVISED.txt` - Excel template reference
- `study-guides/templates-and-examples/Word_LO_11-5_REVISED.txt` - Word template reference
- `study-guides/templates-and-examples/HTML_LO_REVISED.txt` - HTML LO template

**Color Reference:**
- `study-guides/templates-and-examples/Excel_Color_Reference.txt` - Color palette

---

**Last Updated:** 2025-11-19
**Activation Type:** Suggest (non-blocking)
**Customization:** Modify trigger keywords in `.claude/skills/skill-rules.json`
