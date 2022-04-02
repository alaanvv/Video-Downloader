''' Doc 
    Nesse código eu usei um sistema que
    eu considero organizado e me facilita
    a ler e mudar coisas, não sei se é uma
    maneira muito responsável, mas eu 
    distribuo tudo dentro de funções.

    Funções com o sufixo 'tree' servem pra 
    direcionar o algoritmo e fazer pequenas
    ações de acordo com as necessidades, se
    dividindo como galhos de uma árvore.
'''
# ---
#region Importando bibliotecas 

from pytube import YouTube, Playlist
from os import rename, mkdir

#endregion
# ---
#region Funções 

def start():
    '''
    Preparando o terreno e iniciando.
    '''
    link = input('\nLink:\n|> ')

    mode = input('\nType:\n[1] Video mp4\n[2] Audio mp4\n[3] Audio mp3\n|> ')

    try: mkdir('downloads') # Criando uma pasta pra guardar os arquivos gerados
    except: pass
    
    mode_tree(link, mode)

    if input('\nRestart: (y/n)\n|> ') == 'y': start() # Opção pra recomeçar sem ter que reabrir o exe

def mode_tree(link, mode):
    '''
    Separa playlists de videos
    '''

    if 'playlist' in link: playlist_tree(link, mode)
    else: video_tree(link, mode)

def video_tree(link, mode):
    '''
    Envia o objeto YouTube para a função de download
    '''

    yt = YouTube(link)

    if mode == '1':
        download_video(yt)

    elif mode == '2':        
        download_audio(yt)

    else:
        file = download_audio(yt)
        try: rename(file, file[:-3] + 'mp3')
        except: pass

def playlist_tree(link, mode):
    '''
    Itera sobre os vídeos da playlist os enviando para a função de download
    '''

    for yt in Playlist(link).videos:

        if mode == '1': 
            download_video(yt)

        elif mode == '1': 
            download_audio(yt)

        else: 
            file = download_audio(yt)
            try: rename(file, file[:-3] + 'mp3')
            except: pass

def title(yt):
    '''
    Printa o título do vídeo
    '''

    try: print('\n', yt.title) # Nomes dos vídeos podem ter caracteres desconhecidos que gerariam erros
    except: pass

def download_video(yt):
    '''
    Baixa usando o método get_highest_resolution
    e retorna o arquivo final
    '''

    title(yt)
    return yt.streams.get_highest_resolution().download('downloads')
    
def download_audio(yt):
    '''
    Baixa usando o método get_audio_only
    e retorna o arquivo final
    '''

    title(yt)
    return yt.streams.get_audio_only().download('downloads')

#endregion
# ---

start()
