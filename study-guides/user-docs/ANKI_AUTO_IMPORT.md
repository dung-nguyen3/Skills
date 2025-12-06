# Anki Auto-Import Guide

Automatically import generated .apkg files into Anki using AnkiConnect.

---

## Quick Start

### 1. Install AnkiConnect

**In Anki:**
1. Tools → Add-ons → Get Add-ons
2. Enter code: `2055492159`
3. Click OK
4. Restart Anki

### 2. Install Python Requirements

```bash
pip install requests
```

### 3. Enable Auto-Import

Create or edit `.claude/settings.local.json`:

```json
{
  "anki_auto_import": {
    "enabled": true
  }
}
```

### 4. Use the Feature

1. **Keep Anki running**
2. Run `/anki source.txt`
3. Deck auto-imports automatically!

---

## How It Works

**AnkiConnect:**
- Free open-source Anki add-on
- Provides REST API at `http://localhost:8765`
- Allows external programs to interact with Anki

**Auto-Import Process:**
1. Generate .apkg file (always happens)
2. Check if AnkiConnect is available
3. If available → Import via API
4. If not → Show manual import instructions

**Key Benefit:** No more manual File → Import steps!

---

## Configuration

### Settings Location

**User-specific (recommended):**
```
.claude/settings.local.json
```
- Git-ignored (not tracked)
- Your personal preferences

### Configuration Options

```json
{
  "anki_auto_import": {
    "enabled": false,            // Master switch (default: false)
    "show_import_status": true   // Show detailed messages (default: true)
  }
}
```

### Enable Auto-Import

**Option 1: Create new file**
```bash
cat > .claude/settings.local.json << 'EOF'
{
  "anki_auto_import": {
    "enabled": true
  }
}
EOF
```

**Option 2: Edit existing file**
If `.claude/settings.local.json` already exists, add the `anki_auto_import` section to the JSON object.

---

## Requirements

### Software

| Requirement | How to Install | Why Needed |
|-------------|---------------|------------|
| **Anki** | https://apps.ankiweb.net/ | Desktop app for flashcards |
| **AnkiConnect** | Add-on code: `2055492159` | Provides API for auto-import |
| **requests** | `pip install requests` | Python library for HTTP calls |

### Runtime

- ✅ **Anki must be running** (AnkiConnect only works when Anki is open)
- ✅ **AnkiConnect installed and enabled**
- ❌ **No need to close Anki** (unlike direct database approach)

---

## Troubleshooting

### Error: "AnkiConnect not available"

**Full message:**
```
⚠️  Auto-import skipped: AnkiConnect not available
    → Make sure Anki is running
    → Install AnkiConnect add-on (code: 2055492159)
    → Restart Anki after installing
```

**Solutions:**

1. **Start Anki**
   - AnkiConnect only works when Anki is running
   - You'll see Anki's main window open

2. **Install AnkiConnect**
   - In Anki: Tools → Add-ons → Get Add-ons
   - Enter: `2055492159`
   - Restart Anki

3. **Check AnkiConnect is running**
   ```bash
   curl http://localhost:8765
   ```
   Should return: `{"error": "unsupported action", ...}`

4. **Firewall blocking**
   - Some firewalls block localhost connections
   - Add exception for Anki/AnkiConnect

---

### Error: "Import failed: Deck may already exist"

**Full message:**
```
⚠️  Import failed: Deck may already exist or file is invalid
    Check Anki to verify import status
```

**What this means:**
- The .apkg file was created successfully
- AnkiConnect attempted import but received `False`
- This often happens when deck already exists

**Solutions:**

1. **Check Anki**
   - Look for the deck in your collection
   - It may have been imported despite the error

2. **Deck already exists**
   - AnkiConnect will merge/update existing cards
   - This is normal behavior, not a failure

3. **Manual import**
   - If deck didn't import, use: File → Import → Select .apkg

---

### No Error But Deck Not in Anki

**Possible causes:**

1. **Wrong Anki profile**
   - AnkiConnect imports to the currently open profile
   - Switch to the profile you want
   - Re-run `/anki` command

2. **Deck name mismatch**
   - Search for the deck name in Anki
   - It may be in a different location than expected

3. **Import succeeded but not visible**
   - Click "Browse" in Anki
   - Search for cards from the new deck
   - Check deck list (left sidebar)

---

### "Module requests not found"

