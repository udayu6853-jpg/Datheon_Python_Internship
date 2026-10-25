
import os
import shutil
from pathlib import Path

# File extensions and their categories
FILE_CATEGORIES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    ".pptx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    ".cpp": "Code",
}

# Change this to the folder you want to organize.
TARGET_FOLDER = Path.home() / "OneDrive" / "Desktop" / "Organizer_Test"

# Keep True for a safe preview.
# Change to False after checking the preview.
DRY_RUN = False


def get_destination(folder, filename):
    """Find a destination name that does not already exist."""
    destination = folder / filename

    if not destination.exists():
        return destination

    original = Path(filename)
    number = 1

    while True:
        new_name = (
            f"{original.stem}_{number}{original.suffix}"
        )
        destination = folder / new_name

        if not destination.exists():
            return destination

        number += 1


def organize_files():
    moved = 0
    skipped = 0
    errors = 0

    if not TARGET_FOLDER.is_dir():
        print(f"Folder not found: {TARGET_FOLDER}")
        return

    print("\nAUTOMATED FILE ORGANIZER")
    print("=" * 40)
    print(f"Target: {TARGET_FOLDER}")
    print(f"Preview mode: {DRY_RUN}\n")

    # Snapshot the entries before moving files.
    entries = list(os.scandir(TARGET_FOLDER))

    for entry in entries:
        if not entry.is_file(follow_symlinks=False):
            continue

        source = Path(entry.path)
        category = FILE_CATEGORIES.get(
            source.suffix.lower()
        )

        if category is None:
            skipped += 1
            continue

        destination_folder = TARGET_FOLDER / category

        try:
            if not DRY_RUN:
                destination_folder.mkdir(
                    parents=True, exist_ok=True
                )

            destination = get_destination(
                destination_folder, source.name
            )

            if DRY_RUN:
                print(
                    f"[PREVIEW] {source.name} -> "
                    f"{category}/{destination.name}"
                )
            else:
                shutil.move(
                    str(source), str(destination)
                )
                print(
                    f"[MOVED] {source.name} -> "
                    f"{category}/{destination.name}"
                )

            moved += 1

        except PermissionError as error:
            errors += 1
            print(f"[PERMISSION ERROR] {source.name}: {error}")

        except OSError as error:
            errors += 1
            print(f"[FILE ERROR] {source.name}: {error}")

    print("\n" + "=" * 40)
    print("EXECUTION SUMMARY")
    print("=" * 40)

    if DRY_RUN:
        print(f"Files ready to organize: {moved}")
        print("No files were moved. This was a preview.")
    else:
        print(f"Files moved successfully: {moved}")

    print(f"Files skipped: {skipped}")
    print(f"Errors: {errors}")
    print("Finished.")


if __name__ == "__main__":
    organize_files()
