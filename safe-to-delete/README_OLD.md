# Skills Repository - Welcome!

> **This file auto-opens when you launch the workspace in VS Code**

---

## Get Started Immediately

### New User? Start Here:
**[QUICK_START.md](QUICK_START.md)** - Interactive guide with clickable table of contents

### What's in This Repository?

```
Skills/
├── 📚 study-guides/          → Create pharmacy study guides
├── 🏗️  infrastructure-examples/ → Claude Code skills, hooks, agents
├── 📊 analysis-docs/          → Analysis and planning documents
└── 🔧 scripts/                → Utility scripts
```

---

## Quick Navigation

### Study Guide Creation
- **[Slash Commands Reference](SLASH_COMMANDS_REFERENCE.md)** - All 9 commands explained
- **[Quick Start Guide](QUICK_START.md)** - 3-step guide to create study guides
- **[Full How-To Guide](study-guides/user-docs/HOW_TO_USE.md)** - Complete documentation

### Copy & Paste Commands

```bash
# Create Excel drug chart
/create-excel "Pharmacology/Exam 3/Extract/HIV Drugs.txt"

# Create Word study guide
/create-word "Pharmacology/Exam 3/Extract/Lecture 42.txt"

# Create HTML learning objectives guide
/create-lo-guide "Clinical Medicine/Exam 2/Extract/Cardiovascular.txt"

# Verify accuracy before exam
/verify-accuracy "Study Tools/Guide.xlsx" "Extract/Source.txt"
```

---

## Need Help?

| Question | Answer |
|----------|--------|
| How do I create a study guide? | [QUICK_START.md](QUICK_START.md) - See "Create Study Guide (3 Steps)" |
| Which command should I use? | [QUICK_START.md](QUICK_START.md) - See "Study Guide Decision Tree" |
| What are skills/hooks/agents? | [QUICK_START.md](QUICK_START.md) - See sections on each |
| How do I verify a study guide? | [QUICK_START.md](QUICK_START.md) - See "Verify Study Guide (2 Steps)" |
| What keyboard shortcuts work? | [QUICK_START.md](QUICK_START.md) - See "Keyboard Shortcuts" |

---

## Visual Guide to Repository Structure

### For Study Guide Creation

1. **Add source files to:**
   ```
   study-guides/[Class]/[Exam]/Extract/
   ```

2. **Use slash command:**
   ```bash
   /create-excel "study-guides/[Class]/[Exam]/Extract/[File].txt"
   ```

3. **Output saves to:**
   ```
   study-guides/[Class]/[Exam]/Claude Study Tools/
   ```

### For Understanding Infrastructure

1. **Read examples:**
   ```
   infrastructure-examples/.claude/
   ├── commands/     → Slash command examples
   ├── skills/       → Auto-activation examples
   ├── hooks/        → Background enforcement
   └── agents/       → Complex task automation
   ```

2. **Read integration guide:**
   ```
   infrastructure-examples/CLAUDE_INTEGRATION_GUIDE.md
   ```

---

## Command Palette Quick Actions (Mac)

Press `Cmd + Shift + P` and type:

- **"Markdown: Open Preview"** - Preview this README
- **"File: Open File"** - Quick open QUICK_START.md
- **"Snippets: Insert Snippet"** - Insert slash command
- **"Preferences: Open Workspace Settings"** - Configure workspace

---

## Keyboard Shortcuts (Mac)

| Action | Shortcut |
|--------|----------|
| Command Palette | `Cmd + Shift + P` |
| Quick File Open | `Cmd + P` (then type "QUICK") |
| Search in Files | `Cmd + Shift + F` |
| Open Terminal | `Ctrl + ~` |
| Markdown Preview | `Cmd + Shift + V` |

---

## Repository Files Index

### Essential Documentation
- **[QUICK_START.md](QUICK_START.md)** - Start here! Interactive guide
- **[SLASH_COMMANDS_REFERENCE.md](SLASH_COMMANDS_REFERENCE.md)** - All commands detailed
- **[WORKSPACE_SETUP.md](WORKSPACE_SETUP.md)** - Workspace configuration guide
- **[CLAUDE.md](CLAUDE.md)** - Global repository settings

### Study Guides
- **[study-guides/README.md](study-guides/README.md)** - Study guide system overview
- **[study-guides/user-docs/HOW_TO_USE.md](study-guides/user-docs/HOW_TO_USE.md)** - Complete usage guide
- **[study-guides/user-docs/START_HERE.md](study-guides/user-docs/START_HERE.md)** - Quick start

### Infrastructure
- **[infrastructure-examples/README.md](infrastructure-examples/README.md)** - Infrastructure overview
- **[infrastructure-examples/CLAUDE_INTEGRATION_GUIDE.md](infrastructure-examples/CLAUDE_INTEGRATION_GUIDE.md)** - Integration guide
- **[infrastructure-examples/.claude/skills/README.md](infrastructure-examples/.claude/skills/README.md)** - Skills documentation
- **[infrastructure-examples/.claude/hooks/README.md](infrastructure-examples/.claude/hooks/README.md)** - Hooks documentation
- **[infrastructure-examples/.claude/agents/README.md](infrastructure-examples/.claude/agents/README.md)** - Agents documentation

### Analysis
- **[analysis-docs/INFRASTRUCTURE_TOKEN_ANALYSIS.md](analysis-docs/INFRASTRUCTURE_TOKEN_ANALYSIS.md)** - Token usage analysis
- **[analysis-docs/Template_Analysis_All_Templates.md](analysis-docs/Template_Analysis_All_Templates.md)** - Template improvements
- **[analysis-docs/WORKSPACE_REORGANIZATION_PLAN.md](analysis-docs/WORKSPACE_REORGANIZATION_PLAN.md)** - Reorganization details

---

## 30-Second Quick Start

1. **Open this workspace in VS Code:**
   ```bash
   code .vscode/Skills.code-workspace
   ```

2. **Read the interactive guide:**
   [QUICK_START.md](QUICK_START.md) (click to open)

3. **Copy a command and try it:**
   ```bash
   /create-excel "your/source/file.txt"
   ```

That's it! The infrastructure handles everything else automatically.

---

## What Happens Automatically?

When you use a slash command:

✅ Template loads automatically
✅ Verification checklist runs
✅ Source file read completely
✅ Mnemonics researched via web
✅ Study guide created
✅ Post-verification runs
✅ File saved to correct location

**You just type the command!** Everything else is automated.

---

## Tips for New Users

1. **Start with QUICK_START.md** - Has clickable table of contents
2. **Use slash commands** - Don't manually paste templates
3. **Let skills auto-activate** - They work in the background
4. **Press Cmd+P** and type "QUICK" to quickly open QUICK_START.md
5. **Bookmark these files** in VS Code for quick access

---

## Repository Statistics

- **9 slash commands** (6 study guide + 3 infrastructure)
- **5 skills** (auto-activation system)
- **3 hooks** (quality enforcement)
- **2 agents** (complex analysis)
- **4 workspace folders** (multi-root setup)
- **5 revised templates** (39% smaller than originals)

---

**Ready to start?** → [Open QUICK_START.md](QUICK_START.md)

**Need detailed help?** → [Open HOW_TO_USE.md](study-guides/user-docs/HOW_TO_USE.md)

**Want to understand infrastructure?** → [Open CLAUDE_INTEGRATION_GUIDE.md](infrastructure-examples/CLAUDE_INTEGRATION_GUIDE.md)

---

**Last Updated:** 2025-11-19
