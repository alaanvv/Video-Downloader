from pytube import YouTube, Playlist
from os import rename, mkdir

# ---

def download(link):
    ''' Download the link to downloads '''

    videos = [video for video in Playlist(link)] if 'playlist' in link else [
        YouTube(link)]

    for video in videos:
        print(video.title)

        if mode == '1':
            video.streams.get_highest_resolution().download('downloads')

        elif mode == '2':
            video.streams.get_audio_only().download('downloads')

        else:
            file = video.streams.get_audio_only().download('downloads')
            try:
                rename(file, file[:-3] + 'mp3')
            except:
                pass

# ---

while 1:
    link = input('Link:\n|> ')
    mode = input('\nType:\n[1] Video mp4\n[2] Audio mp4\n[3] Audio mp3\n|> ')

    try:
        mkdir('downloads')
    except:
        pass

    download(link)

    if input('Restart: (y/n)\n|> ') != 'y':
        break
