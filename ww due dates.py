# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:00:20 2015

@author: maccomb1
"""

import pyautogui
import time
import csv


inFile = '132 ww due.csv'
entry = [] #will contain the data from the csv file as a list of lists
with open(inFile, 'r') as f:
    reader = csv.reader(f)
    #Add each row in the csv file as a list
    for row in reader:
        entry.append(row)


############ first line

for i in range(0,len(entry)):
    if i == 0:    
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.1)  
    else:
        pyautogui.typewrite(entry[i][2] + ' at 06:00am', interval=0.01) #open date
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(entry[i][1] + ' at 11:59pm', interval=0.01) #close date
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(entry[i][1] + ' at 11:59pm', interval=0.01)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
      
#on new row

############ all other lines


