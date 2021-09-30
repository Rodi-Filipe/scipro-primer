# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 01:02:42 2021

@author: rodin
"""

def f(x):
    
    outputArg1=x*(12-x) + np.sin(np.pi*x)
    
    return outputArg1

def piecewise_lin(x,data):
    
    outputArg1=np.zeros_like(x)
    outputArg1[x==data[-1][1]]=data[-1][0]
    for i in range(len(data)-1):
        outputArg1[x==data[i][1]]=data[i][0]
        tempvec = ((data[i+1][0]-data[i][0]) / (data[i+1][1]-data[i][1])) * (x[np.logical_and(x>data[i][1],x<data[i+1][1])]-data[i][1]) +data[i][0]
        outputArg1[np.logical_and(x>data[i][1],x<data[i+1][1])] = tempvec
    
    return outputArg1

import numpy as np
import matplotlib.pyplot as plt

def viz_trapezoid(f,a,b,n):

    x1=np.linspace(a,b,1000)
    x2=np.linspace(a,b,n+1)
    
    data=[ ( f(x2[k]), x2[k]) for k in range(len(x2)) ]
    
    y1=f(x1)
    y2=piecewise_lin(x1,data)
    y3=np.zeros((2,len(x2)-2))
    y3[1,:]=piecewise_lin(x2,data)[1:-1]
    
    plt.fill_between(x1,y1,y2)
    plt.axis([a,b,np.min(f(x1)),np.max(f(x1))])
    plt.plot(x1,y2,'r--')
    plt.plot(np.resize(x2[1:-1],(2,len(x2)-2)),y3,'r--')
    
    plt.show()
    
viz_trapezoid(lambda x: np.exp(x)*np.arctan(x)*np.sin(x),0,3*np.pi,15) 