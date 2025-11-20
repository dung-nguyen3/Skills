# Claude Code Infrastructure - Quick Reference Guide

**Use this guide to quickly find what you need from the showcase**

---

## 1. QUICK FACTS

| Component | Count | Type | Customization |
|-----------|-------|------|---------------|
| **Skills** | 5 | Modular | ⚠️ Some (paths) |
| **Hooks** | 6 | Automation | ✅ Essential: None; Optional: Heavy |
| **Agents** | 10 | Standalone | ✅ Minimal |
| **Commands** | 3 | Shortcuts | ⚠️ Paths |
| **Resource Files** | 40+ | Documentation | ✅ None |

**Setup Time:** 15-45 minutes
**Production Use:** 6 months tested
**Tech Stack:** Multi-framework support

---

## 2. WHAT GOES IN YOUR .CLAUDE DIRECTORY

```
.claude/
├── skills/
│   ├── [skill-name]/SKILL.md + resources/
│   ├── skill-rules.json (CRITICAL)
│   └── README.md
├── hooks/
│   ├── skill-activation-prompt.sh (ESSENTIAL)
│   ├── post-tool-use-tracker.sh (ESSENTIAL)
│   ├── [optional hooks]
│   └── package.json
├── agents/
│   ├── [agent-name].md
│   └── README.md
├── commands/
│   └── [command-name].md
└── settings.json (Hook registration)
```

---

## 3. THE TWO ESSENTIAL HOOKS (ALWAYS COPY)

### skill-activation-prompt.sh + .ts
**Purpose:** Make skills auto-activate
**Customization:** ✅ None needed
**File:** `.claude/hooks/`
**Config:** Register in settings.json

### post-tool-use-tracker.sh
**Purpose:** Track file changes across sessions
**Customization:** ✅ Auto-detects structure
**File:** `.claude/hooks/`
**Config:** Register in settings.json

---

## 4. THE 5 SKILLS AT A GLANCE

### skill-developer (Meta-Skill)
- **When:** Creating skills or modifying triggers
- **Resources:** 7 files covering skill creation from basics to advanced
- **Customization:** ✅ None - copy as-is
- **For:** Everyone building skills

### backend-dev-guidelines
- **When:** Working on Node.js/Express APIs
- **Tech:** Express, Prisma, Sentry, Zod
- **Resources:** 12 files (architecture, routes, services, database, etc.)
- **Customization:** ⚠️ Update pathPatterns
- **For:** Backend developers

### frontend-dev-guidelines
- **When:** Working on React components
- **Tech:** React 18+, MUI v7, TanStack Query/Router
- **Enforcement:** BLOCK (guardrail)
- **Resources:** 11 files (components, styling, performance, etc.)
- **Customization:** ⚠️ Update pathPatterns
- **For:** Frontend developers

### route-tester
- **When:** Testing authenticated API routes
- **Tech:** JWT cookie authentication (framework agnostic)
- **Resources:** 1 focused file
- **Customization:** ⚠️ Service URLs
- **For:** API testing and debugging

### error-tracking
- **When:** Setting up error monitoring
- **Tech:** Sentry v8
- **Resources:** 1 focused file
- **Customization:** ⚠️ Update pathPatterns
- **For:** All projects (backend + frontend)

---

## 5. SKILL-RULES.JSON STRUCTURE

**File:** `.claude/skills/skill-rules.json`

```json
{
  "version": "1.0",
  "skills": {
    "skill-name": {
      "type": "domain",              // or "guardrail"
      "enforcement": "suggest",      // or "block"
      "priority": "high",            // or "medium", "low"
      "promptTriggers": {
        "keywords": ["word1", "word2"],
        "intentPatterns": ["regex.*pattern"]
      },
      "fileTriggers": {
        "pathPatterns": ["path/**/*.ts"],
        "contentPatterns": ["pattern"]
      }
    }
  }
}
```

**Critical Section:**
```json
"fileTriggers": {
  "pathPatterns": [
    "YOUR_PROJECT_PATH/**/*.ts"  // ← CUSTOMIZE THIS
  ]
}
```

---

