
[app]
title = Falling Man
package.name = fallingman
package.domain = org.kivy.fallingman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
source.main = main.py
android.api = 31
android.minapi = 26
android.ndk = 23b
android.archs = armeabi-v7a,arm64-v8a
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0
