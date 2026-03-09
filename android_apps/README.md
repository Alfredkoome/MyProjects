# Android Apps

Native Android applications built with Kotlin, following modern Android development practices.

---

## 1. Task Manager (`TaskManager/`)

A clean and intuitive Android task management app that helps you keep track of your daily to-dos.

### Features

- ➕ Add tasks via text input or keyboard action key
- ✅ Mark tasks as complete with a checkbox
- 🗑️ Delete individual tasks with undo support (Snackbar)
- 🧹 Clear all completed tasks in one tap
- 📊 Live counter showing remaining active tasks
- 🏗️ Built with **MVVM architecture** (ViewModel + LiveData)

### Architecture

```
TaskManager/
├── app/
│   ├── build.gradle
│   └── src/main/
│       ├── AndroidManifest.xml
│       ├── java/com/example/taskmanager/
│       │   ├── MainActivity.kt      # UI controller
│       │   ├── Task.kt              # Data model
│       │   ├── TaskViewModel.kt     # Business logic / state holder
│       │   └── TaskAdapter.kt       # RecyclerView adapter
│       └── res/
│           ├── layout/
│           │   ├── activity_main.xml
│           │   └── item_task.xml
│           └── values/
│               ├── strings.xml
│               ├── colors.xml
│               └── themes.xml
├── build.gradle
└── settings.gradle
```

### Tech Stack

| Component        | Technology                    |
|-----------------|-------------------------------|
| Language         | Kotlin                        |
| Min SDK          | API 26 (Android 8.0)          |
| Target SDK       | API 34 (Android 14)           |
| Architecture     | MVVM (ViewModel + LiveData)   |
| UI               | Material Design 3 components  |
| Build system     | Gradle                        |

### How to Build

1. Open the `TaskManager/` folder in **Android Studio**
2. Let Gradle sync dependencies
3. Run on an emulator or physical device (API 26+)

```bash
# From the TaskManager/ directory:
./gradlew assembleDebug
```
