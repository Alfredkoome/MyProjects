# MyProjects

A versatile collection of projects including **Android apps**, **web applications**, and **Python tools** — all designed to automate tasks, simplify workflows, and solve real-world problems efficiently. Each project focuses on practical functionality, user-friendly design, and modern technologies that make daily tasks easier.

---

## 📁 Project Structure

```
MyProjects/
├── android_apps/          # Native Android applications (Kotlin)
│   └── TaskManager/       # To-do / task manager Android app
├── web_apps/              # Browser-based web applications
│   └── todo_app/          # TaskFlow – responsive to-do list (HTML/CSS/JS)
└── python_tools/          # Python command-line automation tools
    └── file_organizer.py  # Organizes files into folders by type
```

---

## 🤖 Android Apps

### [Task Manager](android_apps/TaskManager/)

A native Android task management app built with **Kotlin** and **MVVM architecture**.

| Feature | Details |
|---------|---------|
| Add & complete tasks | Checkbox-driven workflow |
| Delete with Undo | Snackbar undo action |
| Active task counter | Live count of remaining tasks |
| Architecture | ViewModel + LiveData (MVVM) |
| Min SDK | Android 8.0 (API 26) |

➡️ See [android_apps/README.md](android_apps/README.md) for build instructions.

---

## 🌐 Web Apps

### [TaskFlow – To-Do App](web_apps/todo_app/)

A clean, responsive task manager that runs entirely in the browser — **no server or build step needed**.

| Feature | Details |
|---------|---------|
| Add, complete, delete tasks | Instant feedback |
| Filter tasks | All / Active / Completed |
| Data persistence | Saved in `localStorage` |
| Responsive design | Works on mobile & desktop |

Open `web_apps/todo_app/index.html` in any modern browser to get started.

➡️ See [web_apps/README.md](web_apps/README.md) for details.

---

## 🐍 Python Tools

### [File Organizer](python_tools/file_organizer.py)

A Python CLI tool that automatically sorts files in any directory into categorized subfolders — perfect for cleaning up cluttered `Downloads` or `Desktop` folders.

| Feature | Details |
|---------|---------|
| Auto-categorize | Images, Videos, Audio, Documents, Code, etc. |
| Dry-run mode | Preview changes before applying them |
| Conflict handling | Auto-renames duplicates |
| Dependencies | None (Python 3.8+ standard library only) |

```bash
python python_tools/file_organizer.py ~/Downloads --dry-run
```

➡️ See [python_tools/README.md](python_tools/README.md) for full usage guide.

---

## 🛠️ Getting Started

Clone the repository and navigate to the project you want to explore:

```bash
git clone https://github.com/Alfredkoome/MyProjects.git
cd MyProjects
```

Each subdirectory contains its own `README.md` with setup and usage instructions.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
