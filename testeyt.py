from yt_dlp import YoutubeDL
import os
import sys
destino="./musicasevideos"

def downvideo(parabaixar):
    print(sys.stderr)
    options = {'format': 'best', 'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),}
    with YoutubeDL(options) as ydl:
        ydl._out_files.error=sys.__stderr__
        for i in parabaixar:
            ydl.download([i])

def downsong(parabaixar):
    print(sys.stderr)
    options = {'format': 'bestaudio','outtmpl': os.path.join(destino, '%(title)s.mp3'),}
    with YoutubeDL(options) as ydl:
        ydl._out_files.error=sys.__stderr__
        for i in parabaixar:
            ydl.download([i])

def downsong2(parabaixar):
    options = {
        "format": "bestaudio",
        "outtmpl": os.path.join(destino, "%(title)s.mp3"),
    }

    with YoutubeDL(options) as ydl:
        print("error:", ydl._out_files.error)
        print("tipo:", type(ydl._out_files.error))
        return