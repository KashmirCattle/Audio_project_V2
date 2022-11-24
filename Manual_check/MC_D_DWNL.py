# python 3.8
import os
print('BASE IN COMMAND LINE, Py 3.8')
#ALSO NEEDS TO BE IN V2 NOT UNDER MC FILE


import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/joaquinboyd/Coding/python/Audio_Project/V2')

# from bs4 import BeautifulSoup

# import importlib.util
# import sys

# file_path = '/Users/joaquinboyd/Coding/python/Audio_Project/V2/Download_wFilmot.py'
# module_name = 'Download_wFilmot'

# spec = importlib.util.spec_from_file_location(module_name, file_path)
# module = importlib.util.module_from_spec(spec)
# sys.modules[module_name] = module
# spec.loader.exec_module(module)

import Download_wFilmot

# spec = importlib.util.spec_from_file_location("Download_wFilmot", "/Users/joaquinboyd/Coding/python/Audio_Project/V2/Download_wFilmot.py")
# import Download_wFilmot


if __name__ == "__main__":
    #VPN, BASE, py38
    person = 'dad_test' #e.g "Linus"
    song = 'song'   #e.g "Mr. Spaceman"
    Channel_id = 'UCL_r1ELEvAuN0peKUxI0Umw'
    

    Kary_audio_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/'+song+'/kary_audio.wav'
    kary_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/'+song+'/kary.json'
    Bst_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/'+song+'/best.json'
    General_transcript_json = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Transcribe.json'


    #m4a
    audio_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Sound/m4a' #Not in use


    video_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Video'       
    not_transcripted_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Sound/Not_Transcripted' #dont end w '/'
    transcribed_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Sound/Transcripted'

    over_write_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Sound/OverWrite.m4a'

Mc_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/V2/Manual_check/MCt.json'


with open(Mc_json_path, 'r') as f:
    v = f.read()
    error_words = eval(v)

def num_of_instances(word): #how many page turns filmot needs to do
    cc = 0

    dir_list = os.listdir(transcribed_folder_path)
    for item in dir_list:
        item = ''.join([i for i in item if not i.isdigit()]).replace('.wav', '')

        if item == word:
            cc += 1

    return cc

    # for count, item in enumerate(dir_list):
        

# for item in error_words:

item = error_words[0]

attempt = num_of_instances(item['word'])
    # print(audio_folder_path, video_folder_path, Channel_id, not_transcripted_folder_path, attempt, over_write_path, item['word'])

# Download_wFilmot.Mc_run(video_folder_path, Channel_id, not_transcripted_folder_path, attempt, over_write_path, item['word'])
    # break
    