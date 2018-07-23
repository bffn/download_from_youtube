#!/usr/bin/python3
import sys
import os
from pathlib import Path
from pytube import YouTube
youtube_url = input('Input YouTube url: ')
home_path = str(Path.home()) + '/'
try:
    yt = YouTube(youtube_url)
except:
    print('Wrong YouTube url')
    sys.exit()
title = yt.title.replace('/','').replace('.','').replace(':','')
choose_va = ''
while(choose_va.lower() not in ['v','video','a','audio']):
    choose_va = input('Download video or audio (write v or a). Write quit or q to exit: ')
    if choose_va.lower() == 'v' or choose_va.lower() == 'video':
        tag_res = {}
        num = 0
        for elem in yt.streams.filter(type='video').filter(subtype='mp4').all():
            if str(elem).find('acodec=') != -1:
                first_dq = str(elem).find('"',str(elem).find('itag='))+1
                second_dq = str(elem).find('"', first_dq)
                itag = str(elem)[first_dq:second_dq]
                first_dq = str(elem).find('"',str(elem).find('res='))+1
                second_dq = str(elem).find('"', first_dq)
                res = str(elem)[first_dq:second_dq]
                num += 1
                tag_res[num] = [itag, res]
        print('Choose resolution: ')
        for key in tag_res:
            print(str(key) + ': ' + tag_res[key][1])
        choose_res = -1
        while(int(choose_res) < 1 or int(choose_res) > len(tag_res)):
            try:
                choose_res = input('Write from 1 to ' + str(len(tag_res)) + ' to choose resolution: ')
                int(choose_res)
            except ValueError:
                choose_res = -1
        print('Start downloading video: ')
        yt.streams.get_by_itag(int(tag_res[int(choose_res)][0])).download(output_path=home_path)
    elif choose_va.lower() == 'a' or choose_va.lower() == 'audio':
        print('Start downloading audio(It will take some time): ')
        yt.streams.filter(type='audio').filter(subtype='mp4').first().download(output_path=home_path)
        os.rename(home_path + title + '.mp4', home_path + title + '.mp3')
    elif choose_va.lower() == 'q' or choose_va.lower() == 'quit':
        sys.exit()
    else:
        print('Wrong input')
print('Download successful')
