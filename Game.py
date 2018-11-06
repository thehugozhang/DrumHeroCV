#!usr/bin/python
#blueprintinterface.py

__author__ = "Rowan O'Connor"
__version__ = "0.0"

'Measuring velocity and stuff'

import tkinter as tk
from PIL import ImageTk, Image
from random import randint
import numpy as np
import argparse
import imutils
import cv2
import drumsounds
from math import sqrt

playSound = 0
playKick = True
playTom1 = True
playTom2 = True
playHiHat = True
playSnare = True    

playSound2 = True
playSound3 = True
playSound4 = True
playSound5 = True
  
kickX = 146
kickY = 700
snareX = 1134
snareY = 700
tom1X = 800
tom1Y = 700
tom2X = 470
tom2Y = 700
hihatX = 1150
hihatY = 0

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

root = tk.Tk()

SIZE = (root.winfo_screenwidth(), root.winfo_screenheight()); CENTER = (SIZE[0] // 2, SIZE[1] // 2)
TK_SIZE = str(SIZE[0]) + 'x' + str(SIZE[1])

root.geometry(TK_SIZE)
root.title("AirDrums")

#[[Sizex, Sizey], x, y]

def camerafeed():
    global colors
    global lower
    global upper
    global camera
    global yellowCnt
    global blueCnt
    global playSound
    global playKick 
    global playTom1 
    global playTom2 
    global playHiHat 
    global playSnare    

    global playSound2
    global playSound3
    global playSound4 
    global playSound5 
      
    global kickX 
    global kickY 
    global snareX 
    global snareY 
    global tom1X 
    global tom1Y
    global tom2X 
    global tom2Y 
    global hihatX
    global hihatY

    
    # grab the current frame
    (grabbed, frame) = camera.read()


    cv2.circle(frame, (kickX,kickY),146, (20,255,2), 2) #kick
    cv2.circle(frame, (tom2X,tom2Y), 146, (252,213,13), 2) #tom2
    cv2.circle(frame, (tom1X,tom1Y), 146, (153,0,255), 2) #tom1
    cv2.circle(frame, (snareX,snareY), 146, (0,0,255), 2) #snare
    cv2.circle(frame, (hihatX,hihatY), 146, (130,120,130), 2) #hihat
 
    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=1366)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    #for each color in dictionary check object in frame
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

##                print("Blue: " + str(blueCnt))
##                print("Yellow: " + str(yellowCnt))
                cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)

                #kick conditional
                if(sqrt((blueCnt[0] - kickX)**2 + (blueCnt[1] - kickY)**2) < (radius + 136) or sqrt((yellowCnt[0] - kickX)**2 + (yellowCnt[1] - kickY)**2) < (radius + 136)):
                    if(playKick == True):
                        playKick = False
                        drumsounds.play_bass()
                elif(playKick == False):
                    playKick = True

                #print(str(playKick))
                #tom2 conditional mid tom
                if(sqrt((blueCnt[0] - tom2X)**2 + (blueCnt[1] - tom2Y)**2) < (radius + 136) or sqrt((yellowCnt[0] - tom2X)**2 + (yellowCnt[1] - tom2Y)**2) < (radius + 136)):
                    if(playTom2 == True):
                        playTom2 = False
                        drumsounds.play_mid_tom()
                elif(playTom2 == False):
                    playTom2 = True

                #tom1 conditional high tom
                if(sqrt((blueCnt[0] - tom1X)**2 + (blueCnt[1] - tom1Y)**2) < (radius + 136) or sqrt((yellowCnt[0] - tom1X)**2 + (yellowCnt[1] - tom1Y)**2) < (radius + 136)):
                    if(playTom1 == True):
                        playTom1 = False
                        drumsounds.play_high_tom()
                elif(playTom1 == False):
                    playTom1 = True

                #snare conditional
                if(sqrt((blueCnt[0] - snareX)**2 + (blueCnt[1] - snareY)**2) < (radius + 136) or sqrt((yellowCnt[0] - snareX)**2 + (yellowCnt[1] - snareY)**2) < (radius + 136)):
                    if(playSnare == True):
                        playSnare = False
                        drumsounds.play_snare()
                elif(playSnare == False):
                    playSnare = True
                #hihat conditional 
                if(sqrt((blueCnt[0] - hihatX)**2 + (blueCnt[1] - hihatY)**2) < (radius + 136) or sqrt((yellowCnt[0] - hihatX)**2 + (yellowCnt[1] - hihatY)**2) < (radius + 136)):
                    if(playHiHat == True):
                        playHiHat = False
                        drumsounds.play_hi_hat()
                elif(playHiHat == False):
                    playHiHat = True

    
    # show the frame to our screen
    frame2 = frame.copy()
    frame2 = cv2.flip(frame2,1)
    cv2.imshow("Frame", frame2)

