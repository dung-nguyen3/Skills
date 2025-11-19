# Phase 4: Specialized Agents - Analysis & Implementation Plan

## Executive Summary

Based on comprehensive analysis of the claude-infrastructure-showcase and research on Claude Code best practices, this document outlines the implementation strategy for Phase 4: Specialized Agents for the Medical Study Guide Automation system.

**Status:** Phase 1-3 complete. Ready to begin Phase 4.

---

## Research Findings

### 1. Agent Architecture Patterns (From Infrastructure Showcase)

**Key Learnings:**

✅ **Agents are standalone** - Just copy the `.md` file and use immediately
✅ **Agents run autonomously** - Separate sub-tasks with minimal supervision
✅ **Agents return comprehensive reports** - Complete analysis when done
✅ **Agents have specialized tool access** - Only necessary tools available

**Best Practice Patterns Found:**

1. **web-research-specialist** agent:
   - Generates 5-10 search query variations
   - Systematically explores multiple sources
   - Structured output format (Executive Summary → Detailed Findings → Sources → Recommendations)
   - **Applies to:** medical-mnemonic-researcher agent

2. **code-architecture-reviewer** agent:
   - Saves output to specific location (`./dev/active/[task-name]/[task-name]-code-review.md`)
   - Returns to parent process with summary
   - Explicitly requests approval before making changes
   - **Applies to:** study-guide-analyzer agent

3. **auto-error-resolver** agent:
   - Checks for cached error information
   - Systematic process (analyze → fix → verify)
   - Uses MultiEdit for similar issues across files
   - Reports completion with summary
   - **Applies to:** Both agents (systematic analysis)

### 2. Hook Patterns (From Infrastructure Showcase & Web Research)

**Critical Findings:**

✅ **UserPromptSubmit hook** - stdout injected as context (enables skill suggestion)
✅ **PreToolUse hook** - Can block with exit code 2, provides automatic feedback
✅ **PostToolUse hook** - Cleanup and notifications, uses matchers for specific tools
✅ **Hook output control** - Use "permissionDecision": "deny" for PreToolUse, "decision": "block" for PostToolUse

**Best Practices:**

- **skill-activation-prompt hook** - THE hook that makes skills auto-activate
- **post-tool-use-tracker hook** - Tracks file changes for context management
- Both hooks use TypeScript (.ts) with fallback shell script (.sh)
- package.json for dependencies (TypeScript, tsx, @types/node)

### 3. Skill Activation Strategies (From Web Research)

**Progressive Disclosure (Critical):**

1. **Level 1: Metadata** - Name + description pre-loaded (small context cost)
2. **Level 2: Main instructions** - Loaded when skill matches
3. **Level 3: Resources** - Loaded only as needed during execution

**Optimal Sizing:**
- Keep SKILL.md body under **500 lines** for optimal performance
- Split content into separate resource files if exceeding
- Use clear, distinct trigger terms in descriptions

**Skill Activation:**
- Model-invoked (Claude decides autonomously)
- Based on description + user request
- Distinct trigger terms crucial for activation

---

## Current Infrastructure Assessment

### ✅ What We Already Have

**Phase 1-3 Complete:**
- ✅ settings.json with hook permissions
- ✅ skill-rules.json with trigger configuration
- ✅ UserPromptSubmit hook (skill-activation-prompt)
- ✅ PreToolUse hook (verification-guard)
- ✅ PostToolUse hook (post-verification-trigger)
- ✅ Stop hook (verification-completion-check)
- ✅ SessionStart hook (session-start-banner)
- ✅ Skills: mnemonic-researcher, study-guide-verifier, source-only-enforcer, template-compliance-checker, drug-classification-assistant
- ✅ Session state tracking (`.claude/hooks/state/`)

**Template Infrastructure:**
- ✅ 4 template types documented (TEMPLATE_TYPES.md)
- ✅ 5 slash commands (create-excel, create-word, create-drug-html, create-lo-guide, create-clinical-guide)
- ✅ Multi-specialty support (pharmacology, pathophysiology, clinical medicine, physical exam)

### ❌ What's Missing (Phase 4)

**Agents:**
- ❌ medical-mnemonic-researcher agent
- ❌ study-guide-analyzer agent

**Advanced Features:**
- ❌ Automatic mnemonic integration during creation
- ❌ Template auto-selection based on content type

---

## Phase 4 Implementation Plan

### Agent 1: medical-mnemonic-researcher

**Purpose:** Dedicated subagent for comprehensive mnemonic research

**Pattern Source:** web-research-specialist agent

**Capabilities:**
1. Generate 5-10 search query variations for medical mnemonics
2. Search across:
   - Medical education forums (StudentDoctor, Reddit r/medicalschool, SDN)
   - USMLE resources (First Aid, Sketchy, Pathoma references)
   - Medical mnemonic databases
   - Educational blogs and YouTube descriptions
