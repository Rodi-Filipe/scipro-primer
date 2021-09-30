# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 02:47:57 2021

@author: rodin
"""

from math import factorial, pi
import numpy as np
import matplotlib.pyplot as plt

def S(x, n):
    
    if type(x)==np.ndarray:
        outputArg1=np.zeros((len(x),1))
        for iterat in range(len(x)):
            outputArg1[iterat]=np.sum([(-1)**i*(x[iterat]**(2*i+1)/factorial(2*i+1)) for i in range(n+1)])
    else:
        outputArg1=np.sum([(-1)**i*(x**(2*i+1)/factorial(2*i+1)) for i in range(n+1)])
    
    return outputArg1

def graph(iterat):
    
    x=np.linspace(0,2*pi,100)
    
    for i in range(len(iterat)):
        plt.subplot(len(iterat),1,i+1)
        plt.plot(x,S(x,iterat[i]))
        plt.xlabel('x value')
        plt.ylabel('y value')
        plt.title('sin(x) curve')
    plt.show()
    
graph([1,2,3,6,12])