#!/Users/test/anaconda/bin/python
# -*- coding:utf-8 -*-

import os
import collections
import json
import numpy as np
import scipy.misc as m
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2

label_colours = [[0, 0, 0], [128, 64, 128], [244, 35, 232], [250, 170, 160], [70, 70, 70], [102, 102, 156],
          [190, 153, 153], [180, 165, 180], [148, 0, 211], [64, 224, 208], [205, 92, 92], [0, 100, 0],
          [255, 69, 0], [0, 0, 128], [0, 128, 128], [128, 0, 128], [128, 64, 128], [128, 64, 0],
          [0, 192, 0], [128, 192, 0], [253,151,32], [0, 64, 128]]

ln = len(label_colours)

lbl_path = "/home/user/Documents/dl/tools/labelTool/convert/123.png"#第一个""内为待着色文件位置
lbl = ndimage.imread(lbl_path,mode='L')
# print lbl.size,lbl.shape
temp = np.array(lbl, dtype=np.int32)
# print lbl.shape
lbl_path2 = "/home/user/Documents/dl/tools/labelTool/convert/321.png"#第一个""内为输出文件位置

# print temp.shape
r = temp.copy()
g = temp.copy()
b = temp.copy()

for l in range(0, ln):
    r[temp == l] = label_colours[l][0]
    g[temp == l] = label_colours[l][1]
    b[temp == l] = label_colours[l][2]
# print r.shape
rgb = np.zeros((temp.shape[0],temp.shape[1],3))
# print rgb
# print rgb.shape
rgb[:, :, 0] = r
rgb[:, :, 1] = g
rgb[:, :, 2] = b
cv2.imwrite(lbl_path2,rgb)
