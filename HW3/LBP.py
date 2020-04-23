# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:56:06 2020

@author: DK
"""

from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
# settings for LBP
radius = 6  # LBP算法中範圍半徑的取值
n_points = 32 # 領域像素點數
# 讀取圖像
image = cv2.imread('F:\\Documents\\IMGW\\HomeWork3\\ROAD_1.jpg')
cv2.imshow('Origin', image)
#灰度轉換
image_g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', image_g)
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork3\\ROAD_1_GRAY.jpg', image_g)
#LBP
lbp = local_binary_pattern(image_g, n_points, radius)
cv2.imshow('LBP', lbp)
cv2.imwrite('F:\\Documents\\IMGW\\HomeWork3\\ROAD_1_LBP.jpg', lbp)
cv2.waitKey(0)
cv2.destroyAllWindows()
