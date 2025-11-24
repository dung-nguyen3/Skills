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

def export_deck(deck, output_path, media_files=None):
    """
    Export deck to .apkg file.

    Args:
        deck: genanki.Deck with notes added
        output_path: Path for output .apkg file
        media_files: Optional list of media file paths to include
    """
    package = genanki.Package(deck)

    if media_files:
        package.media_files = media_files

    package.write_to_file(output_path)
    print(f"Deck exported to: {output_path}")
    print(f"Total cards: {len(deck.notes)}")


# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def create_flashcard_deck(csv_path, deck_name, output_path):
    """
    Complete workflow to create an Anki deck from CSV.

    Args:
        csv_path: Path to CSV file with Question,Answer columns
        deck_name: Name for the Anki deck
        output_path: Path for output .apkg file

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
    export_deck(deck, output_path)

    return len(notes)


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == '__main__':
    # Example: Create a sample CSV and convert to APKG

    # Sample flashcard data (would normally come from source file analysis)
    sample_cards = [
        ("What is the mechanism of action of NRTIs?",
         "Nucleoside/nucleotide reverse transcriptase inhibitors - competitive inhibition of HIV reverse transcriptase"),

        ("Which NRTI requires dose adjustment in renal impairment?",
         "Tenofovir (TDF)"),

        ("What is the black box warning for Abacavir?",
         "HLA-B*5701 screening required - risk of severe hypersensitivity reaction"),

        ("What are the adverse effects of Zidovudine (AZT)?",
         "Bone marrow suppression, anemia, neutropenia"),

        ("Which NRTIs are associated with lactic acidosis?",
         "Didanosine (ddI) and Stavudine (d4T)"),

        ("What is the preferred NRTI backbone for initial HIV therapy?",
         "Tenofovir + Emtricitabine (TDF/FTC) or TAF/FTC"),

        ("Define INSTI",
         "Integrase strand transfer inhibitor - blocks HIV integrase enzyme"),

        ("Which INSTIs have high barrier to resistance?",
         "Dolutegravir and Bictegravir"),
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
        deck_name='Pharmacology::HIV Drugs',
        output_path=output_path
    )

    print(f"\nCreated {card_count} flashcards")
    print(f"Import '{output_path}' into Anki via File -> Import")

    # Clean up sample CSV (optional)
    # os.remove(csv_path)
