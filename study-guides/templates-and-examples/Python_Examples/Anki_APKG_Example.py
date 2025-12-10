"""
Anki APKG Flashcard Generator Example
=====================================

This script demonstrates how to create Anki flashcard decks (.apkg files)
from CSV data using the genanki library.

Requirements:
    pip install genanki

Usage:
    1. Prepare a CSV file with Question,Answer columns
    2. Run this script to generate an .apkg file
    3. Import the .apkg into Anki via File -> Import
"""

import genanki
import csv
import html
import random
import os

# =============================================================================
# CONFIGURATION
# =============================================================================

# Generate unique IDs once and hardcode them for consistent updates
# To generate new IDs: python3 -c "import random; print(random.randrange(1 << 30, 1 << 31))"
MODEL_ID = 1607392319
DECK_ID = 2059400110

# Card styling
CARD_CSS = '''
.card {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 20px;
    text-align: center;
    color: #333;
    background-color: #fafafa;
    padding: 20px;
    line-height: 1.5;
}

.card.night_mode {
    background-color: #2d2d2d;
    color: #e0e0e0;
}

hr#answer {
    border: none;
    border-top: 1px solid #ccc;
    margin: 20px 0;
}

/* Highlight important terms */
b, strong {
    color: #1a73e8;
}

/* Drug names styling */
.drug {
    color: #d93025;
    font-weight: bold;
}

/* Mechanism styling */
.moa {
    color: #188038;
}
'''

# =============================================================================
# MODEL DEFINITION
# =============================================================================

def create_basic_model():
    """
    Create a basic Question/Answer model for Anki.

    Returns:
        genanki.Model: Configured model for flashcards
    """
    return genanki.Model(
        MODEL_ID,
        'Study Guide Flashcard Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div class="question">{{Question}}</div>',
                'afmt': '''
                    <div class="question">{{Question}}</div>
                    <hr id="answer">
                    <div class="answer">{{Answer}}</div>
                ''',
            },
        ],
        css=CARD_CSS
    )


def create_cloze_model():
    """
    Create a cloze deletion model for fill-in-the-blank cards.

    Returns:
        genanki.Model: Configured cloze model
    """
    return genanki.Model(
        MODEL_ID + 1,  # Different ID for cloze model
        'Study Guide Cloze Model',
        model_type=genanki.Model.CLOZE,
        fields=[
            {'name': 'Text'},
            {'name': 'Extra'},
        ],
        templates=[
            {
                'name': 'Cloze',
                'qfmt': '{{cloze:Text}}',
                'afmt': '{{cloze:Text}}<br><br>{{Extra}}',
            },
        ],
        css=CARD_CSS
    )


# =============================================================================
# DECK CREATION
# =============================================================================

def create_deck(deck_name, deck_id=None):
    """
    Create a new Anki deck.

    Args:
        deck_name: Name of the deck (e.g., "Pharmacology::HIV Drugs")
        deck_id: Optional specific deck ID (generates random if None)

    Returns:
        genanki.Deck: Empty deck ready for notes
    """
    if deck_id is None:
        deck_id = random.randrange(1 << 30, 1 << 31)

    return genanki.Deck(deck_id, deck_name)


# =============================================================================
# NOTE CREATION
# =============================================================================

def escape_html(text):
    """
    Escape HTML special characters in text.

    Args:
        text: Raw text that may contain <, >, &, etc.

    Returns:
        str: HTML-escaped text safe for Anki fields
    """
    return html.escape(str(text))


def create_note(model, question, answer):
    """
    Create a single flashcard note.

    Args:
        model: genanki.Model to use
        question: Front of card (question text)
        answer: Back of card (answer text)

    Returns:
        genanki.Note: Note ready to add to deck
    """
    return genanki.Note(
        model=model,
        fields=[escape_html(question), escape_html(answer)]
    )


def load_notes_from_csv(csv_path, model):
    """
    Load flashcard notes from a CSV file.

    CSV format:
        Question,Answer
        "What is X?","Y"
        ...

    Args:
        csv_path: Path to CSV file
        model: genanki.Model to use for notes

    Returns:
        list: List of genanki.Note objects
    """
    notes = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header row

        for row in reader:
            if len(row) >= 2:
                question = row[0].strip()
                answer = row[1].strip()

                if question and answer:  # Skip empty rows
                    note = create_note(model, question, answer)
                    notes.append(note)

    return notes


# =============================================================================
# PACKAGE EXPORT
# =============================================================================

def export_deck(deck, output_path, media_files=None, auto_import=None):
    """
    Export deck to .apkg file.

    Args:
        deck: genanki.Deck with notes added
        output_path: Path for output .apkg file
        media_files: Optional list of media file paths to include
        auto_import: Enable auto-import (None=use config, True=force on, False=force off)
    """
    package = genanki.Package(deck)

    if media_files:
        package.media_files = media_files

    package.write_to_file(output_path)
    print(f"Deck exported to: {output_path}")
    print(f"Total cards: {len(deck.notes)}")

    # Auto-import if enabled
    should_import = auto_import
    if should_import is None:
        settings = load_auto_import_settings()
        should_import = settings.get("enabled", False)

    if should_import:
        auto_import_to_anki(output_path)
    else:
        print("\n💡 To import: Open Anki → File → Import")
        print("   Or enable auto-import in .claude/settings.json")