3. Systematic compilation with:
   - Executive Summary (top 3 mnemonics)
   - Detailed Findings (organized by reliability)
   - Sources (with links)
   - Recommendations (which to use)

**Trigger Patterns:**
- Keywords: "mnemonic", "memory trick", "how to remember", "USMLE"
- Intent: Creating study guides, need memorization aids
- File context: Working on study guide files

**Output Format:**
```markdown
# Mnemonic Research Report: [Topic]

## Executive Summary
Top 3 recommended mnemonics with reliability scores

## Detailed Findings
### Mnemonic 1: [Name/Acronym]
- **What it stands for:** ...
- **How to use:** ...
- **Source:** [Link]
- **Reliability:** High/Medium/Low
- **Votes/Usage:** [If available]

## Recommendations
[Which mnemonic to use and why]

## Additional Notes
[Caveats, alternatives, areas needing verification]
```

**Files to Create:**
- `.claude/agents/medical-mnemonic-researcher.md` (main agent file)

**Integration:**
- Automatically invoked by mnemonic-researcher skill
- Can be manually invoked: "Use medical-mnemonic-researcher agent to find mnemonics for [topic]"

---

### Agent 2: study-guide-analyzer

**Purpose:** Deep analysis agent for existing study guides

**Pattern Source:** code-architecture-reviewer agent

**Capabilities:**
1. **Comprehensive 6-step verification:**
   - Step 1: Read source file completely
   - Step 2: Read study guide completely
   - Step 3: Systematic checks (names, classifications, merged cells, info accuracy, format, emojis)
   - Step 4: Document all issues
   - Step 5: Return to parent with findings
   - Step 6: Wait for approval before fixing

2. **Analysis Categories:**
   - Source Accuracy (source-only compliance, external additions marked with *)
   - Template Compliance (structure, formatting, colors, all required elements)
   - Completeness (all LOs answered, all comparisons, master chart complete)
   - Quality (no incorrect groupings, spelling, consistent terminology)

3. **Output Structure:**
   - Executive Summary (critical findings in 2-3 sentences)
   - Critical Issues (must fix)
   - Important Improvements (should fix)
   - Minor Suggestions (nice to have)
   - Next Steps

**Output Location:**
Save to: `[Class]/[Exam]/Claude Study Tools/[filename]-analysis.md`

**Trigger Patterns:**
- Keywords: "verify accuracy", "analyze study guide", "check completeness"
- Intent: Post-creation verification, quality assurance
- File context: Working with .docx, .xlsx, .html study guide files

**Integration:**
- Automatically invoked by study-guide-verifier skill
- Replaces current /verify-accuracy slash command with agent-based analysis
- Can be manually invoked: "Use study-guide-analyzer agent to verify [filename]"

**Files to Create:**
- `.claude/agents/study-guide-analyzer.md` (main agent file)

---

### Integration Checklist

**For medical-mnemonic-researcher:**
- [ ] Create agent file based on web-research-specialist pattern
- [ ] Update mnemonic-researcher skill to invoke agent
- [ ] Add trigger patterns to skill-rules.json
- [ ] Test with: "Find mnemonics for HIV drugs"
- [ ] Verify output format and source links

**For study-guide-analyzer:**
- [ ] Create agent file based on code-architecture-reviewer pattern
- [ ] Update study-guide-verifier skill to invoke agent
- [ ] Add trigger patterns to skill-rules.json
- [ ] Update /verify-accuracy command to use agent
- [ ] Test with existing study guide
- [ ] Verify analysis saves to correct location
- [ ] Verify approval workflow before fixes

---

## File Organization

```
Copy Study Guide Claude Q3 2/
├── .claude/
│   ├── agents/
│   │   ├── medical-mnemonic-researcher.md  ← NEW (Phase 4.1)
│   │   └── study-guide-analyzer.md         ← NEW (Phase 4.2)
│   ├── commands/
│   │   ├── create-excel.md
│   │   ├── create-word.md
│   │   ├── create-drug-html.md
│   │   ├── create-lo-guide.md
│   │   ├── create-clinical-guide.md
│   │   └── verify-accuracy.md              ← UPDATE (Phase 4.2)
│   ├── hooks/
│   │   ├── skill-activation-prompt.sh/.ts
│   │   ├── verification-guard.sh
│   │   ├── post-verification-trigger.sh
│   │   ├── verification-completion-check.sh
│   │   ├── session-start-banner.sh
│   │   └── state/
│   ├── skills/
│   │   ├── skill-rules.json                ← UPDATE (Phase 4)
│   │   ├── mnemonic-researcher/            ← UPDATE (Phase 4.1)
│   │   ├── study-guide-verifier/           ← UPDATE (Phase 4.2)
│   │   ├── source-only-enforcer/
│   │   ├── template-compliance-checker/
│   │   └── drug-classification-assistant/
│   └── settings.json
├── CLAUDE.md
├── HOW_TO_USE.md                           ← UPDATE (Phase 4)
├── MAINTENANCE.md
├── README.md                               ← UPDATE (Phase 4)
├── TEMPLATE_TYPES.md
└── GIT_WORKFLOW.md
```

