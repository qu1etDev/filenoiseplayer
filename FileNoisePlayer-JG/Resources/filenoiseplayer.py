from tkinter import *
import tkinter as tk
import pygame
import os
from pygame.locals import *
from tkinter import filedialog
import random
import time
from RangeSlider.RangeSlider import RangeSliderH, RangeSliderV
import logging
try:
    from cStringIO import StringIO      # Python 2
except ImportError:
    from io import StringIO
logging.basicConfig()

root = Tk()
root.geometry("640x400")

pygame.mixer.init()

hasRun = 0
ranNum = 0
currentReRun = 0
ranMin = 1
ranMax = 5

hLeft = tk.DoubleVar(value = 1)
hRight = tk.DoubleVar(value = 3600)

frame = Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor="c", relheight=1, relwidth=1) # put at center of window
gridFrame = Frame(root, bg='white')
gridFrame.place(relx=0.5, rely=1, anchor="c", relheight=1, relwidth=1)
gridFrame.grid_columnconfigure((0, 1, 2), weight=1)

sliderLabel = Label(frame, text='Welcome to the Random Noise Player', bg='white', font=('Helvetica', 15, 'bold', 'underline'))
subLabel = Label(frame, text='Pick min - max random time, amount of play times, and .wav or .mp3 file. Please read README.txt for more info', bg='white', font=('Helvetica', 8, 'italic'))
sliderLabel.pack()
subLabel.pack(pady = 5)

hSlider = RangeSliderH(frame , [hLeft, hRight] , padX = 22.28, Height = 51, step_size = 1, min_val = 0, max_val = 3600, font_size = 11, font_family='Helvetica')
sliderLabel = Label(frame, text='   ⮦      -  min time      -      +      -      max time  -      ⮧   ', bg='white', font=('Helvetica', 12))
sliderLabel.pack(pady = 5)
hSlider.pack(pady = 5)

logString = ''

if hasRun == 0:
    amountOfTimes = 5

def AddAOT():
    global amountOfTimes
    amountOfTimes += 1
    aot_CountL = Label(gridFrame, text = str(amountOfTimes), bg='white', font=('Helvetica', 11, 'bold'))
    aot_CountL.grid(row=7, column=1)

def RemoveAOT():
    global amountOfTimes
    if (amountOfTimes > 1):
        amountOfTimes -= 1
    aot_CountL = Label(gridFrame, text = str(amountOfTimes), bg='white', font=('Helvetica', 11, 'bold'))
    aot_CountL.grid(row=7, column=1)
    


def FindFile():
    file = filedialog.askopenfilename(parent=frame, filetypes=[("Audio Files", ".wav", ".mp3")], title="Choose Audio File")
    if file:
        global data
        data = file
        print ("found: {0}".format(len(data)))
        global logString
        logString = 'found: {0}'.format(len(data))
        global logLabel
        logLabel.grid_remove()
        logLabel = Label(gridFrame, text='Log: ' + logString, bg='white')        
        logLabel.grid(row=8, column=0, columnspan=2, sticky='nw', pady=50)
        pygame.mixer.music.load(data)
        button1.grid_remove()
        global button2
        button2 = Button(gridFrame, text="Remove File", command=RemoveFile)
        button2.grid(row=2, column=0, sticky='ew', padx=50, pady=25)
        global button3 
        button3 = Button(gridFrame, text="Play File", command=ResetCount)
        button3.grid(row=2, column=2, sticky='ew', padx=50, pady=25)
        

def ResetCount():
    global currentReRun
    currentReRun = 0
    PlayAudio()

def RemoveFile():
    data = None    
    global button1
    button1 = Button(gridFrame, text="Choose File", command=FindFile)
    button1.grid(row=2, column=1, sticky='ew', padx=50, pady=25)
    button2.grid_remove()
    button3.grid_remove()
    try:
        frame.after_cancel(timer)
        global logLabel
        logLabel.grid_remove()
        logString = 'Timer stopped'
        logLabel = Label(gridFrame, text='Log: ' + logString, bg='white')
        logLabel.grid(row=8, column=0, columnspan=2, sticky='nw', pady=50)
    except:
        return
    
def PlayAudio():
    print(hSlider.getValues())
    sliderVals = hSlider.getValues()
    ranMin = sliderVals[0]
    ranMax = sliderVals[1]
    ranNum = random.randint(ranMin, ranMax)
    print(ranNum)
    global logString
    global logLabel
    logLabel.grid_remove()
    logString = 'Chosen seconds before next play: ' + str(ranNum) + ', has played: ' + str(currentReRun) + ' times so far'
    logLabel = Label(gridFrame, text='Log: ' + logString, bg='white')
    logLabel.grid(row=8, column=0, columnspan=2, sticky='nw', pady=50)
    setTimer(ranNum)
        
    
def setTimer(secs):
    global timer
    timer = frame.after(secs*1000, resetTimer)

def resetTimer():
    global currentReRun
    currentReRun += 1
    print ("playing sound")
    pygame.mixer.stop()
    pygame.mixer.music.play()
    if (currentReRun < amountOfTimes):
        PlayAudio()
    
    
def RunOnce():
    amountOfTimes = 5
    global button1
    button1 = Button(gridFrame, text="Choose File", command=FindFile)
    button1.grid(row=2, column=1, sticky='ew', padx=50, pady=25)
    minusButton = Button(gridFrame, text = '-', command=RemoveAOT)
    minusButton.grid(row=7, column=0, sticky='ew', padx=25)
    aot_CountL = Label(gridFrame, text = str(amountOfTimes), bg='white', font=('Helvetica', 11, 'bold'))
    aot_CountL.grid(row=7, column=1)    
    plusButton = Button(gridFrame, text = '+', command=AddAOT)
    plusButton.grid(row=7, column=2, sticky='ew', padx=25)
    aot_Label = Label(gridFrame, text='Amount of times to be played:', bg='white', font=('Helvetica', 11, 'italic'))
    aot_Label.grid(row=6, column=1)
    global logLabel
    logLabel = Label(gridFrame, text='Log: ', bg='white')
    logLabel.grid(row=8, column=0, columnspan=2, sticky='nw', pady=50)
    

if hasRun == 0: 
    RunOnce()
    hasRun = 1

root.mainloop()
