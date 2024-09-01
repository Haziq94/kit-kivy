[app]
# (str) Title of your application
title = MyApp

# (str) Package name (should be unique)
package.name = myapp

# (str) Package domain (unique domain for your app, often a reverse URL)
package.domain = org.myapp

# (str) Version number (method 1)
version = 0.1

# (list) List of service requirements (e.g., python3, kivy)
requirements = python3,kivy

# (str) Source code directory (default is '.')
source.dir = .

# (str) Path to the application icon
icon.filename = %(source.dir)s/data/icon.png

# (str) Path to a custom background image for the splash screen
# splashscreen.filename = %(source.dir)s/data/splash.png

# (str) Path to a custom Java file
# java.source.dir = %(source.dir)s/java

# (str) Path to a custom Python file
# python.source.dir = %(source.dir)s/python

# (str) Orientation of the application (portrait, landscape, sensorLandscape, sensorPortrait)
orientation = portrait

# (list) List of supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (str) Path to the Android SDK
android.sdk_path = ~/.buildozer/android/platform/android-sdk

# (str) Path to the Android NDK
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r27-linux

# (int) Minimum API level required for Android
android.minapi = 21

# (int) Target API level for Android
android.api = 31

# (str) Android NDK API level
android.ndk_api = 21

# (str) The Android version to use
android.version = 11.0.0

# (str) The app's Android package name
android.package = com.example.myapp

# (bool) Enable or disable fullscreen mode
android.fullscreen = 0

# (bool) Enable or disable windowed mode
android.windowed = 1

# (str) Path to a custom Python module
# (list) List of additional requirements (e.g., numpy, requests)
# requirements = python3,kivy,numpy,requests

# (list) List of extra Pygame modules
# pygame_modules = pygame.freetype, pygame.sndarray

# (str) Build type: release or debug
build_type = debug

# (list) List of Python packages to include in the distribution
# include_packages = package1,package2

# (list) List of additional files to include in the APK
# include_files = data/*,images/*

# (str) Path to a custom buildozer Python module
# (list) List of extra packages to include
# extra_packages = package1,package2

[buildozer]
# (str) Directory to store build artifacts
# build_dir = .buildozer

# (str) The name of the buildozer tool to use
# tool = buildozer

# (bool) Enable or disable verbose logging
log_level = 2

# (bool) Enable or disable parallel builds
# parallel = 1