## 6. SETTINGS.JSON ESSENTIAL SECTIONS

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [{
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/skill-activation-prompt.sh"
        }]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [{
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/post-tool-use-tracker.sh"
        }]
      }
    ]
  }
}
```

---

## 7. THE 10 AGENTS QUICK LOOKUP

**General Purpose Agents:**
- `code-architecture-reviewer` - Review code quality
- `code-refactor-master` - Plan refactoring
- `documentation-architect` - Generate docs
- `plan-reviewer` - Review plans
- `refactor-planner` - Create refactoring plans
- `web-research-specialist` - Research online

**Frontend Specific:**
- `frontend-error-fixer` - Debug browser errors

**Backend/Auth Specific:**
- `auth-route-tester` - Test auth routes
- `auth-route-debugger` - Debug auth issues
- `auto-error-resolver` - Fix TypeScript errors

**How to Use:**
"Use the [agent-name] agent to [task]"

---

## 8. THE 3 SLASH COMMANDS

### /dev-docs [task description]
Creates three files for complex tasks:
- `[task]-plan.md` - Strategic plan
- `[task]-context.md` - Current state
- `[task]-tasks.md` - Checklist

### /dev-docs-update
Updates existing dev docs before context reset

### /route-research-for-testing [description]
Research API route patterns for testing

---

## 9. CRITICAL FILE CUSTOMIZATION POINTS

### skill-rules.json
```json
"pathPatterns": [
  "src/**/*.ts",              // ← CUSTOMIZE
  "backend/**/*.ts",          // ← CUSTOMIZE
  "services/*/src/**/*.ts"    // ← CUSTOMIZE
]
```

### settings.json
```json
"command": "$CLAUDE_PROJECT_DIR/.claude/hooks/skill-activation-prompt.sh"
                               ↑
                      Keep this variable
