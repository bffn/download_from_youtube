#!/usr/bin/python3
import sys
import os
from pytube import YouTube
youtube_url = input('Input YouTube url: ')
yt = YouTube(youtube_url)
path = sys.path[0] + '/'
title = yt.title.replace('/','').replace('.','').replace(':','')
choose_va = input('Download video or audio (write v or a): ')
if choose_va == 'v':
    print('Start downloading video: ')
    yt.streams.first().download()
elif choose_va == 'a':
    print('Start downloading audio: ')
    yt.streams.filter(type='audio').filter(subtype='mp4').first().download()
    os.rename(path + title + '.mp4', path + title + '.mp3')
else:
    print('Wrong input')
