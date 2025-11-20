# Infrastructure Token Usage Analysis

Comparing token usage: **Manual approach** vs **Infrastructure approach**

## Line Count Summary

### Core Infrastructure Components

**CLAUDE.md files:**
- Root CLAUDE.md: 46 lines
- study-guides/CLAUDE.md: 250 lines
- **Total: 296 lines** (auto-loaded by Claude Code)

**Slash Commands:**
- /create-word: 112 lines
- /create-excel: 159 lines
- /create-lo-guide: 99 lines
- /create-clinical-guide: 107 lines
- /create-drug-html: 68 lines
- /verify-accuracy: 289 lines
- **Total available: 834 lines** (only 1 loads per use)

**Skills (with all resource files):**
- template-compliance-checker: 245 lines
- source-only-enforcer: 173 lines + resources
- drug-classification-assistant: 374 lines
- mnemonic-researcher: 314 lines + resources
- study-guide-verifier: 373 lines + resources
- **Total: 4,158 lines** (only load if triggered)

**Agents:**
- medical-mnemonic-researcher: 252 lines
- study-guide-analyzer: 415 lines
- **Total: 667 lines** (only load if explicitly invoked)

**READMEs:**
- **Total: 776 lines** (not auto-loaded, documentation only)

**Templates - OLD:**
- Word LO: 695 lines
- Excel Drugs Chart: 1,144 lines
- Excel Master Chart: 495 lines (not in archive)
- HTML LO: 137 lines
- Autobiography: 252 lines
- **Total: 2,228 lines**

**Templates - REVISED:**
- Word LO: 580 lines
- Excel Drugs Chart: 383 lines
- Excel Master Chart: 393 lines
- HTML LO: 140 lines
- Autobiography: 273 lines
- **Total: 1,769 lines**
- **Reduction: 459 lines (20.6% smaller)**

---

## Token Usage Scenarios

### Scenario 1: Creating Word Study Guide

**WITHOUT Infrastructure (Manual Paste):**
```
Source file:               ~500 lines (typical lecture)
Old Word template:         695 lines
Total context:             1,195 lines
```

**WITH Infrastructure:**
```
CLAUDE.md (global):        46 lines   (auto-loaded)
CLAUDE.md (study-guides):  250 lines  (auto-loaded)
Slash command:             112 lines  (/create-word loads)
REVISED Word template:     580 lines  (command reads it)
Source file:               ~500 lines (user specifies)
---
Subtotal:                  1,488 lines

Skills (if activated):
- source-only-enforcer:    ~173 lines (might activate)
- mnemonic-researcher:     ~314 lines (might activate)

Total WITHOUT skills:      1,488 lines  (+293 vs manual)
Total WITH 1 skill:        1,661 lines  (+466 vs manual)
Total WITH 2 skills:       1,975 lines  (+780 vs manual)
```

**Verdict: Infrastructure uses MORE tokens** (24-65% more depending on skill activation)

---

### Scenario 2: Creating Excel Drug Chart

**WITHOUT Infrastructure:**
```
Source file:               ~800 lines (drug lecture with details)
Old Excel template:        1,144 lines
Total context:             1,944 lines
```

**WITH Infrastructure:**
```
CLAUDE.md (global):        46 lines
CLAUDE.md (study-guides):  250 lines
Slash command:             159 lines  (/create-excel)
REVISED Excel template:    383 lines  (66% reduction!)
Source file:               ~800 lines
---
Subtotal:                  1,638 lines

Skills (if activated):
- drug-classification:     ~374 lines (likely activates)
- source-only-enforcer:    ~173 lines (might activate)

Total WITHOUT skills:      1,638 lines  (-306 vs manual, 16% LESS!)
Total WITH 1 skill:        2,012 lines  (+68 vs manual)
Total WITH 2 skills:       2,185 lines  (+241 vs manual)
```

**Verdict: Infrastructure SAVES tokens** if skills don't all activate (16% savings)

---

### Scenario 3: Second Study Guide (Same Session)

**WITHOUT Infrastructure:**
```
Source file:               ~500 lines
Template:                  695 lines (paste again)
Total:                     1,195 lines (SAME as first)
```

**WITH Infrastructure:**
```
CLAUDE.md:                 296 lines (already in context)
Slash command:             112 lines (expand again)
Template:                  580 lines (read again)
Source file:               ~500 lines
Skills:                    0 lines   (already loaded, won't re-trigger)
---
Total:                     1,488 lines

BUT: Claude "remembers" the workflow from first guide
- May skip re-reading template (just reference it)
- Skills already in context (no re-load)
- Effective context: ~612 lines (command + source)
```