```

---

## 10. INTEGRATION CHECKLIST (15 MINUTES)

- [ ] Create `.claude/` directory
- [ ] Copy `skill-activation-prompt.sh` + `.ts`
- [ ] Copy `post-tool-use-tracker.sh`
- [ ] Create `skill-rules.json` with YOUR pathPatterns
- [ ] Create `settings.json` with hook registration
- [ ] `chmod +x .claude/hooks/*.sh`
- [ ] Copy at least 1 skill directory
- [ ] Test: Edit relevant file, skill should activate
- [ ] Copy relevant agents to `.claude/agents/`

---

## 11. COMMON CUSTOMIZATION PATTERNS

### Single Service Project
```json
{
  "pathPatterns": [
    "src/**/*.ts",
    "backend/**/*.ts"
  ]
}
```

### Monorepo with Packages
```json
{
  "pathPatterns": [
    "packages/api/src/**/*.ts",
    "packages/web/src/**/*.tsx",
    "apps/*/src/**/*.ts"
  ]
}
```

### Multi-Service Monorepo
```json
{
  "pathPatterns": [
    "services/*/src/**/*.ts",
    "backend/*/src/**/*.ts"
  ]
}
```

---

## 12. NAMING CONVENTIONS QUICK REFERENCE

**Backend:**
- Controllers: `PascalCase` (UserController.ts)
- Services: `camelCase` (userService.ts)
- Routes: `camelCase + Routes` (userRoutes.ts)
- Repositories: `PascalCase + Repository` (UserRepository.ts)

**Frontend:**
- Components: `PascalCase` (UserCard.tsx)
- Hooks: `camelCase + Hook` (useUserData.ts)
- Utils: `camelCase` (formatDate.ts)

**Infrastructure:**
- Skills: `kebab-case` (backend-dev-guidelines)
- Hooks: `kebab-case` (skill-activation-prompt.sh)
- Agents: `kebab-case` (code-architecture-reviewer.md)
- Config: Specific (skill-rules.json, settings.json)

---

## 13. TRIGGER PATTERNS COPY-PASTE LIBRARY

### Backend Keywords
```
"keywords": [
  "backend", "API", "controller", "service", "repository",
  "route", "endpoint", "middleware", "Prisma", "database"
]
```

### Backend Intent Patterns
```
"intentPatterns": [
  "(create|add|implement).*?(route|endpoint|API)",
  "(fix|debug).*?(error|exception|backend)"
]
```

### Frontend Keywords
```
"keywords": [
  "component", "React", "UI", "MUI", "styling",
  "form", "modal", "frontend"
]
```

### Frontend Intent Patterns
```
"intentPatterns": [
  "(create|add|build).*?(component|UI|page)",
  "(style|design).*?(component|UI)"
]
```

---

## 14. DEV DOCS PATTERN (For Complex Tasks)

### When to Use
- Multi-day tasks
- Complex features
- Tasks spanning multiple sessions

### Structure
```
dev/active/task-name/
├── task-name-plan.md       (Strategic: phases + tasks)
├── task-name-context.md    (Current state + key files)
└── task-name-tasks.md      (Checklist: track progress)
```

### Three-File Strategy
1. **-plan.md:** Why, what, how (long-term view)
2. **-context.md:** Where we are now (update frequently!)
3. **-tasks.md:** What's done, what's next (checklist)

---

## 15. TROUBLESHOOTING QUICK FIXES

**Skill won't activate:**
- [ ] Check pathPatterns match your files
- [ ] Verify JSON is valid: `jq . skill-rules.json`
- [ ] Confirm hooks are executable: `ls -la .claude/hooks/*.sh`
- [ ] Make sure skill is registered in skill-rules.json
- [ ] Try editing a file that matches pathPattern

**Hook fails:**
- [ ] Make executable: `chmod +x .claude/hooks/*.sh`
- [ ] Check settings.json syntax: `jq . settings.json`
- [ ] Verify path uses `$CLAUDE_PROJECT_DIR`
- [ ] Run hook manually to test

**Agent not found:**
- [ ] Check file exists: `ls .claude/agents/agent-name.md`
- [ ] Verify filename matches what you're calling
- [ ] Check YAML frontmatter syntax (name field)

---

## 16. FILE SIZE BENCHMARKS

**Normal Ranges:**
- Skill SKILL.md: 300-500 lines
- Skill resource file: 200-500 lines
- Hook script: 50-150 lines
- Agent file: 50-100 lines
- skill-rules.json: 200-400 lines
- settings.json: 30-50 lines
- Dev docs plan: 500+ lines OK here

---

## 17. KEY URLS IN SHOWCASE

**Main Documentation:**
- `/README.md` - Overview and quick start
- `/CLAUDE_INTEGRATION_GUIDE.md` - AI integration guide
- `.claude/hooks/README.md` - Hooks documentation
- `.claude/skills/README.md` - Skills documentation
- `.claude/agents/README.md` - Agents documentation
- `dev/README.md` - Dev docs pattern guide

**Examples:**
- `.claude/skills/skill-developer/SKILL.md` - Skill structure example
- `.claude/skills/backend-dev-guidelines/SKILL.md` - Complete backend skill
- `.claude/agents/code-architecture-reviewer.md` - Agent example
- `dev/active/public-infrastructure-repo/` - Real dev docs example

---

## 18. HOOKS AT A GLANCE

### Essential (Use These)
| Hook | Type | Customization | File |
|------|------|---------------|------|
| skill-activation-prompt | UserPromptSubmit | ✅ None | .sh + .ts |
| post-tool-use-tracker | PostToolUse | ✅ Auto | .sh |

### Optional (Advanced)
| Hook | Type | Customization | Best For |
|------|------|---------------|----------|
| tsc-check | Stop | ⚠️ Heavy | Monorepo |
| error-handling-reminder | Stop | ⚠️ Moderate | Error awareness |
| stop-build-check-enhanced | Stop | ⚠️ Moderate | Build validation |
| trigger-build-resolver | Stop | ✅ Minimal | Auto-fix errors |

---

## 19. ONE-PAGE PROJECT CHECKLIST

```markdown
# [Your Project] Claude Infrastructure Setup

## Phase 1: Foundations
- [ ] Create .claude/ directory
- [ ] Copy essential hooks (skill-activation-prompt, post-tool-use-tracker)
- [ ] Create skill-rules.json with correct pathPatterns
- [ ] Create settings.json with hook registration
- [ ] Make hooks executable: chmod +x .claude/hooks/*.sh
- [ ] Verify JSON valid: jq . skill-rules.json && jq . settings.json

## Phase 2: Skills
- [ ] Copy [skill-type] skill to .claude/skills/
- [ ] Update pathPatterns for [skill] to match project structure
- [ ] Test: Edit file in [path], verify skill activates
- [ ] Copy additional skills if relevant

## Phase 3: Agents & Commands
- [ ] Copy [agent-names] to .claude/agents/
- [ ] Copy slash commands if needed to .claude/commands/

## Phase 4: Testing
- [ ] Edit relevant file, verify skill suggestion
- [ ] Test calling an agent
- [ ] Verify no errors in logs
- [ ] Create first dev docs (if long tasks expected)

## Notes
- Project structure: [describe your setup]
- Key paths to trigger skills: [list your paths]
- Team members aware of: [who knows about this]
```

---

## 20. MOST IMPORTANT CONCEPTS

1. **Auto-Activation:** UserPromptSubmit hook + skill-rules.json
2. **Progressive Disclosure:** 500-line main + resource files
3. **Session Awareness:** Don't nag about same skill twice
4. **Context Persistence:** Dev docs survive resets
5. **Modular Design:** Copy only what you need

---

**Save this guide! It answers 95% of common questions.**

