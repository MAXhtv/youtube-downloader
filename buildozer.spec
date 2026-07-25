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

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]

log_level = 2
warn_on_root = 1