**Verdict: Infrastructure MUCH better** for multiple guides in same session

---

### Scenario 4: HTML Study Guide

**WITHOUT Infrastructure:**
```
Source file:               ~400 lines
Old HTML template:         137 lines (already minimal)
Total:                     537 lines
```

**WITH Infrastructure:**
```
CLAUDE.md:                 296 lines
Slash command:             99 lines   (/create-lo-guide)
REVISED HTML template:     140 lines  (3 lines added)
Source file:               ~400 lines
Skills:                    0-173 lines (conditional)
---
Total WITHOUT skills:      935 lines  (+398 vs manual, 74% MORE)
Total WITH skills:         1,108 lines (+571 vs manual, 106% MORE)
```

**Verdict: Infrastructure uses MORE tokens** (HTML template was already lean)

---

## What Actually Loads Into Context?

**Auto-loaded (always present):**
- ✅ Root CLAUDE.md: 46 lines
- ✅ study-guides/CLAUDE.md: 250 lines
- **Total: 296 lines**

**Loaded on command:**
- ✅ Slash command file: 68-289 lines (depends which one)
- ✅ Template file: 140-580 lines (command reads it)
- ✅ Source file: variable

**Conditionally loaded:**
- ⚠️ Skills: 0-4,158 lines (only if triggered by context/prompt)
- ⚠️ Agents: 0-667 lines (only if explicitly invoked)
- ❌ READMEs: 0 lines (documentation, not loaded)
- ❌ Hooks: 0 lines (run in shell, not in Claude context)

---

## Key Findings

### Infrastructure Uses MORE Tokens When:
1. Creating short HTML guides (74% overhead)
2. Creating Word guides with skills activated (24-65% overhead)
3. Single one-off study guide creation
4. Skills all trigger at once

### Infrastructure Uses FEWER Tokens When:
1. Creating Excel drug charts (16% savings from template cleanup)
2. Creating multiple study guides in same session
3. Skills DON'T activate (disabled or not triggered)
4. Using heavily-reduced templates (Excel 66% smaller)

### Infrastructure Provides NON-TOKEN Benefits:
1. **Consistency**: Same output every time (skills enforce rules)
2. **Quality**: Fewer errors (verification skills catch mistakes)
3. **User experience**: Type `/create-word file.txt` vs paste 695 lines
4. **Automation**: Hooks enforce source-only policy automatically
5. **Reusability**: Create 10 guides without re-pasting template
6. **Documentation**: READMEs explain usage (no token cost)

---

## Optimization Recommendations

### To Minimize Token Usage:

1. **Disable unnecessary skills**
   - Edit `study-guides/.claude/skills/skill-rules.json`
   - Remove triggers for skills you don't need
   - Keep only: source-only-enforcer, mnemonic-researcher

2. **Use simpler slash commands**
   - Remove verbose verification checklists
   - Keep only essential instructions
   - Current: 112 lines → Target: 50 lines

3. **Further reduce templates**
   - Word template: 580 → 400 lines (remove examples)
   - Excel template: 383 → 300 lines (reference examples instead)

4. **Session-based workflow**
   - Create multiple guides per session (amortize overhead)
   - First guide: 1,488 lines
   - Second guide: ~612 lines (reuse loaded context)
   - Third guide: ~500 lines (just source)

5. **Manual mode for simple guides**
   - For HTML guides, skip infrastructure
   - Just paste template + source (537 vs 935 lines)

---

## Conclusion

**Token usage verdict: DEPENDS ON USE CASE**

**Infrastructure uses MORE tokens per individual guide** (+24% to +106% depending on type)

**Infrastructure saves OVERALL tokens when:**
- Creating multiple guides in one session
- Using heavily-optimized templates (Excel)
- Skills provide value that reduces back-and-forth corrections

**The real value ISN'T token savings, it's:**
- Quality and consistency
- User experience (commands vs pasting)
- Automation and enforcement
- Scalability (10 guides vs 1)

**Recommendation:**
- For 1-2 simple guides: Manual paste uses fewer tokens
- For regular study guide creation: Infrastructure overhead pays off in quality + UX
- For Excel charts: Infrastructure is actually MORE efficient (16% savings)

**Token budget consideration:**
If you're hitting token limits, disable skills and simplify slash commands. The core template cleanup (459 lines saved) helps, but CLAUDE.md + slash commands add ~400 lines overhead.

**Suggested "lite" mode:**
- Keep slash commands (UX benefit)
- Keep REVISED templates (quality benefit)
- Disable all skills except source-only-enforcer
- Don't invoke agents unless needed
- Token overhead: ~400 lines (manageable)
