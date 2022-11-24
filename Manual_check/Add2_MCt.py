#ADD TO ERROR_WORDS

from pydub import AudioSegment 
from pydub.playback import play
import json

person = 'test5' 
song = 'song'   
bst_json = '/Users/joaquinboyd/Coding/python/Audio_Project/people/'+person+'/'+song+'/best.json'
transcripted_audio_path = '/Users/joaquinboyd/Coding/python/Audio_Project/people/'+person+'/Sound/Transcripted'
Mc_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/V2/Manual_check/MCt.json'
General_transcript_json = '/Users/joaquinboyd/Coding/python/Audio_Project/people/'+person+'/Transcribe.json'


with open(Mc_json_path, 'r') as f:
    v = f.read()
    error_words = eval(v)


def playy(start, end, Audio_File):
    Audio_File = transcripted_audio_path + '/' + Audio_File

    sound = AudioSegment.from_file(Audio_File)

    x = sound[start*1000:end*1000]
    play(x)


def find_error_words():
    with open(bst_json, 'r') as f:
        v = f.read()
        json0 = eval(v)

        for item in json0:
            print(item['word'])
            playy(item['start'], item['end'], item['Audio_File'])

            inpt = input("good, bad, repeat, end")

            if inpt == 'b':
                if item not in error_words:
                    error_words.append(item)
            if inpt == 'g':
                pass
            if inpt == 'repeat':
                playy(item['start'], item['end'], item['Audio_File'])
            if inpt == 'end':
                break

    with open(Mc_json_path, 'w') as f2:
        json.dump(error_words, f2, indent=2)


find_error_words()