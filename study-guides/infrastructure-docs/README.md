# Infrastructure Documentation

This folder contains **technical documentation** for developers and advanced users who want to understand or extend the study guide automation infrastructure.

---

## Who This Is For

**This documentation is for:**
- Developers who want to understand the infrastructure implementation
- Advanced users creating their own skills, hooks, or agents
- Those researching Claude Code automation patterns
- Contributors extending the system

**If you just want to USE the study guide system:**
- See **[../user-docs/](../user-docs/)** instead - user-focused documentation
- Start with **[../user-docs/START_HERE.md](../user-docs/START_HERE.md)**

---

## Documentation Files

### COMPREHENSIVE_INFRASTRUCTURE_ANALYSIS.md
**Research and design analysis for Phase 4-5 infrastructure**

**What's inside:**
- Research from claude-infrastructure-showcase
- Web research on 2025 best practices
- Design decisions for hooks, agents, resource libraries
- Analysis of progressive disclosure patterns
- MCP integration research

**Who it's for:** Understanding the "why" behind Phase 4-5 design decisions

**Size:** ~1,400 lines

---

### PHASE_5_COMPLETION.md
**Phase 5 implementation summary and status**

**What's inside:**
- Phase 5.1: Hook Ecosystem Enhancement (complete)
- Phase 5.2: Progressive Disclosure Resource Libraries (complete)
- Phase 5.3: MCP Integration (deferred)
- Phase 5.4: Automated Quality Gates (complete)
- Success metrics and lessons learned
- Total lines of code/documentation added

**Who it's for:** Understanding what was implemented in Phase 5 and current status

**Size:** ~700 lines

---

### PHASE_5.1_IMPLEMENTATION.md
**Detailed technical documentation for hook ecosystem**

**What's inside:**
- PostToolUse tracker implementation details
- Stop validation hooks (3 hooks)
- Session-based caching architecture
- Helper script documentation
- Testing and validation procedures

**Who it's for:** Developers working with or extending the hook system

**Size:** ~1,200 lines

---

## Phase History

**Completed Phases:**
- ✅ **Phase 1:** Foundation infrastructure (skills, slash commands)
- ✅ **Phase 2:** Quality gate hooks (verification enforcement)
- ✅ **Phase 3:** Reliability improvements (error resilience)
- ✅ **Phase 4:** Specialized Agents (mnemonic-researcher, study-guide-analyzer)
- ✅ **Phase 5:** Advanced Infrastructure (5.1, 5.2, 5.4 complete)
  - ✅ Phase 5.1: Hook Ecosystem Enhancement
  - ✅ Phase 5.2: Progressive Disclosure Resource Libraries
  - ⏸️ Phase 5.3: MCP Integration (deferred)
  - ✅ Phase 5.4: Automated Quality Gates

**Future Phases:**
- 📋 **Phase 6:** Advanced features (template versioning, analytics, testing)
- 📋 **Phase 5.3:** MCP Integration (when MCPs available)

---

## Infrastructure Components

### Skills (`.claude/skills/`)
**Auto-activating knowledge that Claude Code loads when needed**

1. **source-only-enforcer/** - Prevents AI hallucinations
   - Main: `SKILL.md` (174 lines)
   - Resources: 6 files, ~2,400 lines

2. **study-guide-verifier/** - Quality verification skill
   - Main: `SKILL.md` (377 lines)
   - Resources: 2 files, ~750 lines

3. **mnemonic-researcher/** - Finds established mnemonics
   - Main: `SKILL.md` (314 lines)
   - Resources: 1 file, ~160 lines

### Agents (`.claude/agents/`)
**Specialized autonomous agents**

1. **medical-mnemonic-researcher/** - Searches medical education sources
2. **study-guide-analyzer/** - Comprehensive 6-step verification

### Hooks (`.claude/hooks/`)
**Workflow automation and quality gates**

**PostToolUse Hooks:**
- `post-study-guide-tracker.sh` - Metadata tracking

**Stop Hooks:**
- `stop-study-guide-validator.sh` - File size validation
- `stop-medical-accuracy-check.sh` - Source association checks
- `stop-auto-trigger-analyzer.sh` - Critical issue warnings

**Helpers:**
- `helpers/detect-source-association.sh`
- `helpers/detect-template-type.sh`

### Scripts (`.claude/scripts/`)
**Standalone validation tools**

- `check-study-guides.sh` - Batch quality validation
- `README.md` - Usage and CI/CD integration guide

---

## Key Patterns and Concepts

### Progressive Disclosure (500-Line Rule)
- Main SKILL.md files stay under 500 lines
- Deep-dive content split into resource files
- Resources loaded on-demand when needed
- Follows infrastructure showcase best practices

### Hook Ecosystem
- **PostToolUse:** Autonomous metadata tracking
- **Stop:** Quality validation at session end
- **Session caching:** Survives context resets
- **Silent operation:** No user interruption

### Resource Libraries
- Modular documentation (300-500 lines per resource)
- Organized by topic
- Scalable knowledge base
- On-demand loading

### Quality Gates
- Real-time (hooks during creation)
- Batch validation (standalone scripts)
- CI/CD integration ready

---

## How to Extend the Infrastructure

### Creating New Skills
1. Study existing skills in `.claude/skills/`
2. Follow 500-line rule for main SKILL.md
3. Create resource files for deep-dive content
4. Test activation patterns

### Creating New Hooks
1. Study existing hooks in `.claude/hooks/`
2. Follow session-based caching patterns
3. Keep hooks silent (exit 0 for non-blocking)
4. Register in `.claude/settings.json`

### Creating New Agents
1. Study existing agents in `.claude/agents/`
2. Define clear activation criteria
3. Document in parent skill
4. Test with edge cases

---

## Related Documentation

**User Documentation:**
- [../user-docs/HOW_TO_USE.md](../user-docs/HOW_TO_USE.md) - How to create study guides
- [../user-docs/MAINTENANCE.md](../user-docs/MAINTENANCE.md) - Customization and troubleshooting
- [../user-docs/START_HERE.md](../user-docs/START_HERE.md) - 3-step quick start

**Templates:**
- [../templates-and-examples/](../templates-and-examples/) - Template files and examples

**Main Project:**
- [../README.md](../README.md) - Project overview
- [../CLAUDE.md](../CLAUDE.md) - Instructions for Claude Code

---

## Contributing

**Before extending the infrastructure:**
1. Read COMPREHENSIVE_INFRASTRUCTURE_ANALYSIS.md for design principles
2. Review relevant phase documentation
3. Study existing implementations
4. Test thoroughly before committing

**Best practices:**
- Follow progressive disclosure patterns
- Keep hooks silent and non-blocking
- Document in both code and markdown
- Test with real study guide workflows

---

**Last Updated:** 2025-11-19 (Phase 5 completion)
