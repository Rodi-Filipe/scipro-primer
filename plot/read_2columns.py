# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:07:18 2021

@author: rodin
"""

import matplotlib.pyplot as plt
import numpy as np

def get_input():
    
    x=[]
    y=[]
    f_ID=open('xy.dat','r')
    for line in f_ID:
        tempvar=line.split()
        x.append(eval(tempvar[0]))
        y.append(eval(tempvar[1]))
    f_ID.close()
    
    return x, y

def get_inputv1():
    
    data = np.loadtxt('xy.dat', dtype=np.float)
    x = data[:,0] # column with index 0 
    y = data[:,1] # column with index 1
    
    return x, y

def plotfunc(x, y):
    
    x=np.array(x)
    y=np.array(y)
    plt.plot(x,y)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Plot of xy file')
    plt.show()

x,y=get_input()
plotfunc(x, y)       
        
        