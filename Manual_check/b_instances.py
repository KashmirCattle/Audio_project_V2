#check for other instances and input if good

from pydub import AudioSegment 
from pydub.playback import play
import json
import time

person = 'test5' 
song = 'song'   
bst_json = '/Users/joaquinboyd/Coding/python/Audio_Project/people/'+person+'/'+song+'/best.json'
transcripted_audio_path = '/Users/joaquinboyd/Coding/python/Audio_Project/people/'+person+'/Sound/Transcripted'

General_transcript_json = '/Users/joaquinboyd/Coding/python/Audio_Project/people/'+person+'/Transcribe.json'
Mc_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/V2/Manual_check/MCt.json'

# error_words = [{'conf': 1.0, 'end': 0.78, 'start': 0.75, 'word': 'a', 'Audio_File': '14give.wav'}, {'conf': 0.992446, 'end': 2.19, 'start': 2.04, 'word': 'good', 'Audio_File': '5good.wav'}, {'conf': 1.0, 'end': 2.73, 'start': 2.52, 'word': 'and', 'Audio_File': '10a.wav'}, {'conf': 0.995989, 'end': 1.74, 'start': 1.399779, 'word': 'she', 'Audio_File': '8she.wav'}, {'conf': 1.0, 'end': 0.36, 'start': 0.24, 'word': 'you', 'Audio_File': '14give.wav'}, {'conf': 1.0, 'end': 3.03, 'start': 2.76, 'word': 'should', 'Audio_File': '17should.wav'}, {'conf': 1.0, 'end': 0.66, 'start': 0.508292, 'word': 'give', 'Audio_File': '14give.wav'}, {'conf': 1.0, 'end': 1.02, 'start': 0.66, 'word': 'some', 'Audio_File': '16some.wav'}]
# final_json0 = {
#   "result": [
#   ],
#   "text": "NULL"
# }

with open(Mc_json_path, 'r') as f:
    v = f.read()
    error_words = eval(v)


with open(General_transcript_json, 'r') as f:
    v = f.read()
    transcript_json = eval(v)


def playy(start, end, Audio_File):
    Audio_File = transcripted_audio_path + '/' + Audio_File

    sound = AudioSegment.from_file(Audio_File)

    x = sound[start*1000:end*1000]
    play(x)


# find_error_words()

#for each error word--
#make list of other instances of word from transcript
#play instance with number assosiated w it
#input number of best instance, or all bad


def check_instances(error_json): #play instance with number assosiated w it
    global transcript_json


    for count, i in enumerate(transcript_json['result']):
        if (i['word'] == error_json['word']) and (i != error_json): #if transcript word == error word; & not same instance

            print('-------------')
            print(i['word'], count)
            print('-------------')
            playy(i['start'], i['end'], i['Audio_File']) #play instance
            
            if count % 10 == 0:
                if input('break:break ') == 'break':
                    break

            

    while True:
        gb = input('All bad: return, good:#, relisten to number:r#: ')

        if gb.isnumeric() == True:
            transcript_json['result'][int(gb)]['conf'] = 1.1
            error_words.remove(item)
            break

        if len(gb) > 2:
            if gb[0] == 'r':
                gb = gb.replace('r', '')
                playy(transcript_json['result'][int(gb)]['start'], transcript_json['result'][int(gb)]['end'], transcript_json['result'][int(gb)]['Audio_File'])
        else:
            break

        if gb == 'break':
            break

    # print(final_json)
        


for item in error_words:
    print('---------')
    print(':error word:', item['word'])
    check_instances(item)
    print('---------')

for item in transcript_json['result']:
    if item['conf'] == 1.1:
        print(item)


# if True: #DUMP DATA
#     with open(Mc_json_path, 'w') as f:
#         json.dump(error_words, f, indent=2)

#     with open(General_transcript_json, 'w') as f:
#         json.dump(transcript_json, f, indent=2)
    

# print(error_words)

