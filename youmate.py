from __future__ import unicode_literals
import os, sys, time

def linux():
 print("\033[1;33m LINUX \n")
 os.system("sudo apt-get update")
 os.system("sudo apt install python3-pip")
 os.system("pip3 install youtube-dl ")
 os.system("pip3 install pyperclip")
 os.system("clear")
 function()

def windows():
 print("\033[1;33m WINDOWS \n")
 print("\a")
 os.system("pip install youtube-dl")
 os.system("pip install pyperclip")
 function()

def function():
 print("\033[;1;94m(For audio conversion: \033[;2;95mThis program requires ffmpeg, install it for Linux (and other command-line OSes) by running 'apt-get install ffmpeg'. For windows, You can download the package online and convert it manually......)")
 
 print("\033[1;33m \n*** Copy/Paste to you browser to view a list of youtube-dl supported sites ***\n")
 print(" https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md \n")
 print("Enter the URL") 
 print("\033[3;31m#### Type '1' if you want the program to access your clipboard Or '2' if you want to paste it manually ####")
 clip =input("===> ")
 if clip =='1':
  print("[*] Extracting clipboard content.....\n")
  try:
   url = pyperclip.paste()
  except NameError:
   print("There was a problem Try choosing option 2...")
   function()
 elif clip =='2':
  print("\033[3;35m[*] Manual input....")
  url =input("Enter the video url ==> ")
 print(" mp3 or mp4 ?")
 form =input("===> ")
 if form =='mp3':
  print("\033[3;35m[*] Retrieving audio format........")
  ydl_opts = {
      'format':'bestaudio',
      'preferredcodec':'mp3',
      'postprocessors':[{
          'key':'FFmpegExtractAudio',
          }]
      }
      
  try:
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  except ModuleNotFoundError:
   print("\033[1;31;41m Install the requirements first !!!")
   exit()
 elif form =='mp4':
  print("\033[3;34m [*] Extracting video format........")
  ydl_opts={'ext':'mp4'}
  try:
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  except ModuleNotFoundError:
   print("\033[1;31;41m Install the requirements first !!!")
   exit()
 else:
  print("\033[1;31m Error, please follow the instructions ")
  
 
try:
  import youtube_dl
  import pyperclip
except ModuleNotFoundError:
  print("\033[3;91m you dont have all the required modules")
  print("\033[2;36m Would you like the program to install them automatically?")
  print("Y or N")
  install =input(" ===> ")
  if install =='Y':
   print("[*]Installing please wait.......")
   print("[*]Checking your platform......")
   if sys.platform =='linux':
    linux()
   elif sys.platform =='win32':
    windows()
  elif install =='y':                          
   print("[*] Installing please wait.......")
   print("[*] Checking your platform......")
   if sys.platform =='linux':
    linux()
   elif sys.platform =='win32':
    windows()
    
  elif install =='N':
   print(" Exiting...")
   time.sleep(2)
   exit()
  elif install =='n':
   print(" Exiting...")
   time.sleep(2)
   exit()
  else:
   print("\033[5;34m Trouble maker")
   exit()

  
function()
