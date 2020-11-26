# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:39:41 2020

@author: DK
"""

import numpy as np
import math
import cv2
np.set_printoptions(threshold=np.inf)
#step = 網格密集度
def draw_flow(img, flow, step=10):
    # global arrows
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    # print("Lines = {}".format(lines))
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)     
    for (x1, y1), (x2, y2) in lines:
        # arrows.append([x1,y1, math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))])
        # cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
        cv2.arrowedLine(vis, (x1, y1), (x2, y2), (0, 255, 0),thickness=1, line_type=cv2.LINE_4, shift=0, tipLength=0.3)
    return vis

# arrows = []
Test_Video = './cut_movie_10.avi'
cap = cv2.VideoCapture(Test_Video)
# cam = video.create_capture(fn)
ret, prev = cap.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)  
counter = 0  

while True:
    #
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])#u, v
    # 參數說明：prevImg 輸入的8bit單通道前一幀圖像；
    #          nextImg 輸入的8bit單通道當前幀圖像；
    #          pyr_scale 金字塔參數：0.5為經典參數，每一層是下一層尺度的一半；
    #          levels 金字塔的層數
    #          winsize 窗口大小
    #          iterations 迭代次數
    #          poly_n 像素鄰域的大小，大的話表示圖像整體比較平滑
    #          poly_sigma 高斯標準差
    #          flags  可以為下列的組合 OPTFLOW_USE_INITIAL_FLOW  OPTFLOW_FARNEBACK_GAUSSIAN
    # arrows.clear()
    demoImg = draw_flow(gray,flow)
    # print(arrows)
    cv2.imwrite("D:\\20201125\\FB\\Arrow\\cut_movie_10_no_net\\{}.png".format(counter), demoImg)
    cv2.imshow('flow', demoImg) 
    counter = counter + 1      
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    prevgray = gray
cap.release()        
cv2.destroyAllWindows()