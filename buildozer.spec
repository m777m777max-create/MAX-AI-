[app]
title = MAX AI
package.name = maxai
package.domain = org.maxai
source.dir = .
source.include_exts = py,png,jpg,kv,json,md,txt
version = 1.0.0
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = RECORD_AUDIO,INTERNET,WAKE_LOCK
android.minapi = 23
android.api = 35

[buildozer]
log_level = 2
warn_on_root = 1
