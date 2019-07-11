from __future__ import unicode_literals
import os, sys, time

def linux():
 print("============")
 print("   LINUX ")
 print("============\n")
 time.sleep(2.5)
 os.system("sudo apt-get update")
 os.system("sudo apt install python3-pip")
 os.system("pip3 install youtube-dl ")
 os.system("pip3 install pyperclip")
 os.system("clear")
 function()

def windows():
 print("=============")
 print("   WINDOWS  ")
 print("=============\n")
 time.sleep(2.5)
 print("\a")
 os.system("pip install youtube-dl")
 os.system("pip install pyperclip")
 os.system("cls")
 function()

def function():
 if sys.platform == 'linux':
  os.system("clear")
 elif sys.platform == 'win32':
  os.system("cls")	
 print("\033[;1;94m(For audio conversion: \033[;2;95mThis program requires ffmpeg, install it for Linux (and other command-line OSes) by running 'apt-get install ffmpeg'. For windows, You can download the package online and convert it manually......)")
 
 print("\033[1;33m \n*** Copy/Paste to you browser to view a list of youtube-dl supported sites ***\n")
 print(" https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md \n")
 print("Choose 1 or 2") 
 print("1. Take the url from the clipboard automatically")
 print("2. Type/paste The url manually")
 clip =input("===> ")
 if clip =='1':
  print("\033[3;32m[*]Extracting clipboard content.....\n")
  try:
   if pyperclip.paste() == '':
   	print("Your clipboard doesn't seem to havr any contents")
   	exit()
   url = pyperclip.paste()
   time.sleep(0.5)
  except NameError:
   print("There was a problem Try choosing option 2...")
  except pyperclip.PyperclipException:
   print("There doesn't seem to be any copy/paste mechanism for your os. Do try choosing option 2")
   time.sleep(3.5)
   function()
 elif clip =='2':
  print("\033[3;36m[*]Manual input....")
  time.sleep(0.5)
  url =input("Enter the video url ==> ")
  if url == '':
   print("You didnt provide any url")
   print("Exiting......")
   exit()
 print(" mp3 or mp4 ?")
 form =input("===> ")
 if form =='mp3':
  print("\033[3;35m[*]Retrieving audio format........")
  time.sleep(0.5)
  ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',}],
    }
  try:
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  except ModuleNotFoundError:
   print("\033[1;31;41mInstall the requirements first !!!")
   exit()
  except youtube_dl.utils.DownloadError as Error:
   print("Check your url or your connection")
   exit()
 elif form =='mp4':
  print("\033[3;36m[*]Extracting video format........")
  time.sleep(0.5)
  ydl_opts={'ext':'mp4'}
  try:
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  except youtube_dl.utils.DownloadError as Error:
   print("Check your connection or url")
   exit()
 else:
  print("\033[1;31mError, please follow the instructions ")
  
 
try:
  import youtube_dl
  import pyperclip
except ModuleNotFoundError:
  print("\033[3;91mYou dont have all the required modules")
  print("\033[2;37mWould you like the program to install them automatically?")
  print("Y or N")
  install =input(" ===> ")
  if install =='Y' or install =='y':
   print("[*]Installing please wait.......")
   time.sleep(2)
   print("[*]Checking your platform......\n")
   if sys.platform =='linux':
    linux()
   elif sys.platform =='win32':
    windows()
  elif install =='N' or install =='n':
   print(" Exiting......")
   time.sleep(2.53)
   exit()
  else:
   print("\033[1;31m Trouble maker")
   exit()

  
function()
    
    
    