**Error during execution:**
```python
ModuleNotFoundError: No module named 'requests'
```

**Solution:**
```bash
pip install requests
```

**Verify:**
```bash
python3 -c "import requests; print('OK')"
```

---

## Batch Mode

### How It Works

When using batch mode (multiple files), auto-import:
1. Generates all .apkg files first
2. Imports all decks in sequence via AnkiConnect
3. Shows summary of successes/failures

### Example

```bash
/anki "file1.txt;file2.txt;file3.txt"
```

**Output:**
```
🔄 Batch importing 3 decks via AnkiConnect...
✅ Batch import complete: 3/3 succeeded
```

**With failures:**
```
🔄 Batch importing 3 decks via AnkiConnect...
✅ Batch import complete: 2/3 succeeded
⚠️  Failed imports:
   - file2.apkg: Import returned False
```

### Partial Failures

- Successful imports complete normally
- Failed imports are skipped with error message
- All .apkg files are saved regardless of import status

---

## FAQ

### Q: Is auto-import enabled by default?

**A:** No, it's OFF by default. You must explicitly enable it in `.claude/settings.local.json`.

### Q: Can I use auto-import while Anki is closed?

**A:** No, AnkiConnect requires Anki to be running. If Anki is closed, you'll see the "AnkiConnect not available" message.

### Q: What happens if import fails?

**A:** The .apkg file is still saved. You can import manually via File → Import in Anki.

### Q: Will auto-import overwrite my existing decks?

**A:** Anki's normal import behavior applies:
- New cards are added
- Existing cards are updated (if modified)
- No cards are deleted

### Q: Does this work with AnkiDroid or AnkiMobile?

**A:** Only with Anki Desktop. AnkiConnect is a desktop-only add-on. However, decks sync to AnkiWeb and will appear on mobile after sync.

### Q: Can I temporarily disable auto-import for one command?

**A:** Yes, two options:
1. Set `enabled: false` in settings temporarily
2. The Python script accepts `auto_import=False` parameter (advanced)

### Q: Is AnkiConnect safe?

**A:** Yes, it's a widely-used open-source add-on. It only accepts connections from localhost (your computer) by default.

### Q: What if I have multiple Anki profiles?

**A:** AnkiConnect imports to whichever profile is currently open in Anki. Switch to the desired profile before running `/anki`.

---

## Advanced

### Testing AnkiConnect

Test if AnkiConnect is working:

```bash
curl -X POST http://localhost:8765 -d '{
  "action": "version",
  "version": 6
}'
```

**Expected response:**
```json
{"result": 6, "error": null}
```

### Python Test Script

A test script is available at: `test_ankiconnect.py`

```bash
python3 test_ankiconnect.py
```

This validates:
- AnkiConnect is running
- API is accessible
- Import functionality works

### Manual Import via AnkiConnect

```python
import requests

response = requests.post('http://localhost:8765', json={
    "action": "importPackage",
    "version": 6,
    "params": {
        "path": "/full/path/to/deck.apkg"
    }
})

print(response.json())
```

---

## Comparison: Auto-Import vs Manual

| Aspect | Manual Import | Auto-Import |
|--------|--------------|-------------|
| **Steps** | 1. Generate .apkg<br>2. Open Anki<br>3. File → Import<br>4. Select file<br>5. Click Import | 1. Run `/anki`<br>(Done!) |
| **Time** | ~30 seconds | ~2 seconds |
| **Anki State** | Must be open or closed | Must be running |
| **Setup** | None | Install AnkiConnect |
| **Batch** | Import each file separately | All decks at once |
| **Reliability** | Always works | Requires AnkiConnect |

---

## Related Documentation

- [HOW_TO_USE.md](HOW_TO_USE.md) - General usage guide
- [SLASH_COMMANDS_REFERENCE.md](../SLASH_COMMANDS_REFERENCE.md) - All slash commands
- [AnkiConnect GitHub](https://github.com/FooSoft/anki-connect) - Official add-on repo

---

## Support

**Issue:** Auto-import not working
**First steps:**
1. Check Anki is running
2. Verify AnkiConnect installed: Tools → Add-ons
3. Test connection: `curl http://localhost:8765`
4. Check `.apkg` file was created (it always is)

**Still stuck?**
- Check this guide's Troubleshooting section
- .apkg files are always saved - you can import manually
- AnkiConnect is optional - manual import always works
