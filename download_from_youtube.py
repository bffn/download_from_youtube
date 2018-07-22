#!/usr/bin/python3
import sys
from pytube import YouTube
youtube_url = input('Input YouTube url: ')
yt = YouTube(youtube_url)
choose_va = input('Download video or audio (write v or a): ')
if choose_va == 'v':
    print('Start downloading video: ')
    yt.streams.first().download()
elif choose_va == 'a':
    print('Start downloading audio: ')
    print(yt.streams.filter(type='audio').filter(subtype='mp4').first().download())
else:
    print('Wrong input')
