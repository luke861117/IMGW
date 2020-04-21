# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:25:07 2020

@author: DK
"""

import cv2

img = cv2.imread('F:\\Documents\\IMGW\\HomeWork2\\Example.jpg',0)

canny1 = cv2.Canny(img, 70, 140)
canny2 = cv2.Canny(img, 70, 210)

cv2.imshow('canny1', canny1)
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork2\\Canny1.jpg',canny1)

cv2.imshow('canny2', canny2)
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork2\\Canny2.jpg',canny2)

cv2.waitKey(0)
cv2.destroyAllWindows()

