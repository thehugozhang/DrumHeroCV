import numpy as np
import argparse
import imutils
import cv2
import drumsounds
from math import sqrt

def main():

    
    playSound = 0
    playKick = True
    playTom1 = True
    playTom2 = True
    playHiHat = True
    playSnare = True

    screenWidth = 1280
    screenHeight = 650

    playSound2 = True
    playSound3 = True
    playSound4 = True
    playSound5 = True

    drumRadius = 60
      
    
    health = 180
    
    hihatX = screenWidth // 2 + 400
    hihatY = screenHeight - 20

    tom2X = screenWidth  // 2 + 200
    tom2Y = screenHeight - 20

    tom1X = screenWidth // 2
    tom1Y = screenHeight - 20
    
    
    
    snareX = tom1X - 200
    snareY = tom1Y
    
    kickX = snareX - 200
    kickY = tom2Y

    state = "Drums"
    toggledText = "Toggled"
    toggle = True

    startNotes = False

##    format is [0 = color, 1 = centerX, 2 = centerY, 3 = width, 4 = height, 5 = BGR, 6 = centerXIncrease, 7 = centerYIncrease, 8 = sizeXIncrease, 9 = sizeYIncrease, 10 = yThresholdToStartNextNot]"

##    original settings for each color note
##    ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 432]
##    ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0]
##    ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, 240]
##    ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 90]
##    ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, 432]
    orangeBeat = 83.7
    
    songNotes = [["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, 0],
                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, 0],
                 ["green", 720, 800, 20, 5, (0, 255, 0), 0, 0, 0, 0, 1300],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat + 10],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat + 10],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat + 10],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat + 10],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat + 10],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat + 10],
                 
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat], # 49
                 
                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],


                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0], # 16 blue

                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 
                 ["green", 720, 216, 20, 5, (0, 255, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, orangeBeat * 2/3],

                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, orangeBeat * 2/3],

                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, orangeBeat *2/3],

                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["yellow",640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, 1000],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],

                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],
                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],

                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 0],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, orangeBeat],





                 ["red", 680, 216, 20, 5, (0, 0, 255), 0, 0, 0, 0, 0],
                 ["blue", 600, 216, 20, 5, (255, 0, 0), 0, 0, 0, 0, 90],
                 ["yellow", 640, 216, 20, 5, (0, 255, 255), 0, 0, 0, 0, 240],
                 ["orange", 560, 216, 20, 5, (0, 165, 255), 0, 0, 0, 0, 432]]
    songNoteCount = 0

    yellowCnt = (0,0)
    blueCnt = (0,0)

    # define the lower and upper boundaries of the colors in the HSV color space
    lower = {'blue':(97, 100, 117), 'yellow':(23, 59, 119)} #assign new item lower['blue'] = (93, 10, 0)
    upper = {'blue':(117,255,255), 'yellow':(54,255,255)}
     
    # define standard colors for circle around the object
    colors = {'blue':(255,0,0), 'yellow':(0, 255, 217)}

    #pts = deque(maxlen=args["buffer"])
     
    # if a video path was not supplied, grab the reference
    # to the webcam
    camera = cv2.VideoCapture(0)

    
    img = cv2.imread('drum.png', 1)

    # keep looping
    #drumsounds.play_song()
    while True:
        # grab the current frame
        (grabbed, frame) = camera.read()


        
        
     
        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = cv2.resize(frame, (screenWidth, screenHeight), interpolation = cv2.INTER_LINEAR) 
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        #for each color in dictionary check object in frame
        cv2.rectangle(frame, (screenWidth, 0), (0, 226), (0, 0, 0), -1)

        leftPts = np.array([[hihatX + 150, screenHeight], [760, 226], [screenWidth, 226], [screenWidth, screenHeight]])
        leftPts = leftPts.reshape((-1, 1, 2))
        
        
        cv2.fillPoly(frame, [leftPts], (0, 0, 0))

        rightPts = np.array([[kickX - 150, screenHeight], [520, 226], [0, 226], [0, screenHeight]])
        rightPts = rightPts.reshape((-1, 1, 2))
        
        
        cv2.fillPoly(frame, [rightPts], (0, 0, 0))
        bottomWidth = (hihatX + 150) - (kickX - 150)
        topWidth = 760 - 520
        pts = np.array([[kickX - 150, screenHeight], [520, 226], [760, 226], [hihatX + 150, screenHeight]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        overlay = frame.copy()
        output = frame.copy();



        trap = cv2.fillPoly(overlay, [pts], (0, 0, 0))
        

        cv2.ellipse(overlay, ((hihatX + 25),hihatY), (bottomWidth // 11, 50), 0, 0, 360,  (0, 255, 0), -2) #hihat
        cv2.ellipse(overlay, (tom2X + 10,tom2Y), (bottomWidth // 11, 50), 0, 0, 360,(0, 0, 255), -2) #tom2
        cv2.ellipse(overlay, (screenWidth // 2,tom1Y), (bottomWidth // 11, 50), 0, 0, 360,(0, 255, 255), -2) #tom1

        cv2.ellipse(overlay, (screenWidth // 2 - 210,snareY), (bottomWidth // 11, 50), 0, 0, 360,(255,0,0), -2) #snare
        cv2.ellipse(overlay, (screenWidth // 2 - 420,kickY), (bottomWidth // 11, 50), 0, 0, 360,(0, 165, 255), -2) #kick

        '''
        cv2.circle(overlay, (hihatX,hihatY), drumRadius, (0, 255, 0), -2) #hihat
        cv2.circle(overlay, (tom2X,tom2Y), drumRadius, (0, 0, 255), -2) #tom2
        cv2.circle(overlay, (tom1X,tom1Y), drumRadius, (0, 255, 255), -2) #tom1

        cv2.circle(overlay, (snareX,snareY), drumRadius, (255,0,0), -2) #snare
        cv2.circle(overlay, (kickX,kickY), drumRadius, (0, 165, 255), -2) #kick
        '''
        cv2.line(overlay, (hihatX + 150, screenHeight), (760, 226), (255, 255, 255), 5)

        cv2.line(overlay, (hihatX + 150 - bottomWidth//5, screenHeight), (760 - topWidth // 5, 226), (255, 255, 255), 3)
        cv2.line(overlay, (hihatX + 150 - 2 * bottomWidth//5, screenHeight), (760 - 2 * topWidth // 5, 226), (255, 255, 255), 3)
        cv2.line(overlay, (hihatX + 150 - 3 * bottomWidth//5, screenHeight), (760 - 3 * topWidth // 5, 226), (255, 255, 255), 3)
        cv2.line(overlay, (hihatX + 150 - 4 * bottomWidth//5, screenHeight), (760 - 4 * topWidth // 5, 226), (255, 255, 255), 3)
        cv2.line(overlay, (hihatX + 150 - 5 * bottomWidth//5, screenHeight), (760 - 5 * topWidth // 5, 226), (255, 255, 255), 5)

        cv2.line(overlay, (760, 226), (760, 0), (255, 255, 255), 5)
        cv2.line(overlay, (760 - topWidth // 5, 226), (760 - topWidth // 5, 0), (255, 255, 255), 5)
        cv2.line(overlay, (760 - 2 * topWidth // 5, 226), (760 - 2 * topWidth // 5, 0), (255, 255, 255), 5)
        cv2.line(overlay, (760 - 3 * topWidth // 5, 226), (760 - 3 * topWidth // 5, 0), (255, 255, 255), 5)
        cv2.line(overlay, (760 - 4 * topWidth // 5, 226), (760 - 4 * topWidth // 5, 0), (255, 255, 255), 5)
        cv2.line(overlay, (760 - 5 * topWidth // 5, 226), (760 - 5 * topWidth // 5, 0), (255, 255, 255), 5)

        cv2.line(overlay, (screenWidth, screenHeight - 500), (760, 0), (255, 255, 255), 5)
        cv2.line(overlay, (0, screenHeight - 500), (760 - 5 * topWidth // 5, 0), (255, 255, 255), 5)




        
        

        


        

        


        cv2.addWeighted(overlay, 0.5 ,output, 0.5, 0, output)

        frame = output

        #
        #
        # HEALTH BARRRRRRRR
        #
        #

        cv2.ellipse(frame, (1155, 482), (118, 114), 0, 180, 360,(0, 0, 0), -2)
        
        cv2.ellipse(frame, (1155, 476), (110, 100), 0, 180, 360,(0, 0, 0), -2)

        
        healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)


        

                #
        #
        #CREATE NOTESSSSSSSS
        #
        #
        
        #increase the rate of notes on screen
        if startNotes:
            for noteNumber in range(songNoteCount + 1):
                if songNotes[noteNumber][0] == "green":
                    songNotes[noteNumber][6] += 10
                    songNotes[noteNumber][7] += 12
                    songNotes[noteNumber][8] += 2
                    songNotes[noteNumber][9] += 1.0
                elif songNotes[noteNumber][0] == "red":
                    songNotes[noteNumber][6] += 4.94  # 1.9
                    songNotes[noteNumber][7] += 11.7 # 4.5
                    songNotes[noteNumber][8] += 2.34  # 0.9
                    songNotes[noteNumber][9] += 1.3  # 0.5
                elif songNotes[noteNumber][0] == "yellow":
                    songNotes[noteNumber][6] += 0
                    songNotes[noteNumber][7] += 12
                    songNotes[noteNumber][8] += 2.25
                    songNotes[noteNumber][9] += 1.5
                elif songNotes[noteNumber][0] == "blue":
                    songNotes[noteNumber][6] -= 4.94  # 1.9
                    songNotes[noteNumber][7] += 11.7 # 4.5
                    songNotes[noteNumber][8] += 2.34  # 0.9
                    songNotes[noteNumber][9] += 1.3  # 0.5
                elif songNotes[noteNumber][0] == "orange":
                    songNotes[noteNumber][6] -= 10
                    songNotes[noteNumber][7] += 12
                    songNotes[noteNumber][8] += 2
                    songNotes[noteNumber][9] += 1
                    
                cv2.ellipse(frame, (int(songNotes[noteNumber][1] + songNotes[noteNumber][6]), int(songNotes[noteNumber][2] + songNotes[noteNumber][7])), (int(songNotes[noteNumber][3] + songNotes[noteNumber][8]), int(songNotes[noteNumber][4] + songNotes[noteNumber][9])), 0, 0, 360, songNotes[noteNumber][5], -1 , 4)
                cv2.ellipse(frame, (int(songNotes[noteNumber][1] + songNotes[noteNumber][6]), int(songNotes[noteNumber][2] + songNotes[noteNumber][7])), (int(songNotes[noteNumber][3] + songNotes[noteNumber][8]), int(songNotes[noteNumber][4] + songNotes[noteNumber][9])), 0, 0, 360, (0, 0, 0), 2 , 4)

                
            #if current note y is past its custom threshold it will start next note
            if songNotes[songNoteCount][7] > songNotes[songNoteCount][10]:
                songNoteCount += 1
                if (songNoteCount + 1) <= len(songNotes):
                    cv2.ellipse(frame, (int(songNotes[songNoteCount][1] + songNotes[songNoteCount][6]), int(songNotes[songNoteCount][2] + songNotes[songNoteCount][7])), (int(songNotes[songNoteCount][3] + songNotes[songNoteCount][8]), int(songNotes[songNoteCount][4] + songNotes[songNoteCount][9])), 0, 0, 360, songNotes[songNoteCount][5], -1 )
                else:
                    songNoteCount -= 1

            ##
            ##
            ## END CREATE NOTES
            ##
            ##
        
        for key, value in upper.items():
            # construct a mask for the color from dictionary`1, then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
                    
            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

     

            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                radius = 45
                M = cv2.moments(c)
                cursorX = int(abs(M["m10"] / M["m00"]))
                cursorY = int(M["m01"] / M["m00"])
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
                # only proceed if the radius meets a minimum size. Correct this value for your object's size
                if radius > 25:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, center, 5, colors[key], 4)
                    

                    if(colors[key] == (255,0,0)):
                        blueCnt = center
                    elif(colors[key] == (0,255,217)):
                        yellowCnt = center
                    ##print("Blue: " + str(blueCnt))
                    ##print("Yellow: " + str(yellowCnt))
                    '''    
                    blueRight = int(x) - int(radius)
                    blueLeft = int(x) + int(radius)
                    blueTop = int(y) - int(radius)
                    blueBottom = int(y) + int(radius)
                    
                    yellowRight = int(x) - int(radius)
                    yellowLeft = int(x) + int(radius)
                    yellowTop = int(y) - int(radius)
                    yellowBottom = int(y) + int(radius)
                    '''
                    cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                    #cv2.rectangle(frame, (blueLeft, blueTop), (blueRight, blueBottom), (0, 255, 0), 2)
                    #cv2.rectangle(frame, (int(x) + int(radius), int(y) + int(radius)), (int(x) - int(radius), int(y) - int(radius)), (0, 255, 0), 2)

                    #kick conditional
##                    if state == "Drums":
                    if toggle == False:
                        if(sqrt((blueCnt[0] - kickX)**2 + (blueCnt[1] - kickY)**2) < (radius + drumRadius) or sqrt((yellowCnt[0] - kickX)**2 + (yellowCnt[1] - kickY)**2) < (radius + drumRadius)):
                            if(playKick == True):
                                playKick = False
                                if(state == "Random"):
                                   drumsounds.play_moomba()
                                else:
                                   cv2.ellipse(frame, (screenWidth // 2 - 420,kickY), (bottomWidth // 11, 50), 0, 0, 360,(0, 165, 255), -2) #kick
                                   drumsounds.play_bass()
                                   for note in songNotes:
                                        if note[0] == "orange":
                                            distGrade = kickY - (note[2] + note[7])
                                            if distGrade > 160:
                                                if health < 360:
                                                    health += 6
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 120 and distGrade <= 160:
                                                if health < 360:
                                                    health += 4
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 80 and distGrade <= 120:
                                                health += 2
                                                healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 40 and distGrade <= 80:
                                                if health > 180:
                                                    health -= 0
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 0 and distGrade <= 40:
                                                if health > 180:
                                                    health -= 2
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            else:
                                                pass
                        elif(playKick == False):
                            playKick = True

                        #print(str(playKick))
                        #tom2 conditional mid tom
                        if(sqrt((blueCnt[0] - tom2X)**2 + (blueCnt[1] - tom2Y)**2) < (radius + drumRadius) or sqrt((yellowCnt[0] - tom2X)**2 + (yellowCnt[1] - tom2Y)**2) < (radius + drumRadius)):
                            if(playTom2 == True):
                                playTom2 = False
                                if(state == "Random"):
                                    drumsounds.play_dasani()
                                else:
                                    cv2.ellipse(frame, (tom2X + 10,tom2Y), (bottomWidth // 11, 50), 0, 0, 360,(0, 0, 255), -2) #tom2
                                    drumsounds.play_mid_tom()
                                    for note in songNotes:
                                        if note[0] == "red":
                                            distGrade = kickY - (note[2] + note[7])
                                            if distGrade > 160:
                                                if health < 360:
                                                    health += 6
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 120 and distGrade <= 160:
                                                if health < 360:
                                                    health += 4
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 80 and distGrade <= 120:
                                                health += 2
                                                healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 40 and distGrade <= 80:
                                                if health > 180:
                                                    health -= 0
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 0 and distGrade <= 40:
                                                if health > 180:
                                                    health -= 2
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            else:
                                                pass
                        elif(playTom2 == False):
                            playTom2 = True

                        #tom1 conditional high tom
                        if(sqrt((blueCnt[0] - tom1X)**2 + (blueCnt[1] - tom1Y)**2) < (radius + drumRadius) or sqrt((yellowCnt[0] - tom1X)**2 + (yellowCnt[1] - tom1Y)**2) < (radius + drumRadius)):
                            if(playTom1 == True):
                                playTom1 = False
                                if(state == "Random"):
                                    drumsounds.play_cowbell()
                                else:
                                    cv2.ellipse(frame, (screenWidth // 2,tom1Y), (bottomWidth // 11, 50), 0, 0, 360,(0, 255, 255), -2) #tom1
                                    drumsounds.play_high_tom()
                                    for note in songNotes:
                                        if note[0] == "yellow":
                                            distGrade = kickY - (note[2] + note[7])
                                            if distGrade > 160:
                                                if health < 360:
                                                    health += 6
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 120 and distGrade <= 160:
                                                if health < 360:
                                                    health += 4
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 80 and distGrade <= 120:
                                                health += 2
                                                healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 40 and distGrade <= 80:
                                                if health > 180:
                                                    health -= 0
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 0 and distGrade <= 40:
                                                if health > 180:
                                                    health -= 2
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            else:
                                                pass
                                            
                        elif(playTom1 == False):
                            playTom1 = True

                        #snare conditional
                        if(sqrt((blueCnt[0] - snareX)**2 + (blueCnt[1] - snareY)**2) < (radius + drumRadius) or sqrt((yellowCnt[0] - snareX)**2 + (yellowCnt[1] - snareY)**2) < (radius + drumRadius)):
                            if(playSnare == True):
                                playSnare = False
                                if(state == "Random"):
                                    drumsounds.play_clave()
                                else:
                                    cv2.ellipse(frame, (screenWidth // 2 - 210,snareY), (bottomWidth // 11, 50), 0, 0, 360,(255,0,0), -2) #snare
                                    drumsounds.play_snare()
                                    for note in songNotes:
                                        if note[0] == "blue":
                                            distGrade = kickY - (note[2] + note[7])
                                            if distGrade > 160:
                                                if health < 360:
                                                    health += 6
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 120 and distGrade <= 160:
                                                if health < 360:
                                                    health += 4
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 80 and distGrade <= 120:
                                                health += 2
                                                healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 40 and distGrade <= 80:
                                                if health > 180:
                                                    health -= 0
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 0 and distGrade <= 40:
                                                if health > 180:
                                                    health -= 2
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            else:
                                                pass
                        elif(playSnare == False):
                            playSnare = True
                        #hihat conditional 
                        if(sqrt((blueCnt[0] - hihatX)**2 + (blueCnt[1] - hihatY)**2) < (radius + drumRadius) or sqrt((yellowCnt[0] - hihatX)**2 + (yellowCnt[1] - hihatY)**2) < (radius + drumRadius)):
                            if(playHiHat == True):
                                playHiHat = False
                                if(state == "Random"):
                                    drumsounds.play_elephant()
                                else:
                                    cv2.ellipse(frame, ((hihatX + 25),hihatY), (bottomWidth // 11, 50), 0, 0, 360,  (0, 255, 0), -2) #hihat
                                    drumsounds.play_hi_hat()
                                    for note in songNotes:
                                        if note[0] == "green":
                                            distGrade = kickY - (note[2] + note[7])
                                            if distGrade > 160:
                                                if health < 360:
                                                    health += 6
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 120 and distGrade <= 160:
                                                if health < 360:
                                                    health += 4
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 80 and distGrade <= 120:
                                                health += 2
                                                healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 40 and distGrade <= 80:
                                                if health > 180:
                                                    health -= 0
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            elif distGrade > 0 and distGrade <= 40:
                                                if health > 180:
                                                    health -= 2
                                                    healthbar = cv2.ellipse(frame, (1155, 476), (110, 100), 0, health, 360,(255, 0, 255), -2)
                                                break
                                            else:
                                                pass
                                            
                        elif(playHiHat == False):
                            playHiHat = True
                    else:
                        pass

                            
        # show the frame to our screen
        frame2 = frame.copy()
        
        frame2 = cv2.flip(frame2,1)
        text = cv2.putText(frame2, toggledText, (1100, 50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 4)

        cv2.imshow("Frame", frame2)
        
        k = cv2.waitKey(33)
        if k == 27:
            drumsounds.stop_song()
            break
        elif k == 32:
            if toggle == False:
                toggledText = "Toggled"
                toggle = True
                startNotes = False

            elif toggle == True:
                toggledText = "Untoggled"
                toggle = False
                drumsounds.play_song()
                startNotes = True



    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

