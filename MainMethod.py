import os
import webbrowser
import time
import pathlib
from time import sleep

#rickrolling url
url = 'https://youtu.be/dQw4w9WgXcQ'
url2 = 'you just got rickrolled'
webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
#opens the urls 3 times
for x in range(0, 3):
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
