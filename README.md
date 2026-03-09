# 💰 Student Budget Tracker

A lightweight Android mobile application built with **Kotlin** and **Jetpack Compose** that helps students record, categorize, and track their daily expenses. The app provides a clean, intuitive interface for logging spending and viewing a running total — all without needing an internet connection.

---

## 📱 Screenshots

> **Home Screen** — View your total spending and all recorded expenses  
> **Add Expense Screen** — Log a new expense with amount, category, and date

---

## ✨ Features

- 📋 **View all expenses** in a scrollable list with amount, category, and date
- ➕ **Add new expenses** via a simple form (amount, category, date)
- 💵 **Live total calculation** — the total spent updates instantly as expenses are added
- 🗂️ **Categorize spending** — attach a custom category (e.g., Food, Transport, Books)
- 📅 **Date tracking** — record the date of each transaction
- 🧭 **Smooth navigation** between screens using Jetpack Navigation Compose
- 🎨 **Material 3 design** with adaptive light/dark theme support
- 💡 **Dynamic color** support on Android 12+ (Material You)
- 📴 **Fully offline** — no network permissions required

---

## 🛠️ Tech Stack

| Category | Technology | Version |
|---|---|---|
| Language | Kotlin | 2.0.21 |
| UI Framework | Jetpack Compose | 2024.09.00 (via BOM) |
| Design System | Material Design 3 | Latest (via BOM) |
| Navigation | Jetpack Navigation Compose | 2.6.0 |
| Core Library | AndroidX Core KTX | 1.17.0 |
| Activity | AndroidX Activity Compose | 1.12.3 |
| Lifecycle | AndroidX Lifecycle Runtime KTX | 2.10.0 |
| Build System | Gradle | 8.13 |
| Android Gradle Plugin | AGP | 8.13.2 |
| Testing (Unit) | JUnit 4 | 4.13.2 |
| Testing (UI) | Espresso | 3.7.0 |
| Testing (Instrumented) | AndroidX JUnit | 1.3.0 |

---

## 📁 Project Structure

```
MyProjects/
├── app/
│   ├── build.gradle.kts               # App-level Gradle config
│   ├── proguard-rules.pro             # ProGuard rules
│   └── src/
│       ├── androidTest/               # Instrumented (UI) tests
│       │   └── java/com/example/budget/
│       │       └── ExampleInstrumentedTest.kt
│       ├── main/
│       │   ├── AndroidManifest.xml    # App manifest & configuration
│       │   ├── java/com/example/budget/
│       │   │   ├── MainActivity.kt    # Core app logic & all Composables
│       │   │   └── ui/theme/
│       │   │       ├── Color.kt       # Color palette
│       │   │       ├── Theme.kt       # Material 3 theme setup
│       │   │       └── Type.kt        # Typography configuration
│       │   └── res/
│       │       ├── drawable/          # App icons & backgrounds
│       │       ├── mipmap-*/          # Launcher icons (all densities)
│       │       ├── values/
│       │       │   ├── colors.xml
│       │       │   ├── strings.xml
│       │       │   └── themes.xml
│       │       └── xml/
│       │           ├── backup_rules.xml
│       │           └── data_extraction_rules.xml
│       └── test/                      # Unit tests
│           └── java/com/example/budget/
│               └── ExampleUnitTest.kt
├── build.gradle.kts                   # Root Gradle configuration
├── gradle/
│   ├── libs.versions.toml             # Centralized dependency versions
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties  # Gradle version (8.13)
├── gradle.properties                  # Gradle JVM & Android settings
├── gradlew                            # Gradle wrapper (Unix/macOS)
├── gradlew.bat                        # Gradle wrapper (Windows)
└── settings.gradle.kts               # Project settings & module list
```

---

## 🏗️ Architecture

The app follows a straightforward **single-activity, Composable-first** architecture:

```
MainActivity
    └── BudgetApp()                  ← Root Composable + NavHost
            ├── HomeScreen()         ← "home" route
            └── AddExpenseScreen()   ← "add" route
```

### Key Components

| Component | Role |
|---|---|
| `MainActivity` | Single Android Activity; initializes Compose content |
| `BudgetApp()` | Root composable; owns shared state (`expenses` list) and navigation controller |
| `HomeScreen()` | Displays total spent and a scrollable list of all expense cards |
| `AddExpenseScreen()` | Form to capture amount, category, and date; calls `onSave` callback |
| `Expense` | Simple data class holding `amount: Double`, `category: String`, `date: String` |

### State Management

Expenses are held in a `mutableStateListOf<Expense>()` owned by `BudgetApp` and passed down as parameters. This keeps state above the navigation graph so it persists when navigating between screens within a session.

