# Python Tools

A collection of Python command-line tools designed to automate repetitive tasks and simplify daily workflows.

---

## 1. File Organizer (`file_organizer.py`)

Automatically sorts files in any directory into categorized subfolders based on their file type. No more cluttered Downloads or Desktop folders!

### Features

- Organizes files into categories: **Images**, **Videos**, **Audio**, **Documents**, **Archives**, **Code**, **Data**, **Executables**, and **Others**
- **Dry-run mode** lets you preview changes before applying them
- Handles filename conflicts by appending a counter (e.g., `photo_1.jpg`)
- Works on any directory you point it at

### Requirements

- Python 3.8+
- No external dependencies (uses the standard library only)

### Usage

```bash
# Organize the current directory
python file_organizer.py

# Organize a specific directory
python file_organizer.py ~/Downloads

# Preview what would happen (no files are moved)
python file_organizer.py ~/Downloads --dry-run
```

### Example Output

```
INFO: Moved 'report.pdf' -> 'Documents/'
INFO: Moved 'photo.jpg' -> 'Images/'
INFO: Moved 'script.py' -> 'Code/'

=== Organization Summary ===
  Code           : 1 file(s)
  Documents      : 1 file(s)
  Images         : 1 file(s)
  TOTAL          : 3 file(s)
============================
```

### File Categories

| Category    | Extensions                                              |
|-------------|--------------------------------------------------------|
| Images      | jpg, jpeg, png, gif, bmp, svg, webp, tiff, ico         |
| Videos      | mp4, mkv, avi, mov, wmv, flv, webm, m4v               |
| Audio       | mp3, wav, flac, aac, ogg, m4a, wma                    |
| Documents   | pdf, doc, docx, xls, xlsx, ppt, pptx, txt, rtf, odt   |
| Archives    | zip, tar, gz, bz2, rar, 7z, xz                        |
| Code        | py, js, ts, java, c, cpp, html, css, json, yml, etc.  |
| Data        | csv, sql, db, sqlite, parquet                         |
| Executables | exe, msi, apk, dmg, deb, rpm                          |
| Others      | Everything else                                        |