# =============================================================================
# ANKICONNECT AUTO-IMPORT
# =============================================================================

def invoke_ankiconnect(action, **params):
    """
    Call AnkiConnect API.

    Args:
        action: API action name
        **params: Action parameters

    Returns:
        API result or None on error
    """
    import requests

    payload = {
        "action": action,
        "version": 6,
        "params": params
    }

    try:
        response = requests.post('http://localhost:8765', json=payload, timeout=5)
        response_data = response.json()

        if response_data.get('error'):
            return None

        return response_data.get('result')
    except Exception:
        return None


def is_ankiconnect_available():
    """Check if AnkiConnect is running."""
    try:
        result = invoke_ankiconnect("version")
        return result is not None
    except Exception:
        return False


def load_auto_import_settings():
    """Load auto-import settings from environment variables or config files."""
    import os
    import json
    from pathlib import Path

    # Default settings
    settings = {
        "enabled": False,
        "show_import_status": True
    }

    # Check environment variable first (set in .claude/settings.local.json)
    env_enabled = os.environ.get("ANKI_AUTO_IMPORT")
    if env_enabled is not None:
        settings["enabled"] = env_enabled.lower() in ("true", "1", "yes")
        return settings

    # Fallback: Try loading from config files (legacy approach)
    # Note: This may not work due to Claude Code settings schema validation
    settings_path = Path(__file__).parents[3] / ".claude/settings.json"
    if settings_path.exists():
        try:
            with open(settings_path) as f:
                config = json.load(f)
                if "anki_auto_import" in config:
                    settings.update(config["anki_auto_import"])
        except (json.JSONDecodeError, KeyError):
            pass

    # Override with local settings if exists
    local_settings_path = Path(__file__).parents[3] / ".claude/settings.local.json"
    if local_settings_path.exists():
        try:
            with open(local_settings_path) as f:
                local_config = json.load(f)
                if "anki_auto_import" in local_config:
                    settings.update(local_config["anki_auto_import"])
        except (json.JSONDecodeError, KeyError):
            pass

    return settings


