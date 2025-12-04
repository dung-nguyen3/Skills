#!/usr/bin/env python3
"""
COMPLETE EXCEL DRUG CHART EXAMPLE
Reference implementation for creating comprehensive 4-tab drug charts

This file shows a COMPLETE working example with all 4 tabs.
Templates should reference this file rather than including all code inline.

Structure:
- Tab 1: Drug Details (comparison tables by drug class)
- Tab 2: Key Comparisons (mechanisms, toxicities, uses)
- Tab 3: Master Chart (all drugs in one table)
- Tab 4: High-Yield & Pearls (clinical pearls, mnemonics)
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# =============================================================================
# COLOR SCHEME (See Excel_Color_Reference.txt for details)
# =============================================================================

HEADER_BG = '4472C4'  # Dark blue
ROW_COLORS = [
    'D9E2F3',  # Ice Blue
    'C8E6C9',  # Seafoam
    'D1C4E9',  # Light Orchid
    'F7E7CE',  # Champagne
    'BDD7EE',  # Sky Blue
    'F0F8FF',  # Pale Azure
    'FCE4EC',  # Blush Pink
    'EDE7F6',  # Soft Lilac
    'FFE8D6',  # Soft Tangerine
    'BBDEFB',  # Powder Blue
]

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def apply_cell_style(cell, text='', bold=False, font_size=10, bg_color=None,
                     border=True, alignment='left', wrap=True):
    """Apply comprehensive cell styling"""
    cell.value = text
    cell.font = Font(name='Calibri', size=font_size, bold=bold, color='000000')
    cell.alignment = Alignment(
        horizontal=alignment,
        vertical='top',
        wrap_text=wrap
    )

    if bg_color:
        cell.fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type='solid')

    if border:
        cell.border = Border(
            left=Side(style='thin', color='FFFFFF'),
            right=Side(style='thin', color='FFFFFF'),
            top=Side(style='thin', color='FFFFFF'),
            bottom=Side(style='thin', color='FFFFFF')
        )

def create_header_row(ws, headers, row=1):
    """Create formatted header row"""
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row, col_idx)
        apply_cell_style(
            cell, text=header, bold=True, font_size=12,
            bg_color=HEADER_BG, alignment='center'
        )
        cell.font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')

    ws.row_dimensions[row].height = 25
    ws.freeze_panes = f'A{row+1}'

def set_column_widths(ws, widths):
    """Set column widths from dictionary"""
    for col_letter, width in widths.items():
        ws.column_dimensions[col_letter].width = width

def add_mnemonic_row(ws, row, mnemonic_text, color, span_cols=10):
    """Add memory tricks row after drug class table"""
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span_cols)
    cell = ws.cell(row, 1)
    apply_cell_style(
        cell,
        text=f"💡 MEMORY TRICKS: {mnemonic_text}",
        bold=True,
        font_size=10,
        bg_color='FFF3E0',  # Orange background
        alignment='left'
    )
    ws.row_dimensions[row].height = 40

# =============================================================================
# TAB 1: DRUG DETAILS
# =============================================================================

def create_drug_details_tab(wb):
    """
    Tab 1: Drug Details
    - Drug class comparison tables
    - Drugs as columns, properties as rows
    - Merged cells for shared class properties
    - Memory tricks row after each class
    """
    ws = wb.active
    ws.title = "Drug Details"

    # Column widths
    set_column_widths(ws, {
        'A': 30,  # Property name
        'B': 25,  # Drug 1
        'C': 25,  # Drug 2
        'D': 25,  # Drug 3
        'E': 25,  # Drug 4
        'F': 25,  # Drug 5
        'G': 40,  # Analogy column
    })

    current_row = 1
    class_index = 0

    # =========================================================================
    # EXAMPLE: NRTI Drug Class
    # =========================================================================

    # Class header
    ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=7)
    cell = ws.cell(current_row, 1)
    apply_cell_style(cell, text="NUCLEOSIDE REVERSE TRANSCRIPTASE INHIBITORS (NRTIs)",
                    bold=True, font_size=14, bg_color=HEADER_BG, alignment='center')
    cell.font = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
    ws.row_dimensions[current_row].height = 30
    current_row += 1

    # Drug names header
    color = ROW_COLORS[class_index % len(ROW_COLORS)]
    headers = ['Property', 'Tenofovir (Viread)', 'Emtricitabine (Emtriva)',
               'Lamivudine (Epivir)', 'Abacavir (Ziagen)', 'Analogy']
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(current_row, col_idx)
        apply_cell_style(cell, text=header, bold=True, font_size=11,
                        bg_color=color, alignment='center')
    ws.row_dimensions[current_row].height = 25
    current_row += 1

    # Class-wide properties (merged across all drugs)
    class_properties = [
        ('Drug Class', 'NRTI - Nucleoside Reverse Transcriptase Inhibitor'),
        ('Mechanism', 'Competes with natural nucleosides → incorporated into viral DNA → chain termination'),
        ('Route', 'Oral'),
    ]

    for prop_name, prop_value in class_properties:
        # Property name in column A
        cell_a = ws.cell(current_row, 1)
        apply_cell_style(cell_a, text=prop_name, bold=True, bg_color=color)

        # Merge columns B-E for shared value
        ws.merge_cells(start_row=current_row, start_column=2,
                      end_row=current_row, end_column=5)
        cell_value = ws.cell(current_row, 2)
        apply_cell_style(cell_value, text=prop_value, bg_color='FFFFFF')

        # Analogy column (only for mechanism row)
        cell_g = ws.cell(current_row, 6)
        if prop_name == 'Mechanism':
            analogy = "Like giving a construction crew fake bricks (nucleosides). They build them into the wall (DNA chain), but the fake bricks are defective and the wall collapses."
            apply_cell_style(cell_g, text=analogy, bg_color='FFE8D6', font_size=10)
        else:
            apply_cell_style(cell_g, text='', bg_color='FFFFFF')

        current_row += 1

    # Drug-specific properties (individual values per drug)
    drug_properties = [
        ('Uses',
         '🟢 HIV - First line',
         '🟢 HIV - First line',
         'HIV, HBV',
         'HIV (HLA-B*5701 negative)',
         ''),
        ('Major Adverse Effects',
         '⚠️ Nephrotoxicity, ↓ bone density',
         'Minimal (well tolerated)',
         'Minimal (well tolerated)',
         '⚠️ Hypersensitivity reaction',
         ''),
        ('Contraindications',
         'CrCl <50 mL/min',
         'None',
         'None',
         'HLA-B*5701 positive',
         ''),
        ('Special Considerations',
         'Monitor renal function',
         'Safe in pregnancy',
         'Safe in pregnancy, HBV coinfection',
         '❗ Screen HLA-B*5701 BEFORE use',
         ''),
    ]

    for prop_row in drug_properties:
        prop_name = prop_row[0]

        # Property name
        cell_a = ws.cell(current_row, 1)
        apply_cell_style(cell_a, text=prop_name, bold=True, bg_color=color)

        # Individual drug values
        for col_idx, value in enumerate(prop_row[1:], start=2):
            cell = ws.cell(current_row, col_idx)
            apply_cell_style(cell, text=value, bg_color='FFFFFF')

        current_row += 1

    # Memory tricks row
    add_mnemonic_row(
        ws, current_row,
        '"NRTI = Nucleoside Rival Terminating Infection" - Competes with real nucleosides to terminate viral DNA',
        color,
        span_cols=6
    )
    current_row += 2  # Space before next class
    class_index += 1

    # =========================================================================
    # Add more drug classes here following same pattern...
    # =========================================================================

    return ws

# =============================================================================
# TAB 2: KEY COMPARISONS
# =============================================================================

def create_key_comparisons_tab(wb):
    """
    Tab 2: Key Comparisons
    - Side-by-side comparisons across drug classes
    - Mechanisms, toxicities, uses, interactions
    """
    ws = wb.create_sheet("Key Comparisons")

    # Column widths
    set_column_widths(ws, {
        'A': 30,
        'B': 35,
        'C': 35,
        'D': 35,
        'E': 35,
    })

    current_row = 1

    # Comparison 1: Mechanisms Across Classes
    create_header_row(ws, ['Drug Class', 'Mechanism', 'Target', 'Result', 'Analogy'], current_row)
    current_row += 1

    comparison_data = [
        ('NRTI', 'Nucleoside analog → chain termination', 'Reverse transcriptase',
         'Viral DNA synthesis stops', 'Fake bricks in a wall'),
        ('NNRTI', 'Allosteric binding', 'Reverse transcriptase',
         'Enzyme cannot function', 'Jamming the gears of a machine'),
        ('Integrase Inhibitor', 'Blocks integration', 'Integrase enzyme',
         'Viral DNA cannot insert into host', 'Blocking the stapler'),
        ('Protease Inhibitor', 'Competitive inhibition', 'HIV protease',
         'Immature non-infectious virions', 'Assembly line shut down'),
    ]

    for idx, row_data in enumerate(comparison_data):
        color = ROW_COLORS[idx % len(ROW_COLORS)]
        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(current_row, col_idx)
            bold = (col_idx == 1)  # First column bold
            apply_cell_style(cell, text=value, bold=bold, bg_color=color)
        current_row += 1

    current_row += 2  # Space before next comparison

    # Add more comparisons (toxicity, uses, interactions) here...

    return ws

# =============================================================================
# TAB 3: MASTER CHART
# =============================================================================

def create_master_chart_tab(wb):
    """
    Tab 3: Master Chart
    - ALL drugs in one comprehensive table
    - Rows = individual drugs
    - Frozen header for scrolling
    """
    ws = wb.create_sheet("Master Chart")

    # Column widths
    set_column_widths(ws, {
        'A': 20,  # Drug Class
        'B': 25,  # Drug Name
        'C': 15,  # Route
        'D': 35,  # Mechanism
        'E': 35,  # Uses
        'F': 35,  # Adverse Effects
        'G': 30,  # Contraindications
        'H': 30,  # Special Considerations
    })

    # Headers
    headers = ['Drug Class', 'Drug Name (Brand)', 'Route', 'Mechanism',
               'Uses', 'Adverse Effects', 'Contraindications', 'Special Considerations']
    create_header_row(ws, headers, 1)

    # Master chart data (ALL drugs from ALL classes)
    master_data = [
        ('NRTI', 'Tenofovir (Viread)', 'Oral', 'Nucleoside analog → chain termination',
         '🟢 HIV - First line', '⚠️ Nephrotoxicity, ↓ bone density',
         'CrCl <50 mL/min', 'Monitor renal function'),
        ('NRTI', 'Emtricitabine (Emtriva)', 'Oral', 'Nucleoside analog → chain termination',
         '🟢 HIV - First line', 'Minimal', 'None', 'Safe in pregnancy'),
        ('NRTI', 'Lamivudine (Epivir)', 'Oral', 'Nucleoside analog → chain termination',
         'HIV, HBV', 'Minimal', 'None', 'HBV coinfection'),
        ('NRTI', 'Abacavir (Ziagen)', 'Oral', 'Nucleoside analog → chain termination',
         'HIV', '⚠️ Hypersensitivity reaction', 'HLA-B*5701 positive',
         '❗ Screen HLA-B*5701 BEFORE use'),
        # Add all other drugs here...
    ]

    current_row = 2
    class_index = 0
    prev_class = None

    for row_data in master_data:
        drug_class = row_data[0]

        # Change color when class changes
        if drug_class != prev_class:
            class_index += 1
            prev_class = drug_class

        color = ROW_COLORS[class_index % len(ROW_COLORS)]

        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(current_row, col_idx)
            bold = (col_idx == 1)  # Drug class column bold
            apply_cell_style(cell, text=value, bold=bold, bg_color=color)

        current_row += 1

    return ws

# =============================================================================
# TAB 4: HIGH-YIELD & PEARLS
# =============================================================================

def create_high_yield_tab(wb):
    """
    Tab 4: High-Yield & Pearls
    - Clinical pearls
    - Mnemonics
    - "If X Think Y" associations
    - Must-know facts
    """
    ws = wb.create_sheet("High-Yield & Pearls")

    # Column widths
    set_column_widths(ws, {
        'A': 100,  # Full width for content
    })

    current_row = 1

    # Section 1: Clinical Pearls
    ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=1)
    cell = ws.cell(current_row, 1)
    apply_cell_style(cell, text="CLINICAL PEARLS", bold=True, font_size=14,
                    bg_color=HEADER_BG, alignment='center')
    cell.font = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
    current_row += 1

    pearls = [
        "• All NRTIs require activation by host kinases - if kinase activity is low, drug may not work",
        "• Tenofovir + Emtricitabine = most common first-line NRTI backbone",
        "• Abacavir hypersensitivity is life-threatening - NEVER rechallenge if reaction occurs",
        "• NRTI class effect: lactic acidosis and hepatic steatosis (rare but serious)",
    ]

    for pearl in pearls:
        cell = ws.cell(current_row, 1)
        apply_cell_style(cell, text=pearl, bg_color='E0F2F1')
        ws.row_dimensions[current_row].height = 30
        current_row += 1

    current_row += 2

    # Section 2: Mnemonics
    ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=1)
    cell = ws.cell(current_row, 1)
    apply_cell_style(cell, text="MEMORY TRICKS & MNEMONICS", bold=True, font_size=14,
                    bg_color=HEADER_BG, alignment='center')
    cell.font = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
    current_row += 1

    mnemonics = [
        '💡 "NRTI = Nucleoside Rival Terminating Infection"',
        '💡 "Tenofovir = Tender kidneys" (nephrotoxicity)',
        '💡 "Abacavir needs All-Clear Before using" (HLA-B*5701 screening)',
    ]

    for mnemonic in mnemonics:
        cell = ws.cell(current_row, 1)
        apply_cell_style(cell, text=mnemonic, bg_color='FFF3E0')
        ws.row_dimensions[current_row].height = 30
        current_row += 1

    current_row += 2

    # Section 3: If X Think Y
    ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=1)
    cell = ws.cell(current_row, 1)
    apply_cell_style(cell, text='"IF X THINK Y" ASSOCIATIONS', bold=True, font_size=14,
                    bg_color=HEADER_BG, alignment='center')
    cell.font = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
    current_row += 1

    associations = [
        "If HIV-naïve patient → Think: Tenofovir + Emtricitabine + Integrase Inhibitor",
        "If hypersensitivity reaction on HIV meds → Think: Abacavir (check HLA-B*5701)",
        "If rising creatinine on HIV meds → Think: Tenofovir nephrotoxicity",
    ]

    for assoc in associations:
        cell = ws.cell(current_row, 1)
        apply_cell_style(cell, text=assoc, bg_color='F3E5F5')
        ws.row_dimensions[current_row].height = 30
        current_row += 1

    return ws

# =============================================================================
# MAIN FUNCTION
# =============================================================================

def create_drug_chart(output_path):
    """
    Create complete 4-tab drug chart

    Args:
        output_path: Path to save the Excel file
    """
    # Create workbook
    wb = Workbook()

    # Create all tabs
    create_drug_details_tab(wb)
    create_key_comparisons_tab(wb)
    create_master_chart_tab(wb)
    create_high_yield_tab(wb)

    # Save
    wb.save(output_path)
    print(f"✅ Drug chart created: {output_path}")

if __name__ == '__main__':
    # Example usage
    create_drug_chart('HIV_Drugs_Chart.xlsx')
