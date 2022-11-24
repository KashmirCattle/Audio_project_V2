#python 3.8
#play audio files 
#--> Prob NOT going to use at the moment might use

import os
from pydub import AudioSegment 
from pydub.playback import play
person = 'seb_test'

Mc_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/V2/Manual_check/MCt.json'
transcripted_audio_path = '/Users/joaquinboyd/Coding/python/Audio_Project/people/'+person+'/Sound/Transcripted'

with open(Mc_json_path, 'r') as f:
    v = f.read()
    error_words = eval(v)


def playy(start, end, Audio_File):
    Audio_File = transcripted_audio_path + '/' + Audio_File

    sound = AudioSegment.from_file(Audio_File)

    x = sound[start*1000:end*1000]
    play(x)
    
    return input('Good:g, bad:b, Repeat:r: ')


def inst(i): #each downloaded instance
    dir_list = os.listdir(transcripted_audio_path)
    for item in dir_list:
        item = ''.join([i for i in item if not i.isdigit()]).replace('.wav', '')
        if item == i['word']:
            while True:
                good_bad = playy(i['start'], i['end'], i['Audio_File'])
                if good_bad.lower() == 'g':
                    print(i['start'], i['end'], i['Audio_File'], ' MC w/ mp3towav')
                if good_bad.lower() == 'b': 
                    break
                if good_bad.lower() == 'r':
                    print('Repeating...')


for i in error_words:
    # print(i['word'])
    print(i)
    inst(i)