def auto_import_to_anki(apkg_path):
    """
    Import .apkg file into Anki using AnkiConnect.

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Check if AnkiConnect is available
        if not is_ankiconnect_available():
            print("  ⚠️  Auto-import skipped: AnkiConnect not available")
            print("     → Make sure Anki is running")
            print("     → Install AnkiConnect add-on (code: 2055492159)")
            print("     → Restart Anki after installing")
            return False

        print(f"  🔄 Importing deck into Anki via AnkiConnect...")

        # Import the package
        result = invoke_ankiconnect("importPackage", path=str(apkg_path))

        if result is False:
            print(f"  ⚠️  Import failed: Deck may already exist or file is invalid")
            print(f"     Check Anki to verify import status")
            return False

        print(f"  ✅ Successfully imported into Anki!")
        return True

    except Exception as e:
        print(f"  ⚠️  Auto-import failed: {e}")
        print(f"     Import manually via Anki → File → Import")
        return False


def batch_import_to_anki(apkg_paths):
    """
    Import multiple .apkg files using AnkiConnect.

    Returns:
        dict: {'success': [...], 'failed': [...]}
    """
    results = {'success': [], 'failed': []}

    try:
        if not is_ankiconnect_available():
            print("  ⚠️  Batch auto-import skipped: AnkiConnect not available")
            print("     Make sure Anki is running with AnkiConnect installed")
            return results

        print(f"  🔄 Batch importing {len(apkg_paths)} decks via AnkiConnect...")

        for apkg_path in apkg_paths:
            try:
                result = invoke_ankiconnect("importPackage", path=str(apkg_path))

                if result is not False:
                    results['success'].append(apkg_path)
                else:
                    results['failed'].append((apkg_path, "Import returned False"))

            except Exception as e:
                results['failed'].append((apkg_path, str(e)))

        # Print summary
        print(f"  ✅ Batch import complete: {len(results['success'])}/{len(apkg_paths)} succeeded")
        if results['failed']:
            print(f"  ⚠️  Failed imports:")
            for path, error in results['failed']:
                print(f"     - {os.path.basename(path)}: {error}")

        return results

    except Exception as e:
        print(f"  ⚠️  Batch auto-import failed: {e}")
        return results


# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def create_flashcard_deck(csv_path, deck_name, output_path, auto_import=None):
    """
    Complete workflow to create an Anki deck from CSV.

    Args:
        csv_path: Path to CSV file with Question,Answer columns
        deck_name: Name for the Anki deck
        output_path: Path for output .apkg file
        auto_import: Enable auto-import (None=use config, True/False=override)

    Returns:
        int: Number of cards created
    """
    # Create model and deck
    model = create_basic_model()
    deck = create_deck(deck_name)

    # Load notes from CSV
    notes = load_notes_from_csv(csv_path, model)

    # Add notes to deck
    for note in notes:
        deck.add_note(note)

    # Export to .apkg
    export_deck(deck, output_path, auto_import=auto_import)

    return len(notes)


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == '__main__':
    # Example: Create a sample CSV and convert to APKG

    # =============================================================================
    # FLASHCARD DATA - CARD DIRECTION GUIDE
    # =============================================================================
    #
    # REVERSE CARDS (Definition/Features → Term):
    #   Use for: Drug names, diagnostic tools, anatomical structures, diseases
    #   Format: ("What [category] has [characteristics]?", "[Term]")
    #
    #   Examples:
    #     ("What diagnostic tool measures duration, phase, frequency of heart sounds?",
    #      "Phonocardiography"),
    #     ("Which NRTI requires dose adjustment in renal impairment?",
    #      "Tenofovir (TDF)"),
    #
    # FORWARD CARDS (Term/Context → Mechanism/Process):
    #   Use for: Mechanisms, treatments, side effects, pathophysiology
    #   Format: ("How/What/When does [term] [action]?", "[Result/mechanism]")
    #
    #   Examples:
    #     ("How does atropine affect presynaptic M2 receptors?",
    #      "Blocked → ↑NE release → ↑β1 stimulation → ↑HR"),
    #     ("What are the adverse effects of NRTIs?",
    #      "Lactic acidosis, hepatic steatosis, lipodystrophy"),
    #
    # ANSWER FORMATTING - Line Breaks for Multiple Items:
    #   When answers contain multiple items (steps, symptoms, treatments), use line breaks.
    #
    #   ✓ CORRECT:
    #     ("What are the symptoms of heart failure?",
    #      "Dyspnea\nOrthopnea\nParoxysmal nocturnal dyspnea\nPeripheral edema\nFatigue"),
    #
    #     ("How is acute hyperkalemia treated?",
    #      "1. IV Calcium (membrane stabilization)\n2. Insulin + D50W (shift K+ intracellularly)\n3. Albuterol nebulizer\n4. Sodium bicarbonate (if acidotic)\n5. Dialysis (if refractory)"),
    #
    #   ✗ WRONG (comma-separated):
    #     ("What are the symptoms of heart failure?",
    #      "Dyspnea, orthopnea, paroxysmal nocturnal dyspnea, peripheral edema, fatigue"),
    #
    # COMPARISON CARDS (Item A vs Item B):
    #   Use when testing differentiation/contrast between related items.
    #   Format: ("Item A vs Item B: [Category]", "Item A:\n- Char 1\n\nItem B:\n- Char 1")
    #
    #   When to use:
    #     - Source has explicit comparisons ("X vs Y", "compared to", "differentiate")
    #     - Contrasting related items with different characteristics
    #     - Distinguishing between similar concepts
    #
    #   ✓ CORRECT (focused per category):
    #     ("Right heart failure vs left heart failure: Clinical presentation",
    #      "Right heart failure:\nPeripheral edema\nJugular venous distension\nHepatomegaly\nAscites\n\nLeft heart failure:\nDyspnea\nOrthopnea\nParoxysmal nocturnal dyspnea\nPulmonary crackles"),
    #
    #     ("Type I vs Type II hypersensitivity: Mechanism",
    #      "Type I:\nIgE-mediated\nMast cell degranulation\nImmediate reaction\n\nType II:\nIgG/IgM-mediated\nComplement activation\nCytotoxic reaction"),
    #
    #   Default to atomic cards - only use comparison format when differentiation is tested.
    #
    # =============================================================================

    # Sample flashcard data (would normally come from source file analysis)
    sample_cards = [
        # REVERSE CARDS (Features → Term)
        ("What is the mechanism of action of NRTIs?",
         "Nucleoside/nucleotide reverse transcriptase inhibitors"),

        ("Which NRTI requires dose adjustment in renal impairment?",
         "Tenofovir (TDF)"),

        ("What drug class inhibits HIV protease enzyme?",
         "Protease Inhibitors (PIs)"),

        # FORWARD CARDS (Term → Mechanism)
        ("How do NRTIs work?",
         "Competitive inhibition of HIV reverse transcriptase"),

        # FORWARD CARDS with line breaks for multiple items
        ("What are the adverse effects of Tenofovir?",
         "Renal toxicity\nDecreased bone density\nFanconi syndrome"),

        ("What are the symptoms of lactic acidosis from NRTIs?",
         "Nausea\nVomiting\nAbdominal pain\nFatigue\nHypotension"),

        ("When should Abacavir be avoided?",
         "Patients with HLA-B*5701 allele (hypersensitivity risk)"),
    ]

    # Create sample CSV
    csv_path = 'sample_flashcards.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Question', 'Answer'])
        writer.writerows(sample_cards)

    # Generate APKG
    output_path = 'HIV_Drugs_Flashcards.apkg'
    card_count = create_flashcard_deck(
        csv_path=csv_path,
        deck_name='Pharmacology::11 HIV Drugs',  # Include lecture number from filename
        output_path=output_path
    )

    print(f"\nCreated {card_count} flashcards")
    print(f"Import '{output_path}' into Anki via File -> Import")

    # Clean up sample CSV (optional)
    # os.remove(csv_path)
