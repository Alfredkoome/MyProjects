"""
File Organizer Tool
Automates the organization of files in a directory by sorting them into
categorized subfolders based on file type/extension.
"""

import os
import shutil
import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Mapping of file categories to their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt"],
    "Archives": [".zip", ".tar", ".gz", ".bz2", ".rar", ".7z", ".xz"],
    "Code": [".py", ".js", ".ts", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".json", ".xml", ".yml", ".yaml", ".sh", ".go", ".rb", ".php", ".kt", ".swift"],
    "Data": [".csv", ".sql", ".db", ".sqlite", ".parquet"],
    "Executables": [".exe", ".msi", ".apk", ".dmg", ".deb", ".rpm"],
}


def get_category(extension: str) -> str:
    """Return the category name for a given file extension."""
    ext_lower = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext_lower in extensions:
            return category
    return "Others"


def organize_directory(source_dir: str, dry_run: bool = False) -> dict:
    """
    Organize files in the source directory into categorized subfolders.

    Args:
        source_dir: Path to the directory to organize.
        dry_run: If True, only logs what would happen without moving files.

    Returns:
        A summary dict with counts of files moved per category.
    """
    source_path = Path(source_dir).resolve()

    if not source_path.exists():
        raise FileNotFoundError(f"Directory not found: {source_path}")
    if not source_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {source_path}")

    summary = {}
    files = [f for f in source_path.iterdir() if f.is_file()]

    if not files:
        logger.info("No files found in %s", source_path)
        return summary

    for file_path in files:
        category = get_category(file_path.suffix)
        dest_dir = source_path / category

        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            dest_file = dest_dir / file_path.name

            # Avoid overwriting: append a counter if file already exists
            counter = 1
            while dest_file.exists():
                stem = file_path.stem
                suffix = file_path.suffix
                dest_file = dest_dir / f"{stem}_{counter}{suffix}"
                counter += 1

            shutil.move(str(file_path), str(dest_file))
            logger.info("Moved '%s' -> '%s/'", file_path.name, category)
        else:
            logger.info("[DRY RUN] Would move '%s' -> '%s/'", file_path.name, category)

        summary[category] = summary.get(category, 0) + 1

    return summary


def print_summary(summary: dict) -> None:
    """Print a human-readable summary of the organization results."""
    if not summary:
        print("No files were organized.")
        return

    total = sum(summary.values())
    print("\n=== Organization Summary ===")
    for category, count in sorted(summary.items()):
        print(f"  {category:<15}: {count} file(s)")
    print(f"  {'TOTAL':<15}: {total} file(s)")
    print("============================\n")


def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by sorting them into categorized subfolders."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Path to the directory to organize (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without actually moving files",
    )
    args = parser.parse_args()

    try:
        summary = organize_directory(args.directory, dry_run=args.dry_run)
        print_summary(summary)
    except (FileNotFoundError, NotADirectoryError) as e:
        logger.error("%s", e)
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()
