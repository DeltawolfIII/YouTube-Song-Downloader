from __future__ import unicode_literals
import youtubedl
import sys
asciiapollo = """\


  (                  (   (       
   )\                 )\  )\      
((((_)(   `  )    (  ((_)((_) (   
 )\ _ )\  /(/(    )\  _   _   )\  
 (_)_\(_)((_)_\  ((_)| | | | ((_) 
  / _ \  | '_ \)/ _ \| | | |/ _ \ 
 /_/ \_\ | .__/ \___/|_| |_|\___/ 
         |_|                                                                                                                                                           
"""
print(asciiapollo)
if sys.version_info[0] < 3:
	print("Python version lower than 3, please run \"py2.py\"")
if sys.version_info[0] < 3:
    sys.exit(0)
URL = input("Enter a song name or a YouTube playlist URL: ")
if "youtube.com/" not in URL:
    URL = URL + "audio"

quality = input("What quality would like your song to be? (low, medium, or high) ")
if quality == 'low':
	bitrate = '96'
if quality == 'medium':
	bitrate = '192'
if quality == 'high':
	bitrate = '320'


print("Downloading song, please wait...")

ytdl_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': bitrate,
    }],
    'default_search': 'auto',
    'quiet': 'on'
}
with youtubedl.YoutubeDL(ytdl_options) as ytdl:
   ytdl.download([URL])

print("Your song has finished downloading.")
