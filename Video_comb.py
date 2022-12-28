#THIS IS THE ONE I USE!!---------------------
import json
import time

# from typing_extensions import final
# from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, CompositeAudioClip, AudioFileClip, CompositeVideoClip
from moviepy.editor import *
# from moviepy.tools import find_extension
# from numpy.core.fromnumeric import clip

# final_clip = VideoFileClip("/Users/joaquinboyd/Downloads/python/Obam_test/linus_Dance.mp4").subclip(0, 10)    
# clip1 = VideoFileClip('/Users/joaquinboyd/Downloads/python/Obam_test/linus_one.mp4').subclip(372.03, 373.109883)
# clip1 = clip1.set_start(5)
# video = CompositeVideoClip([f inal_clip, clip1])
#-------------------------------------------DO___ --n\\t- ___RUN-----------------------------------------------------------------------------
#region  
if __name__ == "__main__":
    person = 'LastWeekTN' #e.g "Linus"
    song = 'song'   #e.g "Mr. Spaceman"
    

    Bst_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/'+song+'/best.json'
    kary_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/'+song+'/kary.json'

    General_transcript_json = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Transcribe.json'

    transcribed_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Sound/Transcripted'
    video_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/'+person+'/Video/' #w/ the '/'

    dancin_clip = '/Users/joaquinboyd/Coding/python/Audio_Project/linus_Dance.mp4'     

#endregion




# BACKGROUND = VideoFileClip(dancin_clip) # lengthen for lat4er

final_list = [] #BACKGROUND


f = open(kary_json_path, 'r') #Kary
data = json.load(f)

f2 = open(Bst_json_path, 'r') #Best
data2 = json.load(f2)


# def speed_change(mp4_file, speed):
#     pass

def add_word_to_complete_Video():
    # time.sleep(1)
    global final_vid

    karyoke_data = data['result'].pop(0) #a popped off dict of the acutal song (love_again)

    pos = (karyoke_data["start"])  #positon

    best_data = data2.pop(0)   #a popped off dict of the matching words (sng2_lev.json)
    # mp4_file = best_data['Audio_File'][:-7]+'.mp4'

    try:
        next_clip = data['result'][0]

        duration = next_clip['start'] - karyoke_data['start']
    except:
        duration = karyoke_data['end'] - karyoke_data['start']   #LAST WORD

    print('------')
    # clip1 = VideoFileClip('/Users/joaquinboyd/Downloads/python/Obam_test/' + mp4_file).subclip(best_data['start'], best_data['end'])

    # if '_16' in best_data['Audio_File']:
    #     mp4_file = best_data['Audio_File'][:-7]+'.mp4'
    # clip1 = VideoFileClip('/Users/joaquinboyd/Downloads/python/lPhrase_video/' + mp4_file).subclip(best_data['start'], best_data['end'])
    mp4_file = best_data['Audio_File'][:-3]+'mp4'
    clip1 = VideoFileClip(video_folder_path + mp4_file).subclip(best_data['start'], best_data['end'])
    print('pos: ', pos)
    clip1 = clip1.set_start(pos)
    # clip1 / x = duration// x = clip1/duration
    clipdur = clip1.duration
    multi_pi = clipdur / duration #duration = next_clip['start'] - data['start']
    if not multi_pi < 0.3:
        clip1 = clip1.fx( vfx.speedx, multi_pi)

    final_list.append(clip1)
    # final_vid = CompositeVideoClip([final_vid, clip1])
    # complete_audio = complete_audio.overlay(sound2, position=pos*1000) #--nedd
with open(Bst_json_path, 'r') as f:
    ff = json.load(f)
    n = len(ff)

for x in range(n):  #normaly n
    add_word_to_complete_Video()
# next_clip = data['result'][0]
# print(type(next_clip), type(data['result']))
# duration = next_clip['start'] - data['result']['start']
# final_vid.preview()
# print(happy_list)
final_vid = CompositeVideoClip(final_list)
final_vid.write_videofile("test_un_million2.mp4") 
f.close()
f2.close()