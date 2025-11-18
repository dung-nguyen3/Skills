# Study Guide Template Types

This repository supports **4 different template types** for creating medical education study guides across multiple specialties.

## Template Type 1: Drug Chart HTML
**Format:** Interactive HTML
**Use for:** Pharmacology - drug reference charts
**Example:** `Example claude study guides/Drug Chart HTML/`

### Features:
- Self-contained single HTML file (offline-ready)
- 3 main tabs: Drug Classes & Comparisons, Master Chart, Quick Reference
- Sortable drug tables
- Color-coded badges (routes, contraindications, drug choice)
- Highlight boxes for mechanisms, warnings
- Mnemonics for drug lists

### Best for:
- Antiviral drugs, HIV drugs, antibiotics, antifungals
- Comparing drugs within classes
- Quick reference during clinical rotations

### Template location:
`Example claude study guides/Drug Chart HTML/Drug Chart HTML.txt`

---

## Template Type 2: Excel Drug Chart (4-Tab Format)
**Format:** Excel workbook
**Use for:** Pharmacology - comprehensive drug analysis
**Example:** `Example claude study guides/Excel Drug Chart/`

### Features:
- **Tab 1:** Drug Details - Comparison tables by drug class
- **Tab 2:** Key Comparisons - Side-by-side comparisons
- **Tab 3:** Master Chart - All drugs in one sortable table
- **Tab 4:** High-Yield & Pearls - Clinical pearls and mnemonics
- Soft pastel color scheme
- Mechanism analogies
- Researched mnemonics

### Best for:
- Comprehensive drug studying
- Exam preparation
- Print-friendly reference sheets

### Template location:
`Example claude study guides/Excel Drug Chart/Excel Drugs Chart 11-1.txt`

---

## Template Type 3: HTML Learning Objectives (Master Comparison)
**Format:** HTML with multiple tabs
**Use for:** ANY medical topic (pathophysiology, diseases, procedures)
**Example:** `Example claude study guides/HTML LO/`

### Features:
- **Tab 1:** Learning Objectives - Q&A format answering each LO
- **Tab 2:** Key Comparisons - Focused 2-3 way comparisons
- **Tab 3:** Master Comparison Tables - Complete differential diagnosis
- **Tab 4:** Summary - High-yield pearls, mnemonics, "If X Think Y"
- Works for diseases, procedures, physiology, clinical topics

### Best for:
- Cardiovascular pathophysiology
- Hematology conditions
- Immunology
- Rheumatology
- Respiratory physiology
- Any lecture with learning objectives

### Template location:
`Example claude study guides/HTML LO/HTML LO with Master Chart 10-30.txt`

---

## Template Type 4: Clinical Assessment Guide (Physical Exam)
**Format:** Interactive HTML
**Use for:** Clinical skills - history and physical examination
**Example:** `Example claude study guides/Physical Assessment/`

### Features:
- Organized by chief complaint (e.g., "Leg Pain")
- 3 main tabs by onset: Acute, Subacute, Chronic
- Complete HPI (OLDCAARTS) with exact questions to ask
- PMH, FH, SH, ROS checklists
- Detailed focused physical exam by presentation
- Differential diagnosis by pattern
- Clinical decision trees

### Best for:
- Clinical medicine rotations
- Physical diagnosis courses
- OSCE preparation
- Patient encounter practice
- Chief complaint workups

### Template location:
`Example claude study guides/Physical Assessment/Physical Assessment Instructions.txt`

---

## Template Selection Guide

### Choose Template Type based on content:

| Content Type | Recommended Template | Output Format |
|--------------|---------------------|---------------|
| Pharmacology (drugs) | Drug Chart HTML OR Excel Drug Chart | HTML or Excel |
| Disease/pathophysiology with LOs | HTML Learning Objectives | HTML |
| Clinical skills/physical exam | Clinical Assessment Guide | HTML |
| Procedures with steps | HTML Learning Objectives | HTML |
| Physiology concepts | HTML Learning Objectives | HTML |

### Multiple templates for same content:
- **Pharmacology:** Use BOTH Drug Chart HTML (quick reference) AND Excel (comprehensive)
- **Clinical topics:** Use HTML LO for theory + Clinical Assessment for practical skills

---

## Template Characteristics Summary

| Feature | Drug Chart HTML | Excel Drug Chart | HTML LO | Clinical Assessment |
|---------|----------------|------------------|---------|---------------------|
| Subject focus | Drugs only | Drugs only | Any medical topic | Clinical skills |
| Interactivity | High | Medium | High | High |
| Offline use | ✅ | ✅ | ✅ | ✅ |
| Print-friendly | ✅ | ✅ | ✅ | ⚠️ |
| Mobile-friendly | ✅ | ❌ | ✅ | ✅ |
| Mnemonics | ✅ | ✅ | ✅ | ⚠️ |
| Comparison tables | ✅ | ✅ | ✅ | ✅ |
| Clinical decision support | ⚠️ | ⚠️ | ⚠️ | ✅ |
| Practical questions | ❌ | ❌ | ❌ | ✅ |

---

## Usage Notes

1. **All templates require source files** - Never add external knowledge
2. **All templates support verification** - Use `/verify-accuracy` after creation
3. **Templates are content-agnostic within their domain** - HTML LO works for ANY medical topic with learning objectives
4. **Combine templates as needed** - One lecture can generate multiple study guide formats

---

## Future Template Types (Not Yet Implemented)

- Annotations/Summary (Word) - Brief annotations on source material
- Quiz Generator (HTML) - Interactive practice questions
- Flashcards (HTML) - Spaced repetition cards
- Case Studies (Word/HTML) - Clinical scenario practice
