# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 03:00:24 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

def get_vo():
    
    outputArg1=[eval(i) for i in sys.argv[1:]]
    
    return outputArg1

def plotfunc(vo_list):
    
    g=9.81
    plt.figure()
    for i in range(len(vo_list)):
        t=np.linspace(0,(2*vo_list[i])/g,1000)
        y=vo_list[i]*t-0.5*g*t**2
        
        plt.subplot(1,len(vo_list),i+1)
        plt.plot(t,y,'r-')
        plt.axis([min(t), max(t), min(y),max(y)+1.5])
        plt.xlabel('time s')
        plt.ylabel('height m')
        plt.title('Y vs t plot')
    plt.show()

vo_list=get_vo()

plotfunc(vo_list)

    
    
    
    