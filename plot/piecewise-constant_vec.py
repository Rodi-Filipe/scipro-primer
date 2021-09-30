# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:34:04 2021

@author: rodin
"""
import numpy as np
import matplotlib.pyplot as plt

def piecewise_constant_vec(x,data):
    
    outputArg1=np.zeros_like(x)
    outputArg1[x==data[len(data)-1][1]]=data[-2][0]
    for i in range(len(data)-1):
        outputArg1[np.logical_and(x>=data[i][1],x<data[i+1][1])]=data[i][0]
    
    return outputArg1

def plot_piecewise(data,xmax):
    
    x=np.linspace(-2,xmax,1000)
    y=piecewise_constant_vec(x,data)
    
    plt.plot(x,y,'r--')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Piecewise curve')
    
plot_piecewise([(-1,0),(0,1),(2,1.5),(4,2),(6,4),(10,7),(-5,9),(-2,13)],10)
                   