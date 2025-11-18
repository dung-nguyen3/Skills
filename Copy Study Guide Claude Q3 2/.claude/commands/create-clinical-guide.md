---
description: Create clinical assessment guide for history and physical exam
---

# Create Clinical Assessment Guide

Create a **comprehensive history-taking and physical examination guide** organized by chief complaint and presentation pattern.

## Usage

```
/create-clinical-guide [source_file.txt] [chief_complaint]
```

## What This Does

Creates an interactive HTML guide for clinical assessment:
- **Organized by onset**: Acute, Subacute, Chronic presentations
- **Complete HPI (OLDCAARTS)**: Exact questions to ask patients
- **Essential PMH, FH, SH**: Relevant history elements
- **Focused ROS**: Checkbox format for review of systems
- **Detailed Physical Exam**: Inspection, palpation, specialized tests
- **Differential diagnosis**: By presentation pattern
- **Clinical decision trees**: "If X, Think Y" associations

## Example

```
/create-clinical-guide sources/Lower-Extremity.txt "Leg Pain"
/create-clinical-guide sources/Headache-Workup.txt "Headache"
/create-clinical-guide sources/Chest-Pain.txt "Chest Pain"
```

Output: `[Chief_Complaint]_Clinical_Assessment_Guide.html`

## Template Location

The command uses the template at:
```
Example claude study guides/Physical Assessment/Physical Assessment Instructions.txt
```

## Best For

- **Clinical medicine rotations**
- **Physical diagnosis courses**
- **OSCE preparation**
- **Patient encounter practice**
- **Chief complaint workups**
- **Differential diagnosis by presentation**

## Features

- **Practical questions**: Exact wording to use with patients (in quotes)
- **Complete OLDCAARTS**: Onset, Location, Duration, Character, Aggravating, Alleviating, Associated, Radiation, Timing, Setting
- **Medical History Card format**: Allergies, Medications, Medical Conditions, Surgeries, OB/Gyn, Immunizations
- **Comprehensive ROS**: All systems with checkboxes
- **Focused physical exam**: Vital signs, inspection, palpation, ROM, specialized tests
- **Color-coded by urgency**: Red (acute/emergency), Orange (subacute/urgent), Green (chronic)

## Pre-Creation Checklist

Before creating, Claude will verify:
- ☐ Source file identified
- ☐ Chief complaint specified
- ☐ Template loaded from correct location
- ☐ Source-only policy confirmed
- ☐ Follows Medical History Card format exactly
- ☐ Save location: `[Class]/[Exam]/Claude Study Tools/`

## Post-Creation

After creation, Claude automatically:
- ✓ Verifies all questions in directly usable format (quoted)
- ✓ Confirms all OLDCAARTS elements present
- ✓ Checks PMH/FH/SH/ROS completeness
- ✓ Verifies physical exam specificity (what to inspect/palpate FOR)
- ✓ Reports "Post-creation verification complete"

## Structure

The guide organizes content by:
1. **Primary Location** (if applicable): Hip, Knee, Ankle, etc.
2. **Onset Pattern**: Acute → Subacute → Chronic
3. **Differential Diagnosis**: Top differentials for each pattern
4. **Complete Assessment**: Full HPI, PMH, FH, SH, ROS, focused exam
5. **Decision Support**: "If positive X, do Y" algorithms

## Related Commands

- `/create-lo-guide` - For theoretical medical topics with learning objectives
- `/create-drug-html` - For pharmacology/drug topics
- `/verify-accuracy` - Verify accuracy of created study guide

## Template Customization

To modify the clinical assessment template:
1. Edit: `Example claude study guides/Physical Assessment/Physical Assessment Instructions.txt`
2. Changes apply automatically to next `/create-clinical-guide` use
3. Update `HOW_TO_USE.md` if workflow changes

## Important Notes

- **Follow Medical History Card exactly**: Don't ask for specific medications or specific conditions - ask open-ended ("Do you have any medical conditions?")
- **Be specific in exam**: List exactly what to inspect/palpate and what you're looking for
- **Use lecture files**: Combine with source files for condition-specific details
- **Quote all questions**: Patient-facing questions must be in quotes for direct use
