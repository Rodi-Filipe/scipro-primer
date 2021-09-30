# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:38:19 2021

@author: rodin
"""


import numpy as np
from math import pi, sin
import matplotlib.pyplot as plt

def S(t, n, T=2*pi):
    
    if type(t)==np.ndarray or type(t)==list:
        runsum=np.zeros(len(t))
        for i in range(1,n+1):
            tempvar=(4/np.pi) * (1/(2*i-1)) * np.sin((2*(2*i-1)*np.pi*t)/T)
            runsum+=tempvar 
    else:
        runsum=0
        for i in range(1,n+1):
            tempvar=(4/np.pi) * (1 / (2*i-1) ) * np.sin( (2*(2*i-1)*np.pi*t) / T )
            runsum+=tempvar
    return runsum

def graph():
    
    nvalues_vec=[1,3,20,200,100000]
    t=np.arange(0,14*pi,pi/4)
    
    for nvalues in nvalues_vec:
        
        y=S(t,nvalues)
        plt.plot(t,y)
        plt.xlabel('x values')
        plt.ylabel('y values')
        plt.title('Sum of Sines Approximation Curves')
    plt.savefig('c:/Users/rodin/Documents/Python_Scripts/off_white1.png')
    plt.show()
    
graph()
