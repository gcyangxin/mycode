#coding: utf-8
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
data=np.asarray([[0,1,2,3,4,5,6],
            [3,2,1,101,99,98,18],
            [104,100,81,10,5,2,90],
            [0,0,0,0,1,1,1]])
testX=np.array([[50,20]])
label_map={0:'love',1:'action'}
X=data[1:3,:].T
Y=data[3,:]
knn=KNeighborsClassifier()
knn.fit(X,Y)
print label_map[knn.predict(testX)[0]]
