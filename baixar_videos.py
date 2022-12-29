#renann.ntj
#pip install pytube & moviepy

from pytube import YouTube
import moviepy.editor as mp 
import re
import os
import time
link = input('Digite o link do vídeo: ')
path = input('Digite a pasta que queira salvar o vídeo: ')
yt = YouTube(link)

print('Baixando...')
ys = yt.streams.filter(only_audio=True).first().download(path)
print('Download completo.')
time.sleep(3)
os.system('clear')
print('Sucesso!')
