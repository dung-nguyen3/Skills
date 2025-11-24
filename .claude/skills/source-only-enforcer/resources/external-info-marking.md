# External Information Marking

## Purpose

Guide for properly marking the ONE allowed exception to source-only policy: researched mnemonics.

---

## The Exception: Researched Mnemonics

### Why Mnemonics Are Allowed

**Educational value:**
- Help students memorize complex lists
- Established learning aids in medical education
- Widely used in USMLE/board prep

**Low risk:**
- Don't contain medical facts (just memory aids)
- Easily verifiable (student can look up)
- Clearly marked as external (asterisk)

**Source of truth:**
- Researched via mnemonic-researcher agent
- Found on r/medicalschool, SDN, USMLE forums
- Ranked by reliability and usage

### What Counts as "Researched"

**VALID researched mnemonics:**
- Found by mnemonic-researcher agent
- From established medical education sources:
  - r/medicalschool Reddit
  - Student Doctor Network (SDN)
  - USMLE forums
  - First Aid (if cited)
  - Sketchy Medical
  - Pathoma
  - Anki decks (popular ones)
- Have user ratings/confirmation
- Multiple sources agree

**INVALID "researched" mnemonics:**
- Made up by Claude
- From your memory (even if you "know" it's common)
- From single unverified source
- Modified versions of established mnemonics
- Invented on the spot

---

## Marking Protocol

### Required Format

**All researched mnemonics MUST include:**

1. **Asterisk marker (*)** - Immediately after mnemonic
2. **Source attribution** - In parentheses
3. **Reliability info** - If available from agent

**Standard format:**
```
[Fact list]

Mnemonic: "ABCD"* (r/medicalschool, 5-star reliability, 15+ confirmations)
```

### Examples of Correct Marking

**Example 1: Single-source mnemonic**
```
P450 Inducers: Phenytoin, Carbamazepine, Rifampin, St. John's Wort

Mnemonic: "PC BRAS"* (r/medicalschool, highly rated)
```

**Example 2: Multi-source mnemonic**
```
Cranial Nerves:

Mnemonic: "Oh Oh Oh, To Touch And Feel..."* (First Aid 2024, r/medicalschool, widely used)
```

**Example 3: Agent-provided with reliability**
```
Vitamin B12 Deficiency Symptoms:

Mnemonic: "LOST"* (SDN forums, 4-star reliability, verified by multiple users)
- Lethargy
- Oral glossitis
- Subacute combined degeneration
- Tingling/paresthesias
```

### Examples of Incorrect Marking

**WRONG - No asterisk:**
```
Mnemonic: "ABCD" (r/medicalschool)
```

**WRONG - No source:**
```
Mnemonic: "ABCD"*
```

**WRONG - Vague source:**
```
Mnemonic: "ABCD"* (common mnemonic)
```

**WRONG - Invented mnemonic:**
```
Mnemonic: "ABCD"* (created for this guide)
```

---

## Using Mnemonic-Researcher Agent

### When to Use

**Use agent when:**
- Source doesn't have mnemonic for complex list
- List has 4+ items students need to memorize
- Topic commonly has mnemonics (e.g., drug classes, symptoms)
- Creating study guide for exam prep

**DON'T use agent when:**
- List is only 2-3 items (unnecessary)
- Source already provides mnemonic
- Mnemonic would be unhelpful (e.g., list of unrelated facts)

### How to Invoke

**Via skill:**
```
"I need to research a mnemonic for [topic]"
```

**Agent automatically:**
1. Searches r/medicalschool, SDN, USMLE forums
2. Finds 3 top-rated mnemonics
3. Ranks by reliability (1-5 stars)
4. Provides user feedback and sources

### Agent Output Format

**Typical response:**
```
Top 3 Mnemonics for [Topic]:

1. "ABCD"
   - Source: r/medicalschool
   - Reliability: ⭐⭐⭐⭐⭐ (15+ confirmations)
   - Components: A=X, B=Y, C=Z, D=W

2. "WXYZ"
   - Source: SDN forums, First Aid 2024
   - Reliability: ⭐⭐⭐⭐ (verified by 8 users)
   - Components: W=X, X=Y, Y=Z, Z=W

3. "MNOP"
   - Source: USMLE forums
   - Reliability: ⭐⭐⭐ (mentioned by 3 users)
   - Components: M=X, N=Y, O=Z, P=W
```

**Choose the highest-rated option** and mark it appropriately in study guide.

---

## Placement Guidelines

### Where to Put Mnemonics

**Recommended locations:**

**1. End of section (preferred):**
```
[Detailed content from source]

Summary:
- Fact 1
- Fact 2
- Fact 3

Mnemonic: "ABC"* (r/medicalschool, 5-star)
```

**2. After fact list:**
```
Drug Class Side Effects:
- Nausea
- Vomiting
- Diarrhea

Mnemonic: "NVD"* (SDN, commonly used)
```

**3. Separate "Mnemonics" section:**
```
## High-Yield Mnemonics

P450 Inducers: "PC BRAS"* (r/medicalschool)
P450 Inhibitors: "SICKFACES.COM"* (First Aid 2024)
```

### Where NOT to Put Mnemonics

**Avoid:**
- In the middle of detailed explanations (disrupts flow)
- Before introducing the facts (student won't understand mnemonic yet)
- In tables/charts (formatting issues)
- Mixed with source content (confusing what's from source vs. researched)

---

## Quality Standards

### Mnemonic Selection Criteria

**Choose mnemonics that are:**

1. **Accurate** - Components match facts exactly
2. **Memorable** - Actually helps memorization (not just acronym)
3. **Established** - Widely used, not obscure
4. **Appropriate** - Professional, not offensive
5. **Verified** - High reliability rating from agent

**Reject mnemonics that:**
- Have components not in study guide
- Are overly complex or confusing
- Use offensive language
- Have low reliability (<3 stars)
- Can't be verified

### Reliability Thresholds

**Agent provides reliability ratings:**
- ⭐⭐⭐⭐⭐ (5 stars) - Excellent, widely confirmed → PREFERRED
- ⭐⭐⭐⭐ (4 stars) - Very good, multiple sources → ACCEPTABLE
- ⭐⭐⭐ (3 stars) - Good, some confirmation → USE WITH CAUTION
- ⭐⭐ (2 stars) - Low confirmation → AVOID
- ⭐ (1 star) - Single mention, unverified → REJECT

**Minimum threshold: 3 stars**

If no 3+ star mnemonics found → Don't include mnemonic

---

## Verification After Marking

### Checklist for Every Mnemonic

Before finalizing study guide:

- [ ] Mnemonic marked with asterisk (*)
- [ ] Source attribution provided
- [ ] Source is valid (r/medicalschool, SDN, First Aid, etc.)
- [ ] Reliability rating included (if available)
- [ ] All mnemonic components match study guide facts
- [ ] Mnemonic placement is appropriate
- [ ] No invented mnemonics included

### Common Marking Errors

**Error 1: Forgetting asterisk**
- Looks like mnemonic from source
- User can't distinguish researched vs. source content
- Fix: Add asterisk to ALL researched mnemonics

**Error 2: Vague source citation**
- "Common mnemonic" - not acceptable
- "Medical students use this" - not acceptable
- Fix: Cite specific source (r/medicalschool, First Aid, etc.)

**Error 3: Modified mnemonics**
- Taking established mnemonic and changing it
- Even small changes = invented mnemonic
- Fix: Use mnemonic exactly as found, or don't use it

**Error 4: Source inconsistency**
- Marking some mnemonics, not others
- Inconsistent format across study guide
- Fix: Apply marking protocol to ALL researched mnemonics

---

## Special Cases

### Case 1: Source Has Mnemonic

**If source provides mnemonic:**
- Use it WITHOUT asterisk
- No source citation needed (it's from source)
- Treat as regular source content

**Example:**
```
Source: "Remember P450 inducers with PC BRAS"

Study guide: "Mnemonic: PC BRAS"
(No asterisk - from source)
```

### Case 2: Multiple Mnemonics for Same Topic

**If agent finds 3 good mnemonics:**
- Include top 1-2 (not all 3)
- Choose most reliable + most memorable
- Mark each appropriately

**Example:**
```
Mnemonic Option 1: "ABCD"* (r/medicalschool, 5-star, most popular)
Mnemonic Option 2: "WXYZ"* (First Aid 2024, also widely used)
```

### Case 3: Mnemonic Doesn't Fit All Facts

**If established mnemonic only covers subset of facts:**
- Note limitation in parentheses
- List remaining facts separately

**Example:**
```
Drug Class Side Effects: A, B, C, D, E, F

Mnemonic: "ABC"* (r/medicalschool, 4-star) - covers first 3
Remaining: D, E, F
```

### Case 4: Agent Can't Find Mnemonic

**If mnemonic-researcher agent returns no results:**
- Accept that no established mnemonic exists
- Don't invent one
- List facts without mnemonic

**Example:**
```
Drug X Side Effects:
- Nausea
- Headache
- Rash

(No established mnemonic found for this drug)
```

---

## Summary

**Key principles:**

1. **Only exception:** Researched mnemonics are the ONLY allowed external addition
2. **Always mark:** Asterisk (*) + source citation for ALL researched mnemonics
3. **Use agent:** mnemonic-researcher agent finds verified, established mnemonics
4. **Quality standards:** Minimum 3-star reliability, accurate components, appropriate content
5. **No invention:** Never make up mnemonics, even if they seem helpful

**Proper marking format:**
```
Mnemonic: "[mnemonic]"* (source, reliability)
```

**Remember:**
- Mnemonics are teaching aids, not medical facts
- Clear marking prevents confusion about what's from source
- Students can independently verify researched mnemonics
- Maintains study guide integrity while adding learning value

---

**See also:**
- [Source Validation Guide](source-validation-guide.md) - What counts as source content
- [Hallucination Prevention](hallucination-prevention.md) - Why external additions are dangerous
- [Complete Examples](complete-examples.md) - Full study guide examples with marked mnemonics
