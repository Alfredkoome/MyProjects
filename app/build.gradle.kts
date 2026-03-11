plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
}

android {
    namespace = "com.example.budget"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.budget"
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

    compileOptions {
        // This controls 'compileDebugJavaWithJavac'
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }

    kotlinOptions {
        // This controls 'compileDebugKotlin'
        jvmTarget = "21" // Must match the version above
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.compose.ui)
    implementation(libs.androidx.compose.material3)
    implementation(libs.androidx.compose.material.icons.extended)
    implementation(libs.androidx.navigation.compose)
}
