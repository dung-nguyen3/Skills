#!/usr/bin/env python3
"""
COMPLETE EXCEL COMPARISON CHART EXAMPLE
Reference implementation for creating comprehensive 3-tab comparison charts

This file shows a COMPLETE working example with all 3 tabs.
Use for ANY medical topic comparisons (conditions, mechanisms, concepts).

Structure:
- Tab 1: Key Comparisons (multiple side-by-side tables, one category per table)
- Tab 2: Master Chart (all items in one comprehensive table)
- Tab 3: Summary (mnemonics, "If X Think Y", high-yield pearls)

Category Selection:
Categories are selected from comprehensive menus (A-M) in the template based on
learning objectives. This example uses Menu B (Medical Conditions) categories:
- Mechanism comparison (Table 1)
- Clinical presentation comparison (Table 2)
- Treatment comparison (Table 3)

Categories are flexible - use menus in Excel_Comparison_Chart_REVISED.txt to
select relevant categories for any medical topic (diagnostic tools, drugs,
conditions, mechanisms, anatomy, procedures, etc.).

Example: Hypersensitivity Reactions Type I-IV
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# =============================================================================
# COLOR SCHEME (See Excel_Color_Reference.txt for details)
# =============================================================================

# Two-shade system: Each color has HEADER (25% darker) and MAIN (lighter) variants
# - HEADER shade: Table title rows, column headers
# - MAIN shade: Data rows

MAIN_TITLE_BG = '4472C4'  # Dark blue - ONLY for sheet titles
MNEMONIC_BG = 'E6F3FF'    # Light blue for mnemonics
CLINICAL_PEARL_BG = 'E8F5E9'  # Light green for clinical pearls

# HEADER_COLORS: 25% darker shades for table titles and column headers
HEADER_COLORS = [
    'B4C6E7',  # Ice Blue HEADER
    'A8CCA8',  # Seafoam HEADER
    'B8A4D0',  # Light Orchid HEADER
    'E0D0B0',  # Champagne HEADER
    '9DC3E6',  # Sky Blue HEADER
    'D0E8FF',  # Pale Azure HEADER
    'E8C4CC',  # Blush Pink HEADER
    'D0C8DC',  # Soft Lilac HEADER
    'E0C8B0',  # Soft Tangerine HEADER
    'A0C4E8',  # Powder Blue HEADER
]

# MAIN_COLORS: Lighter shades for data rows
MAIN_COLORS = [
    'D9E2F3',  # Ice Blue MAIN
    'C8E6C9',  # Seafoam MAIN
    'D1C4E9',  # Light Orchid MAIN
    'F7E7CE',  # Champagne MAIN
    'BDD7EE',  # Sky Blue MAIN
    'F0F8FF',  # Pale Azure MAIN
    'FCE4EC',  # Blush Pink MAIN
    'EDE7F6',  # Soft Lilac MAIN
    'FFE8D6',  # Soft Tangerine MAIN
    'BBDEFB',  # Powder Blue MAIN
]

# COLOR RULE: Same table/category = same color set
# - Table title row: HEADER_COLORS[index]
# - Column headers: HEADER_COLORS[index]
# - Data rows: MAIN_COLORS[index]
# Rotate to next color SET only when starting a NEW table/category

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def apply_cell_style(cell, text='', bold=False, font_size=11, bg_color=None,
                     border=True, alignment='left', wrap=True, font_color='000000'):
    """Apply comprehensive cell styling"""
    cell.value = text
    cell.font = Font(name='Calibri', size=font_size, bold=bold, color=font_color)
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

def create_comparison_header(ws, title, row, span_cols=5, table_index=0):
    """Create merged title row for a comparison table

    Args:
        table_index: Index for color selection (uses HEADER_COLORS[table_index])
    """
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span_cols)
    cell = ws.cell(row, 1)
    header_color = HEADER_COLORS[table_index % len(HEADER_COLORS)]
    apply_cell_style(cell, text=title, bold=True, font_size=14,
                    bg_color=header_color, alignment='center', font_color='000000')
    cell.font = Font(name='Calibri', size=14, bold=True, color='000000')
    ws.row_dimensions[row].height = 30

def create_column_headers(ws, headers, row, start_col=1, table_index=0):
    """Create column headers for comparison table

    Args:
        table_index: Index for color selection (uses HEADER_COLORS[table_index])
    """
    header_color = HEADER_COLORS[table_index % len(HEADER_COLORS)]
    for col_idx, header in enumerate(headers, start=start_col):
        cell = ws.cell(row, col_idx)
        apply_cell_style(cell, text=header, bold=True, font_size=11,
                        bg_color=header_color, alignment='center', font_color='000000')
    ws.row_dimensions[row].height = 25

def create_master_header_row(ws, headers, row=1):
    """Create formatted header row with freeze for Master Chart

    Uses dark blue (#4472C4) with white text - NOT the two-shade system.
    Master Chart header is always dark blue, data rows use MAIN_COLORS.
    """
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row, col_idx)
        apply_cell_style(
            cell, text=header, bold=True, font_size=12,
            bg_color=MAIN_TITLE_BG, alignment='center', font_color='FFFFFF'
        )
        cell.font = Font(name='Calibri', size=12, bold=True, color='FFFFFF')

    ws.row_dimensions[row].height = 25
    ws.freeze_panes = f'A{row+1}'

def set_column_widths(ws, widths):
    """Set column widths from dictionary"""
    for col_letter, width in widths.items():
        ws.column_dimensions[col_letter].width = width

def add_mnemonic_row(ws, row, mnemonic_text, span_cols=5):
    """Add mnemonic row directly below a comparison table"""
    # Label in column A
    cell_a = ws.cell(row, 1)
    apply_cell_style(cell_a, text='MEMORY AID', bold=True, font_size=11,
                    bg_color=MNEMONIC_BG, alignment='left', font_color='0000FF')

    # Mnemonic content merged across remaining columns
    ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=span_cols)
    cell_content = ws.cell(row, 2)
    apply_cell_style(cell_content, text=mnemonic_text, bg_color=MNEMONIC_BG)
    ws.row_dimensions[row].height = 60

def add_section_header(ws, row, title):
    """Add section header in Summary tab

    Uses MAIN_TITLE_BG (dark blue) for sheet-level section headers
    """
    cell = ws.cell(row, 1)
    apply_cell_style(cell, text=title, bold=True, font_size=14,
                    bg_color=MAIN_TITLE_BG, alignment='center', font_color='FFFFFF')
    cell.font = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
    ws.row_dimensions[row].height = 30

# =============================================================================
# TAB 1: KEY COMPARISONS
# =============================================================================

def create_key_comparisons_tab(wb):
    """
    Tab 1: Key Comparisons
    - Multiple side-by-side comparison tables
    - One category per table (e.g., separate tables for Mechanism, Clinical, Treatment)
    - Mnemonics placed directly below relevant tables
    """
    ws = wb.active
    ws.title = "Key Comparisons"

    # Column widths
    set_column_widths(ws, {
        'A': 25,  # Category/Row label
        'B': 35,  # Item 1 (e.g., Type I)
        'C': 35,  # Item 2 (e.g., Type II)
        'D': 35,  # Item 3 (e.g., Type III)
        'E': 35,  # Item 4 (e.g., Type IV)
    })

    current_row = 1

    # =========================================================================
    # COMPARISON TABLE 1: Mechanism (uses color set 0 = Ice Blue)
    # =========================================================================
    table_index = 0

    create_comparison_header(ws, "HYPERSENSITIVITY REACTIONS: MECHANISM", current_row,
                            span_cols=5, table_index=table_index)
    current_row += 1

    # Column headers (items being compared)
    headers = ['Category', 'Type I (Immediate)', 'Type II (Cytotoxic)',
               'Type III (Immune Complex)', 'Type IV (Delayed)']
    create_column_headers(ws, headers, current_row, table_index=table_index)
    current_row += 1

    # Comparison data for Mechanism table
    mechanism_data = [
        ('Antibody Involved', 'IgE', 'IgG, IgM', 'IgG, IgM', 'None (T-cell mediated)'),
        ('Time to Reaction', 'Minutes', 'Hours', 'Hours to days', '24-72 hours'),
        ('Mechanism', 'Mast cell degranulation', 'Complement activation, ADCC',
         'Immune complex deposition', 'T-cell activation'),
        ('Mediators', 'Histamine, leukotrienes', 'Complement, NK cells',
         'Complement, neutrophils', 'Cytokines (IFN-γ, TNF)'),
    ]

    # Table 1 uses ONE color SET: HEADER for title/headers, MAIN for data rows
    table_1_main = MAIN_COLORS[table_index]
    for row_data in mechanism_data:
        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(current_row, col_idx)
            bold = (col_idx == 1)  # First column bold
            apply_cell_style(cell, text=value, bold=bold, bg_color=table_1_main)
        current_row += 1

    # Mnemonic directly below Mechanism table
    current_row += 1
    add_mnemonic_row(ws, current_row,
        'MNEMONIC: "ACID"\n\nA = Anaphylactic (Type I)\nC = Cytotoxic (Type II)\n'
        'I = Immune complex (Type III)\nD = Delayed (Type IV)', span_cols=5)
    current_row += 3  # Space before next table

    # =========================================================================
    # COMPARISON TABLE 2: Clinical Presentation (uses color set 1 = Seafoam)
    # =========================================================================
    table_index = 1

    create_comparison_header(ws, "HYPERSENSITIVITY REACTIONS: CLINICAL PRESENTATION", current_row,
                            span_cols=5, table_index=table_index)
    current_row += 1

    create_column_headers(ws, headers, current_row, table_index=table_index)
    current_row += 1

    clinical_data = [
        ('Classic Examples', 'Anaphylaxis, allergic rhinitis, asthma',
         'Hemolytic anemia, Goodpasture', 'SLE, serum sickness, PSGN',
         'Contact dermatitis, TB test'),
        ('Target Organs', 'Skin, airways, GI, cardiovascular', 'Blood cells, basement membrane',
         'Joints, kidneys, skin', 'Skin, organs with granulomas'),
        ('Key Finding', 'Wheal and flare', 'Coombs test positive',
         'Vasculitis, glomerulonephritis', 'Granulomas, indurated skin'),
        ('Severity', 'Can be life-threatening', 'Variable', 'Chronic inflammation', 'Usually localized'),
    ]

    # Table 2 uses ONE color SET: HEADER for title/headers, MAIN for data rows
    table_2_main = MAIN_COLORS[table_index]
    for row_data in clinical_data:
        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(current_row, col_idx)
            bold = (col_idx == 1)
            apply_cell_style(cell, text=value, bold=bold, bg_color=table_2_main)
        current_row += 1

    current_row += 3  # Space before next table

    # =========================================================================
    # COMPARISON TABLE 3: Treatment (uses color set 2 = Light Orchid)
    # =========================================================================
    table_index = 2

    create_comparison_header(ws, "HYPERSENSITIVITY REACTIONS: TREATMENT", current_row,
                            span_cols=5, table_index=table_index)
    current_row += 1

    create_column_headers(ws, headers, current_row, table_index=table_index)
    current_row += 1

    treatment_data = [
        ('First-Line Treatment', 'Epinephrine (anaphylaxis), antihistamines',
         'Stop offending agent, supportive', 'Corticosteroids, immunosuppressants',
         'Remove antigen, topical steroids'),
        ('Adjunct Therapy', 'Corticosteroids, bronchodilators', 'Plasmapheresis (severe)',
         'Plasmapheresis', 'Systemic steroids if severe'),
        ('Prevention', 'Allergen avoidance, desensitization', 'Avoid trigger medications',
         'Treat underlying condition', 'Avoid known antigens'),
    ]

    # Table 3 uses ONE color SET: HEADER for title/headers, MAIN for data rows
    table_3_main = MAIN_COLORS[table_index]
    for row_data in treatment_data:
        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(current_row, col_idx)
            bold = (col_idx == 1)
            apply_cell_style(cell, text=value, bold=bold, bg_color=table_3_main)
        current_row += 1

    # Mnemonic for Treatment
    current_row += 1
    add_mnemonic_row(ws, current_row,
        'Type I = Epi first!\nType IV = Time heals (delayed onset, delayed resolution)', span_cols=5)

    return ws

# =============================================================================
# TAB 2: MASTER CHART
# =============================================================================

def create_master_chart_tab(wb):
    """
    Tab 2: Master Chart
    - All items in one comprehensive table
    - One row per condition/type
    - Frozen header for scrolling
    """
    ws = wb.create_sheet("Master Chart")

    # Column widths
    set_column_widths(ws, {
        'A': 20,  # Type
        'B': 25,  # Antibody
        'C': 15,  # Onset
        'D': 35,  # Mechanism
        'E': 35,  # Examples
        'F': 35,  # Key Finding
        'G': 35,  # Treatment
    })

    # Headers
    headers = ['Type', 'Antibody', 'Onset', 'Mechanism', 'Examples', 'Key Finding', 'Treatment']
    create_master_header_row(ws, headers, 1)

    # Master chart data (all hypersensitivity types)
    master_data = [
        ('Type I', 'IgE', 'Minutes', 'Mast cell degranulation → histamine release',
         'Anaphylaxis, allergic rhinitis, asthma, urticaria',
         'Wheal and flare, elevated tryptase', 'Epinephrine, antihistamines, steroids'),
        ('Type II', 'IgG, IgM', 'Hours', 'Antibody binds cell surface → complement/ADCC',
         'Hemolytic anemia, Goodpasture, Graves, MG',
         'Direct Coombs test positive', 'Stop trigger, plasmapheresis'),
        ('Type III', 'IgG, IgM', 'Hours-days', 'Immune complex deposition → inflammation',
         'SLE, serum sickness, PSGN, RA',
         'Vasculitis, glomerulonephritis', 'Steroids, immunosuppressants'),
        ('Type IV', 'None', '24-72 hrs', 'T-cell mediated → cytokine release',
         'Contact dermatitis, TB skin test, transplant rejection',
         'Granulomas, induration', 'Remove antigen, steroids'),
    ]

    current_row = 2
    # Master Chart: Each row is a different TYPE/CATEGORY, so each gets its own color
    # If multiple items were in same category, they would share the same MAIN color
    # Data rows use font size 10 (not 11) per iCloud source spec
    for idx, row_data in enumerate(master_data):
        color = MAIN_COLORS[idx % len(MAIN_COLORS)]
        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(current_row, col_idx)
            bold = (col_idx == 1)  # First column bold
            apply_cell_style(cell, text=value, bold=bold, font_size=10, bg_color=color)
        ws.row_dimensions[current_row].height = 50  # Taller rows for content
        current_row += 1

    return ws

# =============================================================================
# TAB 3: SUMMARY
# =============================================================================

def create_summary_tab(wb):
    """
    Tab 3: Summary
    - Mnemonics with full breakdowns
    - "If X Think Y" associations
    - Critical values
    - Key definitions
    - High-yield pearls
    """
    ws = wb.create_sheet("Summary")

    # Column width - wide for content
    set_column_widths(ws, {
        'A': 100,
    })

    current_row = 1

    # =========================================================================
    # Section 1: MNEMONICS
    # =========================================================================

    add_section_header(ws, current_row, "MNEMONICS")
    current_row += 1

    mnemonics = [
        ('ACID', 'A = Anaphylactic (Type I)\nC = Cytotoxic (Type II)\n'
         'I = Immune complex (Type III)\nD = Delayed (Type IV)'),
        ('Type I timing', '"I" = Immediate (minutes)'),
        ('Type IV timing', '"IV" looks like "4" = 4th type = delayed (days)'),
    ]

    for mnemonic_name, mnemonic_content in mnemonics:
        cell = ws.cell(current_row, 1)
        full_text = f'MNEMONIC: "{mnemonic_name}"\n\n{mnemonic_content}'
        apply_cell_style(cell, text=full_text, bg_color=MNEMONIC_BG)
        ws.row_dimensions[current_row].height = 80
        current_row += 1

    current_row += 2

    # =========================================================================
    # Section 2: IF X THINK Y
    # =========================================================================

    add_section_header(ws, current_row, '"IF X THINK Y" ASSOCIATIONS')
    current_row += 1

    associations = [
        "If immediate reaction after drug/food/sting → Think Type I hypersensitivity",
        "If hemolytic anemia with positive Coombs → Think Type II hypersensitivity",
        "If arthritis + nephritis + rash → Think Type III (immune complex disease)",
        "If contact dermatitis or PPD+ → Think Type IV (delayed/T-cell)",
        "If needs epinephrine → Think Type I anaphylaxis",
        "If granulomas on biopsy → Think Type IV hypersensitivity",
    ]

    for assoc in associations:
        cell = ws.cell(current_row, 1)
        apply_cell_style(cell, text=assoc, bg_color='F3E5F5')
        ws.row_dimensions[current_row].height = 30
        current_row += 1

    current_row += 2

    # =========================================================================
    # Section 3: KEY DEFINITIONS
    # =========================================================================

    add_section_header(ws, current_row, "KEY DEFINITIONS")
    current_row += 1

    definitions = [
        "Anaphylaxis: Severe, life-threatening systemic Type I reaction",
        "ADCC: Antibody-dependent cellular cytotoxicity (Type II mechanism)",
        "Immune complex: Antigen-antibody aggregate that deposits in tissues (Type III)",
        "Granuloma: Collection of macrophages/giant cells (Type IV hallmark)",
        "Arthus reaction: Localized Type III reaction at injection site",
        "Serum sickness: Systemic Type III reaction (fever, rash, arthralgia, lymphadenopathy)",
    ]

    for defn in definitions:
        cell = ws.cell(current_row, 1)
        apply_cell_style(cell, text=defn, bg_color='E8F5E9')
        ws.row_dimensions[current_row].height = 30
        current_row += 1

    current_row += 2

    # =========================================================================
    # Section 4: HIGH-YIELD PEARLS
    # =========================================================================

    add_section_header(ws, current_row, "HIGH-YIELD PEARLS")
    current_row += 1

    pearls = [
        "• Type I is the ONLY type that involves IgE",
        "• Type IV is the ONLY type that is antibody-INDEPENDENT (T-cell mediated)",
        "• Type II and III both involve IgG/IgM but differ by target (cell surface vs soluble)",
        "• Epinephrine is FIRST-LINE for anaphylaxis - don't delay!",
        "• PPD test reads at 48-72 hours because Type IV is DELAYED",
        "• Goodpasture = Type II (anti-basement membrane antibodies)",
        "• SLE = Type III (immune complex deposition in multiple organs)",
        "• Contact dermatitis = Type IV (think poison ivy)",
    ]

    for pearl in pearls:
        cell = ws.cell(current_row, 1)
        apply_cell_style(cell, text=pearl, bg_color='E0F2F1')
        ws.row_dimensions[current_row].height = 30
        current_row += 1

    return ws

# =============================================================================
# MAIN FUNCTION
# =============================================================================

def create_comparison_chart(output_path):
    """
    Create complete 3-tab comparison chart

    Args:
        output_path: Path to save the Excel file
    """
    # Create workbook
    wb = Workbook()

    # Create all tabs
    create_key_comparisons_tab(wb)
    create_master_chart_tab(wb)
    create_summary_tab(wb)

    # Save
    wb.save(output_path)
    print(f"Comparison chart created: {output_path}")

if __name__ == '__main__':
    # Example usage
    create_comparison_chart('Hypersensitivity_Comparison_Chart.xlsx')
