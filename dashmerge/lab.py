#!/Users/test/anaconda/bin/python
# -*- coding:utf-8 -*-

import os
import collections
import json
import numpy as np
import scipy.misc as m
import matplotlib.pyplot as plt
from PIL import Image

file_list = tuple(open("list.txt", 'r'))
file_list = [id_.rstrip() for id_ in file_list]

for f in file_list:
	lbl_path = "/data/ma.luo/train/cpng/"+f+"_labelIds.png"#第一个""内为虚线连接标注的文件夹位置
	lbl = m.imread(lbl_path)
	lbl = np.array(lbl, dtype=np.int32)

	lbl_path2 = "/data/ma.luo/train/dpng/"+f+"_labelIds.png"#第一个""内为虚线未连接标注的文件夹位置
	lbl2 = m.imread(lbl_path2)
	lbl2 = np.array(lbl2, dtype=np.int32)

	lbl_path3 = "/data/ma.luo/train/mpng/"+f+"_labelIds.png"#第一个""内为合成后文件夹的位置
	lbl3 = np.zeros_like(lbl2)

	rows = len(lbl)
	cols = len(lbl[0])
	for i in range(rows):
		for j in range(cols):
			if 4 == lbl[i][j] and 4 != lbl2[i][j]:
				lbl3[i][j] = 19
			else:
				lbl3[i][j] = lbl2[i][j]
	img = Image.fromarray(lbl3)
	img.save(lbl_path3)
