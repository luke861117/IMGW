# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:34:10 2020

@author: 朱可望
"""


#import dlib
import cv2
#import imutils


face_cascade = cv2.CascadeClassifier('D:\\anaconda3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')#使用人臉辨識設定檔
img = cv2.imread('D:\\GS_Lab_Code\\face_ID\\faces.png')
reimg = cv2.resize(img, (720, 480))#重設圖片大小
gray = cv2.cvtColor(reimg, cv2.COLOR_BGR2GRAY)#轉灰度
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 2, minSize = (32, 32))
count=0
for (x, y, w, h) in faces:    
    cv2.rectangle(reimg, (x, y), (x + w, y + h), (255, 255, 255), 1)
    crop_img = reimg[y:y+h, x:x+w]
    cv2.imshow("ID{}".format(count), crop_img)
    cv2.imwrite("ID{}.png".format(count), crop_img)    
    count += 1
    
    

cv2.imshow("faces", reimg)
cv2.waitKey(0)
cv2.destroyAllWindows()