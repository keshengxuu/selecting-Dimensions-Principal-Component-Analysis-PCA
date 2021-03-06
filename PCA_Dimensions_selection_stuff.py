# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:17:00 2016
Here is the example for the PCA stuff  writing with python codes
% Use the yeast data.

 This pythod codes modified from matlab codes in the book
 Exploratory Data Analysis with MATLAB, 2nd Edition
% Wendy L. and Angel R. Martinez and Jeff Solka

@author: ksxuu
"""

import numpy as np
import matplotlib.pyplot as plt 
import sys
#print sys.argv[0]

data=np.loadtxt('lop_s0_G6.8e-04.txt',delimiter=',')

n,p=np.shape(data)
# centering the data 
datac=data-np.tile(np.mean(data,axis=1),(n,1))
#Find the covariance matrix.s
covm =np.cov(datac)
eigval,eigvec=np.linalg.eig(covm)

#Return the cumulative sum of the elements along a given axis np.cumsum()
pervar = 100*np.cumsum(eigval)/sum(eigval)

ks=range(len(eigval))
pervar_th1=np.tile(70,n)
pervar_th2=np.tile(95,n)
fig=plt.figure(figsize=(9,5))
plt.clf()
#Do a scree plot.
ax1=plt.subplot(121)
ax1.plot(ks,eigval,'b-o')
ax1.set_title('scree plot')
ax1.set_xlabel('Eigenvalue Index - k')
ax1.set_ylabel('Eigenvalue')
# From this plot, dimensionality of 4 seems reasonable.
# Now for the percentage of variance explained.
ax2=plt.subplot(122)
ax2.plot(ks,pervar,'b-o')
ax2.plot(ks,pervar_th1,'r-.')
ax2.plot(ks,pervar_th2,'r-.')
ax2.set_title('Cumulative Percentage of Variance Explained',fontsize='small')
ax2.set_xlabel('Eigenvalue Index - k')
ax2.set_ylabel('Percentage of Variance')

plt.subplots_adjust(left = 0.1,bottom=0.1, right=0.92, top=0.95, wspace=0.2, hspace=0.5)
plt.show()
plt.savefig('pca_test.png')