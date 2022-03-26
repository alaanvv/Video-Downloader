from pytube import YouTube

link = input('Link:\n|> ')
yt = YouTube(link)

type_mode = input('\n\nType:\n[1] Video\n[2] Audio\n|> ')

if type_mode == '1':
    yt.streams.get_highest_resolution().download()
else:
    yt.streams.get_audio_only().download()