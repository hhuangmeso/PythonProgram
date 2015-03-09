'''
plot results from kNN
'''
from numpy import *
import kNN
datingDataMat,datingLabels=kNN.file2matrix('datingTestSet.txt')
import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
