import os

PING_HOST='10.10.10.10'  # some host on the other side of the VPN


retcode = os.system('ping -c 1 %s' % PING_HOST)
if retcode: 
    print('e')





# person = 'Template_copy'
# song = 'Song'
# import os
# for file in os.listdir('/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/'):
#     if ('kary_audio' in file) and ('txt') not in file:
#         print(file)



# Kary_audio_path = '/Users/joaquinboyd/Coding/python/Audio_Project/_People_/'+person+'/'+song+'/kary_audio.wav'