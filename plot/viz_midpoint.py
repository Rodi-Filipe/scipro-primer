# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:05:10 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    
    outputArg1=x*(12-x) + np.sin(np.pi*x)
    
    return outputArg1

def piecewise_constant_vec(x,data):
    
    outputArg1=np.zeros_like(x)
    outputArg1[x==data[len(data)-1][1]]=data[-2][0]
    for i in range(len(data)-1):
        outputArg1[np.logical_and(x>=data[i][1],x<data[i+1][1])]=data[i][0]
    
    return outputArg1

def viz_midpoint(f,a,b,n):

    x1=np.linspace(a,b,1000)
    x2=np.linspace(a,b,n)
    
    data=[ ( f(x2[k]+(x2[k+1]-x2[k])/2), x2[k]) for k in range(len(x2)-1) ]
    data.append((0,b))
    
    y1=f(x1)
    y2=piecewise_constant_vec(x1, data)
    y3=np.zeros((2,len(x2)))
    y3[1,:]=piecewise_constant_vec(x2+1E-20,data)
    
    plt.fill_between(x1,y1,y2)
    plt.axis([a,b,np.min(f(x1)),np.max(f(x1))])
    plt.plot(x1,y2,'r--')
    plt.plot(np.resize(x2,(2,len(x2))),y3,'r--')
    
    plt.show()
    
viz_midpoint(lambda x: np.exp(x)*np.arctan(x)*np.sin(x),0,2*np.pi,20) 
