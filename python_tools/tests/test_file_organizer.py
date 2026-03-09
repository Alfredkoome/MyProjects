"""
Unit tests for file_organizer.py
"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path

# Allow importing from the parent directory
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from file_organizer import get_category, organize_directory, FILE_CATEGORIES


class TestGetCategory(unittest.TestCase):
    """Tests for the get_category() helper function."""

    def test_known_image_extensions(self):
        for ext in [".jpg", ".jpeg", ".png", ".gif", ".svg"]:
            self.assertEqual(get_category(ext), "Images", f"Failed for {ext}")

    def test_known_document_extensions(self):
        for ext in [".pdf", ".doc", ".docx", ".txt"]:
            self.assertEqual(get_category(ext), "Documents", f"Failed for {ext}")

    def test_known_code_extensions(self):
        for ext in [".py", ".js", ".java", ".html"]:
            self.assertEqual(get_category(ext), "Code", f"Failed for {ext}")

    def test_known_archive_extensions(self):
        for ext in [".zip", ".tar", ".gz", ".rar"]:
            self.assertEqual(get_category(ext), "Archives", f"Failed for {ext}")

    def test_unknown_extension_returns_others(self):
        self.assertEqual(get_category(".unknownxyz"), "Others")

    def test_empty_extension_returns_others(self):
        self.assertEqual(get_category(""), "Others")

    def test_case_insensitive(self):
        self.assertEqual(get_category(".JPG"), "Images")
        self.assertEqual(get_category(".PDF"), "Documents")
        self.assertEqual(get_category(".PY"), "Code")

    def test_all_categories_are_covered(self):
        """Every extension listed in FILE_CATEGORIES must map to its category."""
        for category, extensions in FILE_CATEGORIES.items():
            for ext in extensions:
                self.assertEqual(
                    get_category(ext), category,
                    f"Extension {ext!r} should map to {category!r}"
                )


class TestOrganizeDirectory(unittest.TestCase):
    """Integration tests for organize_directory()."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def _create_files(self, *filenames):
        """Create empty files in the test directory and return their paths."""
        paths = []
        for name in filenames:
            p = Path(self.test_dir) / name
            p.touch()
            paths.append(p)
        return paths

    # ── Basic organisation ───────────────────────────────────────────────────

    def test_files_moved_to_correct_category_folders(self):
        self._create_files("photo.jpg", "report.pdf", "script.py")

        summary = organize_directory(self.test_dir)

        self.assertEqual(summary["Images"], 1)
        self.assertEqual(summary["Documents"], 1)
        self.assertEqual(summary["Code"], 1)

        self.assertTrue((Path(self.test_dir) / "Images" / "photo.jpg").exists())
        self.assertTrue((Path(self.test_dir) / "Documents" / "report.pdf").exists())
        self.assertTrue((Path(self.test_dir) / "Code" / "script.py").exists())

    def test_unknown_extension_goes_to_others(self):
        self._create_files("file.unknownxyz")

        summary = organize_directory(self.test_dir)

        self.assertEqual(summary.get("Others"), 1)
        self.assertTrue((Path(self.test_dir) / "Others" / "file.unknownxyz").exists())

    def test_empty_directory_returns_empty_summary(self):
        summary = organize_directory(self.test_dir)
        self.assertEqual(summary, {})

    def test_total_count_matches_files_created(self):
        filenames = ["a.jpg", "b.mp3", "c.pdf", "d.zip", "e.py"]
        self._create_files(*filenames)

        summary = organize_directory(self.test_dir)

        self.assertEqual(sum(summary.values()), len(filenames))

    # ── Dry-run mode ────────────────────────────────────────────────────────

    def test_dry_run_does_not_move_files(self):
        self._create_files("photo.jpg", "report.pdf")

        summary = organize_directory(self.test_dir, dry_run=True)

        # Original files must still be in place
        self.assertTrue((Path(self.test_dir) / "photo.jpg").exists())
        self.assertTrue((Path(self.test_dir) / "report.pdf").exists())
        # Category subdirectories must NOT have been created
        self.assertFalse((Path(self.test_dir) / "Images").exists())
        self.assertFalse((Path(self.test_dir) / "Documents").exists())
        # Summary should still report what *would* happen
        self.assertEqual(summary["Images"], 1)
        self.assertEqual(summary["Documents"], 1)

    # ── Conflict handling ────────────────────────────────────────────────────

    def test_duplicate_filenames_are_renamed(self):
        """When a destination file already exists the new file gets a counter suffix."""
        img_dir = Path(self.test_dir) / "Images"
        img_dir.mkdir()
        (img_dir / "photo.jpg").touch()   # pre-existing file

        self._create_files("photo.jpg")   # file that would clash

        organize_directory(self.test_dir)

        # Original and renamed file both exist
        self.assertTrue((img_dir / "photo.jpg").exists())
        self.assertTrue((img_dir / "photo_1.jpg").exists())

    # ── Error handling ───────────────────────────────────────────────────────

    def test_nonexistent_directory_raises(self):
        with self.assertRaises(FileNotFoundError):
            organize_directory("/nonexistent/path/that/does/not/exist")

    def test_file_path_instead_of_directory_raises(self):
        file_path = Path(self.test_dir) / "some_file.txt"
        file_path.touch()
        with self.assertRaises(NotADirectoryError):
            organize_directory(str(file_path))


if __name__ == "__main__":
    unittest.main()
