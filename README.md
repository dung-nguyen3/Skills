# Skills Repository - Quick Commands Reference

Pharmacy study guide generation system using Claude Code.

---

## Study Guide Commands

### Word Study Guide
```
/word "path/to/lecture.txt"
```

### Excel Drug Chart
```
/excel "path/to/drugs.txt"
```

### HTML Learning Objectives Guide
```
/html-LO "path/to/lecture.txt"
```

### HTML Drug Reference (Mobile)
```
/html-drug "path/to/drugs.txt"
```

### Clinical Assessment Guide
```
/clinical "path/to/source.txt" "Chief Complaint"
```

### Drug Biography Stories
```
/biography "path/to/drugs.txt"
```

### Anki Flashcard Deck
```
/anki "path/to/source.txt"
```

---

## Verification

### Verify Study Guide Accuracy
```
/verify-accuracy "path/to/study-guide.xlsx" "path/to/source.txt"
```

---

## Which Command Should I Use?

| Content Type | Command |
|--------------|---------|
| Pharmacology drugs (Excel) | `/excel` |
| Pharmacology drugs (HTML/mobile) | `/html-drug` |
| Drug stories (creative/memorable) | `/biography` |
| Any medical topic (HTML) | `/html-LO` |
| Any medical topic (Word) | `/word` |
| Clinical exams | `/clinical` |
| Flashcards | `/anki` |
| Verify existing guide | `/verify-accuracy` |

---

## Mnemonics

Mnemonics are automatically researched when creating study guides.

To research mnemonics manually: "Find mnemonics for [topic]"

---

## Full Documentation

- [QUICK_START.md](QUICK_START.md) - Complete interactive guide
- [SLASH_COMMANDS_REFERENCE.md](SLASH_COMMANDS_REFERENCE.md) - Detailed command docs
- [study-guides/user-docs/HOW_TO_USE.md](study-guides/user-docs/HOW_TO_USE.md) - Full usage guide

---

## Repository Structure

```
.claude/           # Claude infrastructure (commands, skills, hooks)
study-guides/      # Templates and documentation
```

See [CLAUDE.md](CLAUDE.md) for full repository details.
