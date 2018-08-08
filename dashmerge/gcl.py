#!/Users/test/anaconda/bin/python
# -*- coding:utf-8 -*-

import os
import collections
import json
import numpy as np
import scipy.misc as m
import matplotlib.pyplot as plt
import cv2

label_colours = [[0, 0, 0], [128, 64, 128], [244, 35, 232], [250, 170, 160], [70, 70, 70], [102, 102, 156],
          [190, 153, 153], [180, 165, 180], [148, 0, 211], [64, 224, 208], [205, 92, 92], [0, 100, 0],
          [255, 69, 0], [0, 0, 128], [0, 128, 128], [128, 0, 128], [128, 64, 128], [128, 64, 0],
          [0, 192, 0], [128, 192, 0], [253,151,32], [0, 64, 128]]

ln = len(label_colours)

file_list = tuple(open("/data/ma.luo/data212/ygomi/train.txt", 'r'))#第一个""内为待着色文件列表txt文件位置
file_list = [id_.rstrip() for id_ in file_list]
file_list.sort()
for file in file_list:
    lbl_path = "/data/ma.luo/data212/ygomi/leftImg8bit/train/"+file+".jpg"#第一个""内为待着色文件位置
    lbl = m.imread(lbl_path)
    temp = np.array(lbl, dtype=np.int32)

    lbl_path2 = "/data/ma.luo/clpng213/"+file+"_labelIds.png"#第一个""内为输出文件位置
    lbl2 = np.array([np.zeros_like(lbl) for _ in range(3)])


    r = temp.copy()
    g = temp.copy()
    b = temp.copy()
    for l in range(0, ln):
        r[temp == l] = label_colours[l][0]
        g[temp == l] = label_colours[l][1]
        b[temp == l] = label_colours[l][2]
    rgb = np.zeros((temp.shape[0], temp.shape[1], 3))
    rgb[:, :, 0] = r
    rgb[:, :, 1] = g
    rgb[:, :, 2] = b
    cv2.imwrite(lbl_path2,rgb)
