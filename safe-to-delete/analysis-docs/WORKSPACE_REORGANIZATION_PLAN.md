# Skills Repository - VS Code Workspace Reorganization Plan

## Current Issues
- Root directory cluttered with analysis markdown files
- Folder names not clear (e.g., "Copy Study Guide Claude Q3 2")
- No VS Code workspace file for multi-folder workflow
- Scripts scattered in root directory

## Proposed Structure

```
Skills/
├── .vscode/
│   └── skills.code-workspace          # Multi-root workspace configuration
│
├── CLAUDE.md                           # Global settings for all projects
├── README.md                           # Repository overview
├── .gitignore
│
├── infrastructure-examples/            # Renamed from claude-infrastructure-showcase
│   ├── .claude/
│   │   ├── commands/                   # Example slash commands
│   │   ├── skills/                     # Example skills
│   │   └── hooks/                      # Example hooks
│   ├── agents/                         # Example agents
│   └── README.md                       # How to use these examples
│
├── study-guides/                       # Renamed from "Copy Study Guide Claude Q3 2"
│   ├── .claude/
│   │   └── commands/                   # /create-excel, /create-word, etc.
│   ├── CLAUDE.md                       # Study guide specific settings
│   ├── templates-and-examples/
│   │   ├── *_REVISED.txt               # Cleaned templates
│   │   ├── Python_Examples/            # Reference implementation code
│   │   └── Excel_Color_Reference.txt
│   ├── source-files/                   # Lecture notes and source material
│   ├── generated-guides/               # Output location for created study guides
│   └── README.md                       # How to use study guide system
│
├── analysis-docs/                      # All analysis markdown files
│   ├── Template_Analysis_All_Templates.md
│   ├── Word_LO_Template_Analysis.md
│   ├── CLAUDE_INFRASTRUCTURE_ANALYSIS.md
│   ├── INFRASTRUCTURE_ANALYSIS_INDEX.md
│   ├── PHASE_4_ANALYSIS_AND_PLAN.md
│   ├── QUICK_REFERENCE_GUIDE.md
│   ├── README_ANALYSIS.md
│   ├── TEMPLATE_TYPES.md
│   ├── GIT_WORKFLOW.md
│   └── Template_Cleanup_Plan.md
│
└── scripts/                            # Standalone utility scripts
    └── create_respiration_study_guide.py
```

## VS Code Workspace Configuration

Create `Skills.code-workspace` with:

```json
{
  "folders": [
    {
      "name": "📁 Skills Repository (Root)",
      "path": "."
    },
    {
      "name": "🏗️ Infrastructure Examples",
      "path": "infrastructure-examples"
    },
    {
      "name": "📚 Study Guides",
      "path": "study-guides"
    },
    {
      "name": "📊 Analysis Documents",
      "path": "analysis-docs"
    }
  ],
  "settings": {
    "files.exclude": {
      "**/.git": true,
      "**/.DS_Store": true,
      "**/node_modules": true,
      "**/__pycache__": true,
      "**/*.pyc": true
    },
    "editor.formatOnSave": true,
    "editor.rulers": [80, 120],
    "python.defaultInterpreterPath": "/usr/bin/python3"
  }
}
```

## Benefits

1. **Clear Organization**: Each folder has a specific purpose
2. **Multi-Root Workspace**: VS Code treats each folder as a separate project
3. **Clean Root**: Analysis docs and scripts organized
4. **Better Names**: "study-guides" instead of "Copy Study Guide Claude Q3 2"
5. **Claude Code Ready**: Proper .claude/ structure in each project
6. **Scalable**: Easy to add new projects to workspace

## Implementation Steps

1. Create `.vscode/` directory and workspace file
2. Move analysis markdown files to `analysis-docs/`
3. Rename `claude-infrastructure-showcase` → `infrastructure-examples`
4. Rename `Copy Study Guide Claude Q3 2` → `study-guides`
5. Move standalone scripts to `scripts/`
6. Create README.md in each major folder
7. Update all path references in CLAUDE.md files
8. Update slash commands with new paths
9. Test workspace by opening in VS Code
10. Commit and push changes

## Migration Commands

```bash
# Create new directories
mkdir -p .vscode analysis-docs scripts

# Move analysis docs
mv *_ANALYSIS*.md analysis-docs/
mv TEMPLATE*.md analysis-docs/
mv GIT_WORKFLOW.md analysis-docs/
mv QUICK_REFERENCE_GUIDE.md analysis-docs/
mv README_ANALYSIS.md analysis-docs/
mv Template_Cleanup_Plan.md analysis-docs/
mv Word_LO_Template_Analysis.md analysis-docs/

# Move scripts
mv create_respiration_study_guide.py scripts/

# Rename directories
mv "claude-infrastructure-showcase" infrastructure-examples
mv "Copy Study Guide Claude Q3 2" study-guides

# Create workspace file
# (Will be created programmatically)
```

## Files to Update After Reorganization

1. `/CLAUDE.md` - Update references to folder names
2. `/study-guides/CLAUDE.md` - Update any path references
3. `/study-guides/.claude/commands/*.md` - Update template paths if needed
4. Any scripts that reference old folder names

## Testing Checklist

- [ ] Open workspace in VS Code
- [ ] Verify all folders appear in sidebar
- [ ] Test slash commands work with new paths
- [ ] Verify CLAUDE.md is read correctly
- [ ] Run a test study guide creation
- [ ] Ensure git still works correctly
- [ ] Check that relative paths still resolve
