# Web Apps

Browser-based applications built with plain HTML, CSS, and JavaScript — no build tools required.

---

## 1. TaskFlow – To-Do App (`todo_app/`)

A clean, responsive task management app that runs entirely in the browser. Tasks persist across page reloads using `localStorage`.

### Features

- ✅ Add, complete, and delete tasks
- 🔍 Filter tasks by **All / Active / Completed**
- 💾 Data persists automatically in `localStorage`
- 📱 Fully responsive — works on mobile and desktop
- ♿ Accessible markup with ARIA attributes

### How to Run

No server or build step needed — just open the file in your browser:

```bash
# macOS / Linux
open web_apps/todo_app/index.html

# Windows
start web_apps/todo_app/index.html
```

Or drag `index.html` into any modern browser.

### Project Structure

```
todo_app/
├── index.html   # App markup
├── style.css    # Styles and animations
└── app.js       # Application logic
```

### Screenshots

| Empty state | Tasks added | Completed filter |
|-------------|-------------|-----------------|
| Open the app to see it in action! | | |
