import cv2
from Hand_Detection import hand_data
import math
import numpy as np
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

def findDistance(p1, p2, img,lmList_all, draw=True):
        x1, y1 = lmList_all[0][p1][1],lmList_all[0][p1][2]
        x2, y2 = lmList_all[1][p2][1],lmList_all[1][p2][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        return  img,length  

def finger_up_down(lmList_all):
        tipIds = [4, 8, 12, 16, 20]
        fingers = []
        hand1=[]
        hand2=[]
        if lmList_all[0][4][1]>lmList_all[0][3][1]:
            hand1.append(0)
        else:
            hand1.append(1)
        for id in range(1, 5):
            if lmList_all[0][tipIds[id]][2]<lmList_all[0][tipIds[id]-2][2]:
                    hand1.append(1)
            else:
                hand1.append(0)
        fingers.append(hand1)

        if lmList_all[1][4][1]>lmList_all[1][3][1]:
            hand2.append(1)
        else:
            hand2.append(0)
        for id in range(1, 5):
            if lmList_all[1][tipIds[id]][2]<lmList_all[1][tipIds[id]-2][2]:
                    hand2.append(1)
            else:
                hand2.append(0)
        fingers.append(hand2)
        return fingers

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    img,lmList_all,bbox=hand_data(img,bdraw=True)
    img1=cv2.imread("dog.jpg")
    img1=cv2.resize(img1, (240,240))
    
    if len(lmList_all) != 0:
        if lmList_all[0]!="NULL":
                tipIds=[]
                if len(lmList_all)==2:
                    img,l=findDistance(9, 9, img,lmList_all, draw=True)  
                    fingers=finger_up_down(lmList_all) 
                    # print( fingers)
                    if fingers[0]==[0, 1, 1, 0, 0] and \
                    fingers[1]==[0, 1, 1, 0, 0]:

                        print("zoom")
    img[10:250,10:250]=img1
    cv2.imshow("VIDEO",img)
    cv2.waitKey(1)     