#!/usr/bin/env python3
"""
Mnemonic Cache Helper

Provides functions for caching researched medical mnemonics to avoid
redundant WebSearch operations.

Token efficiency: ~5k tokens saved per cache hit
"""

import json
import time
from pathlib import Path
from typing import Optional, Dict, List
import hashlib

CACHE_FILE = Path(__file__).parent / "cache.json"
TTL_DAYS = 90  # Default time-to-live in days


def _load_cache() -> Dict:
    """Load cache from JSON file."""
    if not CACHE_FILE.exists():
        return {
            "version": "1.0",
            "entries": [],
            "stats": {
                "total_hits": 0,
                "total_misses": 0,
                "total_entries": 0,
                "token_savings": 0
            }
        }

    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def _save_cache(cache: Dict) -> None:
    """Save cache to JSON file."""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def _generate_key(topic: str, category: str) -> str:
    """Generate normalized cache key."""
    # Normalize: lowercase, remove spaces, hyphens
    topic_norm = topic.lower().replace(" ", "-").replace("_", "-")
    category_norm = category.lower().replace(" ", "-").replace("_", "-")
    return f"{topic_norm}-{category_norm}-mnemonic"


def _is_expired(entry: Dict) -> bool:
    """Check if cache entry has expired."""
    created_at = entry.get("created_at", 0)
    ttl_days = entry.get("ttl_days", TTL_DAYS)
    ttl_seconds = ttl_days * 24 * 60 * 60

    current_time = int(time.time())
    return (current_time - created_at) > ttl_seconds


def lookup(topic: str, category: str = "general") -> Optional[str]:
    """
    Lookup mnemonic in cache.

    Args:
        topic: Medical topic (e.g., "beta-blockers", "HIV antivirals")
        category: Mnemonic category (e.g., "adverse-effects", "mechanism", "general")

    Returns:
        Cached mnemonic value if found and not expired, None otherwise

    Example:
        >>> mnemonic = lookup("beta-blockers", "adverse-effects")
        >>> if mnemonic:
        >>>     print(f"Cache hit: {mnemonic}")
        >>> else:
        >>>     print("Cache miss - need to WebSearch")
    """
    cache = _load_cache()
    key = _generate_key(topic, category)

    # Find entry
    for entry in cache["entries"]:
        if entry["key"] == key:
            # Check if expired
            if _is_expired(entry):
                print(f"⏰ Cache entry expired: {key}")
                return None

            # Update stats
            cache["stats"]["total_hits"] += 1
            cache["stats"]["token_savings"] += 4950  # ~5k tokens saved
            entry["hit_count"] = entry.get("hit_count", 0) + 1
            entry["last_accessed"] = int(time.time())

            _save_cache(cache)

            print(f"✓ Cache hit: {key} (hit count: {entry['hit_count']})")
            print(f"💰 Token savings: ~{cache['stats']['token_savings']:,} tokens total")
            return entry["value"]

    # Cache miss
    cache["stats"]["total_misses"] += 1
    _save_cache(cache)

    print(f"✗ Cache miss: {key} - WebSearch required")
    return None


def store(
    topic: str,
    category: str,
    mnemonic: str,
    source_url: str = "",
    tags: List[str] = None,
    ttl_days: int = TTL_DAYS
) -> None:
    """
    Store mnemonic in cache.

    Args:
        topic: Medical topic
        category: Mnemonic category
        mnemonic: The mnemonic text
        source_url: URL where mnemonic was found
        tags: Optional tags for categorization
        ttl_days: Time-to-live in days (default: 90)

    Example:
        >>> store(
        >>>     topic="beta-blockers",
        >>>     category="adverse-effects",
        >>>     mnemonic="BASH: Bradycardia, Asthma, Shock, Heart block",
        >>>     source_url="https://www.medschoolbootcamp.com/mnemonics",
        >>>     tags=["pharmacology", "cardiovascular"]
        >>> )
    """
    cache = _load_cache()
    key = _generate_key(topic, category)

    # Check if entry already exists
    for i, entry in enumerate(cache["entries"]):
        if entry["key"] == key:
            # Update existing entry
            cache["entries"][i] = {
                "key": key,
                "value": mnemonic,
                "source_url": source_url,
                "topic": topic,
                "category": category,
                "created_at": entry.get("created_at", int(time.time())),
                "last_accessed": int(time.time()),
                "ttl_days": ttl_days,
                "hit_count": entry.get("hit_count", 0),
                "tags": tags or []
            }
            _save_cache(cache)
            print(f"♻️  Updated cache entry: {key}")
            return

    # Create new entry
    entry = {
        "key": key,
        "value": mnemonic,
        "source_url": source_url,
        "topic": topic,
        "category": category,
        "created_at": int(time.time()),
        "last_accessed": int(time.time()),
        "ttl_days": ttl_days,
        "hit_count": 0,
        "tags": tags or []
    }

    cache["entries"].append(entry)
    cache["stats"]["total_entries"] = len(cache["entries"])
    _save_cache(cache)

    print(f"✓ Stored in cache: {key}")
    print(f"📊 Total entries: {cache['stats']['total_entries']}")


