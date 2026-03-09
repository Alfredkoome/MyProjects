plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("comp.android.tools.build:gradle:2.0.21")
}

android {
    namespace = "com.example.studentbudgettracker"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.studentbudgettracker"
        minSdk = 21
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
        buildFeatures{
            compose=true
        }
    }

    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.3"
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.10.1")
    implementation("androidx.activity:activity-compose:1.7.2")
    implementation(platform("androidx.compose:compose-bom:2023.10.01"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.material:material-icons-extended")
    implementation("androidx.navigation:navigation-compose:2.6.0")
}