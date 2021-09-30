# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 00:54:43 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def piecewise(x,data):
    
    if isinstance(x,np.ndarray):
        outputArg1=np.zeros(len(x))
        for k in range(len(x)):
            for i in range(len(data)-1):
                if x[k]>=data[i][1] and x[k]<data[i+1][1]:
                    outputArg1[k]=data[i][0]
                elif i==(len(data)-2) and x[k]==data[len(data)-1][1]:
                    outputArg1[k]=data[i][0]
    else:
        for i in range(len(data)-1):
            if x>=data[i][1] and x<data[i+1][1]:
                outputArg1=data[i][0]
            elif i==(len(data)-2) and x==data[len(data)-1][1]:
                outputArg1=data[i][0]
        
    return outputArg1

def plot_piecewise(data,xmax):
    
    x=np.linspace(-2,xmax,1000)
    y=piecewise(x,data)
    
    plt.plot(x,y,'--')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Piecewise curve')


plot_piecewise([(-1,0),(0,1),(2,1.5),(4,2),(6,4),(10,7),(-5,9),(-2,13)],10)