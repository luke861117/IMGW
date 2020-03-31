# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:46:14 2020

@author: USER
"""

import cv2
import timeit

print(cv2. __version__ )
def opening(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    return img

def closing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)
    return img

img = cv2.imread('F:\\Documents\\IMGW\\HomeWork1\\R6.jpg',0) 
cv2.imshow('origin', img)
#Binarization
img[img > 128] = 255
img[img <= 128] = 0
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork1\\GRAY.jpg',img)

cv2.setUseOptimized(True) 
print('----------opening x100----------','\n')
print ('Enable AVX:',cv2.useOptimized())
opening_with_avx = img
start = timeit.default_timer()
for i in range (0,100):
    opening_with_avx = opening(opening_with_avx)
stop = timeit.default_timer()
t1 = stop - start
print('Runtime with AVX: ', t1,"\n")
            


opening_without_avx = img
cv2.setUseOptimized(False) 

print ('Enable AVX:',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    opening_without_avx = opening(opening_without_avx)
stop = timeit.default_timer()
t2 = stop - start
print('Runtime without AVX: ', t2,'\n')
print('Speedup:',t2/t1,'\n')

print('----------closing x100----------','\n')
closing_whit_avx = img

cv2.setUseOptimized(True) 
print ('Enable AVX:',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    closing_whit_avx = closing(closing_whit_avx)
stop = timeit.default_timer()
t1_ = stop - start
print('Runtime with AVX: ', t1_,"\n")



closing_whitout_avx = img
cv2.setUseOptimized(False) 
print ('Enable AVX:',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    closing_whitout_avx = closing(closing_whitout_avx)
stop = timeit.default_timer()
t2_ = stop - start
print('Runtime without AVX: ', t2_,'\n')
print('Speedup:',t2_/t1_)

cv2.imwrite('F:\\Documents\\IMGW\\HomeWork1\\open_avx.jpg',opening_with_avx)
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork1\\close_avx.jpg',closing_whit_avx)
cv2.imshow('afteropening', opening_with_avx)
cv2.imshow('afterclosing', closing_whit_avx)
cv2.waitKey(0)
cv2.destroyAllWindows()