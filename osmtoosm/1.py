from numpy import *
path='/home/user/xun.txt'
datamat=[];labelmat=[]
fr=open(path).readlines()
for line in fr:
    linearr=line.strip().split()
    datamat.append([1.0,float(linearr[0]),float(linearr[1])])
    labelmat.append(int(linearr[2]))
print datamat,labelmat