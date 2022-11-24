#Record Kary Audio store .wav under; Person > Song (Next to .Json files), (Record w/ C_Kary.py)

import D_Vosk
import Create_bst
# import Src_Dnl
import Download_wFilmot

if __name__ == "__main__":
    #VPN, BASE, py38
    person = 'Template_copy' #e.g "Linus"
    song = 'song'   #e.g "Mr. Spaceman"
    Channel_id = 'UCsXVk37bltHxD1rDPwtNM8Q'
    

    Kary_audio_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/kary_audio.wav'
    kary_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/kary.json'
    Bst_json_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/best.json'
    General_transcript_json = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Transcribe.json'


    #m4a
    audio_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Sound/m4a' #Not in use


    video_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Video'       
    not_transcripted_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Sound/Not_Transcripted' #dont end w '/'
    transcribed_folder_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Sound/Transcripted'

    over_write_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/Sound/OverWrite.m4a'


input("CHECK_inputed_info / use a VPN / use 'BASE' in command line")
input("check __name__ info")



# Convert Karyoke audio into transcript  Vosk   transcript under; person > Song > Kary.Json



# D_Vosk.run_single_file(Kary_audio_path, 'kary_audio.wav', kary_json_path) # _/
Create_bst.initial_bst_add(kary_json_path, Bst_json_path, General_transcript_json) # _/


for attempt in range(4):
    Download_wFilmot.run(audio_folder_path, video_folder_path, Bst_json_path, Channel_id, not_transcripted_folder_path, attempt, over_write_path)
    D_Vosk.run_folder(not_transcripted_folder_path, General_transcript_json, transcribed_folder_path)
    Create_bst.initial_bst_add(kary_json_path, Bst_json_path, General_transcript_json)



print('')
print('Manual testing -/')
print('Pydub runs on py 3.6')

