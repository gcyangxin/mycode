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
def load_img(root,train=True):
    txt_name=root+('train.txt' if train else 'val.txt')
    with open(txt_name,'r') as f:
        images=f.readlines()
    data=[os.path.join(root,('train/jpg/' if train else 'val/jpg/'),o.rstrip()) for o in images if train]
    label=[os.path.join(root,('train/label/'if train else 'val/jpg/'),o.rstrip().replace('.jpg','_labelIds.png')) for o in images]
    return data,label
class MyDataset(Dataset):
    def __init__(self,root,train,transforms):
        self.transforms=transforms
        self.data_list,self.label_list=load_img(root=root)

    def __getitem__(self,idx):
        img=self.data_list[idx]
        label=self.label_list[idx]
        img=np.array(Image.open(img))
        label=np.array(Image.open(label))
        img,label=self.transforms(img,label)
        return img,label

    def __len__(self):
        return len(self.data_list)

class FCN(nn.Module):
    def __init__(self,num_classes=22):
        super(FCN,self).__init__()
        self.conv1=nn.Sequential(
        nn.Conv2d(3, 8, kernel_size=5,padding=2),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2)
        )
        self.conv2=nn.Sequential(
        nn.Conv2d(8,16,5,2),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
        self.conv3=nn.Sequential(
        nn.Conv2d(16,32,5,2),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
        self.conv4=nn.Sequential(
        nn.Conv2d(32,64,5,2),
        nn.ReLU(),
        nn.MaxPool2d(2)#16
        )
        self.out=nn.Softmax(22)
    def forward(self,x):
        x=self.conv1(x)
        x=self.conv2(x)
        x=self.conv3(x)
        x=self.conv4(x)
        x=x.view(x.size(0),-1)
        output=self.out(x)
        return output

fcn=FCN()
print fcn



# root='./'
# train_data=MyDataset(root, train=True,transforms)
# val_data=MyDataset(root, train=False, transforms)
# trainloader=DataLoader(train_data,shuffle=True,batch_size=4)
# valloader=DataLoader(val_data,batch_size=4)
#










#
