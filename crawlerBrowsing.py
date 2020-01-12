# !pip3 install xlrd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import random
import time
# import xlrd
import csv

# from pynput.keyboard import Key, Controller
# TODO , If the sit ends with .net may need to replace it.
with open('C:/Users/97250/Desktop/top-1m.csv', 'r') as f:
    reader = csv.reader(f)
    URLS = []
    i = 0
    for row in reader:
        if i == 100:
            break
        URLS.append("http://" + row[1])
        i = i + 1

# TODO : Add timings for the sites.
while True:
    randomURLFromList = random.randint(0, len(URLS) - 1)
    currentURL = URLS[randomURLFromList]
    counterForTabs = 0
    nextNumber = False
    for i in range(0, 6):
        try:
            page = urlopen(currentURL)
        except:
            print("Page error")
            break
        counterForTabs = counterForTabs + 1
        soup = BeautifulSoup(page, features="html.parser")
        links = soup.findAll('a', attrs={'href': re.compile("^http://|^https://")})
        if len(links) == 0:
            links = soup.findAll('link', attrs={'href': re.compile("^https://|^https://")})
        if len(links) == 0:
            print("Page has no links")
            break
        randomNum = random.randint(0, len(links) - 1)
        currentURL = (links[randomNum]['href'])
        if (i == 0):
            webbrowser.open(currentURL)
        else:
            #             randomNumForTabs = random.randint(0,1)
            #             print(randomNumForTabs)
            #             keyboard.press(Key.ctrl)
            #             keyboard.press('w')
            #             keyboard.release(Key.ctrl)
            #             keyboard.release('w')
            webbrowser.open(currentURL)

        x = np.random.weibull(3)
        x = x * 65
        time.sleep(x)
#     keyboard.press(Key.ctrl)
#     keyboard.press('w')
#     keyboard.release(Key.ctrl)
#     keyboard.release('w')