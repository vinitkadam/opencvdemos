import numpy as np
import cv2
import math
vidcap = cv2.VideoCapture('test.mp4')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("outputs/frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 60 #it will capture image in each second
success = getFrame(sec)
while success:
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)