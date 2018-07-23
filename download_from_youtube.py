#!/usr/bin/python3
import sys
import os
from pytube import YouTube
youtube_url = input('Input YouTube url: ')
#youtube_url = 'https://youtu.be/Cav9lT-UmW0'
yt = YouTube(youtube_url)
path = sys.path[0] + '/'
title = yt.title.replace('/','').replace('.','').replace(':','')
choose_va = ''
while(choose_va.lower() not in ['v','video','a','audio']):
    choose_va = input('Download video or audio (write v or a). Write quit or q to exit: ')
    if choose_va.lower() == 'v' or choose_va.lower() == 'video':
        print('Start downloading video: ')
        #yt.streams.filter(type='video').filter(subtype='mp4').get_by_itag(22).download()
        yt.streams.first().download()
    elif choose_va.lower() == 'a' or choose_va.lower() == 'audio':
        print('Start downloading audio: ')
        yt.streams.filter(type='audio').filter(subtype='mp4').first().download()
        os.rename(path + title + '.mp4', path + title + '.mp3')
    elif choose_va.lower() == 'q' or choose_va.lower() == 'quit':
        sys.exit()
    else:
        print('Wrong input')
