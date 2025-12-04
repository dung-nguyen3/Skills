#!/usr/bin/env python3
"""
Post-Processing Automation Runner

Executes post-processing tasks after study guide creation:
1. Auto-consolidate Excel master charts
2. Generate/update QUICK_ACCESS index

Detects course type (Pharmacology vs Clinical Medicine) from folder path.
"""

import sys
import re
import subprocess
from pathlib import Path

# Script locations
SCRIPTS_DIR = Path(__file__).parent.parent.parent / "study-guides" / "templates-and-examples" / "Python_Examples"
CONSOLIDATE_SCRIPT = SCRIPTS_DIR / "Auto_Consolidate_Master_Charts.py"
QUICK_ACCESS_SCRIPT = SCRIPTS_DIR / "Generate_Quick_Access_Index.py"


def detect_course_info(file_path: Path):
    """
    Detect course type and folder from file path.

    Returns:
        tuple: (course_type, course_folder) or (None, None) if not detected
    """
    current = file_path.parent

    # Walk up directory tree
    while current.name:
        # Check for Pharmacology pattern
        if re.match(r'Pharmacology\s*\d*', current.name, re.IGNORECASE):
            return ("Pharmacology", current)

        # Check for Clinical Medicine pattern
        if re.match(r'Clinical\s*Medicine\s*\d*', current.name, re.IGNORECASE):
            return ("Clinical_Medicine", current)

        current = current.parent

        # Stop if we've gone too far up
        if len(current.parts) < 3:
            break

    return (None, None)


def has_master_chart_sheet(excel_path: Path) -> bool:
    """
    Check if Excel file has a 'Master Chart' sheet.

    Returns:
        bool: True if Master Chart sheet exists
    """
    try:
        import openpyxl
        wb = openpyxl.load_workbook(excel_path, read_only=True)
        has_sheet = "Master Chart" in wb.sheetnames
        wb.close()
        return has_sheet
    except Exception as e:
        print(f"⚠️  Could not read Excel file: {e}")
        return False


def run_consolidation(study_guide_path: Path, course_folder: Path, course_type: str) -> bool:
    """
    Run master chart consolidation script.

    Returns:
        bool: True if successful
    """
    reference_file = course_folder / f"{course_type}_Master_Reference.xlsx"

    print(f"\n🔄 Running consolidation...")
    print(f"  Source: {study_guide_path.name}")
    print(f"  Target: {reference_file.name}")

    try:
        result = subprocess.run(
            ["python3", str(CONSOLIDATE_SCRIPT), str(study_guide_path), str(reference_file)],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print("✓ Consolidation complete")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"❌ Consolidation failed:")
            print(result.stderr)
            return False

    except subprocess.TimeoutExpired:
        print("❌ Consolidation timed out (>30s)")
        return False
    except Exception as e:
        print(f"❌ Consolidation error: {e}")
        return False


def run_quick_access_update(course_folder: Path, course_type: str) -> bool:
    """
    Run QUICK_ACCESS index generation script.

    Returns:
        bool: True if successful
    """
    quick_access_file = course_folder / f"QUICK_ACCESS_{course_type}.md"

    print(f"\n📇 Updating QUICK_ACCESS index...")
    print(f"  Scanning: {course_folder.name}")
    print(f"  Output: {quick_access_file.name}")

    try:
        result = subprocess.run(
            ["python3", str(QUICK_ACCESS_SCRIPT), str(course_folder), str(quick_access_file)],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            print("✓ QUICK_ACCESS index updated")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"❌ QUICK_ACCESS update failed:")
            print(result.stderr)
            return False

    except subprocess.TimeoutExpired:
        print("❌ QUICK_ACCESS update timed out (>60s)")
        return False
    except Exception as e:
        print(f"❌ QUICK_ACCESS update error: {e}")
        return False


def main():
    """Main execution."""
    if len(sys.argv) < 2:
        print("Usage: python3 post-processing-automation-runner.py <study-guide-path>")
        sys.exit(1)

    study_guide_path = Path(sys.argv[1]).resolve()

    if not study_guide_path.exists():
        print(f"❌ File not found: {study_guide_path}")
        sys.exit(1)

    print("━" * 60)
    print("POST-PROCESSING AUTOMATION")
    print("━" * 60)
    print(f"\nStudy guide: {study_guide_path.name}")

    # Detect course info
    course_type, course_folder = detect_course_info(study_guide_path)

    if not course_type:
        print("\n⚠️  Could not detect course folder")
        print("Expected folder pattern: 'Pharmacology X' or 'Clinical Medicine X'")
        print("Skipping post-processing.")
        sys.exit(0)

    print(f"Course detected: {course_type}")
    print(f"Course folder: {course_folder}")

    # Determine actions needed
    is_excel = study_guide_path.suffix.lower() == '.xlsx'
    should_consolidate = False

    if is_excel:
        if has_master_chart_sheet(study_guide_path):
            should_consolidate = True
            print("\n✓ Excel file with Master Chart sheet detected")
        else:
            print("\nℹ️  Excel file has no Master Chart sheet")
            print("Skipping consolidation, will update QUICK_ACCESS only")
    else:
        print(f"\nℹ️  Non-Excel file ({study_guide_path.suffix})")
        print("Skipping consolidation, will update QUICK_ACCESS only")

    # Execute post-processing
    consolidation_success = True
    quick_access_success = True

    if should_consolidate:
        consolidation_success = run_consolidation(study_guide_path, course_folder, course_type)

    quick_access_success = run_quick_access_update(course_folder, course_type)

    # Summary
    print("\n" + "━" * 60)
    if consolidation_success and quick_access_success:
        print("✅ POST-PROCESSING COMPLETE")
        print("\nActions completed:")
        if should_consolidate:
            print(f"  ✓ Master chart consolidated → {course_type}_Master_Reference.xlsx")
        print(f"  ✓ QUICK_ACCESS updated → QUICK_ACCESS_{course_type}.md")
        print(f"\nReference files location:")
        print(f"  {course_folder}")
    else:
        print("⚠️  POST-PROCESSING COMPLETED WITH ERRORS")
        if should_consolidate and not consolidation_success:
            print("  ❌ Consolidation failed")
        if not quick_access_success:
            print("  ❌ QUICK_ACCESS update failed")
        print("\nStudy guide was created successfully.")
        print("Post-processing errors can be manually resolved.")

    print("━" * 60)

    # Exit with error code if any step failed
    if not (consolidation_success and quick_access_success):
        sys.exit(1)


if __name__ == "__main__":
    main()
