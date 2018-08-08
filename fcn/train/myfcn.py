import numpy as np
import torch
import os
from torch.autograd import Variable
from torch import nn
from torch.utils.data import Dataset,DataLoader
import matplotlib.pyplot as plt
from PIL import Image

def transforms(img,label):
    normalize=([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    img=img/255.0
    label=label
    for a in range(3):
        img[:,:,a]=(img[:,:,a]-normalize[0][a])/normalize[1][a]
    return img,label
def load_img(root):
    txt_name=root+'name.txt'
    with open(txt_name,'r') as f:
        images=f.readlines()
    data=[os.path.join(root,'train/',o.rstrip()) for o in images]
    label=[os.path.join(root,'label/',o.rstrip().replace('.jpg','_label.png')) for o in images]
    return data,label
class MyDataset(Dataset):
    def __init__(self,root,transforms):
        self.transforms=transforms
        self.data_list,self.label_list=load_img(root=root)

    def __getitem__(self,idx):
        img=self.data_list[idx]
        label=self.label_list[idx]
        img=Image.open(img)
        label=Image.open(label).convert('RGB')
        img,label=self.transforms(img,label)
        return img,label

    def __len__(self):
        return len(self.data_list)

root='./'
train=MyDataset(root, transforms)
print train[0]
