from __future__ import unicode_literals
import os, sys, time


def linux():
    print("==++===========++==")
    print("       LINUX         ")
    print("==++===========++==\n")
    time.sleep(2.5)
    s = os.system
    s("sudo apt-get update")
    s("sudo apt install python3-pip")
    s("pip3 install youtube-dl")
    s("pip3 install pyperclip")
    s("clear")
    function()

def windows():
    print("==++===========++==")
    print("      WINDOWS       ")
    print("==++===========++==\n")
    time.sleep(2.5)
    s = os.system
    s("pip install youtube-dl")
    s("pip install pyperclip")
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
    print("2. Type/paste the url manually")
    clip = input("===> ")
    if clip == '1':
        print("\n[*]Extracting clipboard content........")
        try:
            url = pyperclip.paste()
            if url == '':
                print("Your clipboard doesn't seem to have any contents")
                print("[+]Exiting.....")
                exit()
                 
        except pyperclip.PyperclipException:
            print("Your platform doesn't seem to possess any copy/paste mechanism, Do try choosing option 2")
            time.sleep(3.5)

    elif clip == '2':
        print("\033[3;35m[*]Manual input....")
        time.sleep(0.5)
        url = input("Enter the video url ==> ")
        if url == '':
            print("You didn't provide any url")
            print("[+]Exiting......")
            exit()

    print("mp3 or mp4 ? \n('mp3 is audio and mp4 is video')")
    form = input("===> ")
    if form == 'mp3':
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
        except youtube_dl.utils.DownloadError:
            pass
            
            
    elif form == 'mp4':
        print("\033[3;36m[*]Extracting Video Format.........")
        time.sleep(0.5)
        ydl_opts = {'ext':'mp4'}

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except youtube_dl.utils.DownloadError:
            pass
        
    else:
        print("\033[1;31mError, Please follow the instructions.")


        
try:
    import youtube_dl
    import pyperclip
except ModuleNotFoundError:
    print("\033[3;91mYou dont have all the required modules.")
    print("\033[2;37mWould you like the program to install them automatically?")
    print("Y or N")
    install = input("====> ")
    if install == 'Y' or install == 'y':
        print("[*]Installing Please wait.......")
        time.sleep(2)
        print("Checking your platform.......\n")
        if sys.platform == 'linux':
            linux()
        elif sys.platform == 'win32':
            windows()
    elif install == 'N' or install == 'n':
        print("Exiting......")
        time.sleep(2.5)
        exit()
    else:
        print("\033[1;31mTrouble maker")
        exit()

function()        
