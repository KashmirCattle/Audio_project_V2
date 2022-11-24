#Python 3.8
#RUN BASE IN COMMAND LINE FOR DOWNLOADING
from typing import Final
import requests
from bs4 import BeautifulSoup
import os
from datetime import timedelta
import json
import subprocess as sp

needed_word = []
final_list = []

#{'url': 'https://www.youtube.com/watch?v=5ahkLW00XTI', 'time': '164', 'word': 'test2'}
#youtube-dl -f 140 -x --audio-format wav 'https://www.youtube.com/watch?v=YKsQJVzr3a8' --postprocessor-args "-ar 16000"

#Seach a channel for a specific word, [video url] and [time word is said] is returned.
# last week tonight channel id = UC3XTzVzaHQEd30rQbuvCtTQ 
 
def add_2_needed_word(bst_json_path, Channel_id, second_boo): #add to all "NULL_COULD_NOT_FIND" to "needed word"
    with open(bst_json_path, 'r+') as f:
        data = json.load(f)
        # print(data)

        for count, item in enumerate(data):
            # print(item, count)
            if "NULL_COULD_NOT_FIND" in item:
                print(item)
                split = item.split(" ")
                print(split[-1])
                search_channel(split[-1], Channel_id, second_boo)

                # if var == "not found on filmot":
                #     data[count] = "not found on filmot"
        
        # f.seek(0)  
        # json.dump(data, f, indent=2)  
        # f.truncate()      



def search_channel(word, channel_ID, second_boo): #Searches with filmot and added to final list
    filmot_link = 'https://filmot.com/search/' + word + '/5ahkLW00XTI/1?channelID=' + channel_ID 

    r = requests.get(filmot_link)

    doc = BeautifulSoup(r.text, "html.parser")
    # doc.find(id='nextVideoButton')

    try:
        if second_boo == True:
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
        # return "not found on filmot"

    
def DOWNLOAD(audio_folder_path, video_folder_path, not_transcripted_audio_path): #Downloads every needed item in final_list
    # ARE_U_USING_a_VPN = input("USE A VPN: ")
    audio_dir_len = len(os.listdir(not_transcripted_audio_path)) # later should only use video len
    video_dir_len = len(os.listdir(video_folder_path))

    # num += 1  #ALREADY PLUS ONE CUZ HIDDIN FILE
    for item in final_list:
        try:
            audio_dir_len += 1
            video_dir_len += 1

            yt_dl_AUDIO = "youtube-dl -f 140 --get-url '" + str(item['url']) + "'"
            yt_dl_VIDEO = "youtube-dl -f 136 --get-url '" + str(item['url']) + "'"

            # print(yt_dl_AUDIO)
            # print(yt_dl_VIDEO)

            real_audio_url = sp.getoutput(yt_dl_AUDIO) 
            real_video_url = sp.getoutput(yt_dl_VIDEO) 
            

            # start = timedelta(seconds=item['start'])
            # duration = timedelta(seconds=item['duration'])
            start = int(item['time'])
            duration = 5


            ffmpeg_VIDEO = "ffmpeg -ss " + str(start) + " -i '" + real_video_url + "' -t " + str(duration) + " -c copy "+ video_folder_path+'/'+ str(video_dir_len) + item['word'] + ".mp4"
            # ffmpeg_audio = "ffmpeg -ss " + str(start) + " -i '" + real_audio_url + "' -t " + str(duration) + " -c copy "+ audio_folder_path+'/' + str(num) + item['word'] + ".m4a"
            ffmpeg_audio = "ffmpeg -y -ss " + str(start) + " -i '" + real_audio_url + "' -t " + str(duration) + " -c copy /Users/joaquinboyd/Coding/python/Audio_Project/Ariana_Grande/Sound/m4a/OverWrite.m4a"

            # print(ffmpeg_audio)
            # print(ffmpeg_VIDEO)
            # ffmpeg_audio = "ffmpeg -ss " + str(start) + " -i '" + real_audio_url + "' -t " + str(duration) + " -c copy /Users/joaquinboyd/Downloads/python/lyt_p_not_done" + str(num) + ".m4a" 


            os.system(ffmpeg_audio)
            os.system(ffmpeg_VIDEO)

            ffmp_16_convert = "ffmpeg -i /Users/joaquinboyd/Coding/python/Audio_Project/Ariana_Grande/Sound/m4a/OverWrite.m4a" + " -ar 16000 "+not_transcripted_audio_path +'/'+ str(audio_dir_len) + item['word'] + ".wav"
            os.system(ffmp_16_convert)



        except Exception as e: 
            print('error', item, e)
            input('waiting for responce: ')
    
def convert_2_16bit(audio_folder_path, not_transcripted_audio_path):
    for file in os.listdir(audio_folder_path): #---> lyt_p_not_done
        if file.endswith(".m4a"):
            print(file)
            file_no_m4a = file[:-4]

            ffmp_16_convert = "ffmpeg -i "+audio_folder_path + file + " -ar 16000 "+not_transcripted_audio_path + file_no_m4a + ".wav"
            print(ffmp_16_convert)
            os.system(ffmp_16_convert)
    print("MAKE IT OVER WRITE LATER ON OK")





def run(audio_folder_path, video_folder_path, bst_json_path, Channel_id, not_transcripted_audio_path, second_boo):
    # audio_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/Ariana_Grande/Sound/m4a/'
    # video_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/Ariana_Grande/Video/'
    # bst_json_path = ''

    # Channel_id = 'UC9CoOnJkIBMdeijd9qYoT_g'

    # input("CHECK_inputed_info / use a VPN / use 'BASE' in command line")

    add_2_needed_word(bst_json_path, Channel_id, second_boo) #calls on seach channel -/ completes final_list
    
    # print(final_list)

    DOWNLOAD(audio_folder_path, video_folder_path, not_transcripted_audio_path)


# run()


# convert_2_16bit()
    

