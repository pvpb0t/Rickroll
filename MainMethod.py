import os
import webbrowser
import time
import pathlib
from time import sleep
import tkinter.messagebox

#rickrolling url
url = 'https://youtu.be/dQw4w9WgXcQ'
url2 = 'you just got rickrolled'
#downloading video
url3 = 'https://cdn.discordapp.com/attachments/751378848913948734/875841534879203348/funds.mp4'
webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url3)

#shows windows error msg
tkinter.messagebox.showerror('Yeah, you kinda screwed up', 'you just got rickrolled')


#opens the urls 3 times
for x in range(0, 5):
    webbrowser.get('chrome').open(url)
    webbrowser.get('chrome').open(url2)
    webbrowser.get('chrome').open(url)
    sleep(1)

sleep(5)
#creates the txt
fh = open('rickrolled.txt', 'w')


try:
    for i in range(100):
        fh.write("rickrolled number %d\n" % (i+1))
finally:
    fh.close()

fh = open('rickinjector.dll', 'w')
fh = open('rickloader.bat', 'w')
#
