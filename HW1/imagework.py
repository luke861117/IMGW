# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:55:50 2020

@author: USER
"""

import cv2
image = cv2.imread('R6.jpg')
image_g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('R6-gray.jpg',image_g)