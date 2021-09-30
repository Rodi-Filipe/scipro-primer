# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:51:08 2021

@author: rodin
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

def calc_velocity(data,k,delta_t):
    
    if k<=0:
        runsum=0
    else:
        runsum=0.5*data[0]+0.5*data[k]+sum(data[1:k])
        runsum=delta_t*runsum
    
    return runsum

def get_input():
    
    delta_t=eval(sys.argv[1])

    acc=np.loadtxt('acc.dat',dtype=float)
    t=np.linspace(0,delta_t*(len(acc)-1),len(acc))
    veloc=np.zeros(len(acc),dtype=float)
    for i in range(1,len(acc)):
        veloc[i]=calc_velocity(acc,i-1,delta_t)+0.5*delta_t*(acc[i-1]+acc[i])
    
    return t, acc, veloc, delta_t

def plotfunc_v1(x,y):
    
    plt.plot(x,y,'r-')
    plt.xlabel('time')
    plt.ylabel('acceleration')
    plt.title('time vs acceleration')
    plt.show()
    
def plotfunc_v2(x,y):
    
    plt.plot(x,y,'m-')
    plt.xlabel('time')
    plt.ylabel('velocity')
    plt.title('time vs velocity')
    plt.show()
    
t, acc, veloc, delta_t=get_input()
plotfunc_v1(t,acc)
plotfunc_v2(t,veloc)  