---

## Expected Improvements

### Performance Benefits

**Before Phase 4:**
- Manual mnemonic research (5-10 minutes per topic)
- Inline verification (limited depth, can miss issues)
- No systematic analysis workflow

**After Phase 4:**
- Automated mnemonic research with agent (30 seconds, comprehensive)
- Deep analysis with systematic 6-step protocol
- Approval workflow prevents accidental changes

### Quality Benefits

**Mnemonic Quality:**
- Multiple source validation
- Reliability scoring
- USMLE-specific focus
- Verification of established mnemonics

**Verification Quality:**
- Comprehensive systematic analysis
- Statistical completeness checks
- Pattern detection across study guide
- Detailed reporting with severity levels

---

## Testing Strategy

### Agent 1: medical-mnemonic-researcher

**Test Cases:**
1. Simple topic: "Find mnemonics for cranial nerves"
2. Drug topic: "Find mnemonics for HIV drug classes"
3. Disease topic: "Find mnemonics for heart failure signs"

**Success Criteria:**
- ✅ Generates 5+ search queries
- ✅ Finds 3+ reliable mnemonics per topic
- ✅ Includes source links
- ✅ Ranks by reliability
- ✅ Completes in < 1 minute

### Agent 2: study-guide-analyzer

**Test Cases:**
1. Perfect study guide (should pass all checks)
2. Study guide with missing LOs (should catch)
3. Study guide with external knowledge unmarked (should catch)
4. Study guide with incorrect merged cells (should catch)

**Success Criteria:**
- ✅ Completes 6-step analysis
- ✅ Saves analysis to correct location
- ✅ Identifies all deliberate issues
- ✅ Returns to parent with summary
- ✅ Waits for approval before fixing

---

## Documentation Updates

### HOW_TO_USE.md

Add section:
```markdown
## Using Agents for Advanced Tasks

### Automatic Mnemonic Research

When creating study guides, the medical-mnemonic-researcher agent automatically:
- Searches multiple medical education sources
- Finds established USMLE mnemonics
- Ranks by reliability
- Provides source links

**Manual invocation:**
```
Use medical-mnemonic-researcher agent to find mnemonics for [topic]
```

### Deep Study Guide Analysis

For comprehensive verification, the study-guide-analyzer agent:
- Performs systematic 6-step analysis
- Checks source accuracy, template compliance, completeness, quality
- Saves detailed report
- Requests approval before fixes

**Manual invocation:**
```
Use study-guide-analyzer agent to verify [filename]
```
```

### README.md

Update Infrastructure Status section:
```markdown
## Infrastructure Status

- ✅ Phase 1: Foundation infrastructure (completed)
- ✅ Phase 2: Quality gate hooks (completed)
- ✅ Phase 3: Reliability improvements (completed)
- ✅ Phase 4: Specialized Agents (completed) ← NEW
  - medical-mnemonic-researcher agent
  - study-guide-analyzer agent
```

---

## Next Steps

**Immediate (Phase 4.1):**
1. Create medical-mnemonic-researcher.md agent
2. Update mnemonic-researcher skill to invoke agent
3. Test with multiple medical topics
4. Document in HOW_TO_USE.md

**Follow-up (Phase 4.2):**
1. Create study-guide-analyzer.md agent
2. Update study-guide-verifier skill to invoke agent
3. Update /verify-accuracy command
4. Test with existing study guides
5. Document in HOW_TO_USE.md

**Final (Phase 4 completion):**
1. Update README.md with Phase 4 status
2. Update skill-rules.json with new triggers
3. Commit and push changes
4. Test complete workflow end-to-end

---

## Phase 5 Preview

**After Phase 4 completion, consider:**
- Study guide analytics agent (metrics, productivity tracking)
- Template auto-selection based on content type
- MCP server integration (PubMed medical search)
- Additional template types (flashcards, quizzes)

---

## References

**Infrastructure Showcase:**
- `claude-infrastructure-showcase/.claude/agents/web-research-specialist.md`
- `claude-infrastructure-showcase/.claude/agents/code-architecture-reviewer.md`
- `claude-infrastructure-showcase/.claude/hooks/skill-activation-prompt.ts`
- `claude-infrastructure-showcase/.claude/skills/README.md`

**Web Research:**
- Claude Code Best Practices (Anthropic official)
- Skill Authoring Best Practices (Claude Docs)
- Hooks Reference (Claude Code Docs)
- Progressive Disclosure patterns

**Current Project:**
- `CLAUDE.md` - Medical study guide creation protocol
- `TEMPLATE_TYPES.md` - 4 template types documentation
- `HOW_TO_USE.md` - User guide
- `MAINTENANCE.md` - Maintenance guide
