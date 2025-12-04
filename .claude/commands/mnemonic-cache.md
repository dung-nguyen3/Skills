---
description: Manage mnemonic cache - view stats, clean expired entries, list cached mnemonics
argument-hint: stats | clean | list [topic] | lookup <topic> <category> | help
---

Mnemonic Cache Management: $ARGUMENTS

## Command Usage

**View cache statistics:**
```
/mnemonic-cache stats
```

**Clean expired entries:**
```
/mnemonic-cache clean
```

**List all cached mnemonics:**
```
/mnemonic-cache list
```

**List mnemonics for specific topic:**
```
/mnemonic-cache list beta-blockers
```

**Lookup specific mnemonic:**
```
/mnemonic-cache lookup beta-blockers adverse-effects
```

**Show help:**
```
/mnemonic-cache help
```

---

## Instructions

### Parse Arguments

Extract command from $ARGUMENTS:
- First word is the command: stats | clean | list | lookup | help
- Remaining words are parameters

### Execute Command

#### Command: stats

Show cache statistics:
```bash
python3 .claude/mnemonic-cache/mnemonic_cache_helper.py stats
```

Displays:
- Total entries
- Cache hits/misses
- Hit rate percentage
- Total token savings

---

#### Command: clean

Remove expired entries (TTL > 90 days):
```bash
python3 .claude/mnemonic-cache/mnemonic_cache_helper.py clean
```

Reports:
- Number of entries removed
- Remaining entries count

---

#### Command: list [topic]

List cached mnemonics, optionally filtered by topic:

**All mnemonics:**
```bash
python3 .claude/mnemonic-cache/mnemonic_cache_helper.py list
```

**Filtered by topic:**
```bash
python3 .claude/mnemonic-cache/mnemonic_cache_helper.py list "beta-blockers"
```

Displays:
- Cache key
- Mnemonic value (truncated)
- Hit count

---

#### Command: lookup <topic> <category>

Lookup specific mnemonic:

**Example:**
```bash
python3 .claude/mnemonic-cache/mnemonic_cache_helper.py lookup "beta-blockers" "adverse-effects"
```

Returns:
- Full mnemonic text if found
- Cache miss message if not found

---

#### Command: help

Display usage information:

```
MNEMONIC CACHE MANAGEMENT

The mnemonic cache stores researched medical mnemonics to avoid
redundant WebSearch operations during study guide creation.

Token Efficiency:
- First use (cache miss): ~5,000 tokens (WebSearch)
- Subsequent uses (cache hit): ~50 tokens (read from cache)
- Savings: ~4,950 tokens per reuse

Available Commands:
  /mnemonic-cache stats              - View cache statistics
  /mnemonic-cache clean              - Remove expired entries
  /mnemonic-cache list               - List all cached mnemonics
  /mnemonic-cache list <topic>       - List mnemonics for topic
  /mnemonic-cache lookup <t> <c>     - Lookup specific mnemonic
  /mnemonic-cache help               - Show this help

Cache Location:
  .claude/mnemonic-cache/cache.json

Documentation:
  .claude/mnemonic-cache/README.md

Automatic Usage:
  All study guide commands automatically check the cache before
  performing WebSearch for mnemonics. No manual intervention needed.
```

---

## Example Usage

### View Stats

**Input:**
```
/mnemonic-cache stats
```

**Output:**
```
==================================================
MNEMONIC CACHE STATISTICS
==================================================
Total entries:    15
Cache hits:       42
Cache misses:     18
Hit rate:         70.0%
Token savings:    ~207,900 tokens
==================================================
```

---

### Clean Expired Entries

**Input:**
```
/mnemonic-cache clean
```

**Output:**
```
🧹 Cleaned 3 expired entries
📊 Remaining entries: 12
```

---

### List Cached Mnemonics

**Input:**
```
/mnemonic-cache list
```

**Output:**
```
Found 15 entries:

  • beta-blockers-adverse-effects-mnemonic
    Value: BASH: Bradycardia, Asthma exacerbation, Shock (cardiogenic), Heart bloc...
    Hits: 8

  • ace-inhibitors-adverse-effects-mnemonic
    Value: CAPTOPRIL: Cough, Angioedema, Proteinuria, Taste changes, Orthostatic h...
    Hits: 5

  • hiv-nrti-adverse-effects-mnemonic
    Value: LACTIC: Lactic Acidosis, Abdominal pain, Cytopenias (bone marrow suppres...
    Hits: 12
```

---

### List by Topic

**Input:**
```
/mnemonic-cache list hiv
```

**Output:**
```
Found 4 entries:

  • hiv-nrti-adverse-effects-mnemonic
    Value: LACTIC: Lactic Acidosis, Abdominal pain, Cytopenias...
    Hits: 12

  • hiv-pi-adverse-effects-mnemonic
    Value: GRHLS: GI upset, Rash, Hyperlipidemia, Lipodystrophy, Stevens-Johnson...
    Hits: 7
```

---

### Lookup Specific Mnemonic

**Input:**
```
/mnemonic-cache lookup beta-blockers adverse-effects
```

**Output:**
```
✓ Cache hit: beta-blockers-adverse-effects-mnemonic (hit count: 9)
💰 Token savings: ~208,950 tokens total

Mnemonic: BASH: Bradycardia, Asthma exacerbation, Shock (cardiogenic), Heart block
```

---

## Notes

- Cache automatically used by all study guide commands
- No manual lookup needed during normal workflow
- Use this command for cache maintenance and monitoring
- Expired entries (>90 days old) are auto-removed on next access
- Cache persists across sessions and quarters

---

## Integration with Study Guide Commands

When creating study guides, commands automatically:

1. **Before WebSearch:**
   - Check cache for existing mnemonic
   - If found: Use cached value (saves ~5k tokens)
   - If not found: Proceed with WebSearch

2. **After WebSearch:**
   - Store researched mnemonic in cache
   - Future study guides can reuse it

**No user action required** - cache works automatically!

---

## Advanced Usage

### Manual Cache Operations

For advanced users, direct Python access:

**Lookup from Python:**
```python
from mnemonic_cache_helper import lookup, store

# Check cache
mnemonic = lookup("beta-blockers", "adverse-effects")

if mnemonic:
    print(f"Found: {mnemonic}")
else:
    # WebSearch and store
    mnemonic = "BASH: Bradycardia, Asthma..."
    store("beta-blockers", "adverse-effects", mnemonic,
          source_url="https://...")
```

**Get stats programmatically:**
```python
from mnemonic_cache_helper import get_stats

stats = get_stats()
print(f"Hit rate: {stats['hit_rate']}%")
print(f"Token savings: {stats['token_savings']}")
```

---

## Maintenance Schedule

**Weekly:** Run `/mnemonic-cache stats` to monitor hit rate
**Monthly:** Run `/mnemonic-cache clean` to remove expired entries
**Quarterly:** Review cached mnemonics for accuracy
**Per semester:** Backup cache.json for historical reference
