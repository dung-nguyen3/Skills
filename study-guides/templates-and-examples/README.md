# Study Guide Templates and Examples

This folder contains template files and example study guides.

---

## What's In This Folder

### Template Files

**Python template scripts (.py):**
- `Excel Drugs Chart 11-1 template.py` - Python code for generating Excel Drug Charts
- `LO Word 11-5 template.py` - Python code for generating Word Learning Objective guides
- `Drug_Class_Chart_Templates.py` - Drug classification chart templates
- `Color_Samples.py` - Color scheme utilities

**Text template instructions (.txt):**
- `Excel Drugs Chart 11-1.txt` - Instructions for Excel Drug Chart template
- `Word LO 11-5.txt` - Instructions for Word LO template
- `HTML LO with Master Chart 10-30.txt` - Instructions for HTML LO template
- `Excel Master Chart Only.txt` - Instructions for Master Chart only
- `Autobiography Drug Stories.txt` - Example source material

### Example Study Guides

**Excel examples:**
- `Example 24 HIV Chart excel.xlsx` - Example HIV drug chart
- `24 HIV Chart excel.xlsx` - Another HIV drug chart example
- `Drug_Chart_Example.xlsx` - General drug chart example
- `Drug_Class_Chart_Templates.xlsx` - Drug class chart template example

**Color reference:**
- `Light_Pastel_Color_Samples.xlsx` - Color palette for study guides

---

## How to Use These Templates

### Option 1: Use Slash Commands (Recommended)

Claude Code has built-in commands that automatically use these templates:

```
/excel [source-file]     - Creates Excel Drug Chart
/word [source-file]      - Creates Word LO Guide
/html-drug [source-file] - Creates HTML Drug Chart
/html-LO [source-file]   - Creates HTML LO Guide
```

**The system handles template selection automatically!**

### Option 2: Reference Templates Manually

If you want to understand template structure:

1. **For Excel Drug Charts:**
   - Read `Excel Drugs Chart 11-1.txt` for format details
   - See `Example 24 HIV Chart excel.xlsx` for completed example
   - Reference `Drug_Chart_Example.xlsx` for structure

2. **For Word LO Guides:**
   - Read `Word LO 11-5.txt` for format details
   - Use `LO Word 11-5 template.py` code reference

3. **For HTML Guides:**
   - Read `HTML LO with Master Chart 10-30.txt` for format details

### Option 3: Customize Templates

**If you want to modify templates:**

1. Copy the relevant `.txt` or `.py` file
2. Make your changes
3. Update slash command to reference your custom template
4. See `../user-docs/MAINTENANCE.md` for customization guide

---

## Template Types Overview

### 1. Excel Drug Chart (4-tab format)
**Best for:** Pharmacology, drug classes
**Tabs:** Drug Details, Key Comparisons, Master Chart, High-Yield
**Example:** `Example 24 HIV Chart excel.xlsx`

### 2. HTML Learning Objectives Guide (4-tab format)
**Best for:** Any medical topic with learning objectives
**Tabs:** LO Q&A, Key Comparisons, Master Tables, Summary
**Instructions:** `HTML LO with Master Chart 10-30.txt`

### 3. Word Learning Objectives Guide
**Best for:** Traditional document format
**Template:** `LO Word 11-5 template.py`
**Instructions:** `Word LO 11-5.txt`

### 4. Clinical Assessment Guide (HTML)
**Best for:** History-taking, physical exam by chief complaint
**Format:** OLDCAARTS framework

---

## Example Source Material

`Autobiography Drug Stories.txt` - Example source file showing proper format for study guide creation

**Use this to:**
- See what a good source file looks like
- Test the system with known-good input
- Understand source structure

---

## Color Schemes

`Light_Pastel_Color_Samples.xlsx` - Reference for color palettes used in study guides

**Consistent colors help with:**
- Visual learning
- Quick topic identification
- Professional appearance

---

## Notes

**Temp files (~$*.xlsx):**
- Excel temp files (ignore these)
- Created when Excel files are open
- Safe to delete if not in use

**Python files (.py):**
- Template generation code
- Reference only (slash commands use these automatically)
- Advanced users can modify for custom templates

---

## Getting Help

**For template usage questions:**
- See `../user-docs/HOW_TO_USE.md` - Complete usage guide
- See `../user-docs/MAINTENANCE.md` - Customization guide

**For slash command reference:**
- Type `/` in Claude Code to see available commands
- All commands automatically handle template selection

---

**Last Updated:** 2025-11-19 (Reorganized in Phase 5 completion)
