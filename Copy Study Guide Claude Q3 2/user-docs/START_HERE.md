# START HERE - Quick Guide

**New to the medical study guide system? This is your starting point.**

---

## What This System Does

Creates comprehensive medical study guides from your lecture notes with:
- ✅ **Source-only enforcement** - Prevents AI hallucinations
- ✅ **Multiple formats** - Excel, Word, HTML
- ✅ **Automatic verification** - Quality checks built-in
- ✅ **Time savings** - Minutes instead of hours

---

## Quick Start (3 Steps)

### Step 1: Prepare Your Source File

Create a text file (.txt) with your lecture notes:
```
HIV_Lecture_Notes.txt
```

**Put it in the same directory as your study guide will go.**

### Step 2: Create Study Guide

Use a slash command based on your content type:

**For drug information (pharmacology):**
```
/create-excel HIV_Lecture_Notes.txt
```
→ Creates 4-tab Excel drug chart

**For learning objectives (any medical topic):**
```
/create-lo-guide HIV_Lecture_Notes.txt
```
→ Creates interactive HTML guide

**For clinical scenarios:**
```
/create-clinical-guide Chest_Pain_History.txt
```
→ Creates history/physical exam guide

### Step 3: Verify Accuracy

After creation, run verification:
```
/verify-accuracy [study-guide-file] [source-file]
```

**Done!** Your study guide is ready.

---

## What Format Should I Use?

| Content Type | Recommended Format | Command |
|--------------|-------------------|---------|
| Drug classes, pharmacology | Excel Drug Chart | `/create-excel` |
| Learning objectives (any topic) | HTML LO Guide | `/create-lo-guide` |
| History-taking, physical exam | Clinical Guide | `/create-clinical-guide` |
| General notes | Word Document | `/create-word` |

---

## Next Steps

**Once you've created your first study guide:**

1. **Read the full guide:** [HOW_TO_USE.md](HOW_TO_USE.md)
   - Learn all features
   - Understand verification process
   - Advanced techniques

2. **If you need to customize:** [MAINTENANCE.md](MAINTENANCE.md)
   - Template customization
   - Troubleshooting
   - System configuration

3. **See template examples:** [../templates-and-examples/](../templates-and-examples/)
   - Example study guides
   - Template structure reference

---

## Common Questions

**Q: What if I don't have a source file?**
A: You MUST have source material. The system prevents AI hallucinations by requiring everything to come from your source file.

**Q: Can I add extra information not in the source?**
A: Only researched mnemonics (marked with *). Everything else must be from source.

**Q: What if the system blocks me?**
A: It's checking for source file and verification. Follow the prompts. Emergency override: `export SKIP_STUDY_GUIDE_VERIFICATION=1`

**Q: How do I know if my study guide is accurate?**
A: Use `/verify-accuracy` - the study-guide-analyzer agent performs comprehensive 6-step verification.

---

## Support

**Stuck? Check these in order:**

1. ✅ **This file** - Quick start covered?
2. ✅ **[HOW_TO_USE.md](HOW_TO_USE.md)** - Detailed usage guide
3. ✅ **[MAINTENANCE.md](MAINTENANCE.md)** - Troubleshooting section

---

## System Requirements

**What you need:**
- Claude Code (web or VS Code extension)
- Source file in text format (.txt, .md, or .pdf)
- Basic familiarity with slash commands

**That's it!** The system handles everything else automatically.

---

**Ready to create your first study guide?**

1. Prepare your source file
2. Run `/create-excel [source-file]` (or your preferred format)
3. Follow the prompts
4. Verify with `/verify-accuracy`

**Good luck with your studies!** 📚
