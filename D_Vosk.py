#!/usr/bin/env python3
from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import json
import shutil

# sample_rate=16000
# model = Model("/Users/joaquinboyd/Downloads/python/vosk-model-en-us-daanzu-20200905-lgraph")
# rec = KaldiRecognizer(model, sample_rate)


def initiate():
    SetLogLevel(0)
    global sample_rate
    global rec

    if not os.path.exists("/Users/joaquinboyd/Coding/python/vosk-model-en-us-daanzu-20200905-lgraph"):
        print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit (1)

    sample_rate=16000
    model = Model("/Users/joaquinboyd/Coding/python/vosk-model-en-us-daanzu-20200905-lgraph")
    rec = KaldiRecognizer(model, sample_rate)

def run(Audio_path, Audio_N, transcript_json):
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                                Audio_path,
                                '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                                stdout=subprocess.PIPE)

    while True:
        data = process.stdout.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # print(rec.Result())
            pass
        else:
            # print(rec.PartialResult())
            pass
        # print(rec.FinalResult())

    a_dictionary = {"Audio_File": Audio_N} #this is a dictionary
    json1 = rec.FinalResult()
    json1 = eval(json1)

    for i in json1['result']:
        i.update(a_dictionary)

    with open(transcript_json, 'r') as fp:
        v = fp.read()
        json0 = eval(v)
        
        for i in json1['result']:
            json0['result'].append(i)

        # for item in json0['result']:
        #     print(item)
        with open(transcript_json, 'w') as f:  #'song_infoo/sucker/skr_kary.json'
            json.dump(json0, f, indent=2)

            

def run_single_file(audio_path, ad_name, transcript_json): #transcript_json would probaly be kary.json
    initiate()
    run(audio_path, ad_name, transcript_json)


def run_folder(folder_path, transcript_json, new_folder_path):
    
    for Audio_name in os.listdir(folder_path):
        try:
            if Audio_name != '.DS_Store':
                initiate()
                # if move_file_path != 'NULL':
                Audio_path = folder_path + '/' + Audio_name
                moved_file_path = new_folder_path + '/' + Audio_name

                shutil.move(Audio_path, moved_file_path)
                

                run(moved_file_path, Audio_name, transcript_json)


                    
        except Exception as e:
            print(e, '|ERROR|', Audio_name)


#WARNING: RUNING CODING IN FILE WILL AFFECT IMPORTS
if __name__ == "__main__":
    run_single_file('/Users/joaquinboyd/Desktop/Audio_Junk/For_sure_abs.wav', 'Ocean_man.wav', '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/Tom_Scott/Transcribe.json')