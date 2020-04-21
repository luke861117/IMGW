# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:25:07 2020

@author: DK
"""

import cv2
import numpy as np


img = cv2.imread('F:\\Documents\\IMGW\\HomeWork2\\Example.jpg',0)   
#使用高斯霧化
blurred = cv2.GaussianBlur(img, (5, 5), 0)
sobelwithblur1 = cv2.Sobel(blurred, cv2.CV_64F, 1, 0)
sobelwithblur2 = cv2.Sobel(blurred, cv2.CV_64F, 0, 1)
sobelwithblur1 = np.uint8(np.absolute(sobelwithblur1))
sobelwithblur2 = np.uint8(np.absolute(sobelwithblur2))
sobelCombine_withblur = cv2.bitwise_or(sobelwithblur1, sobelwithblur2)
#無使用高斯霧化
sobel1 = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel2 = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel1 = np.uint8(np.absolute(sobel1))
sobel2 = np.uint8(np.absolute(sobel2))
sobelCombine = cv2.bitwise_or(sobel1, sobel2)



cv2.imshow('sobelCombine_withblur', sobelCombine_withblur)
cv2.imshow('sobelCombine', sobelCombine)
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork2\\sobelwithblur.jpg',sobelCombine_withblur)
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork2\\sobel.jpg',sobelCombine)
cv2.waitKey(0)
cv2.destroyAllWindows()

