[app]

title = YT Downloader

package.name = ytdownloader
package.domain = org.maxhtv

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg

version = 1.0

requirements = python3,kivy,yt-dlp

orientation = portrait
fullscreen = 0

android.accept_sdk_license = True
android.api = 34
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET

presplash.color = #202020

[buildozer]

log_level = 2
warn_on_root = 1
