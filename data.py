import cv2
import numpy as np
import os

def get_frame_count(cap):
    return int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

def get_images(cap, counter, name):
	
    os.mkdir('{}_images'.format(name))
    count=0
    i=1
    while(cap.isOpened() and count!=6000):
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not i%counter:
           count+=1
           resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
           cv2.imwrite('./{}_images/{}.png'.format(name,count),resized)
        i+=1

    cap.release()

mar = cv2.VideoCapture('Mario.mp4')
war = cv2.VideoCapture('Wario.mp4')

mario_frames = get_frame_count(mar)
wario_frames = get_frame_count(war)

mar_counter = mario_frames//6000
war_counter = wario_frames//6000

dim = (64, 64)

get_images(mar, mar_counter,name='mario')
get_images(war, war_counter,name='wario')

cv2.destroyAllWindows()
