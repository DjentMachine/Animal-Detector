# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:06:20 2021
@author: DBarros

A script to retrive frames from a video

TODO:
    Loop trough all videos and not only one
"""
import os
import cv2
os.chdir("ADIR")

#Temporary way to store a video's path
vid = "teste2.mp4"
cap = cv2.VideoCapture("ADIR" + vid)


#Loops through a video, chops a frame every 10 frames
def frameCutter(self, video, imagesPerSecond):
    i=0
    while(video.isOpened()):
        ret, frame = video.read()
        if ret == False:
            break
        if i%10 == 0:     
            cv2.imwrite("%s/%s" %() +str(i)+".jpg",frame)
        i+=1
        cap.release()
        cv2.destroyAllWindows()        
        return


    