> ⚠️ **Note:** State is currently **in-memory only** and is lost when the app is closed. See [Planned Enhancements](#-planned-enhancements) for persistence options.

---

## 🚀 Getting Started

### Prerequisites

- **Android Studio** Hedgehog (2023.1.1) or newer
- **JDK 11** or higher
- **Android SDK** with API Level 34 installed
- An Android emulator or a physical Android device (API 21+)

### Clone the Repository

```bash
git clone https://github.com/Alfredkoome/MyProjects.git
cd MyProjects
```

### Open in Android Studio

1. Launch Android Studio
2. Click **File → Open** and navigate to the cloned `MyProjects` directory
3. Wait for Gradle sync to complete
4. Click the **Run ▶** button (or press `Shift + F10`) to build and deploy to your device/emulator

### Build via Command Line

```bash
# Unix / macOS / Linux
./gradlew assembleDebug

# Windows
gradlew.bat assembleDebug
```

The generated APK will be at:
```
app/build/outputs/apk/debug/app-debug.apk
```

---

## 🔧 Build Commands

| Command | Description |
|---|---|
| `./gradlew assembleDebug` | Build a debug APK |
| `./gradlew assembleRelease` | Build a release APK (requires signing config) |
| `./gradlew installDebug` | Build and install debug APK on connected device/emulator |
| `./gradlew clean` | Clean build artifacts |
| `./gradlew clean assembleDebug` | Clean and rebuild debug APK |
| `./gradlew build` | Run full build (compiles + tests) |

---

## 🧪 Testing

### Run Unit Tests

```bash
./gradlew test
```

### Run Instrumented Tests (requires device or emulator)

```bash
./gradlew connectedAndroidTest
```

### Run All Tests

```bash
./gradlew build
```

### Test Structure

| Test Type | Location | Framework |
|---|---|---|
| Unit Tests | `app/src/test/java/com/example/budget/` | JUnit 4 |
| Instrumented Tests | `app/src/androidTest/java/com/example/budget/` | AndroidJUnit4, Espresso |

---

## 📦 Dependencies

All dependencies are managed through Gradle's [Version Catalog](gradle/libs.versions.toml).

### Runtime Dependencies

```toml
androidx-core-ktx = "1.17.0"
androidx-activity-compose = "1.12.3"
compose-bom = "2024.09.00"          # Jetpack Compose BOM
material3                           # Material Design 3 (via BOM)
navigation-compose = "2.6.0"        # Jetpack Navigation
lifecycle-runtime-ktx = "2.10.0"
```

### Test Dependencies

```toml
junit = "4.13.2"
androidx-junit = "1.3.0"
espresso-core = "3.7.0"
```

---

## ⚙️ Configuration

### Android SDK Targets

| Setting | Value |
|---|---|
| `compileSdk` | 34 (Android 14) |
| `targetSdk` | 34 (Android 14) |
| `minSdk` | 21 (Android 5.0 Lollipop) |
| Application ID | `com.example.studentbudgettracker` |
| Version Name | 1.0 |
| Version Code | 1 |

### Gradle / JVM

| Setting | Value |
|---|---|
| Gradle Version | 8.13 |
| Android Gradle Plugin | 8.13.2 |
| JVM Heap | 2048 MB (`-Xmx2048m`) |
| Kotlin Code Style | Official |
| AndroidX | Enabled |

---

## 🗺️ Navigation Routes

| Route | Screen | Description |
|---|---|---|
| `home` | `HomeScreen` | Lists all recorded expenses and total spent |
| `add` | `AddExpenseScreen` | Form to add a new expense entry |

---

## 🎨 Theming

The app uses **Material Design 3** with a purple-based color palette:

| Token | Light Mode | Dark Mode |
|---|---|---|
| Primary | `Purple40` (#6650A4) | `Purple80` (#D0BCFF) |
| Secondary | `PurpleGrey40` (#625B71) | `PurpleGrey80` (#CCC2DC) |
| Tertiary | `Pink40` (#7D5260) | `Pink80` (#EFB8C8) |

- Supports **light and dark mode** automatically based on system settings
- **Dynamic color** (Material You) is enabled on Android 12+

---

## 🔮 Planned Enhancements

- [ ] **Data persistence** — Integrate Room database so expenses survive app restarts
- [ ] **Date picker** — Replace free-text date entry with a proper date picker dialog
- [ ] **Category picker** — Provide a dropdown of preset categories
- [ ] **Input validation** — Enforce numeric input for amount and non-empty category
- [ ] **Edit & delete expenses** — Allow updating or removing existing records
- [ ] **Expense filtering** — Filter by date range or category
- [ ] **Summary statistics** — Charts and breakdowns by category
- [ ] **Export data** — Export expense history as CSV or PDF
- [ ] **Budget limit** — Set a monthly spending limit with alerts
- [ ] **Multi-currency support** — Support currencies beyond Kenyan Shillings (Ksh)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is open source. Feel free to use, modify, and distribute it.

---

## 👤 Author

**Alfred Koome**  
GitHub: [@Alfredkoome](https://github.com/Alfredkoome)
