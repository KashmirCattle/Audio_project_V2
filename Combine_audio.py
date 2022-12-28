
from pydub import AudioSegment
from pydub.playback import play
import json
import time 
import librosa
import soundfile

person = ''
song = ''

Bst_Json_file = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/Best.Json'
Kary_Json_File = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/Kary.json'
Output_File = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/Final_output.wav'
Transcripted_audio_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Sound/Transcripted'
conb_overwrite_file = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Conb_oWrite.wav'

kary_audio = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/kary_audio.wav'

pitch_ratio = {0.5:12, 0.6:9, 0.7:6.5, 0.8:4, 0.9:1.5, 1:0, 1.1:-2, 1.2:-5}

ins = AudioSegment.from_file(kary_audio)   #normally need (instermental) can also use kary_audio
ins_dur = ins.duration_seconds


complete_audio = AudioSegment.silent(duration=ins_dur * 1000)

f = open(Kary_Json_File, 'r') #kary json
karyoke_data = json.load(f)

f2 = open(Bst_Json_file, 'r') #Bst_json
bst_data = json.load(f2)

def speed_change(sound, speed=1.0):

    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def pitch_change(multi_pi): #Not Currently using 
    x_steps = pitch_ratio[round(float(multi_pi), 1)]

    y2, sample_r = librosa.load(conb_overwrite_file, sr=16000) 
    y_third = librosa.effects.pitch_shift(y2, sample_r, n_steps=x_steps) #may want to have a constart pitch instead OR GET PITCH OF ACTUAL SONG AND COMPARE IT
    soundfile.write(conb_overwrite_file, y_third, sample_r)

def add_word_to_complete_aduio():
    global complete_audio
    # global pitch_ratio 
    print('--------')
    # q_lis = ['light', 'then', 'lawn']
    const_vol = -15
    kary_pop = karyoke_data['result'].pop(0) #a popped off dict of the acutal song (kary)
    pos = (kary_pop["start"]) #positon - see line 44

    Bst_pop = bst_data.pop(0)           #a popped off dict of the matching words (sng2_lev.json)
    # Audio_Name = Bst_pop['Audio_File']

    Audio_Name = Bst_pop['Audio_File']
    sound = AudioSegment.from_file(Transcripted_audio_path+'/'+Audio_Name)



    word = sound[Bst_pop['start']*1000:Bst_pop['end']*1000] #This is the word (cut out of an audio clip)
    Bst_dur = Bst_pop['end'] - Bst_pop['start']
    

    print(Bst_pop)
    # word.export(Output_File, format="wav")



    Kary_dur = kary_pop['end'] - kary_pop['start']
    multi_pi = Bst_dur / Kary_dur
    # multi_pi * 2   #REMOVE THIS LOL
    if multi_pi > 1.2: #The point of all of this is to limit the amount that a word can be stretched
        multi_pi = 1.2
    if multi_pi < 0.45:
        multi_pi = 0.5


    # if len(Bst_pop['word']) < 3 or Bst_pop['word'] in q_lis:
    # #     chng_vol = chng_vol - 10
    #     word = word - 10
    #     word.fade(to_gain=+10, start=(0*1000), duration=int(duration*1000)) 

    # print(chng_vol, 'c vol', volume) # v + x = dv //// dv - v = x ////// -24 + x = -15 
    print('--')

    if len(Bst_pop['word']) > 1000:   #MAKE > 0 IF YOU WANT THIS TO RUN
        print(Bst_pop['word'], multi_pi)
        word = speed_change(word, multi_pi)

        word.export(conb_overwrite_file, format="wav")
        pitch_change(multi_pi)
        word = AudioSegment.from_file(conb_overwrite_file)

    # chng_vol = const_vol - word.dBFS
    # word = word + chng_vol
    chng_vol = const_vol - word.dBFS
    word = word + chng_vol
    print(pos)
    
    # clip_of_word = match_vol[kary_pop['start']*1000:kary_pop['end']*1000]
    # clip_volume = clip_of_word.dBFS
    # loudness_difference = clip_volume - word.dBFS
    # word.apply_gain(loudness_difference)

    complete_audio = complete_audio.overlay(word, position=pos*1000) #--nedd


with open(Bst_Json_file, 'r') as f: #NUMBER OF ITEMS IN SNG2_LEV
    ff = json.load(f)
    n = len(ff)

print(n)
for x in range(n):    #should normally be for x in range n
    add_word_to_complete_aduio()

# complete_audio.export("/Users/joaquinboyd/Desktop/ok_whatevs.wav", format="wav")

# complete_audio = complete_audio[:10*1000]
# play(complete_audio)
# new = complete_audio.low_pass_filter(5000).high_pass_filter(200)

complete_audio.export(Output_File, format="wav")
# play(complete_audio)

f.close()
f2.close() 
