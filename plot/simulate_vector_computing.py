# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:38:19 2021

@author: rodin
"""

from math import cos,sin,exp
import numpy as np

def ycompute():
    
    x=np.array([0, 2],float)
    t=np.array([1,1.5])
    y=np.zeros_like(x)
    for i in range(len(x)):
        y[i]=cos(sin(x[i])) + exp(1/t[i])
    
    return y

def ycomputev1():
    x=np.array([0, 2])
    t=np.array([1,1.5])
    y=np.cos(np.sin(x)) + np.exp(1/t)
    
    return y

print(ycompute())
print(ycomputev1())

