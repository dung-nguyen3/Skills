# Mnemonic Cache System

## Purpose

Saves researched medical mnemonics to avoid redundant WebSearch operations across study guide creation sessions.

## Token Efficiency

**First use (cache miss):**
- WebSearch for mnemonic: ~5,000 tokens
- Store in cache: ~50 tokens
- **Total: ~5,050 tokens**

**Subsequent uses (cache hit):**
- Read from cache: ~50 tokens
- **Savings: ~4,950 tokens per reuse**

**Break-even:** After 1 reuse

## Cache Entry Structure

```json
{
  "key": "beta-blockers-adverse-effects-mnemonic",
  "value": "BASH: Bradycardia, Asthma exacerbation, Shock (cardiogenic), Heart block",
  "source_url": "https://www.medschoolbootcamp.com/mnemonics",
  "topic": "beta-blockers",
  "category": "adverse-effects",
  "created_at": 1704398400,
  "last_accessed": 1704398400,
  "ttl_days": 90,
  "hit_count": 3,
  "tags": ["pharmacology", "cardiovascular", "adverse-effects"]
}
```

## Cache Operations

### Lookup (Before WebSearch)

```python
# Pseudo-code for agents/commands
cache_key = f"{topic}-{category}-mnemonic"
cached_mnemonic = lookup_cache(cache_key)

if cached_mnemonic:
    # Cache hit - use cached value (~50 tokens)
    return cached_mnemonic
else:
    # Cache miss - perform WebSearch (~5,000 tokens)
    mnemonic = websearch_mnemonic(topic, category)
    store_cache(cache_key, mnemonic)
    return mnemonic
```

### Store (After WebSearch)

Automatically stores new mnemonics with:
- Key: `{topic}-{category}-mnemonic`
- TTL: 90 days (configurable)
- Metadata: source URL, tags, timestamp

### Eviction

- **TTL-based:** Entries expire after 90 days
- **Manual cleanup:** Run `/mnemonic-cache-clean` to remove expired entries
- **Stats tracking:** Hit/miss ratio, token savings

## Integration

### Commands That Use Cache

All study guide commands check cache before WebSearch:
- `/4-tab-excel`
- `/LO-word`
- `/LO-html`
- `/drugs-html`
- `/word-excel-anki`
- `/autobiography-trick`

### Automatic Cache Usage

When commands encounter mnemonic research step:
1. Generate cache key from topic + category
2. Check cache for existing mnemonic
3. If found: Use cached value (saves ~5k tokens)
4. If not found: WebSearch and store result

## Cache Management

### View Cache Stats

```bash
cat .claude/mnemonic-cache/cache.json | jq '.stats'
```

### List All Cached Mnemonics

```bash
cat .claude/mnemonic-cache/cache.json | jq '.entries[] | {key, value, hit_count}'
```

### Clear Expired Entries

Entries older than TTL are auto-removed on next access.

Manual cleanup:
```bash
/mnemonic-cache-clean
```

### Reset Cache (Emergency)

```bash
cp .claude/mnemonic-cache/cache.json .claude/mnemonic-cache/cache.json.backup
echo '{"version":"1.0","entries":[],"stats":{"total_hits":0,"total_misses":0,"total_entries":0,"token_savings":0}}' > .claude/mnemonic-cache/cache.json
```

## Performance Tracking

Cache tracks:
- **Total hits:** How many times cache was used
- **Total misses:** How many WebSearches were needed
- **Hit rate:** `hits / (hits + misses)`
- **Token savings:** `hits * 4,950 tokens`

## Best Practices

1. **Consistent key naming:** Use `{topic}-{category}-mnemonic` format
2. **Verify accuracy:** Always check cached mnemonics are still accurate
3. **Update when needed:** If better mnemonic found, update cache entry
4. **Monitor hit rate:** Aim for >30% hit rate over time

## Example Usage

### Scenario: Creating HIV drug charts

**First study guide (Exam 1):**
- Need mnemonic for NRTIs side effects
- Cache miss → WebSearch (~5k tokens)
- Store: `"nrti-adverse-effects-mnemonic": "LACTIC: Lactic Acidosis, Abdominal pain, ..."`

**Second study guide (Exam 2):**
- Need same NRTI mnemonic
- Cache hit → Read from cache (~50 tokens)
- **Saved: ~4,950 tokens**

**Third study guide (Exam 3):**
- Need same NRTI mnemonic
- Cache hit → Read from cache (~50 tokens)
- **Saved: ~4,950 tokens**

**Total savings across 3 study guides: ~9,900 tokens**

## Cache Location

- **Cache file:** `.claude/mnemonic-cache/cache.json`
- **Backup directory:** `.claude/mnemonic-cache/backups/` (created on first backup)
- **This README:** `.claude/mnemonic-cache/README.md`

## Maintenance Schedule

- **Weekly:** Review hit/miss stats
- **Monthly:** Clean expired entries
- **Quarterly:** Review and update outdated mnemonics
- **Per semester:** Backup cache for historical reference
