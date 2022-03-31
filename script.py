from pytube import YouTube, Playlist

link = input('Link:\n|> ')

type_mode = input('\n\nType:\n[1] Video\n[2] Audio\n|> ')

if type_mode == '1':
    
    if 'playlist' in link:
        for yt in Playlist(link).videos:
            try: print(yt.title) # os nomes dos vídeos podem ter caracteres desconhecidos
            except: pass

            yt.streams.get_highest_resolution().download()
            
    else:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download()
else:
    if 'playlist' in link:
        for yt in Playlist(link).videos:
            try: print(yt.title)
            except: pass
            yt.streams.get_audio_only().download()
            
    else:
        yt = YouTube(link)
        yt.streams.get_audio_only().download()