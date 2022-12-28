# Song Stitching Automation
## Overview
There is a popular trend on the internet to combine different instances of words someone has said into a song. Here's an example of someone doing this https://www.youtube.com/watch?v=74gx0v5ZJzw. Maestro Ziikos (the person behind the Trump Havanna video) manually stitches together clips of words into a song. My program automates this process, with a Youtube Channel ID and a song transcript as an input, the program will output a completed video.
 
 
## How it works:
This program consists of 5 files that contribute to the final product.
 
Srt_to_Json can be ignored at the moment while I'm in the process of converting from Vosk machine learning model to Openai whisper.
Step for use:
 
1. You need a Song transcription. With heavy auto-tune and loud background noise transcribing a song directly will not work. To get around this either find a word by word transcription of a song online, or use the C_KARY.py file. This file will get your karaoke version of the song which will be transcribable.
 
2. The Create_bst.py file will search your already downloaded audio transcriptions of your person to find what words need to be downloaded. Create_bst.py will make a json file that has what clips of words you already have downloaded and a placeholder for words that still need to be downloaded.
 
3. Download_wFilmot.py uses https://filmot.com/ to search Youtube's transcripts (unfortunately not word timestamps, but sentences). Then with Youtube-dl it will download audio clips on youtube from your channel where each needed word is said. Will also download video clips for later use.
 
4. D_Vosk is run, this will transcribe the newly downloaded audio adding the results to a json file.
 
5. Create_bst.py is run again. This will re-check what words are missing. Sometimes the youtube transcriptions and Vosk transcriptions aren't the same so words may be missing.
 
6. This process is repeated, finding new clips where the word is said, and transcribing them until create_bst.py finds no missing words.
 
7. At this point you have your word for word transcript of a song (from C_KARY.py), and all clips words downloaded.
 
8. Now, Combine_audio.py will combine all clips of words into their appropriate locations by looking at your C_KARY transcript.
 
9. Now Video_comb will do the same thing with the video file.
 
10. Now combine the video and audio with ffmpeg and you have your final product.
 
 
 
## How to run:
This project is run with A_Group_runV2.py . This file imports other files and executes them at the correct times. To get a final product you need a bit of setup. First in file you need a folder titled _People_. Then in it a folder title someone's name (e.g John).
Important to note, All audio needs to be .wav and 16000 Hz sampling rate
 
In the John folder you need:
 
```comb.json (empty)
Conb_oWrite.wav (empty)
Sound           (empty folder)
Video           (empty folder)

Transcribe.json
Needs the following Json setup
{
 "result": [
 ],
 "text": "NULL"
}
```
 
In the John folder you will make a folder for each song. (e.g Penny Lane)

Penny Lane should have the following:
```
Best.Json (empty)
Final_output.wav (empty)
Your Karaoke version of a song in .wav
 
 
Kary.json
Needs the following Json setup
{
 "result": [
 ],
 "text": "NULL"
}
```
 
Now with all this setup enter the Peron, Song, and Channel_id info into A_Group_runV2.py
The Channel_id is the youtube channel id where you want your audio to be coming from.
After you run that (with a VPN on) run the combine_audio.py and Video_comb.py files.
