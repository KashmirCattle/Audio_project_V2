#Python 3.8
#RUN BASE IN COMMAND LINE FOR DOWNLOADING
# print("RUN BASE IN COMMAND LINE MF")
import requests
from bs4 import BeautifulSoup
import os
import json
import subprocess as sp
import time

needed_word = []
final_list = []

 
def add_2_needed_word(bst_json_path, Channel_id, second_boo): #add to all "NULL_COULD_NOT_FIND" to "needed word"
    global final_list
    final_list = []
    with open(bst_json_path, 'r+') as f:
        data = json.load(f)
        # print(data)

        for count, item in enumerate(data):
            # print(item, count)
            if "NULL_COULD_NOT_FIND" in item:
                # print(item)
                split = item.split(" ")
                print(split[-1])
                search_channel(split[-1], Channel_id, second_boo)



def search_channel(word, channel_ID, second_boo): #Searches with filmot and added to final list
    filmot_link = 'https://filmot.com/search/' + word + '/5ahkLW00XTI/1?channelID=' + channel_ID 

    r = requests.get(filmot_link)

    doc = BeautifulSoup(r.text, "html.parser")
    # doc.find(id='nextVideoButton')

    try:
        if second_boo != 0: #second boo is number of extras skips
            for _ in range(second_boo): 
                href = doc.find(id='nextVideoButton')['href']
                
                r = requests.get('https://filmot.com' + href)
                doc = BeautifulSoup(r.text, "html.parser")

        url_and_time = doc.find(id="divVideoDetails").find(class_="col-6").find('a', href=True)['href']
        # print(url_and_time)
        (url, time) = url_and_time.split('&t=')
        time = time.replace('s', '')
        # print(video_link, time)
        
        final_lis_dict = {}
        final_lis_dict.update({'url':url,'time':time, 'word':word})
        print(final_lis_dict)
        final_list.append(final_lis_dict.copy())
        final_lis_dict.clear()

        # print(final_list)

    except Exception as e:
        print(word + " :COULD NOT BE FOUND")

    
def DOWNLOAD(video_folder_path, not_transcripted_audio_path, over_write_path): #Downloads every needed item in final_list

    video_dir_len = len(os.listdir(video_folder_path))

    for item in final_list:
        try:

            video_dir_len += 1

            yt_dl_AUDIO = "youtube-dl -f 140 --get-url '" + str(item['url']) + "'"
            yt_dl_VIDEO = "youtube-dl -f 136 --get-url '" + str(item['url']) + "'"

            start = int(item['time'])
            duration = 5



            real_audio_url = sp.getoutput(yt_dl_AUDIO) 
            ffmpeg_audio = "ffmpeg -y -ss " + str(start) + " -i '" + real_audio_url + "' -t " + str(duration) + " -c copy " + over_write_path

            check = os.system(ffmpeg_audio)
            if check != 0:
                print('Audio Donwload Fail')

            else:

                real_video_url = sp.getoutput(yt_dl_VIDEO) 
                ffmpeg_VIDEO = "ffmpeg -ss " + str(start) + " -i '" + real_video_url + "' -t " + str(duration) + " -c copy "+ video_folder_path+'/'+ str(video_dir_len) + item['word'] + ".mp4"

                check = os.system(ffmpeg_VIDEO)
                if check != 0:
                    print('Video Donwload Fail')
                    time.sleep(0.5)
                else:
                    ffmp_16_convert = "ffmpeg -i "+ over_write_path + " -ar 16000 "+not_transcripted_audio_path +'/'+ str(video_dir_len) + item['word'] + ".wav"
                    os.system(ffmp_16_convert)

        except Exception as e: 
            print('error', item, e)
            input('waiting for responce: ')
    






def run(audio_folder_path, video_folder_path, bst_json_path, Channel_id, not_transcripted_audio_path, second_boo, over_write_path):
    
    add_2_needed_word(bst_json_path, Channel_id, second_boo)

    print('')
    print(final_list)
    print('')
    
    DOWNLOAD(video_folder_path, not_transcripted_audio_path, over_write_path)


def Mc_run(video_folder_path, Channel_id, not_transcripted_audio_path, attempt, over_write_path, word):

    for x in range(1): #Have x for range in incase need to change number of runs
        try:
            search_channel(word, Channel_id, attempt)
            attempt += 1
        except:
            print(word, " COULD NOT BE FOUND")
            break

    # search_channel(word, Channel_id, second_boo += 1)
    DOWNLOAD(video_folder_path, not_transcripted_audio_path, over_write_path)



# add_2_needed_word('/Users/joaquinboyd/Coding/python/Audio_Project/LastWeekTN/Song/Best.Json', 'UC3XTzVzaHQEd30rQbuvCtTQ', True)

# print(final_list)