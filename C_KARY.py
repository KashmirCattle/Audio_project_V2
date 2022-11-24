#Python 3.6
import multiprocessing 
from multiprocessing import Queue
import pyaudio
import wave
import time
from pydub import AudioSegment

song_name = '/Users/joaquinboyd/Money.wav' #path to song
output_wav = '/Users/joaquinboyd/Desktop/Money4.wav'



s_t = time.time()

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
# seconds = 6
# filename = "rec_output.wav"

saved_chekpoint = 0
chunk = 1024
glob_frames = []




def play(queue):
    global saved_chekpoint
    _running = True
    audio = pyaudio.PyAudio()

    chunktotal = 0
    wf = wave.open(song_name, 'rb')

    stream = audio.open(format =audio.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = wf.getframerate(),output = True)
    # print(wf.getframerate())
    # read data (based on the chunk size)
    data = wf.readframes(chunk)

    #THIS IS THE TOTAL LENGTH OF THE AUDIO
    audiolength = wf.getnframes() / float(wf.getframerate())

    while _running:
        if data != '':
            stream.write(data)
            
            chunktotal = chunktotal + chunk

            data = wf.readframes(chunk)

            if queue.empty() == False:
                
                msg = queue.get()  
                if msg == 'SAVE':
                    current_seconds = chunktotal/float(wf.getframerate())  
                    # print(saved_chekpoint, current_seconds)
                    saved_chekpoint += current_seconds
                if msg == "MISTAKE":
                    # current_seconds = chunktotal/float(wf.getframerate())  
                    # print(saved_chekpoint, current_seconds, 'M1')

                    chunktotal = 0 #Stars playing from last checkpoint so resent time from last checkpoint
                    wf.setpos(int(saved_chekpoint * wf.getframerate())) #Play from last checkpoint

                    # current_seconds = chunktotal/float(wf.getframerate())  
                    # print(saved_chekpoint, current_seconds, "m2")
                if msg == "STOP":
                    break
            # current_seconds = chunktotal/float(wf.getframerate())
            # print(current_seconds, wf.getframerate(), chunktotal)
            # st += 100000000
            # wf.setpos(int(180 * wf.getframerate()))  #180 = time in seconds
            # _running = False

        if data == b'':
            break

    # cleanup stream
    stream.close()


def record(queue): #Simpily records and add into global_frames/ then saves 

    global glob_frames  #FIND WAY TO APPEND TO GLOB-FRAMES WITHOUT BREAKING IT

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,   
                    input=True)

    frames = []  # Initialize array to store frames   #MAYBE HAVE FRAMES_FINAL (ADD TO AFTER SAVE) AND FRAMES_NOT_FINAL WITH THE UNSAVED FRAMES
 
    # with open('output.wav', 'rb') as fd:
    #     contents = fd.read()
    #     frames.append(contents)
    def save_rec():  #WRITE AUDIO(FRAMES) INTO REC_OUTPUT
        # print(len(glob_frames))
        wf = wave.open(output_wav, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(glob_frames))  #bytes
        wf.close()

    while True:
        if queue.empty() == False:
            msg = queue.get()  
            if msg == 'SAVE':
                # save_rec() #ADD TO GLOBAL_FRAMES?
                for item in frames:
                    glob_frames.append(item)
                # break
            if msg == 'MISTAKE':
                frames = [] # FOREGET UNSAVED FRAMES
            if msg == 'STOP':
                for item in frames:
                    glob_frames.append(item)
                save_rec()
                break



        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file

# percentage = (self.chunktotal/wf.getnframes())*100
    # Store data in chunks for 3 seconds



def start_input(rec_queue, play_queue):
    # global saved_chekpoint
    while True:
        var = input('m/sa/st: ')
        if var == 'm':
            play_queue.put('MISTAKE') 
            rec_queue.put('MISTAKE') #One mistake for play and one for record 

            time.sleep(0.5)

        if var in ['s', 'save', 'sa']:
            rec_queue.put('SAVE') #KEEP PLAYING AND RE-START RECORDING (WITH SAVE) TEMP_WRITE.wav
            play_queue.put('SAVE')
            time.sleep(0.5)

        if var in ['stop', 'st']:
            rec_queue.put('STOP') # STOPS PLAYING AND RECORDING 
            play_queue.put('STOP')
            break





if __name__ == "__main__": 
    rec_queue = Queue()
    play_queue = Queue()

    start = time.time()
    record_p1 = multiprocessing.Process(target=record, args=((rec_queue), ))
    # play(play_queue)
    play_p2 = multiprocessing.Process(target=play, args=((play_queue), ))
    # play_p3 = multiprocessing.Process(target=print_lyrics, args=((pqueue), ))
    # p2.daemon = True
    record_p1.start()
    play_p2.start()
    # play_p3.start()
    time.sleep(1)
    start_input(rec_queue, play_queue)

print(time.time() - s_t)



# if add == True: #APPEND REC OUTPUT INTO FRAMES[] DONT THINNK I NEED THIS
#     with wave.open('rec_output.wav') as fd:
#         params = fd.getparams()
#         _frames = fd.readframes(1000000)
#         frames.append(_frames)