def clean_expired() -> int:
    """
    Remove expired entries from cache.

    Returns:
        Number of entries removed
    """
    cache = _load_cache()
    original_count = len(cache["entries"])

    # Filter out expired entries
    cache["entries"] = [
        entry for entry in cache["entries"]
        if not _is_expired(entry)
    ]

    removed_count = original_count - len(cache["entries"])
    cache["stats"]["total_entries"] = len(cache["entries"])

    _save_cache(cache)

    print(f"🧹 Cleaned {removed_count} expired entries")
    print(f"📊 Remaining entries: {cache['stats']['total_entries']}")

    return removed_count


def get_stats() -> Dict:
    """
    Get cache statistics.

    Returns:
        Dictionary with cache stats
    """
    cache = _load_cache()
    stats = cache["stats"].copy()

    total_requests = stats["total_hits"] + stats["total_misses"]
    if total_requests > 0:
        stats["hit_rate"] = round((stats["total_hits"] / total_requests) * 100, 1)
    else:
        stats["hit_rate"] = 0.0

    return stats


def list_entries(topic_filter: str = None) -> List[Dict]:
    """
    List cache entries, optionally filtered by topic.

    Args:
        topic_filter: Optional topic string to filter by

    Returns:
        List of cache entries
    """
    cache = _load_cache()
    entries = cache["entries"]

    if topic_filter:
        topic_lower = topic_filter.lower()
        entries = [
            e for e in entries
            if topic_lower in e.get("topic", "").lower() or topic_lower in e.get("key", "").lower()
        ]

    return entries


def print_stats() -> None:
    """Print formatted cache statistics."""
    stats = get_stats()

    print("\n" + "="*50)
    print("MNEMONIC CACHE STATISTICS")
    print("="*50)
    print(f"Total entries:    {stats['total_entries']}")
    print(f"Cache hits:       {stats['total_hits']}")
    print(f"Cache misses:     {stats['total_misses']}")
    print(f"Hit rate:         {stats['hit_rate']}%")
    print(f"Token savings:    ~{stats['token_savings']:,} tokens")
    print("="*50 + "\n")


# CLI interface
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python mnemonic_cache_helper.py lookup <topic> <category>")
        print("  python mnemonic_cache_helper.py store <topic> <category> <mnemonic> [source_url]")
        print("  python mnemonic_cache_helper.py clean")
        print("  python mnemonic_cache_helper.py stats")
        print("  python mnemonic_cache_helper.py list [topic_filter]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "lookup":
        if len(sys.argv) < 4:
            print("Usage: lookup <topic> <category>")
            sys.exit(1)
        topic, category = sys.argv[2], sys.argv[3]
        result = lookup(topic, category)
        if result:
            print(f"\nMnemonic: {result}\n")

    elif command == "store":
        if len(sys.argv) < 5:
            print("Usage: store <topic> <category> <mnemonic> [source_url]")
            sys.exit(1)
        topic, category, mnemonic = sys.argv[2], sys.argv[3], sys.argv[4]
        source_url = sys.argv[5] if len(sys.argv) > 5 else ""
        store(topic, category, mnemonic, source_url)

    elif command == "clean":
        clean_expired()

    elif command == "stats":
        print_stats()

    elif command == "list":
        topic_filter = sys.argv[2] if len(sys.argv) > 2 else None
        entries = list_entries(topic_filter)
        print(f"\nFound {len(entries)} entries:\n")
        for entry in entries:
            print(f"  • {entry['key']}")
            print(f"    Value: {entry['value'][:80]}...")
            print(f"    Hits: {entry.get('hit_count', 0)}")
            print()

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
