import youtube_dl
options = {}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=oqXQkx-BATQ'])