def random_hex_color(r_range, g_range, b_range):
    '''Generates a random shade of green in hex'''
    return '#%02X%02X%02X' % (randint(r_range[0], r_range[1]), randint(g_range[0], g_range[1]),
                              randint(b_range[0], b_range[1]))

notes = []
def create_note(column, y, mode):
    size = (50, 80)
    if mode == 0:
        color_ranges = ((200, 255), (150, 150), (150, 150))
    elif mode == 1:
        color_ranges = ((244, 255), (133, 200), (66, 132))
    elif mode == 2:
        color_ranges = ((200, 225), (180, 200), (100, 120))
    elif mode == 3:
        color_ranges = ((100, 125), (200, 255), (100, 125))
    else:
        color_ranges = ((100, 125), (100, 125), (200, 255))
    notes.append([size, column, y, random_hex_color(color_ranges[0], color_ranges[1], color_ranges[2])])

def draw_note(canvas, index):
##    print('Canvas:', canvas)
##    print('Top Corner: (' + str(notes[index][1]) + ', ' + str(notes[index][2]) + ')')
##    print('Bottom Corner: (' + str(notes[index][1] + notes[index][0][0]) + ', '
##           + str(notes[index][2] + notes[index][0][1]) + ')', end='\n\n')
    canvas.create_rectangle((notes[index][1] * 100 + 433, notes[index][2]),
                            (notes[index][1] * 100 + 433 + notes[index][0][0], notes[index][2] + notes[index][0][1]),
                            fill=notes[index][3])


# drum_set_img = ImageTk.PhotoImage(Image.open("Drumset.png"))
# drum_set_pic = tkinter.Label(image=drum_set_img)
# drum_set_pic.place(x=100, y=100, anchor="center")

pic_x = 600
pic_y = 100

canvas = tk.Canvas(root, width=SIZE[0], height=SIZE[1])
canvas.config(background='black')


# note_img = ImageTk.PhotoImage(Image.open("Music.jpg"))
# note_pic = tkinter.Label(image=note_img)
# note_pic.place(x=pic_x, y=pic_y)

for height in range(10):
    for column in range(5):
        create_note(column, height * -300 - column * 35, column)


def update():
    global colors
    global lower
    global upper
    global camera
    global yellowCnt
    global blueCnt
    global playSound
    global playKick 
    global playTom1 
    global playTom2 
    global playHiHat 
    global playSnare    

    global playSound2
    global playSound3
    global playSound4 
    global playSound5 
      
    global kickX 
    global kickY 
    global snareX 
    global snareY 
    global tom1X 
    global tom1Y
    global tom2X 
    global tom2Y 
    global hihatX
    global hihatY

    canvas.delete('all')


    for index in range(len(notes)):
        notes[index][2] += 5
        for drum in range(5):
            if notes[index][0] == drum and 700 <= notes[index][2] <= 768:
                pass # Add collision code here:





        draw_note(canvas, index)
    
    camerafeed()
    canvas.after(15, update)
canvas.pack()

update()

root.mainloop()
