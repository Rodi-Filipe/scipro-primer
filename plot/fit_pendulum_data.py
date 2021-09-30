# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 20:11:00 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def get_input():
    
    outputArg1=np.loadtxt('pendulum.dat',skiprows=1,dtype=float)
    return outputArg1

def plotfunc(x,y,deg):
    
    tempvar=['exact']
    plt.plot(x,y,'k-o')
    plt.xlabel('Length')
    plt.ylabel('Period')
    plt.title('Length vs Period')

    for i in range(len(deg)):
         coeff=np.polynomial.polynomial.Polynomial.fit(x,y,int(deg[i])).convert().coef
         ynew=np.polynomial.polynomial.polyval(x,coeff)
         plt.plot(x,ynew,linestyle='--',marker='*')
         tempvar.append('polynomial %d approximation' %deg[i])
    plt.legend(tempvar)
    plt.show()
    
data=get_input()
plotfunc(data[:,0],data[:,0],[1,2,3])